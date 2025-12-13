# Image Optimization Guide

## Current Status
- **Total Images Found:** 16
- **PNG Files:** 16
- **JPG/JPEG Files:** 0

## Conversion Steps

### 1. Install WebP Tools
```bash
# Mac
brew install webp

# Linux
sudo apt-get install webp

# Windows
# Download from: https://developers.google.com/speed/webp/download
```

### 2. Convert Images
Run the generated script:
```bash
./convert-images-to-webp.sh
```

### 3. Update HTML Files
Replace image references with WebP and fallback:

**Before:**
```html
<img src="image.png" alt="Description">
```

**After:**
```html
<picture>
  <source srcset="image.webp" type="image/webp">
  <img src="image.png" alt="Description">
</picture>
```

Or with lazy loading:
```html
<picture>
  <source srcset="image.webp" type="image/webp">
  <img src="image.png" alt="Description" loading="lazy" width="800" height="600">
</picture>
```

## Benefits
- **30-50% smaller file sizes**
- **Faster page loads**
- **Better performance scores**
- **Modern browser support with fallback**

## Files to Update

**Total HTML files to check:** 387

Use search and replace to update `<img>` tags to `<picture>` format.
