#!/bin/bash
# JavaScript Minification Script
# Requires: terser (npm install -g terser)

echo "📦 MINIFYING ALL JAVASCRIPT FILES"
echo "=================================="
echo ""

# Check if terser is installed
if ! command -v terser &> /dev/null; then
    echo "❌ terser is not installed!"
    echo ""
    echo "Please install it first:"
    echo "  npm install -g terser"
    echo ""
    exit 1
fi

echo "✅ terser found"
echo ""

# Counter
total=0
minified=0
skipped=0
errors=0

# Find all JS files (excluding node_modules, .min.js, etc.)
find js/ -name "*.js" ! -name "*.min.js" ! -path "*/node_modules/*" | while read file; do
    total=$((total + 1))
    
    # Get base name and create .min.js filename
    dir=$(dirname "$file")
    base=$(basename "$file" .js)
    min_file="${dir}/${base}.min.js"
    
    echo "📄 Processing: $file"
    
    # Minify the file
    if terser "$file" -c -m -o "$min_file" 2>/dev/null; then
        # Get sizes
        original_size=$(wc -c < "$file" | tr -d ' ')
        minified_size=$(wc -c < "$min_file" | tr -d ' ')
        
        if [ "$minified_size" -lt "$original_size" ]; then
            reduction=$((100 - (minified_size * 100 / original_size)))
            echo "  ✅ Created: $min_file"
            echo "     Size: $original_size → $minified_size bytes (${reduction}% reduction)"
            minified=$((minified + 1))
        else
            echo "  ⚠️  Minified file larger, skipping"
            rm -f "$min_file"
            skipped=$((skipped + 1))
        fi
    else
        echo "  ❌ Error minifying"
        errors=$((errors + 1))
    fi
    echo ""
done

echo "=================================="
echo "✅ COMPLETE"
echo ""
echo "Total files: $total"
echo "Minified: $minified"
echo "Skipped: $skipped"
echo "Errors: $errors"
echo ""
echo "📝 Next steps:"
echo "  1. Test all functionality"
echo "  2. Update HTML to reference .min.js files"
echo "  3. Update references in HTML files"
echo ""

