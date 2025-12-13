# Critical CSS Extraction Guide

## What is Critical CSS?

Critical CSS is the CSS needed to render the **above-the-fold** content (visible without scrolling). By inlining this CSS, we can eliminate render-blocking CSS and improve First Contentful Paint (FCP).

## Benefits

- **Faster First Paint** - Content appears sooner
- **Better FCP/LCP Scores** - Improved Lighthouse metrics
- **Reduced Render Blocking** - Non-critical CSS loaded asynchronously

## Current CSS Files

- avatar-styles.css (6,088 bytes)
- css/accessibility.css (7,082 bytes)
- css/checklist-styles.css (2,591 bytes)
- css/core-styles.css (1,631 bytes)
- css/dark-mode.css (2,507 bytes)
- css/design-system-unified.css (2,436 bytes)
- css/email-capture.css (5,388 bytes)
- css/pwa-install-banner.css (2,529 bytes)
- css/sync-status-indicator.css (2,614 bytes)
- css/variables.css (1,479 bytes)
- css/xp-level-system.css (2,657 bytes)
- enhance-core-css-micro-interactions.css (3,938 bytes)


## Critical CSS Selectors (Above-the-Fold)

These selectors should be inlined in `<head>`:

### Base Styles
- `*`, `html`, `body`
- Typography (font-family, font-size, line-height)
- Colors (background, color)
- Layout (margin, padding, width, height)

### Navigation/Header
- `.nav`, `.header`, `.navigation`
- Navigation links and buttons

### Loading States
- `.loading`, `.skeleton`
- Initial page skeleton

### Core Components (Visible First)
- `.container`
- `.btn-primary` (main CTAs)
- First visible `.card` or module

## Implementation Strategy

### Option 1: Manual Extraction (Recommended for Start)

1. Identify above-the-fold elements on key pages:
   - `index.html` - Hero section, navigation
   - `gym-dashboard.html` - Header, first cards
   - `learning-hub.html` - Header, first modules

2. Extract CSS for these elements from:
   - `css/core-styles.css`
   - `css/variables.css`
   - Inline styles in HTML

3. Create `css/critical.css` with only critical styles

4. Inline in `<head>`:
```html
<style>
  /* Critical CSS here */
  /* Extracted from core-styles.css */
</style>
```

5. Load full CSS asynchronously:
```html
<link rel="preload" href="css/core-styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="css/core-styles.css"></noscript>
```

### Option 2: Automated Extraction (Advanced)

Use tools like:
- `critical` npm package: `npm install -g critical`
- `criticalcss` npm package
- `addyosmani/critical` (Gulp plugin)

## Example: Critical CSS for index.html

```css
/* Critical CSS - Above the Fold */
:root {
    --tap-primary-navy: #1a365d;
    --tap-font-family: 'Inter', sans-serif;
}

* {
    box-sizing: border-box;
}

body {
    font-family: var(--tap-font-family);
    margin: 0;
    padding: 0;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
}

/* Navigation - visible on load */
.nav {
    display: flex;
    justify-content: space-between;
    padding: 1rem;
}

/* Hero section - visible first */
.hero {
    padding: 2rem;
    text-align: center;
}

.btn-primary {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    background: var(--tap-primary-navy);
    color: white;
    border-radius: 8px;
}
```

## Files to Update

1. **Main Entry Pages:**
   - `index.html`
   - `index-DUAL-ENTRY.html`
   - `gym-dashboard.html`
   - `learning-hub.html`

2. **Process:**
   - Extract critical CSS from existing files
   - Inline in `<head>` with `<style>` tag
   - Load full CSS asynchronously
   - Test page load performance

## Performance Impact

**Expected Improvements:**
- FCP: -200ms to -500ms
- LCP: -300ms to -600ms
- Lighthouse Performance: +2 to +5 points

## Testing

After implementation:
1. Test with Lighthouse (Performance audit)
2. Check FCP/LCP metrics
3. Verify no visual regressions
4. Test on slow 3G connection

---

**Next Steps:**
1. Extract critical CSS manually for key pages
2. Create `css/critical.css` file
3. Update HTML to inline critical CSS
4. Load full CSS asynchronously
5. Measure improvements
