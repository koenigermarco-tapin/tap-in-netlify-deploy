# Subresource Integrity (SRI) Guide

## For CDN Resources

When using external scripts/styles from CDNs, add integrity attributes:

```html
<!-- Example: Confetti library -->
<script 
    src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"
    integrity="sha384-..."
    crossorigin="anonymous">
</script>
```

## Generate SRI Hashes

Use online tool: https://www.srihash.org/

Or command line:
```bash
curl -s https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js | openssl dgst -sha384 -binary | openssl base64 -A
```

## Resources Currently Using CDN:
- canvas-confetti (jsdelivr)
- @supabase/supabase-js (jsdelivr)

## Note:
For development, SRI is optional. For production, add SRI to all CDN resources.
