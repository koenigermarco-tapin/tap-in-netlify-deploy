# JavaScript Minification Workflow Setup

## Prerequisites

Install terser globally:
```bash
npm install -g terser
```

Or use locally:
```bash
npm install terser --save-dev
```

## Usage

### Option 1: Run the Script
```bash
chmod +x minify-all-javascript.sh
./minify-all-javascript.sh
```

### Option 2: Manual Minification

Minify a single file:
```bash
terser js/filename.js -c -m -o js/filename.min.js
```

Minify all JS files:
```bash
find js/ -name "*.js" ! -name "*.min.js" -exec terser {} -c -m -o {}.min.js \;
```

## Update HTML References

After minification, update HTML files to use `.min.js` versions:

**Before:**
```html
<script src="js/core-gamification.js"></script>
```

**After:**
```html
<script src="js/core-gamification.min.js"></script>
```

## Automation Script

Use `update-html-js-references.py` to automatically update all HTML files:

```bash
python3 update-html-js-references.py
```

## Benefits

- **30-50% smaller file sizes**
- **Faster page loads**
- **Better performance scores**
- **Reduced bandwidth usage**

## Testing

After minification:
1. Test all functionality
2. Check browser console for errors
3. Verify all features work
4. Check performance metrics

