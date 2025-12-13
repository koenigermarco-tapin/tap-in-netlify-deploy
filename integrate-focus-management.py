#!/usr/bin/env python3
"""
Integrate Focus Management into Pages with Modals
Adds focus-management.js to pages that need it
"""

import os
import re
from pathlib import Path

# Pages that likely have modals or need focus management
MODAL_KEYWORDS = ['modal', 'popup', 'dialog', 'overlay', 'auth', 'assessment']

def has_modal_or_popup(content):
    """Check if page has modals or popups"""
    modal_patterns = [
        r'\.modal',
        r'\.popup',
        r'role="dialog"',
        r'class=".*modal.*"',
        r'class=".*popup.*"',
        r'id=".*modal.*"',
        r'id=".*popup.*"',
        r'auth-modal',
        r'overlay'
    ]
    
    for pattern in modal_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True
    return False

def already_has_focus_management(content):
    """Check if page already includes focus management"""
    return 'focus-management.js' in content or 'FocusManagement' in content

def add_focus_management_script(filepath):
    """Add focus management script to HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ⚠️  Error reading {filepath}: {e}")
        return False
    
    # Skip if already has it
    if already_has_focus_management(content):
        return False
    
    # Find insertion point (before closing </body>)
    body_close = content.rfind('</body>')
    if body_close == -1:
        # Try to find end of file
        body_close = len(content)
    
    # Script to add
    script_tag = '\n    <!-- Focus Management for Accessibility -->\n    <script src="js/focus-management.js" defer></script>\n'
    
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
    print("🎯 INTEGRATING FOCUS MANAGEMENT INTO PAGES")
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
    
    # Filter files that need focus management
    files_with_modals = []
    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if file has modals or matches keywords
            filename = os.path.basename(filepath).lower()
            has_keyword = any(keyword in filename for keyword in MODAL_KEYWORDS)
            
            if has_modal_or_popup(content) or has_keyword:
                files_with_modals.append(filepath)
        except:
            continue
    
    print(f"🔍 Found {len(files_with_modals)} files with modals/popups")
    print()
    
    # Add focus management script
    updated = 0
    skipped = 0
    
    for filepath in sorted(files_with_modals):
        rel_path = os.path.relpath(filepath, '.')
        if add_focus_management_script(filepath):
            print(f"  ✅ Updated: {rel_path}")
            updated += 1
        else:
            skipped += 1
    
    print()
    print("=" * 80)
    print(f"✅ COMPLETE: Updated {updated} files, Skipped {skipped} files")
    print("=" * 80)
    
    # Also add to main entry pages
    print()
    print("📝 Adding to main entry pages...")
    main_pages = [
        'index.html',
        'gym-dashboard.html',
        'learning-hub.html',
        'index-DUAL-ENTRY.html'
    ]
    
    for page in main_pages:
        if os.path.exists(page):
            if add_focus_management_script(page):
                print(f"  ✅ Added to: {page}")
            else:
                print(f"  ⏭️  Already has or skipped: {page}")

if __name__ == '__main__':
    main()

