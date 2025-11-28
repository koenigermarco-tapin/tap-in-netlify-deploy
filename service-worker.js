// TAP-IN Service Worker - Offline Support & Caching
const CACHE_NAME = 'tap-in-v11-2024-11-27-FORCE-REFRESH'; // bump version to force update
const urlsToCache = [
  '/',
  '/index.html',
  '/learning-hub.html',
  '/energy-management-module-gamified.html',
  '/boundaries-module-gamified.html',
  '/deep-work-module-gamified.html',
  '/feedback-module-gamified.html',
  '/expectation-management-module-gamified.html',
  '/stoic-tools-module-gamified.html',
  '/limiting-beliefs-module-gamified.html',
  '/active-listening-module-gamified.html',
  '/empathy-module-gamified.html',
  '/coaching-module-gamified.html',
  '/worker-type-assessment.html',
  '/worker-type-assessment.de.html',
  '/leadership-style-carousel.html',
  '/leadership-style-carousel.de.html',
  '/team-assessment-enhanced-v2.html',
  '/combined-complete-profile.html',
  '/combined-complete-profile.de.html',
  '/combined-profile-carousel.de.html',
  '/manifest.json'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
      .catch(err => console.log('Cache install error:', err))
  );
  self.skipWaiting();
});

self.addEventListener('fetch', event => {
  const requestUrl = new URL(event.request.url);

  if (requestUrl.pathname === '/' || requestUrl.pathname.endsWith('/index.html')) {
    event.respondWith(
      fetch(event.request)
        .then(networkResponse => {
          if (networkResponse && networkResponse.status === 200) {
            const responseClone = networkResponse.clone();
            caches.open(CACHE_NAME).then(cache => cache.put(event.request, responseClone));
          }
          return networkResponse;
        })
        .catch(() => caches.match(event.request))
    );
    return;
  }

  event.respondWith(
    caches.match(event.request).then(response => {
      if (response) {
        return response;
      }

      const fetchRequest = event.request.clone();
      return fetch(fetchRequest).then(networkResponse => {
        if (!networkResponse || networkResponse.status !== 200 || networkResponse.type !== 'basic') {
          return networkResponse;
        }

        const responseToCache = networkResponse.clone();
        caches.open(CACHE_NAME).then(cache => cache.put(event.request, responseToCache));
        return networkResponse;
      });
    })
  );
});

self.addEventListener('activate', event => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(cacheNames => Promise.all(
      cacheNames.map(cacheName => cacheWhitelist.includes(cacheName) ? null : caches.delete(cacheName))
    ))
  );
  self.clients.claim();
});

self.addEventListener('sync', event => {
  if (event.tag === 'sync-assessments') {
    event.waitUntil(syncAssessments());
  }
});

function syncAssessments() {
  return Promise.resolve();
}
