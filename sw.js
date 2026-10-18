// BioPeat · service worker: primero internet (sin caché HTTP), si no hay conexión usa la última copia.
const CACHE='biopeat-app';
self.addEventListener('install',e=>{self.skipWaiting();e.waitUntil(caches.open(CACHE).then(c=>c.addAll(['./','index.html','manifest.json']).catch(()=>{})));});
self.addEventListener('activate',e=>e.waitUntil(self.clients.claim()));
self.addEventListener('fetch',e=>{
  const r=e.request;
  if(r.method!=='GET'||new URL(r.url).origin!==location.origin)return;
  e.respondWith(fetch(r,{cache:'no-cache'}).then(res=>{if(res.ok){const copy=res.clone();caches.open(CACHE).then(c=>c.put(r,copy));}return res;}).catch(()=>caches.match(r).then(m=>m||caches.match('index.html'))));
});
