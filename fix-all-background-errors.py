#!/usr/bin/env python3
"""
Fix all background error sources systematically
"""

import re
import os
from pathlib import Path

def fix_error_handlers(filepath):
    """Fix error handlers in a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        filename = Path(filepath).name
        changes = []
        
        # 1. Fix Service Worker registrations - add proper error handling
        sw_pattern = r"(navigator\.serviceWorker\.register\([^)]+\))(?:\s*\.catch\([^)]+\))?"
        
        def replace_sw(match):
            reg_code = match.group(1)
            # Check if already has catch
            after_match = content[content.find(match.group(0)) + len(match.group(0)):content.find(match.group(0)) + len(match.group(0)) + 100]
            if '.catch' in after_match:
                return match.group(0)  # Already handled
            
            return reg_code + '''

        .then(() => {
            // Service Worker registered successfully
            if (console && console.debug) {
                console.debug('[SW] Registered successfully');
            }
        })
        .catch(err => {
            // Silently handle - SW registration can fail in various scenarios
            // (user in private mode, older browser, etc.) - this is expected
            if (console && console.debug) {
                console.debug('[SW] Registration note:', err.message || err);
            }
            // Don't let this bubble up to error handlers
            return Promise.resolve(); // Swallow the error
        })'''
        
        new_content = re.sub(sw_pattern, replace_sw, content)
        if new_content != content:
            changes.append("Fixed service worker error handling")
            content = new_content
        
        # 2. Wrap localStorage operations in try/catch
        ls_pattern = r"localStorage\.(getItem|setItem|removeItem)\(([^)]+)\)"
        
        def wrap_storage(match):
            method = match.group(1)
            key = match.group(2)
            
            # Check if already in try/catch
            match_idx = content.find(match.group(0))
            prev_200 = content[max(0, match_idx-200):match_idx]
            
            if 'try' in prev_200 and '{' in prev_200[-50:]:
                return match.group(0)  # Already protected
            
            # Wrap in try/catch
            if method == 'getItem':
                return f'''(function() {{
                    try {{
                        return localStorage.getItem({key});
                    }} catch(e) {{
                        console.debug('[Storage] getItem failed:', e);
                        return null;
                    }}
                }})()'''
            elif method == 'setItem':
                return f'''(function() {{
                    try {{
                        localStorage.setItem({key}, arguments[1]);
                    }} catch(e) {{
                        console.debug('[Storage] setItem failed (quota exceeded?):', e);
                    }}
                }})()'''
            else:
                return f'''(function() {{
                    try {{
                        localStorage.removeItem({key});
                    }} catch(e) {{
                        console.debug('[Storage] removeItem failed:', e);
                    }}
                }})()'''
        
        # Only wrap unprotected ones - be careful with this
        # Let's just identify them for now
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed {filename}: {', '.join(changes)}")
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error fixing {filepath}: {e}")
        return False

# Fix service worker registrations in key files
key_files = [
    'gym-dashboard.html',
    'index.html',
    'learning-hub.html',
    'index-DUAL-ENTRY.html'
]

fixed_count = 0
for file in key_files:
    if Path(file).exists():
        if fix_error_handlers(file):
            fixed_count += 1

print(f"\n✅ Fixed {fixed_count} file(s)")

