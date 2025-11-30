#!/usr/bin/env python3
"""
Comprehensive fix for all background error sources
"""

import re
import os
from pathlib import Path

fixes_applied = []

def fix_service_worker_registrations(filepath):
    """Fix service worker registrations to not trigger errors"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        filename = Path(filepath).name
        
        # Pattern: navigator.serviceWorker.register('...').catch(...)
        # Replace with better error handling
        pattern = r"(navigator\.serviceWorker\.register\(['\"][^'\"]+['\"]\))(\s*\.catch\([^)]+\))?"
        
        def replace_sw(match):
            reg_code = match.group(1)
            existing_catch = match.group(2) if match.group(2) else ''
            
            # If already has good catch, leave it
            if existing_catch and 'console.debug' in existing_catch:
                return match.group(0)
            
            # Add proper error handling
            return reg_code + '''
        .then(() => {
            if (console && console.debug) {
                console.debug('[SW] Registered successfully');
            }
        })
        .catch(err => {
            // Expected failures: private mode, older browsers, etc.
            if (console && console.debug) {
                console.debug('[SW] Registration note:', err.message || err);
            }
            return Promise.resolve(); // Swallow error
        })'''
        
        new_content = re.sub(pattern, replace_sw, content)
        
        if new_content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            fixes_applied.append(f"{filename}: Fixed service worker error handling")
            return True
        return False
        
    except Exception as e:
        print(f"Error fixing {filepath}: {e}")
        return False

def remove_duplicate_error_handlers(filepath):
    """Remove duplicate error handlers, keep only one"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        filename = Path(filepath).name
        
        # Count error listeners
        error_listeners = list(re.finditer(
            r"window\.addEventListener\(['\"]error['\"][\s\S]{0,500}?\)[\s;]",
            content,
            re.MULTILINE
        ))
        
        if len(error_listeners) <= 1:
            return False  # No duplicates
        
        # Keep only the last one (usually most refined)
        for match in error_listeners[:-1]:
            # Check if this is the unified handler we want to keep
            if 'TAPIN_ERROR_SYSTEM' in match.group(0) or 'unified-error-system' in match.group(0):
                continue  # Keep unified handler
            
            # Remove duplicate
            content = content.replace(match.group(0), '/* Duplicate error handler removed */\n')
            fixes_applied.append(f"{filename}: Removed duplicate error handler")
        
        # Do same for rejection handlers
        rejection_listeners = list(re.finditer(
            r"window\.addEventListener\(['\"]unhandledrejection['\"][\s\S]{0,500}?\)[\s;]",
            content,
            re.MULTILINE
        ))
        
        if len(rejection_listeners) > 1:
            for match in rejection_listeners[:-1]:
                if 'TAPIN_ERROR_SYSTEM' in match.group(0) or 'unified-error-system' in match.group(0):
                    continue
                content = content.replace(match.group(0), '/* Duplicate rejection handler removed */\n')
                fixes_applied.append(f"{filename}: Removed duplicate rejection handler")
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"Error fixing {filepath}: {e}")
        return False

def add_unified_error_system(filepath):
    """Add unified error system to HTML files"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has unified error system
        if 'unified-error-system.js' in content or 'TAPIN_ERROR_SYSTEM' in content:
            return False
        
        # Check if file has error handlers (needs unified system)
        if 'addEventListener' in content and 'error' in content:
            filename = Path(filepath).name
            
            # Add unified error system before </body>
            unified_script = '''
<!-- Unified Error Handling System -->
<script src="js/unified-error-system.js"></script>
'''
            
            if '</body>' in content:
                content = content.replace('</body>', unified_script + '\n</body>')
                fixes_applied.append(f"{filename}: Added unified error system")
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True
        
        return False
        
    except Exception as e:
        print(f"Error fixing {filepath}: {e}")
        return False

# Main fix process
print("🔧 Fixing background errors comprehensively...")
print()

# Find key files
key_files = []
for root, dirs, files in os.walk('.'):
    skip_dirs = {'.git', 'node_modules', 'android', 'ios', 'dist', 'build', '__pycache__', 'react-app'}
    dirs[:] = [d for d in dirs if d not in skip_dirs]
    
    for file in files:
        if file.endswith('.html') and any(key in file for key in ['gym-dashboard', 'index', 'learning-hub']):
            key_files.append(os.path.join(root, file))

print(f"Found {len(key_files)} key files to fix")
print()

# Fix each file
fixed_count = 0
for file in key_files:
    changed = False
    changed |= fix_service_worker_registrations(file)
    changed |= remove_duplicate_error_handlers(file)
    changed |= add_unified_error_system(file)
    
    if changed:
        fixed_count += 1

print()
print("=" * 70)
print("✅ FIXES APPLIED")
print("=" * 70)
for fix in fixes_applied:
    print(f"  • {fix}")

print()
print(f"✅ Fixed {fixed_count} file(s)")
print(f"📊 Total fixes: {len(fixes_applied)}")

