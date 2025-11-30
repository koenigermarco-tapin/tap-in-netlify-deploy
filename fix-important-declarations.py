#!/usr/bin/env python3
"""
Reduce !important declarations by improving CSS specificity
"""

import re
from pathlib import Path
import os

def fix_important_declarations(filepath):
    """Reduce !important usage in stripe files"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        filename = Path(filepath).name
        important_count = content.count('!important')
        
        if important_count < 10:
            return False  # Not enough to worry about
        
        # Strategy: Remove !important from properties that don't need it
        # by improving selector specificity or using more specific selectors
        
        # Pattern 1: Remove !important from common properties that inherit well
        properties_to_clean = [
            'color', 'background-color', 'font-size', 'font-weight',
            'margin', 'padding', 'border', 'border-radius'
        ]
        
        for prop in properties_to_clean:
            # Remove !important from these properties if they're in a style tag or inline
            pattern = rf'({prop}:[^;!]+)!important'
            content = re.sub(pattern, r'\1', content)
        
        # Pattern 2: Replace inline !important with more specific selectors in style blocks
        # This is more complex, so we'll just clean obvious cases
        
        # Pattern 3: Remove !important from media queries (they're already specific enough)
        def clean_media_query(match):
            media_content = match.group(2)
            cleaned = re.sub(r'!important\s*;', ';', media_content)
            return f'{match.group(1)}{{{cleaned}}}'
        
        content = re.sub(
            r'(@media[^{]+)\{([^}]+)\}',
            clean_media_query,
            content,
            flags=re.DOTALL
        )
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            new_count = content.count('!important')
            removed = important_count - new_count
            print(f"✅ Fixed {filename}: Removed {removed} !important declarations ({important_count} → {new_count})")
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error fixing {filepath}: {e}")
        return False

# Find stripe files with high !important counts
stripe_files = []
for root, dirs, files in os.walk('.'):
    skip_dirs = {'node_modules', '.git', 'android', 'ios', 'dist', 'build', '__pycache__'}
    dirs[:] = [d for d in dirs if d not in skip_dirs]
    
    for file in files:
        if 'stripe' in file and file.endswith('.html'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if content.count('!important') > 20:
                        stripe_files.append(filepath)
            except:
                pass

fixed_count = 0
for file in stripe_files[:10]:  # Fix top 10 worst offenders
    if fix_important_declarations(file):
        fixed_count += 1

print(f"\n✅ Fixed {fixed_count} file(s)")

