#!/usr/bin/env python3
"""
Add accessibility improvements to all HTML pages
- Skip links
- ARIA labels
- Semantic HTML structure
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

def add_skip_links(content):
    """Add skip links at the beginning of body"""
    
    skip_links = '''    <!-- Skip Links for Accessibility -->
    <a href="#main-content" class="skip-link">Skip to main content</a>
    <a href="#navigation" class="skip-link">Skip to navigation</a>
'''
    
    if 'class="skip-link"' in content:
        return content, False
    
    # Insert after <body>
    body_pattern = r'(<body[^>]*>)'
    if re.search(body_pattern, content):
        content = re.sub(body_pattern, r'\1\n' + skip_links, content, count=1)
        return content, True
    
    return content, False

def add_accessibility_css(content):
    """Add accessibility CSS link"""
    
    css_link = '<link rel="stylesheet" href="css/accessibility.css">'
    
    if 'css/accessibility.css' in content:
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

def add_keyboard_nav_js(content):
    """Add keyboard navigation script"""
    
    js_script = '<script src="js/keyboard-navigation.js" defer></script>'
    
    if 'js/keyboard-navigation.js' in content:
        return content, False
    
    # Insert before </body> or </html>
    if '</body>' in content:
        content = re.sub(r'(</body>)', '    ' + js_script + '\n\1', content, count=1)
        return content, True
    elif '</html>' in content:
        content = re.sub(r'(</html>)', '    ' + js_script + '\n\1', content, count=1)
        return content, True
    
    return content, False

def add_semantic_ids(content):
    """Add semantic IDs to main and nav elements"""
    
    changes = False
    
    # Add id="main-content" to main
    if '<main' in content and 'id="main-content"' not in content:
        content = re.sub(r'(<main[^>]*)(>)', r'\1 id="main-content" tabindex="-1"\2', content, count=1)
        changes = True
    
    # Add id="navigation" to nav
    if '<nav' in content and 'id="navigation"' not in content:
        # Check if there's already an id
        if not re.search(r'<nav[^>]*id=', content):
            content = re.sub(r'(<nav[^>]*)(>)', r'\1 id="navigation"\2', content, count=1)
            changes = True
    
    return content, changes

def add_aria_labels(content):
    """Add basic ARIA labels to common elements"""
    
    changes = False
    
    # Add aria-label to close buttons
    if '×' in content or 'close' in content.lower():
        # Find button elements without aria-label that might be close buttons
        close_pattern = r'(<button[^>]*>)(\s*(?:×|Close|X))'
        if re.search(close_pattern, content, re.IGNORECASE):
            content = re.sub(
                r'(<button)([^>]*>)(\s*(?:×|Close|X))',
                r'\1\2 aria-label="Close"\3',
                content,
                count=10,
                flags=re.IGNORECASE
            )
            changes = True
    
    return content, changes

def improve_accessibility(filepath):
    """Apply all accessibility improvements"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # 1. Add skip links
    content, changed = add_skip_links(content)
    if changed:
        changes.append("skip links")
    
    # 2. Add accessibility CSS
    content, changed = add_accessibility_css(content)
    if changed:
        changes.append("accessibility CSS")
    
    # 3. Add keyboard nav JS
    content, changed = add_keyboard_nav_js(content)
    if changed:
        changes.append("keyboard navigation")
    
    # 4. Add semantic IDs
    content, changed = add_semantic_ids(content)
    if changed:
        changes.append("semantic IDs")
    
    # 5. Add basic ARIA labels
    content, changed = add_aria_labels(content)
    if changed:
        changes.append("ARIA labels")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes
    
    return False, []

def main():
    print("=" * 80)
    print("♿ ADDING ACCESSIBILITY IMPROVEMENTS")
    print("=" * 80)
    print()
    
    files_to_update = []
    
    # Add priority pages
    for page in PRIORITY_PAGES:
        if Path(page).exists():
            files_to_update.append(Path(page))
    
    files_to_update.sort()
    
    print(f"Found {len(files_to_update)} priority files to update\n")
    
    updated = 0
    skipped = 0
    
    for filepath in files_to_update:
        print(f"📝 {filepath.name}...")
        try:
            success, changes = improve_accessibility(filepath)
            if success:
                updated += 1
                print(f"  ✅ Added: {', '.join(changes)}")
            else:
                skipped += 1
                print(f"  ⏭️  Already has accessibility features")
        except Exception as e:
            print(f"  ❌ Error: {e}")
        print()
    
    print("=" * 80)
    print(f"✅ Updated: {updated}/{len(files_to_update)}")
    print(f"⏭️  Skipped: {skipped}")
    print("=" * 80)

if __name__ == '__main__':
    main()

