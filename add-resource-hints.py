#!/usr/bin/env python3
"""
Add Resource Hints to All HTML Pages
Improves performance by preconnecting to external domains
"""

import os
import re
from pathlib import Path

# Resource hints to add
RESOURCE_HINTS = """    <!-- Performance: Resource Hints -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="dns-prefetch" href="https://cdn.jsdelivr.net">
    <link rel="dns-prefetch" href="https://fonts.googleapis.com">
    <link rel="dns-prefetch" href="https://fonts.gstatic.com">
"""

# External domains that need preconnect/dns-prefetch
EXTERNAL_DOMAINS = [
    'fonts.googleapis.com',
    'fonts.gstatic.com',
    'cdn.jsdelivr.net',
    'cdnjs.cloudflare.com'
]

def has_resource_hints(content):
    """Check if file already has resource hints"""
    return 'preconnect' in content or 'dns-prefetch' in content

def find_insert_position(content):
    """Find where to insert resource hints (after charset/viewport)"""
    # Look for viewport meta tag
    viewport_match = re.search(r'<meta\s+name="viewport"', content, re.IGNORECASE)
    if viewport_match:
        # Find end of viewport tag
        end_pos = viewport_match.end()
        # Find next > or newline
        next_pos = content.find('>', end_pos)
        if next_pos != -1:
            return next_pos + 1
    
    # Fallback: after charset
    charset_match = re.search(r'<meta\s+charset="[^"]+"', content, re.IGNORECASE)
    if charset_match:
        end_pos = charset_match.end()
        next_pos = content.find('>', end_pos)
        if next_pos != -1:
            return next_pos + 1
    
    # Last resort: after <head>
    head_match = re.search(r'<head[^>]*>', content, re.IGNORECASE)
    if head_match:
        return head_match.end()
    
    return -1

def add_resource_hints_to_file(filepath):
    """Add resource hints to a single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ⚠️  Error reading {filepath}: {e}")
        return False
    
    # Skip if already has hints
    if has_resource_hints(content):
        # Check if we need to add missing ones
        needs_update = False
        for domain in EXTERNAL_DOMAINS:
            if domain not in content:
                needs_update = True
                break
        
        if not needs_update:
            return False  # Already complete
    
    # Find insertion point
    insert_pos = find_insert_position(content)
    if insert_pos == -1:
        print(f"  ⚠️  Could not find insertion point in {filepath}")
        return False
    
    # Insert resource hints
    new_content = content[:insert_pos] + '\n' + RESOURCE_HINTS + content[insert_pos:]
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    except Exception as e:
        print(f"  ⚠️  Error writing {filepath}: {e}")
        return False

def main():
    """Main function to process all HTML files"""
    print("=" * 80)
    print("🔗 ADDING RESOURCE HINTS TO ALL HTML PAGES")
    print("=" * 80)
    print()
    
    # Find all HTML files
    html_files = []
    exclude_dirs = {'node_modules', '.git', 'archive', '__pycache__', 'android', 'ios', 'dist', 'build', 'react-app'}
    
    for root, dirs, files in os.walk('.'):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                html_files.append(filepath)
    
    print(f"📋 Found {len(html_files)} HTML files")
    print()
    
    # Process files
    updated = 0
    skipped = 0
    
    for filepath in sorted(html_files):
        rel_path = os.path.relpath(filepath, '.')
        if add_resource_hints_to_file(filepath):
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

