# Deployment Checklist

## Before Every Deploy

- [ ] Update VERSION in `cache-buster.js` (use current date)
  ```javascript
  const VERSION = '2024-MM-DD-v1'; // Change this!
  ```

- [ ] Test changes locally

- [ ] Review git diff

- [ ] Commit with clear message

## After Deploy

- [ ] Wait 2 minutes for Netlify build

- [ ] Check deploy log for errors

- [ ] Test in incognito window

- [ ] Verify cache headers:
  ```bash
  curl -I https://your-site.netlify.app/index.html | grep -i cache
  # Should show: Cache-Control: no-cache, no-store, must-revalidate
  ```

- [ ] Check Service Worker status (should be none):
  - Open DevTools → Application → Service Workers
  - Should show: "No service workers registered"

- [ ] Test functionality on mobile device

## Cache Header Verification

Expected headers:

**HTML files:**
```
Cache-Control: no-cache, no-store, must-revalidate
```

**JavaScript/CSS:**
```
Cache-Control: public, max-age=300, must-revalidate
```

**Images:**
```
Cache-Control: public, max-age=86400
```

## If Cache Issues Occur

1. Clear browser cache (Ctrl+Shift+Delete)

2. Check Netlify deploy log

3. Verify netlify.toml deployed correctly

4. Force Netlify cache purge:
   - Site Settings → Build & Deploy → Post Processing → Clear Cache

5. Test in multiple browsers
