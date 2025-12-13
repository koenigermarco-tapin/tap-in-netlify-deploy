#!/usr/bin/env python3
"""
Update HTML files to reference .min.js versions
Replaces .js references with .min.js where .min.js exists
"""

import os
import re
from pathlib import Path

def find_min_js_files():
    """Find all .min.js files"""
    min_js_files = set()
    
    for root, dirs, files in os.walk('js'):
        # Skip node_modules
        dirs[:] = [d for d in dirs if d != 'node_modules']
        
        for file in files:
            if file.endswith('.min.js'):
                rel_path = os.path.relpath(os.path.join(root, file), '.')
                # Get non-min version
                base_path = rel_path.replace('.min.js', '.js')
                min_js_files.add((base_path, rel_path))
    
    return min_js_files

def update_html_file(filepath, min_js_mapping):
    """Update HTML file to use .min.js versions"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ⚠️  Error reading {filepath}: {e}")
        return False
    
    original_content = content
    updated = False
    
    # Replace .js with .min.js for files that have minified versions
    for base_path, min_path in min_js_mapping:
        # Pattern: src="path/to/file.js" or src='path/to/file.js'
        pattern = rf'src=["\']({re.escape(base_path)})["\']'
        replacement = f'src="{min_path}"'
        
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            updated = True
    
    if updated:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"  ⚠️  Error writing {filepath}: {e}")
            return False
    
    return False

def main():
    """Main function"""
    print("=" * 80)
    print("🔄 UPDATING HTML FILES TO USE MINIFIED JAVASCRIPT")
    print("=" * 80)
    print()
    
    # Find all .min.js files
    min_js_mapping = find_min_js_files()
    
    if not min_js_mapping:
        print("⚠️  No .min.js files found!")
        print("   Please run minification first:")
        print("   ./minify-all-javascript.sh")
        return
    
    print(f"📦 Found {len(min_js_mapping)} minified JavaScript files")
    print()
    
    # Find HTML files
    html_files = []
    exclude_dirs = {'node_modules', '.git', 'archive', '__pycache__', 'android', 'ios', 'dist', 'build', 'react-app'}
    
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                html_files.append(filepath)
    
    print(f"📋 Found {len(html_files)} HTML files")
    print()
    
    # Update HTML files
    updated = 0
    skipped = 0
    
    for filepath in sorted(html_files):
        rel_path = os.path.relpath(filepath, '.')
        if update_html_file(filepath, min_js_mapping):
            print(f"  ✅ Updated: {rel_path}")
            updated += 1
        else:
            skipped += 1
    
    print()
    print("=" * 80)
    print(f"✅ COMPLETE: Updated {updated} files, Skipped {skipped} files")
    print("=" * 80)
    print()
    print("📝 Next steps:")
    print("  1. Test all functionality")
    print("  2. Verify no errors in browser console")
    print("  3. Check performance improvements")

if __name__ == '__main__':
    main()

