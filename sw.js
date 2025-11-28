/**
 * Service Worker UNINSTALLER
 * 
 * This file completely removes the old service worker and clears all caches.
 * What this does:
 * 1. Unregisters the service worker
 * 2. Deletes all cached content
 * 3. Reloads all open tabs with fresh content
 * 4. Stops intercepting network requests
 */

console.log('🧹 SW UNINSTALLER: Starting cleanup process...');

// Install immediately
self.addEventListener('install', event => {
  console.log('🧹 SW UNINSTALLER: Installing...');
  self.skipWaiting();
});

// When activated, clean everything and unregister
self.addEventListener('activate', event => {
  console.log('🧹 SW UNINSTALLER: Activating...');
  
  event.waitUntil(
    // Step 1: Delete ALL caches
    caches.keys()
      .then(cacheNames => {
        console.log('🧹 SW UNINSTALLER: Found', cacheNames.length, 'caches to delete');
        return Promise.all(
          cacheNames.map(cacheName => {
            console.log('🧹 SW UNINSTALLER: Deleting cache:', cacheName);
            return caches.delete(cacheName);
          })
        );
      })
      .then(() => {
        console.log('✅ SW UNINSTALLER: All caches deleted');
        // Step 2: Unregister this service worker
        return self.registration.unregister();
      })
      .then(unregistered => {
        if (unregistered) {
          console.log('✅ SW UNINSTALLER: Service worker unregistered');
        }
        return self.clients.claim();
      })
      .then(() => {
        return self.clients.matchAll({ 
          type: 'window',
          includeUncontrolled: true 
        });
      })
      .then(clients => {
        console.log('🧹 SW UNINSTALLER: Reloading', clients.length, 'client(s)');
        clients.forEach(client => {
          client.postMessage({
            type: 'SW_UNINSTALLED',
            message: 'Service worker removed. Reloading for fresh content...'
          });
        });
        console.log('🎉 SW UNINSTALLER: Cleanup complete!');
      })
      .catch(error => {
        console.error('❌ SW UNINSTALLER: Error during cleanup:', error);
      })
  );
});

// DON'T INTERCEPT ANY REQUESTS
self.addEventListener('fetch', event => {
  console.log('🚫 SW UNINSTALLER: Not intercepting:', event.request.url);
  return;
});

// Listen for messages
self.addEventListener('message', event => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    console.log('🧹 SW UNINSTALLER: Received SKIP_WAITING message');
    self.skipWaiting();
  }
});
