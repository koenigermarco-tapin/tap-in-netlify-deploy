#!/usr/bin/env python3
"""
Fix mobile font sizes - replace small fonts (10px, 13px) with readable sizes
"""

from pathlib import Path
import re

# Files with font size issues
FILES_TO_FIX = [
    'index.html',
    'gym-dashboard.html',
    'learning-hub.html',
]

def fix_font_sizes(content):
    """Replace small font sizes with mobile-friendly sizes"""
    
    changes = 0
    
    # Replace 10px with 12px (minimum readable on mobile)
    content_new = re.sub(r'font-size:\s*10px', 'font-size: 12px', content)
    if content_new != content:
        changes += 1
        content = content_new
    
    # Replace 13px with 14px (better readability)
    content_new = re.sub(r'font-size:\s*13px', 'font-size: 14px', content)
    if content_new != content:
        changes += 1
        content = content_new
    
    # Ensure mobile breakpoint has minimum 14px for body text
    # This is a safety check - we'll add a media query if missing
    if '@media' in content and 'max-width: 768' in content:
        # Check if there's a body font-size in mobile breakpoint
        if 'font-size:' not in re.search(r'@media[^}]+max-width:\s*768[^}]+}', content, re.DOTALL):
            # Add minimum font size for mobile
            mobile_fix = '''
        /* Mobile font size fix - ensure readable text */
        body {
            font-size: 16px !important;
        }
        p, li, span {
            font-size: 14px !important;
        }
'''
            # Insert before closing brace of mobile media query
            content = re.sub(
                r'(@media[^}]+max-width:\s*768[^}]+)(})',
                r'\1' + mobile_fix + r'\2',
                content,
                count=1,
                flags=re.DOTALL
            )
    
    return content, changes > 0

def main():
    print("=" * 80)
    print("📱 FIXING MOBILE FONT SIZES")
    print("=" * 80)
    print()
    
    updated = 0
    
    for filename in FILES_TO_FIX:
        filepath = Path(filename)
        if not filepath.exists():
            print(f"⚠️  {filename} - File not found, skipping")
            continue
        
        print(f"📝 {filename}...")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            content, changed = fix_font_sizes(content)
            
            if changed or content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated += 1
                print(f"  ✅ Fixed font sizes")
            else:
                print(f"  ⏭️  No font size issues found")
        except Exception as e:
            print(f"  ❌ Error: {e}")
        print()
    
    print("=" * 80)
    print(f"✅ Updated: {updated}/{len(FILES_TO_FIX)}")
    print("=" * 80)
    print()
    print("💡 Font size changes:")
    print("   - 10px → 12px (minimum readable)")
    print("   - 13px → 14px (better readability)")
    print("   - Added mobile-specific minimum sizes")

if __name__ == '__main__':
    main()

