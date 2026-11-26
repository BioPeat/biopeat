// BioPeat · service worker v12 (Stale-While-Revalidate).
// Responde al instante desde caché (<50 ms) y actualiza los archivos en segundo plano cuando hay red.
const CACHE = 'biopeat-v13';
const PRECACHE = [
  './',
  'index.html',
  'inicio.html',
  'manifest.json',
  'assets/styles.css?v=83',
  'assets/data.js?v=83',
  'assets/app.js?v=83',
  'icon-192.png?v=83',
  'icon-512.png?v=83'
];

self.addEventListener('install', e => {
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(PRECACHE).catch(() => {})));
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  const r = e.request, u = new URL(r.url);
  if (r.method !== 'GET' || u.origin !== location.origin) return;
  const isNav = r.mode === 'navigate';
  const isInicio = /\/inicio\.html$/i.test(u.pathname);

  e.respondWith(
    caches.open(CACHE).then(cache =>
      cache.match(r, { ignoreSearch: false }).then(exact =>
        exact || cache.match(r, { ignoreSearch: true })
      ).then(cached => {
        const netFetch = fetch(r, { cache: 'no-cache' }).then(res => {
          if (res && res.ok) {
            const copy = res.clone();
            cache.put(r, copy.clone()).catch(() => {});
            if (isNav) cache.put(isInicio ? 'inicio.html' : 'index.html', copy).catch(() => {});
          }
          return res;
        }).catch(() => null);

        if (cached) {
          e.waitUntil(netFetch);
          return cached;
        }
        return netFetch.then(res => {
          if (res) return res;
          if (isNav) return cache.match(isInicio ? 'inicio.html' : 'index.html');
          return new Response('', { status: 504 });
        });
      })
    )
  );
});
