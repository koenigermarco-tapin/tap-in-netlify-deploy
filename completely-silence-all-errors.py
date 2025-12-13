#!/usr/bin/env python3
"""
Completely Silence All Background Error Messages
- Replace all console.error with silent logging
- Replace all console.warn with silent logging  
- Ensure error-suppressor.js loads FIRST
- Remove any remaining error notifications
"""

import re
from pathlib import Path

def silence_console_errors_in_html():
    """Replace console.error and console.warn with silent versions in HTML"""
    html_files = list(Path('.').rglob('*.html'))
    html_files = [f for f in html_files if 'archive' not in str(f) and 'node_modules' not in str(f)]
    
    critical_files = [
        'gym-dashboard.html',
        'gym-dashboard-de.html',
        'learning-hub.html',
        'learning-hub-de.html',
        'index.html',
        'belt-assessment-v2.html',
        'belt-assessment-v2-de.html',
    ]
    
    for file_path in critical_files:
        if not Path(file_path).exists():
            continue
        
        try:
            content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
            original = content
            
            # Replace console.error calls (but keep localhost logging)
            # Pattern: console.error(...) -> silent version
            content = re.sub(
                r'console\.error\(([^)]+)\)',
                r'if (window.location.hostname === \'localhost\' || window.location.hostname === \'127.0.0.1\') { console.error(\1); }',
                content
            )
            
            # Replace console.warn calls
            content = re.sub(
                r'console\.warn\(([^)]+)\)',
                r'if (window.location.hostname === \'localhost\' || window.location.hostname === \'127.0.0.1\') { console.warn(\1); }',
                content
            )
            
            if content != original:
                Path(file_path).write_text(content, encoding='utf-8')
                print(f"✅ Silenced console errors in {file_path}")
        except Exception as e:
            print(f"⚠️  Error processing {file_path}: {e}")

def ensure_error_suppressor_first():
    """Ensure error-suppressor.js loads FIRST before any other scripts"""
    critical_files = [
        'gym-dashboard.html',
        'gym-dashboard-de.html',
        'learning-hub.html',
        'learning-hub-de.html',
        'index.html',
        'belt-assessment-v2.html',
        'belt-assessment-v2-de.html',
    ]
    
    suppressor_tag = '<script src="js/error-suppressor.js"></script>'
    
    for file_path in critical_files:
        if not Path(file_path).exists():
            continue
        
        try:
            content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
            
            # Remove all instances of error-suppressor
            content = re.sub(r'<script[^>]*error-suppressor\.js[^>]*></script>', '', content, flags=re.IGNORECASE)
            
            # Insert right after <head> tag
            if '<head>' in content:
                content = content.replace('<head>', f'<head>\n    {suppressor_tag}', 1)
                Path(file_path).write_text(content, encoding='utf-8')
                print(f"✅ Error suppressor now loads FIRST in {file_path}")
            elif '<head ' in content:
                # Handle <head> with attributes
                match = re.search(r'<head[^>]*>', content)
                if match:
                    pos = match.end()
                    content = content[:pos] + f'\n    {suppressor_tag}' + content[pos:]
                    Path(file_path).write_text(content, encoding='utf-8')
                    print(f"✅ Error suppressor now loads FIRST in {file_path}")
        except Exception as e:
            print(f"⚠️  Error processing {file_path}: {e}")

def add_global_error_suppression():
    """Add global error suppression script to all critical pages"""
    suppression_script = '''
    <!-- Global Error Suppression - Must be FIRST -->
    <script>
    (function() {
        'use strict';
        
        // Suppress ALL error notifications immediately
        const originalError = window.console.error;
        const originalWarn = window.console.warn;
        
        window.console.error = function() {
            // Only log in development
            if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
                originalError.apply(console, arguments);
            }
        };
        
        window.console.warn = function() {
            // Only log in development
            if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
                originalWarn.apply(console, arguments);
            }
        };
        
        // Prevent all error popups
        window.addEventListener('error', function(e) {
            e.preventDefault();
            return false;
        }, true);
        
        window.addEventListener('unhandledrejection', function(e) {
            e.preventDefault();
            return false;
        });
    })();
    </script>
    '''
    
    critical_files = [
        'gym-dashboard.html',
        'gym-dashboard-de.html',
        'learning-hub.html',
        'learning-hub-de.html',
        'index.html',
        'belt-assessment-v2.html',
        'belt-assessment-v2-de.html',
    ]
    
    for file_path in critical_files:
        if not Path(file_path).exists():
            continue
        
        try:
            content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
            
            # Check if already added
            if 'Global Error Suppression' in content:
                continue
            
            # Add right after <head>
            if '<head>' in content:
                content = content.replace('<head>', f'<head>{suppression_script}', 1)
                Path(file_path).write_text(content, encoding='utf-8')
                print(f"✅ Added global error suppression to {file_path}")
        except Exception as e:
            print(f"⚠️  Error processing {file_path}: {e}")

def main():
    print("🔇 Completely Silencing All Background Error Messages...\n")
    
    print("1. Adding global error suppression...")
    add_global_error_suppression()
    
    print("\n2. Ensuring error suppressor loads FIRST...")
    ensure_error_suppressor_first()
    
    print("\n✅ All error messages are now completely silenced!")

if __name__ == '__main__':
    main()

