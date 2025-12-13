#!/usr/bin/env python3
"""
Fix All Background Error Messages
Replace alert() calls and ensure error suppressor is loaded on all pages
"""

import re
from pathlib import Path

def fix_gym_dashboard_alerts():
    """Fix alert() calls in gym-dashboard.html"""
    file_path = 'gym-dashboard.html'
    
    if not Path(file_path).exists():
        print(f"⚠️  File not found: {file_path}")
        return
    
    content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
    original = content
    
    # Replace alert calls with silent logging
    patterns = [
        (r"alert\('Stripe page not found\. Starting fresh\.'\);", 
         "// Silent: Clear invalid progress\n                    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {\n                        console.log('ℹ️ Stripe page not found, starting fresh');\n                    }"),
        (r"alert\('Error loading saved progress\. Starting fresh\.'\);", 
         "// Silent: Clear invalid progress\n                    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {\n                        console.log('ℹ️ Error loading saved progress, starting fresh');\n                    }"),
    ]
    
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    
    if content != original:
        Path(file_path).write_text(content, encoding='utf-8')
        print(f"✅ Fixed alert() calls in {file_path}")
    else:
        print(f"ℹ️  No alert() calls found in {file_path}")

def ensure_error_suppressor_loaded():
    """Ensure error-suppressor.js is loaded early on all critical pages"""
    critical_files = [
        'gym-dashboard.html',
        'gym-dashboard-de.html',
        'learning-hub.html',
        'learning-hub-de.html',
        'index.html',
        'belt-assessment-v2.html',
        'belt-assessment-v2-de.html',
    ]
    
    suppressor_script = '<script src="js/error-suppressor.js"></script>'
    
    for file_path in critical_files:
        if not Path(file_path).exists():
            continue
        
        content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
        
        # Check if error suppressor is already loaded
        if 'error-suppressor.js' in content:
            # Make sure it's loaded early (before other scripts)
            if suppressor_script in content[:2000]:  # Check first 2000 chars
                print(f"✅ {file_path}: Error suppressor already loaded early")
                continue
            else:
                # Move it to the top
                lines = content.split('\n')
                head_end = None
                for i, line in enumerate(lines):
                    if '</head>' in line:
                        head_end = i
                        break
                
                if head_end:
                    # Remove existing suppressor script
                    lines = [l for l in lines if 'error-suppressor.js' not in l]
                    # Insert at top of head
                    for i, line in enumerate(lines):
                        if '<head' in line:
                            lines.insert(i + 1, f'    {suppressor_script}')
                            break
                    
                    Path(file_path).write_text('\n'.join(lines), encoding='utf-8')
                    print(f"✅ {file_path}: Moved error suppressor to top")
        else:
            # Add error suppressor
            content = content.replace('<head>', f'<head>\n    {suppressor_script}', 1)
            Path(file_path).write_text(content, encoding='utf-8')
            print(f"✅ {file_path}: Added error suppressor")

def main():
    print("🔧 Fixing All Background Error Messages...\n")
    
    print("1. Fixing alert() calls in gym-dashboard.html...")
    fix_gym_dashboard_alerts()
    
    print("\n2. Ensuring error suppressor is loaded on all pages...")
    ensure_error_suppressor_loaded()
    
    print("\n✅ All background error fixes applied!")

if __name__ == '__main__':
    main()

