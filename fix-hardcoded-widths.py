#!/usr/bin/env python3
"""
Replace hardcoded pixel widths with responsive units in gym-dashboard.html
"""

import re
from pathlib import Path

def fix_hardcoded_widths(filepath):
    """Fix hardcoded pixel widths in a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        filename = Path(filepath).name
        changes = []
        
        # Pattern 1: width: XXXpx -> max-width: XXXpx or width: 100% with max-width
        # For small widths (< 100px), keep as max-width
        # For larger widths, convert to percentage or use max-width
        
        def replace_width(match):
            full_match = match.group(0)
            value = int(match.group(1))
            context = match.group(0)
            
            # If it's in a media query or already responsive, leave it
            if '@media' in context or 'max-width' in context:
                return full_match
            
            # Small fixed sizes (icons, badges) - keep as max-width
            if value <= 100:
                return f'max-width: {value}px; width: auto;'
            
            # Medium sizes - use percentage with max-width
            elif value <= 500:
                percentage = (value / 1000) * 100  # Assuming ~1000px container
                return f'width: min({percentage}%, {value}px);'
            
            # Large sizes - use percentage
            else:
                return f'width: 100%; max-width: {value}px;'
        
        # Replace width: XXXpx patterns
        content = re.sub(
            r'width:\s*(\d+)px(?![\w-])',
            replace_width,
            content
        )
        
        # Pattern 2: Replace fixed heights that might break
        def replace_height(match):
            value = int(match.group(1))
            if value > 200:  # Only fix large heights
                return f'min-height: {value}px; height: auto;'
            return match.group(0)
        
        content = re.sub(
            r'height:\s*(\d+)px(?![\w-])',
            replace_height,
            content
        )
        
        # Pattern 3: Replace fixed min-width with responsive
        content = re.sub(
            r'min-width:\s*(\d{3,})px',
            lambda m: f'min-width: min({int(m.group(1))/10}vw, {m.group(1)}px)',
            content
        )
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            changes_count = len([m for m in re.finditer(r'width:\s*\d+px|height:\s*\d+px', original) if m])
            print(f"✅ Fixed {filename}: Converted hardcoded dimensions to responsive")
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error fixing {filepath}: {e}")
        return False

# Fix gym-dashboard.html
files_to_fix = [
    'gym-dashboard.html'
]

fixed_count = 0
for file in files_to_fix:
    if Path(file).exists():
        if fix_hardcoded_widths(file):
            fixed_count += 1
    else:
        print(f"⚠️  File not found: {file}")

print(f"\n✅ Fixed {fixed_count} file(s)")

