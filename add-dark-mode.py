#!/usr/bin/env python3
"""
Add dark mode support to all HTML pages
"""

from pathlib import Path
import re

# Priority pages to update first
PRIORITY_PAGES = [
    'index.html',
    'gym-dashboard.html',
    'learning-hub.html',
    'belt-assessment-v2.html',
]

# All stripe files
STRIPE_PATTERNS = [
    '*-stripe*-gamified.html',
]

def add_dark_mode_css(content):
    """Add dark mode CSS link"""
    
    css_link = '<link rel="stylesheet" href="css/dark-mode.css">'
    
    if 'css/dark-mode.css' in content:
        return content, False
    
    # Find existing CSS links
    css_pattern = r'(<link[^>]*rel="stylesheet"[^>]*>)'
    
    if re.search(css_pattern, content):
        # Insert after first CSS link
        content = re.sub(css_pattern, r'\1\n    ' + css_link, content, count=1)
        return content, True
    
    # Fallback: before </head>
    head_pattern = r'(</head>)'
    if re.search(head_pattern, content):
        content = re.sub(head_pattern, '    ' + css_link + '\n\1', content, count=1)
        return content, True
    
    return content, False

def add_dark_mode_js(content):
    """Add dark mode JavaScript"""
    
    js_script = '<script src="js/dark-mode.js"></script>'
    
    if 'js/dark-mode.js' in content:
        return content, False
    
    # Insert before </body> or before other scripts
    body_pattern = r'(</body>)'
    
    if re.search(body_pattern, content):
        content = re.sub(body_pattern, '    ' + js_script + '\n\1', content, count=1)
        return content, True
    
    return content, False

def add_dark_mode(filepath):
    """Apply dark mode to a file"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # 1. Add CSS
    content, changed = add_dark_mode_css(content)
    if changed:
        changes.append("dark mode CSS")
    
    # 2. Add JS
    content, changed = add_dark_mode_js(content)
    if changed:
        changes.append("dark mode JS")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes
    
    return False, []

def main():
    print("=" * 80)
    print("🌙 ADDING DARK MODE SUPPORT")
    print("=" * 80)
    print()
    
    files_to_update = []
    
    # Add priority pages
    for page in PRIORITY_PAGES:
        if Path(page).exists():
            files_to_update.append(Path(page))
    
    # Add stripe files (sample first 10)
    for pattern in STRIPE_PATTERNS:
        for file in list(Path('.').glob(pattern))[:10]:
            if any(skip in str(file) for skip in ['node_modules', '.git', 'react-app']):
                continue
            if file not in files_to_update:
                files_to_update.append(file)
    
    files_to_update.sort()
    
    print(f"Found {len(files_to_update)} files to update\n")
    
    updated = 0
    skipped = 0
    
    for filepath in files_to_update:
        print(f"📝 {filepath.name}...")
        try:
            success, changes = add_dark_mode(filepath)
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
    print(f"✅ Updated: {updated}/{len(files_to_update)}")
    print(f"⏭️  Skipped: {skipped}")
    print("=" * 80)

if __name__ == '__main__':
    main()

