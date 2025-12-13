# Image Optimization Workflow Setup

## Prerequisites

### Install WebP Tools

**Mac:**
```bash
brew install webp
```

**Linux:**
```bash
sudo apt-get install webp
```

**Windows:**
Download from: https://developers.google.com/speed/webp/download

## Usage

### Option 1: Run the Conversion Script

```bash
chmod +x convert-images-to-webp.sh
./convert-images-to-webp.sh
```

### Option 2: Manual Conversion

Convert a single image:
```bash
cwebp -q 85 image.png -o image.webp
```

Convert all PNG images:
```bash
find . -name "*.png" -exec sh -c 'cwebp -q 85 "$1" -o "${1%.png}.webp"' _ {} \;
```

## Update HTML Files

After conversion, update HTML to use WebP with fallback:

### Before:
```html
<img src="image.png" alt="Description">
```

### After:
```html
<picture>
  <source srcset="image.webp" type="image/webp">
  <img src="image.png" alt="Description" loading="lazy" width="800" height="600">
</picture>
```

## Automation Script

Use `update-html-images-to-webp.py` to automatically update all HTML files:

```bash
python3 update-html-images-to-webp.py
```

## Quality Settings

- **Quality 85**: Good balance (recommended)
- **Quality 90**: Higher quality, larger files
- **Quality 75**: Smaller files, slightly lower quality

## Benefits

- **30-50% smaller file sizes**
- **Faster page loads**
- **Better performance scores**
- **Modern browser support with fallback**

## Testing

After optimization:
1. Verify images load correctly
2. Check browser support
3. Test fallback to PNG
4. Check performance metrics

