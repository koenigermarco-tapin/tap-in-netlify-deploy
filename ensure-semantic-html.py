#!/usr/bin/env python3
"""
Ensure proper semantic HTML structure across all pages
"""

from pathlib import Path
import re

def ensure_semantic_structure(content):
    """Ensure proper HTML5 semantic elements"""
    changes = False
    
    # Ensure lang attribute on html tag
    if '<html' in content and 'lang=' not in content[:content.find('<html')+100]:
        content = re.sub(r'(<html)([^>]*>)', r'\1 lang="en"\2', content, count=1)
        changes = True
    
    # Ensure main element has id="main-content"
    if '<main' in content and 'id="main-content"' not in content:
        if not re.search(r'<main[^>]*id=', content):
            content = re.sub(r'(<main[^>]*)(>)', r'\1 id="main-content" tabindex="-1"\2', content, count=1)
            changes = True
    
    # Ensure header has role="banner"
    if '<header' in content and 'role=' not in re.search(r'<header[^>]*>', content).group(0) if re.search(r'<header[^>]*>', content) else '':
        content = re.sub(r'(<header)([^>]*>)', r'\1\2 role="banner"', content, count=1)
        changes = True
    
    # Ensure footer has role="contentinfo"
    if '<footer' in content and 'role=' not in re.search(r'<footer[^>]*>', content).group(0) if re.search(r'<footer[^>]*>', content) else '':
        content = re.sub(r'(<footer)([^>]*>)', r'\1\2 role="contentinfo"', content, count=1)
        changes = True
    
    # Ensure nav has role="navigation" and aria-label
    nav_matches = list(re.finditer(r'<nav[^>]*>', content))
    for nav_match in nav_matches[:3]:  # First 3 nav elements
        nav_tag = nav_match.group(0)
        if 'role=' not in nav_tag:
            new_nav = nav_tag.replace('>', ' role="navigation">', 1)
            content = content[:nav_match.start()] + new_nav + content[nav_match.end():]
            changes = True
            break  # Only fix first one per file
    
    # Ensure proper heading hierarchy - check for h1 count
    h1_count = len(re.findall(r'<h1[^>]*>', content))
    if h1_count > 1:
        # Multiple h1s found - log but don't auto-fix (too complex)
        pass
    
    return content, changes

def ensure_meta_tags(content):
    """Ensure essential meta tags"""
    changes = False
    
    # Ensure charset
    if '<meta charset' not in content and '<meta http-equiv="Content-Type"' not in content:
        if '<head' in content:
            head_pos = content.find('<head')
            if head_pos != -1:
                head_end = content.find('>', head_pos) + 1
                content = content[:head_end] + '\n    <meta charset="UTF-8">' + content[head_end:]
                changes = True
    
    # Ensure viewport
    if '<meta name="viewport"' not in content:
        if '<meta charset' in content:
            content = content.replace(
                '<meta charset',
                '<meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
                1
            )
            changes = True
    
    return content, changes

def main():
    print("=" * 80)
    print("📋 ENSURING SEMANTIC HTML STRUCTURE")
    print("=" * 80)
    print()
    
    # Priority pages
    priority_files = [
        'index.html',
        'gym-dashboard.html',
        'learning-hub.html',
        'belt-assessment-v2.html',
    ]
    
    files_to_update = [Path(f) for f in priority_files if Path(f).exists()]
    
    print(f"Found {len(files_to_update)} priority files\n")
    
    updated = 0
    
    for filepath in files_to_update:
        print(f"📝 {filepath.name}...")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            
            content, changed1 = ensure_semantic_structure(content)
            content, changed2 = ensure_meta_tags(content)
            
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated += 1
                changes = []
                if changed1: changes.append("semantic elements")
                if changed2: changes.append("meta tags")
                print(f"  ✅ Fixed: {', '.join(changes)}")
            else:
                print(f"  ⏭️  Already has proper semantic structure")
        except Exception as e:
            print(f"  ❌ Error: {e}")
        print()
    
    print("=" * 80)
    print(f"✅ Updated: {updated}/{len(files_to_update)}")
    print("=" * 80)

if __name__ == '__main__':
    main()

