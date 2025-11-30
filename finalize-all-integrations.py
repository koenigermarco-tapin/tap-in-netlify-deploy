#!/usr/bin/env python3
"""
Finalize all integrations - ensure dark mode and micro-interactions are in all priority pages
"""

from pathlib import Path
import re

PRIORITY_PAGES = [
    'index.html',
    'gym-dashboard.html',
    'learning-hub.html',
    'belt-assessment-v2.html',
]

def ensure_scripts(filepath):
    """Ensure dark mode and micro-interactions scripts are present"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # Check and add dark mode CSS
    if 'css/dark-mode.css' not in content:
        css_link = '<link rel="stylesheet" href="css/dark-mode.css">'
        if 'css/core-styles.css' in content:
            content = content.replace(
                '<link rel="stylesheet" href="css/core-styles.css">',
                '<link rel="stylesheet" href="css/core-styles.css">\n    ' + css_link
            )
            changes.append("dark mode CSS")
        elif '</head>' in content:
            content = re.sub(r'(</head>)', '    ' + css_link + '\n\1', content)
            changes.append("dark mode CSS")
    
    # Check and add dark mode JS
    if 'js/dark-mode.js' not in content:
        js_dark = '<script src="js/dark-mode.js"></script>'
        if '</body>' in content:
            content = re.sub(r'(</body>)', '    ' + js_dark + '\n\1', content)
            changes.append("dark mode JS")
    
    # Check and add micro-interactions JS
    if 'js/micro-interactions.js' not in content:
        js_micro = '<script src="js/micro-interactions.js"></script>'
        if '</body>' in content:
            content = re.sub(r'(</body>)', '    ' + js_micro + '\n\1', content)
            changes.append("micro-interactions JS")
    
    # Check and add enhanced loading states
    if 'js/enhanced-loading-states.js' not in content:
        js_loading = '<script src="js/enhanced-loading-states.js"></script>'
        if '</body>' in content:
            content = re.sub(r'(</body>)', '    ' + js_loading + '\n\1', content)
            changes.append("loading states JS")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes
    
    return False, []

def main():
    print("=" * 80)
    print("🔧 FINALIZING ALL INTEGRATIONS")
    print("=" * 80)
    print()
    
    updated = 0
    
    for filename in PRIORITY_PAGES:
        filepath = Path(filename)
        if not filepath.exists():
            continue
        
        print(f"📝 {filename}...")
        try:
            success, changes = ensure_scripts(filepath)
            if success:
                updated += 1
                print(f"  ✅ Added: {', '.join(changes)}")
            else:
                print(f"  ✅ Already complete")
        except Exception as e:
            print(f"  ❌ Error: {e}")
        print()
    
    print("=" * 80)
    print(f"✅ Finalized: {updated}/{len(PRIORITY_PAGES)}")
    print("=" * 80)

if __name__ == '__main__':
    main()

