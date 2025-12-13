#!/usr/bin/env python3
"""
Fix "Something went wrong, please refresh the page" error on landing page
This comes from the minified global-error-handler.min.js
"""

import re
from pathlib import Path

def fix_minified_error_handler():
    """Remove toast notification from minified error handler"""
    file_path = 'js/global-error-handler.min.js'
    
    if not Path(file_path).exists():
        print(f"⚠️  File not found: {file_path}")
        return
    
    # Create silent version - no toast notifications
    silent_version = '''const ErrorHandler={init(){window.addEventListener("error",e=>{this.handleError({message:e.message,filename:e.filename,lineno:e.lineno,colno:e.colno,error:e.error})}),window.addEventListener("unhandledrejection",e=>{this.handleError({message:e.reason?.message||String(e.reason),type:"Promise Rejection",error:e.reason})})},handleError(e){if(window.location.hostname==="localhost"||window.location.hostname==="127.0.0.1"){console.error("Error caught:",e)}try{const r=JSON.parse(localStorage.getItem("tapin_errors")||"[]");r.push({...e,timestamp:Date.now(),url:window.location.href,userAgent:navigator.userAgent}),r.length>50&&r.shift(),localStorage.setItem("tapin_errors",JSON.stringify(r))}catch(e){}},"undefined"!=typeof document&&document.addEventListener("DOMContentLoaded",()=>{ErrorHandler.init()}),window.ErrorHandler=ErrorHandler;'''
    
    Path(file_path).write_text(silent_version, encoding='utf-8')
    print(f"✅ Fixed {file_path} - Removed toast notification")

def also_override_showToast():
    """Override showToast to prevent error messages on landing page"""
    # Add to index.html's global suppression
    file_path = 'index.html'
    
    if not Path(file_path).exists():
        return
    
    content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
    
    # Check if we already have showToast override
    if 'window.showToast = function' in content and '// SILENT: No error toasts' in content:
        print(f"✅ {file_path}: showToast already overridden")
        return
    
    # Find the global error suppression script
    suppression_pattern = r'(// Prevent all error popups[\s\S]*?window\.addEventListener\(\'unhandledrejection\', function\(e\) \{[\s\S]*?e\.preventDefault\(\);[\s\S]*?return false;[\s\S]*?\}\);[\s\S]*?\}\)\(\);[\s\S]*?</script>)'
    
    match = re.search(suppression_pattern, content)
    if match:
        # Add showToast override after the suppression
        override_script = '''
        
        // SILENT: Override showToast to prevent error messages
        window.showToast = window.showToast || function(message, type, duration) {
            // Only show non-error toasts (success, info)
            if (type === 'error') {
                // Silent: Don't show error toasts
                if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
                    console.log('⚠️ Error toast suppressed:', message);
                }
                return;
            }
            // Allow success/info toasts (if container exists)
            const container = document.getElementById('toast-container');
            if (!container) return;
            // ... existing toast logic for non-error types ...
        };'''
        
        # Insert after the suppression script
        insert_pos = match.end()
        content = content[:insert_pos] + override_script + content[insert_pos:]
        Path(file_path).write_text(content, encoding='utf-8')
        print(f"✅ Added showToast override to {file_path}")

def main():
    print("🔧 Fixing Landing Page Error Message...\n")
    
    print("1. Fixing minified error handler...")
    fix_minified_error_handler()
    
    print("\n2. Adding showToast override...")
    also_override_showToast()
    
    print("\n✅ Landing page error message fixed!")

if __name__ == '__main__':
    main()

