#!/usr/bin/env python3
"""
Inline Critical CSS into Key Pages
Reads css/critical.css and inlines it in <head> of key pages
"""

import os
import re

# Key pages that need critical CSS inlining
KEY_PAGES = [
    'index.html',
    'index-DUAL-ENTRY.html',
    'gym-dashboard.html',
    'learning-hub.html'
]

CRITICAL_CSS_PATH = 'css/critical.css'

def read_critical_css():
    """Read the critical CSS file"""
    try:
        with open(CRITICAL_CSS_PATH, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"⚠️  Error reading {CRITICAL_CSS_PATH}: {e}")
        return None

def has_inline_critical_css(content):
    """Check if page already has inline critical CSS"""
    return 'Critical CSS' in content or 'critical.css' in content or '/* Critical Above-the-Fold CSS */' in content

def inline_critical_css(filepath, critical_css):
    """Inline critical CSS in HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ⚠️  Error reading {filepath}: {e}")
        return False
    
    # Skip if already has it
    if has_inline_critical_css(content):
        print(f"  ⏭️  Already has critical CSS: {os.path.basename(filepath)}")
        return False
    
    # Find <head> tag
    head_match = re.search(r'<head[^>]*>', content, re.IGNORECASE)
    if not head_match:
        print(f"  ⚠️  No <head> tag found in {filepath}")
        return False
    
    head_end = head_match.end()
    
    # Create inline style tag with critical CSS
    critical_css_tag = f'\n    <!-- Critical CSS - Inlined for Performance -->\n    <style>\n{critical_css}\n    </style>'
    
    # Insert after <head>
    new_content = content[:head_end] + critical_css_tag + content[head_end:]
    
    # Also add async loading for full CSS (if not already present)
    # Look for css/core-styles.css link
    css_link_pattern = r'<link[^>]*href=["\']css/core-styles\.css["\']'
    if re.search(css_link_pattern, new_content):
        # Replace with async loading version
        async_css = '''<link rel="preload" href="css/core-styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="css/core-styles.css"></noscript>'''
        
        # Replace first occurrence of core-styles.css link
        new_content = re.sub(css_link_pattern, async_css, new_content, count=1, flags=re.IGNORECASE)
    
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
    print("⚡ INLINING CRITICAL CSS IN KEY PAGES")
    print("=" * 80)
    print()
    
    # Read critical CSS
    critical_css = read_critical_css()
    if not critical_css:
        print("❌ Could not read critical CSS file!")
        return
    
    print(f"📄 Read critical CSS ({len(critical_css)} bytes)")
    print()
    
    # Process key pages
    updated = 0
    skipped = 0
    not_found = 0
    
    for page in KEY_PAGES:
        if not os.path.exists(page):
            print(f"  ⚠️  Not found: {page}")
            not_found += 1
            continue
        
        rel_path = os.path.relpath(page, '.')
        if inline_critical_css(page, critical_css):
            print(f"  ✅ Updated: {rel_path}")
            updated += 1
        else:
            skipped += 1
    
    print()
    print("=" * 80)
    print(f"✅ COMPLETE: Updated {updated} files, Skipped {skipped} files, Not Found {not_found} files")
    print("=" * 80)
    print()
    print("📝 Next steps:")
    print("   - Test page load performance")
    print("   - Verify no visual regressions")
    print("   - Check Lighthouse scores")

if __name__ == '__main__':
    main()

