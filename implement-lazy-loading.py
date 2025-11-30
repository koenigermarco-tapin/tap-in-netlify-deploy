#!/usr/bin/env python3
"""
Implement lazy loading for images and non-critical scripts
"""

import re
from pathlib import Path
import os

def add_lazy_loading(filepath):
    """Add lazy loading attributes to images"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        filename = Path(filepath).name
        changes = 0
        
        # Add loading="lazy" to images without it
        img_pattern = r'<img([^>]*?)(?<!/)>'
        
        def add_lazy(match):
            attrs = match.group(1)
            # Skip if already has loading attribute
            if 'loading=' in attrs:
                return match.group(0)
            
            # Skip if it's a critical image (logo, hero, etc.)
            if any(keyword in attrs.lower() for keyword in ['logo', 'hero', 'banner', 'above']):
                return match.group(0)
            
            # Add loading="lazy"
            return f'<img{attrs} loading="lazy">'
        
        new_content = re.sub(img_pattern, add_lazy, content, flags=re.IGNORECASE)
        
        if new_content != original:
            changes += 1
        
        # Add defer to non-critical scripts
        script_pattern = r'<script([^>]*?)src=["\']([^"\']+)["\']([^>]*?)(?<!/)>'
        
        def add_defer_if_needed(match):
            before_src = match.group(1)
            src = match.group(2)
            after_src = match.group(3)
            
            # Skip if already has defer or async
            if 'defer' in before_src or 'defer' in after_src or 'async' in before_src or 'async' in after_src:
                return match.group(0)
            
            # Critical scripts that shouldn't be deferred
            critical = ['analytics', 'auth-system', 'core-gamification', 'performance-optimizer']
            if any(c in src for c in critical):
                return match.group(0)
            
            # Add defer
            return f'<script{before_src}src="{src}"{after_src} defer>'
        
        new_content = re.sub(script_pattern, add_defer_if_needed, new_content)
        
        if new_content != original:
            changes += 1
        
        if new_content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Fixed {filename}: Added lazy loading")
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error fixing {filepath}: {e}")
        return False

# Apply to key pages
key_files = [
    'index.html',
    'gym-dashboard.html',
    'learning-hub.html'
]

fixed_count = 0
for file in key_files:
    if Path(file).exists():
        if add_lazy_loading(file):
            fixed_count += 1

print(f"\n✅ Fixed {fixed_count} file(s)")

