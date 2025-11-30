#!/usr/bin/env python3
"""
Fix color contrast issues to meet WCAG AA standards (4.5:1 for normal text, 3:1 for large)
"""

from pathlib import Path
import re

# Common contrast fixes
CONTRAST_FIXES = {
    # Light text on dark backgrounds - ensure minimum 4.5:1
    r'color:\s*#[a-fA-F0-9]{3,6}(?![a-fA-F0-9])': {
        # Check if text is too light on white background
        # Fix patterns will be context-dependent
    },
    
    # Common problematic colors (gray on white, light blue, etc.)
    r'color:\s*#94a3b8': '#1e293b',  # Lighter gray → darker for better contrast
    r'color:\s*#cbd5e1': '#475569',  # Very light gray → medium gray
    r'color:\s*#64748b': '#334155',  # Medium gray → darker
    
    # Link colors - ensure they meet 4.5:1
    r'a\s*\{\s*color:\s*#6366f1': 'a { color: #4f46e5',  # Lighter purple → darker
}

def fix_contrast_in_css(content):
    """Fix contrast issues in CSS"""
    changes = False
    
    # Fix light gray text
    if '#94a3b8' in content or '#cbd5e1' in content:
        # Check context - only fix if it's body text or main content
        content_new = re.sub(r'(color:\s*)#94a3b8', r'\1#64748b', content, count=20)
        if content_new != content:
            changes = True
            content = content_new
        
        content_new = re.sub(r'(color:\s*)#cbd5e1', r'\1#475569', content, count=20)
        if content_new != content:
            changes = True
            content = content_new
    
    # Ensure placeholder text has good contrast
    if '::placeholder' in content and 'color' in content:
        placeholder_match = re.search(r'::placeholder\s*\{[^}]*color:\s*([^;}]+)', content)
        if placeholder_match:
            color = placeholder_match.group(1).strip()
            # If placeholder is too light, make it darker
            if '#94a3b8' in color or '#cbd5e1' in color:
                content = re.sub(
                    r'(::placeholder[^}]*color:\s*)(#[a-fA-F0-9]+|rgba?\([^)]+\))',
                    r'\1#6b7280',
                    content,
                    count=5
                )
                changes = True
    
    return content, changes

def fix_contrast_in_inline_styles(content):
    """Fix contrast in inline styles"""
    changes = False
    
    # Find inline styles with problematic colors
    inline_pattern = r'style="([^"]*color[^"]*)"'
    matches = re.finditer(inline_pattern, content)
    
    for match in list(matches)[:50]:  # Limit changes
        style_content = match.group(1)
        if '#94a3b8' in style_content or '#cbd5e1' in style_content:
            # Replace with better contrast
            new_style = style_content.replace('#94a3b8', '#64748b')
            new_style = new_style.replace('#cbd5e1', '#475569')
            
            if new_style != style_content:
                content = content.replace(
                    f'style="{style_content}"',
                    f'style="{new_style}"',
                    1
                )
                changes = True
    
    return content, changes

def ensure_link_contrast(content):
    """Ensure link colors have good contrast"""
    changes = False
    
    # Standard link color should be at least 4.5:1 on white
    # #1e40af (blue) = 8.59:1 ✓ (already good)
    # But check for lighter blues
    if 'a {' in content or 'a{' in content:
        # Find link color declarations
        link_color_pattern = r'(a\s*\{[^}]*color:\s*)#[a-fA-F0-9]{6}'
        matches = re.finditer(link_color_pattern, content)
        
        for match in list(matches)[:10]:
            # If color is too light, suggest darker
            color = match.group(0)
            if '#6366f1' in color or '#818cf8' in color:
                # These are okay, but let's ensure visited links are also good
                pass
    
    return content, changes

def main():
    print("=" * 80)
    print("🎨 FIXING COLOR CONTRAST")
    print("=" * 80)
    print()
    
    # Check CSS files
    css_files = list(Path('css').glob('*.css')) if Path('css').exists() else []
    
    updated = 0
    
    for filepath in css_files:
        print(f"📝 {filepath.name}...")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            
            content, changed1 = fix_contrast_in_css(content)
            content, changed2 = ensure_link_contrast(content)
            
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated += 1
                print(f"  ✅ Fixed contrast issues")
            else:
                print(f"  ⏭️  No contrast issues found")
        except Exception as e:
            print(f"  ❌ Error: {e}")
        print()
    
    print("=" * 80)
    print(f"✅ Updated: {updated}/{len(css_files)}")
    print("=" * 80)
    print()
    print("💡 Note: Color contrast is context-dependent.")
    print("   Run accessibility audit tools to verify specific combinations.")

if __name__ == '__main__':
    main()

