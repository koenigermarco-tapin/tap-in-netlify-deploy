#!/usr/bin/env python3
"""
Fix unhandled fetch calls that can cause background errors
"""

import re
from pathlib import Path

def fix_unhandled_fetch(filepath):
    """Wrap fetch calls in proper error handling"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        filename = Path(filepath).name
        
        # Find fetch calls without .catch
        fetch_pattern = r'fetch\([^)]+\)'
        fetch_matches = list(re.finditer(fetch_pattern, content))
        
        changes = 0
        for match in reversed(fetch_matches):  # Reverse to maintain indices
            fetch_call = match.group(0)
            start_idx = match.start()
            end_idx = match.end()
            
            # Check if already has .catch or .then().catch
            next_100 = content[end_idx:end_idx+100]
            if '.catch' in next_100 or '.then' in next_100:
                continue  # Already handled
            
            # Check if in try/catch
            prev_200 = content[max(0, start_idx-200):start_idx]
            if 'try' in prev_200 and '{' in prev_200[-50:]:
                continue  # Already in try/catch
            
            # Wrap with .catch
            safe_fetch = f'''{fetch_call}
                .catch(err => {{
                    console.debug('[Fetch] Request failed (non-critical):', err.message || err);
                    return Promise.reject(err); // Re-throw for caller to handle
                }})'''
            
            content = content[:start_idx] + safe_fetch + content[end_idx:]
            changes += 1
        
        if changes > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed {filename}: Wrapped {changes} fetch call(s)")
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error fixing {filepath}: {e}")
        return False

# Fix known files with unhandled fetch
files_to_fix = [
    'gym-dashboard.html',
    'js/talent-finder.js',
    'js/progress-sync-init.js'
]

fixed_count = 0
for file in files_to_fix:
    if Path(file).exists():
        if fix_unhandled_fetch(file):
            fixed_count += 1

print(f"\n✅ Fixed {fixed_count} file(s)")

