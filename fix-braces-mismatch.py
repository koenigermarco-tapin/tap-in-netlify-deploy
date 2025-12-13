#!/usr/bin/env python3
"""
Fix braces mismatch in German dual entry file
"""

from pathlib import Path

def fix_braces():
    """Fix braces mismatch"""
    file_path = Path('index-DUAL-ENTRY-de.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # Find the handler section
    handler_start = content.find('// Language switch handler - Navigate to language-specific page')
    handler_end = content.find('})();', handler_start)
    
    if handler_start > 0 and handler_end > handler_start:
        handler_code = content[handler_start:handler_end+5]
        
        # Check for duplicate code after the handler
        lines = content[handler_end:handler_end+100].split('\n')
        duplicate_start = None
        for i, line in enumerate(lines):
            if '// Store preference' in line and i < 10:
                duplicate_start = handler_end + sum(len(l) + 1 for l in lines[:i])
                break
        
        # Remove duplicate code
        if duplicate_start:
            # Find where the duplicate ends
            duplicate_end = content.find('})();', duplicate_start)
            if duplicate_end > duplicate_start:
                # Remove the duplicate
                content = content[:handler_end+5] + content[duplicate_end+5:]
                file_path.write_text(content, encoding='utf-8')
                print("✅ Removed duplicate code after handler")
    
    # Also simplify navigation to direct paths
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # Replace complex navigation with simple
    simple_nav = '''            // Navigate to language-specific page
            if (targetLang === 'de') {
                window.location.href = 'index-DUAL-ENTRY-de.html';
            } else {
                window.location.href = 'index-DUAL-ENTRY.html';
            }'''
    
    # Find and replace the complex navigation
    nav_pattern = r'// Navigate to language-specific page[\s\S]*?window\.location\.href = [^;]+;[\s\S]*?\}[\s\S]*?\}[\s\S]*?\}'
    
    import re
    if re.search(nav_pattern, content):
        content = re.sub(
            r'// Navigate to language-specific page[\s\S]*?if \(targetLang === \'de\'\) \{[\s\S]*?\} else \{[\s\S]*?\}',
            simple_nav,
            content,
            count=1
        )
        file_path.write_text(content, encoding='utf-8')
        print("✅ Simplified navigation code")

if __name__ == '__main__':
    fix_braces()

