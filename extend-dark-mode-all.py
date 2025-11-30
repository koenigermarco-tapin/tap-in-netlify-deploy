#!/usr/bin/env python3
"""
Extend dark mode to all stripe files
"""

from pathlib import Path
import re

def add_dark_mode_to_file(filepath):
    """Add dark mode CSS and JS to file"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # Add CSS
    if 'css/dark-mode.css' not in content:
        css_link = '<link rel="stylesheet" href="css/dark-mode.css">'
        
        # Find CSS links
        css_pattern = r'(<link[^>]*rel="stylesheet"[^>]*>)'
        if re.search(css_pattern, content):
            content = re.sub(css_pattern, r'\1\n    ' + css_link, content, count=1)
            changes.append("CSS")
        elif '</head>' in content:
            content = re.sub(r'(</head>)', '    ' + css_link + '\n\1', content)
            changes.append("CSS")
    
    # Add JS
    if 'js/dark-mode.js' not in content:
        js_script = '<script src="js/dark-mode.js"></script>'
        
        if '</body>' in content:
            content = re.sub(r'(</body>)', '    ' + js_script + '\n\1', content)
            changes.append("JS")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes
    
    return False, []

def main():
    print("=" * 80)
    print("🌙 EXTENDING DARK MODE TO ALL STRIPE FILES")
    print("=" * 80)
    print()
    
    stripe_files = list(Path('.').glob('*-stripe*-gamified.html'))
    stripe_files.sort()
    
    print(f"Found {len(stripe_files)} stripe files\n")
    
    updated = 0
    skipped = 0
    
    for filepath in stripe_files:
        if any(skip in str(filepath) for skip in ['node_modules', '.git', 'react-app']):
            continue
        
        print(f"📝 {filepath.name}...")
        try:
            success, changes = add_dark_mode_to_file(filepath)
            if success:
                updated += 1
                print(f"  ✅ Added: {', '.join(changes)}")
            else:
                skipped += 1
                print(f"  ⏭️  Already has dark mode")
        except Exception as e:
            print(f"  ❌ Error: {e}")
    
    print()
    print("=" * 80)
    print(f"✅ Updated: {updated}/{len(stripe_files)}")
    print(f"⏭️  Skipped: {skipped}")
    print("=" * 80)

if __name__ == '__main__':
    main()

