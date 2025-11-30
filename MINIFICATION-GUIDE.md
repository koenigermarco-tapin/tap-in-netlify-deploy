# Minification Guide

## Quick Start

1. Install tools:
```bash
npm install -g uglify-js clean-css-cli
```

2. Run build:
```bash
./build.sh
```

3. Minified files will be in `dist/` directory

## Production Usage

In production, update HTML files to use minified versions:
- `css/styles.css` → `dist/css/styles.min.css`
- `js/app.js` → `dist/js/app.min.js`

## Current Status

- ✅ Build script created
- ⏳ Minification tools need to be installed
- ⏳ HTML files need to reference minified versions

**Recommendation:** Use a build tool (Webpack, Vite, etc.) for automated minification
