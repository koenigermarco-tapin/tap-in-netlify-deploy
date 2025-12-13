#!/usr/bin/env python3
"""
Fix language switcher timing issues on all pages
"""

import re
from pathlib import Path

def fix_language_switcher(file_path: Path):
    """Fix language switcher to wait for DOM ready"""
    try:
        content = file_path.read_text(encoding='utf-8')
        original = content
        
        # Pattern: Elements selected immediately with const
        pattern = r'(<script>\s*\(function\(\) \{\s*// Language Switcher Logic\s*)const (toggle|dropdown|currentFlag|currentLang) = document\.getElementById\([\'"](\w+)[\'"]\);'
        
        if re.search(pattern, content):
            # Replace const with let and move selection inside init function
            # Step 1: Change const to let declarations
            content = re.sub(
                r'const (toggle|dropdown|currentFlag|currentLang) = document\.getElementById',
                r'let \1 = document.getElementById',
                content
            )
            
            # Step 2: Wrap in init function if not already wrapped
            if 'function initLanguageSwitcher' not in content:
                # Find where event listeners start
                listener_pattern = r'(// Toggle dropdown\s+toggle\.addEventListener)'
                if re.search(listener_pattern, content):
                    # Insert init function wrapper
                    content = re.sub(
                        r'(let toggle[^\n]+\nlet dropdown[^\n]+\nlet currentFlag[^\n]+\nlet currentLang[^\n]+\n)',
                        r'\1    // Wait for DOM to be ready\n    function initLanguageSwitcher() {\n        // Get elements after DOM is ready\n        toggle = document.getElementById(\'langToggle\');\n        dropdown = document.getElementById(\'langDropdown\');\n        currentFlag = document.getElementById(\'currentFlag\');\n        currentLang = document.getElementById(\'currentLang\');\n        \n        // Check if elements exist\n        if (!toggle || !dropdown || !currentFlag || !currentLang) {\n            console.error(\'Language switcher elements not found\');\n            return;\n        }\n        \n        ',
                        content
                    )
                    
                    # Close the function and add initialization
                    content = re.sub(
                        r'(\s+\}\);\s*</script>)',
                        r'\n    }\n    \n    // Initialize when DOM is ready\n    if (document.readyState === \'loading\') {\n        document.addEventListener(\'DOMContentLoaded\', initLanguageSwitcher);\n    } else {\n        initLanguageSwitcher();\n    }\1',
                        content
                    )
            else:
                # Already has init function, just ensure elements are selected inside it
                if 'toggle = document.getElementById(\'langToggle\')' not in content.split('function initLanguageSwitcher')[1]:
                    # Add element selection inside init function
                    content = re.sub(
                        r'(function initLanguageSwitcher\(\) \{)\s*',
                        r'\1\n        // Get elements after DOM is ready\n        toggle = document.getElementById(\'langToggle\');\n        dropdown = document.getElementById(\'langDropdown\');\n        currentFlag = document.getElementById(\'currentFlag\');\n        currentLang = document.getElementById(\'currentLang\');\n        \n        // Check if elements exist\n        if (!toggle || !dropdown || !currentFlag || !currentLang) {\n            console.error(\'Language switcher elements not found\');\n            return;\n        }\n        \n        ',
                        content
                    )
        
        # Fix navigation to ensure it goes to corresponding page
        # For gym-dashboard pages
        if 'gym-dashboard' in str(file_path):
            is_german = '-de.html' in str(file_path) or '.de.html' in str(file_path)
            if is_german:
                # German page should navigate to English gym-dashboard
                if 'gym-dashboard.html' not in content or 'window.location.href = \'gym-dashboard.html\'' not in content:
                    # Fix navigation
                    content = re.sub(
                        r'window\.location\.href = [\'"]gym-dashboard-de\.html[\'"]',
                        'window.location.href = \'gym-dashboard.html\'',
                        content
                    )
            else:
                # English page should navigate to German gym-dashboard
                if 'gym-dashboard-de.html' not in content or 'window.location.href = \'gym-dashboard-de.html\'' not in content:
                    content = re.sub(
                        r'window\.location\.href = [\'"]gym-dashboard\.html[\'"]',
                        'window.location.href = \'gym-dashboard-de.html\'',
                        content
                    )
        
        # For learning-hub pages
        if 'learning-hub' in str(file_path):
            is_german = '-de.html' in str(file_path) or '.de.html' in str(file_path)
            if is_german:
                # German page should navigate to English learning-hub
                if 'learning-hub.html' not in content or 'window.location.href = \'learning-hub.html\'' not in content:
                    content = re.sub(
                        r'window\.location\.href = [\'"]learning-hub-de\.html[\'"]',
                        'window.location.href = \'learning-hub.html\'',
                        content
                    )
            else:
                # English page should navigate to German learning-hub
                if 'learning-hub-de.html' not in content or 'window.location.href = \'learning-hub-de.html\'' not in content:
                    content = re.sub(
                        r'window\.location\.href = [\'"]learning-hub\.html[\'"]',
                        'window.location.href = \'learning-hub-de.html\'',
                        content
                    )
        
        if content != original:
            file_path.write_text(content, encoding='utf-8')
            print(f"✅ Fixed: {file_path.name}")
            return True
        return False
        
    except Exception as e:
        print(f"❌ Error fixing {file_path.name}: {e}")
        return False

def main():
    print("🔧 Fixing language switchers...\n")
    
    files_to_fix = [
        Path("gym-dashboard.html"),
        Path("gym-dashboard-de.html"),
        Path("learning-hub.html"),
        Path("learning-hub-de.html"),
    ]
    
    fixed = 0
    for file_path in files_to_fix:
        if file_path.exists():
            if fix_language_switcher(file_path):
                fixed += 1
        else:
            print(f"⚠️  Not found: {file_path}")
    
    print(f"\n✅ Fixed {fixed} files")

if __name__ == "__main__":
    main()

