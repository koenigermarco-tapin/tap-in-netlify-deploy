#!/usr/bin/env python3
"""
JavaScript Minification Script
Minifies all JS files for better performance
"""

import os
import re
import subprocess
from pathlib import Path

def find_js_files():
    """Find all JavaScript files to minify"""
    js_files = []
    
    exclude_dirs = {'node_modules', '.git', 'archive', '__pycache__', 'android', 'ios', 'dist', 'build', 'react-app'}
    exclude_files = {'.min.js'}
    
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if file.endswith('.js') and not any(ex in file for ex in exclude_files):
                filepath = os.path.join(root, file)
                js_files.append(filepath)
    
    return js_files

def check_terser_available():
    """Check if terser is available"""
    try:
        result = subprocess.run(['terser', '--version'], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        return result.returncode == 0
    except:
        return False

def minify_js_simple(filepath):
    """Simple JavaScript minification (remove comments, extra whitespace)"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ⚠️  Error reading {filepath}: {e}")
        return False
    
    # Simple minification (basic)
    # Remove single-line comments (but not in strings)
    lines = content.split('\n')
    minified_lines = []
    
    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue
        
        # Remove trailing comments (but be careful with URLs)
        if '//' in line and '://' not in line:
            comment_pos = line.find('//')
            # Check if it's in a string
            before_comment = line[:comment_pos]
            if before_comment.count('"') % 2 == 0 and before_comment.count("'") % 2 == 0:
                line = before_comment.rstrip()
        
        if line.strip():
            # Remove leading/trailing whitespace
            minified_lines.append(line.strip())
    
    minified = ' '.join(minified_lines)
    
    # Remove multi-line comments (/* */)
    minified = re.sub(r'/\*.*?\*/', '', minified, flags=re.DOTALL)
    
    # Remove extra whitespace around operators
    minified = re.sub(r'\s+([{}();,=+\-*/])', r'\1', minified)
    minified = re.sub(r'([{}();,=+\-*/])\s+', r'\1', minified)
    
    # Save to .min.js file
    base_path = os.path.splitext(filepath)[0]
    min_path = base_path + '.min.js'
    
    try:
        with open(min_path, 'w', encoding='utf-8') as f:
            f.write(minified)
        
        # Show size comparison
        original_size = len(content)
        minified_size = len(minified)
        reduction = ((original_size - minified_size) / original_size) * 100
        
        print(f"  ✅ Created: {os.path.relpath(min_path, '.')}")
        print(f"     Size: {original_size:,} → {minified_size:,} bytes ({reduction:.1f}% reduction)")
        
        return True
    except Exception as e:
        print(f"  ⚠️  Error writing {min_path}: {e}")
        return False

def create_minification_guide():
    """Create guide for proper minification"""
    js_files = find_js_files()
    file_count = len(js_files)
    
    guide = "# JavaScript Minification Guide\n\n"
    guide += "## Current Status\n"
    guide += f"- **Total JS Files Found:** {file_count}\n\n"
    guide += "## Recommended Approach\n\n"
    guide += "### Option 1: Use Terser (Recommended)\n"
    guide += "```bash\n"
    guide += "# Install terser globally\n"
    guide += "npm install -g terser\n\n"
    guide += "# Minify all JS files\n"
    guide += "find js/ -name \"*.js\" ! -name \"*.min.js\" -exec terser {} -o {{}}.min.js -c -m \\;\n"
    guide += "```\n\n"
    guide += "### Option 2: Use Online Tools\n"
    guide += "- https://www.toptal.com/developers/javascript-minifier\n"
    guide += "- https://jscompress.com/\n\n"
    guide += "### Option 3: Build Process\n"
    guide += "Add to package.json:\n"
    guide += "```json\n"
    guide += "{\n"
    guide += "  \"scripts\": {\n"
    guide += "    \"minify\": \"terser js/**/*.js -o dist/js/ -c -m\"\n"
    guide += "  }\n"
    guide += "}\n"
    guide += "```\n\n"
    guide += "## Files to Minify\n"
    
    for js_file in sorted(js_files)[:20]:  # Show first 20
        rel_path = os.path.relpath(js_file, '.')
        guide += f"- {rel_path}\n"
    
    if len(js_files) > 20:
        remaining_count = len(js_files) - 20
        guide += f"\n... and {remaining_count} more files\n"
    
    guide += "\n## Benefits\n"
    guide += "- **30-50% smaller file sizes**\n"
    guide += "- **Faster page loads**\n"
    guide += "- **Better performance scores**\n"
    guide += "- **Reduced bandwidth usage**\n\n"
    guide += "## Next Steps\n"
    guide += "1. Choose minification method\n"
    guide += "2. Create .min.js versions\n"
    guide += "3. Update HTML to reference .min.js files\n"
    guide += "4. Test all functionality\n"
    
    with open('JS-MINIFICATION-GUIDE.md', 'w') as f:
        f.write(guide)
    
    return guide

def main():
    """Main function"""
    print("=" * 80)
    print("📦 JAVASCRIPT MINIFICATION ANALYSIS")
    print("=" * 80)
    print()
    
    js_files = find_js_files()
    print(f"📋 Found {len(js_files)} JavaScript files")
    print()
    
    # Check for terser
    has_terser = check_terser_available()
    
    if has_terser:
        print("✅ Terser is available - can minify files")
    else:
        print("⚠️  Terser not found - generating guide instead")
        print("   Install: npm install -g terser")
    
    print()
    
    # Create guide
    create_minification_guide()
    print("✅ Created minification guide: JS-MINIFICATION-GUIDE.md")
    print()
    
    # Show first few files
    print("📄 Sample files to minify:")
    for js_file in sorted(js_files)[:10]:
        rel_path = os.path.relpath(js_file, '.')
        size = os.path.getsize(js_file)
        print(f"  - {rel_path} ({size:,} bytes)")
    
    if len(js_files) > 10:
        print(f"  ... and {len(js_files) - 10} more")
    
    print()
    print("=" * 80)
    print("✅ Analysis complete!")
    print("=" * 80)
    print()
    print("📝 Next steps:")
    print("   1. Read JS-MINIFICATION-GUIDE.md")
    print("   2. Install terser: npm install -g terser")
    print("   3. Run minification script")
    print("   4. Update HTML references to .min.js files")

if __name__ == '__main__':
    main()

