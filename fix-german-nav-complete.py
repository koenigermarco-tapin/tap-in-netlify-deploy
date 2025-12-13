#!/usr/bin/env python3
"""
Complete fix for German dual entry navigation - remove all duplicate code
"""

from pathlib import Path

def fix_german_nav():
    """Fix German navigation by removing duplicate code"""
    file_path = Path('index-DUAL-ENTRY-de.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    lines = content.split('\n')
    new_lines = []
    skip_duplicate = False
    
    for i, line in enumerate(lines):
        # Find duplicate code starting after the first navigation block
        if i >= 826 and '// Switch to English page' in line:
            # Check if this is duplicate (we already have navigation above)
            if 'window.location.href = \'index-DUAL-ENTRY.html\';' in '\n'.join(new_lines[-20:]):
                skip_duplicate = True
                continue
        
        if skip_duplicate:
            # Skip until we hit the closing of the duplicate
            if '});' in line:
                skip_duplicate = False
            continue
        
        new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    # Also ensure the navigation is simple and direct
    # Replace complex navigation with simple
    content = content.replace(
        '''                // Switch to English page
                const englishUrl = currentFile.replace('-de.html', '.html').replace('/index-DUAL-ENTRY-de.html', '/index-DUAL-ENTRY.html');
                if (englishUrl.includes('-de.html')) {
                    window.location.href = 'index-DUAL-ENTRY.html';
                } else {
                    window.location.href = englishUrl;
                }''',
        ''
    )
    
    file_path.write_text(content, encoding='utf-8')
    print("✅ Fixed German navigation - removed duplicate code")

if __name__ == '__main__':
    fix_german_nav()

