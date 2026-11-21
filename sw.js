// BioPeat · service worker. Red primero: con internet siempre carga la última versión publicada;
// sin internet usa la copia guardada. No hace falta cambiar este archivo al actualizar la app.
const CACHE='biopeat-v8';
self.addEventListener('install',e=>{self.skipWaiting();e.waitUntil(caches.open(CACHE).then(c=>c.addAll(['./','index.html','inicio.html','manifest.json','icon-192.png','icon-512.png']).catch(()=>{})));});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));});
self.addEventListener('fetch',e=>{
  const r=e.request,u=new URL(r.url);
  if(r.method!=='GET'||u.origin!==location.origin)return;
  const isNav=r.mode==='navigate',isInicio=/\/inicio\.html$/i.test(u.pathname);
  const ctl=new AbortController(),tm=setTimeout(()=>ctl.abort(),4000);
  e.respondWith(fetch(r,{cache:'no-store',signal:ctl.signal}).then(res=>{
    clearTimeout(tm);
    if(res.ok){
      const copy=res.clone();
      caches.open(CACHE).then(c=>{c.put(r,copy.clone());if(isNav)c.put(isInicio?'inicio.html':'index.html',copy);}).catch(()=>{});
    }
    return res;
  }).catch(()=>{
    clearTimeout(tm);
    return caches.match(r,{ignoreSearch:true}).then(m=>m||caches.match(isNav&&isInicio?'inicio.html':'index.html'));
  }));
});
