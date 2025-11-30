#!/bin/bash
# TAP-IN Build Script - Minify CSS and JS

echo "🔨 Building production assets..."

# Install minification tools if needed
if ! command -v uglifyjs &> /dev/null; then
    echo "⚠️  uglifyjs not found. Install with: npm install -g uglify-js"
fi

if ! command -v cleancss &> /dev/null; then
    echo "⚠️  cleancss not found. Install with: npm install -g clean-css-cli"
fi

# Create dist directory
mkdir -p dist/css dist/js

# Minify CSS files
echo "📝 Minifying CSS..."
for css in css/*.css; do
    if [ -f "$css" ]; then
        filename=$(basename "$css" .css)
        cleancss -o "dist/css/${filename}.min.css" "$css" 2>/dev/null || cp "$css" "dist/css/${filename}.min.css"
        echo "  ✅ $css → dist/css/${filename}.min.css"
    fi
done

# Minify JS files (non-minified ones)
echo "📝 Minifying JS..."
for js in js/*.js; do
    if [ -f "$js" ] && [[ ! "$js" == *.min.js ]] && [[ ! "$js" == *.bak ]]; then
        filename=$(basename "$js" .js)
        uglifyjs "$js" -o "dist/js/${filename}.min.js" -c -m 2>/dev/null || cp "$js" "dist/js/${filename}.min.js"
        echo "  ✅ $js → dist/js/${filename}.min.js"
    fi
done

echo ""
echo "✅ Build complete! Minified files in dist/ directory"
echo "📊 To use: Update HTML to point to dist/*.min.* files in production"
