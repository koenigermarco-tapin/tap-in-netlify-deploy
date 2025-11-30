#!/usr/bin/env python3
"""
Add micro-interactions to all HTML pages
"""

from pathlib import Path
import re

# Priority pages
PRIORITY_PAGES = [
    'index.html',
    'gym-dashboard.html',
    'learning-hub.html',
    'belt-assessment-v2.html',
]

def add_micro_interactions(filepath):
    """Add micro-interactions script to file"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    js_script = '<script src="js/micro-interactions.js"></script>'
    
    if 'js/micro-interactions.js' in content:
        return content, False
    
    # Insert before </body>
    body_pattern = r'(</body>)'
    if re.search(body_pattern, content):
        content = re.sub(body_pattern, '    ' + js_script + '\n\1', content, count=1)
        return content, True
    
    return content, False

def main():
    print("=" * 80)
    print("✨ ADDING MICRO-INTERACTIONS")
    print("=" * 80)
    print()
    
    files_to_update = []
    
    for page in PRIORITY_PAGES:
        if Path(page).exists():
            files_to_update.append(Path(page))
    
    print(f"Found {len(files_to_update)} files to update\n")
    
    updated = 0
    skipped = 0
    
    for filepath in files_to_update:
        print(f"📝 {filepath.name}...")
        try:
            content, changed = add_micro_interactions(filepath)
            if changed:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated += 1
                print(f"  ✅ Added micro-interactions")
            else:
                skipped += 1
                print(f"  ⏭️  Already has micro-interactions")
        except Exception as e:
            print(f"  ❌ Error: {e}")
        print()
    
    print("=" * 80)
    print(f"✅ Updated: {updated}/{len(files_to_update)}")
    print(f"⏭️  Skipped: {skipped}")
    print("=" * 80)

if __name__ == '__main__':
    main()

