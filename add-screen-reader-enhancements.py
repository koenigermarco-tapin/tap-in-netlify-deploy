#!/usr/bin/env python3
"""
Add Screen Reader Enhancements to All HTML Pages
Adds screen-reader-enhancements.js to all pages
"""

import os
import re
from pathlib import Path

def already_has_screen_reader_enhancements(content):
    """Check if page already includes screen reader enhancements"""
    return 'screen-reader-enhancements.js' in content or 'ScreenReaderEnhancements' in content

def add_screen_reader_script(filepath):
    """Add screen reader enhancements script to HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ⚠️  Error reading {filepath}: {e}")
        return False
    
    # Skip if already has it
    if already_has_screen_reader_enhancements(content):
        return False
    
    # Find insertion point (before closing </body>)
    body_close = content.rfind('</body>')
    if body_close == -1:
        # Try to find end of file
        body_close = len(content)
    
    # Script to add
    script_tag = '\n    <!-- Screen Reader Enhancements for Accessibility -->\n    <script src="js/screen-reader-enhancements.js" defer></script>\n'
    
    # Insert before </body>
    new_content = content[:body_close] + script_tag + content[body_close:]
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    except Exception as e:
        print(f"  ⚠️  Error writing {filepath}: {e}")
        return False

def main():
    """Main function"""
    print("=" * 80)
    print("🔊 ADDING SCREEN READER ENHANCEMENTS TO ALL HTML PAGES")
    print("=" * 80)
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
    
    # Add screen reader enhancements
    updated = 0
    skipped = 0
    
    for filepath in sorted(html_files):
        rel_path = os.path.relpath(filepath, '.')
        if add_screen_reader_script(filepath):
            print(f"  ✅ Updated: {rel_path}")
            updated += 1
        else:
            skipped += 1
    
    print()
    print("=" * 80)
    print(f"✅ COMPLETE: Updated {updated} files, Skipped {skipped} files")
    print("=" * 80)

if __name__ == '__main__':
    main()

