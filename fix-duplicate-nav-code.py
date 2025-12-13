#!/usr/bin/env python3
"""
Remove duplicate navigation code in German dual entry file
"""

from pathlib import Path

def remove_duplicate_nav():
    """Remove duplicate navigation code"""
    file_path = Path('index-DUAL-ENTRY-de.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # Find duplicate navigation code and remove it
    # The duplicate starts after the first complete navigation block
    lines = content.split('\n')
    new_lines = []
    skip_duplicate = False
    in_duplicate = False
    
    for i, line in enumerate(lines):
        # Detect start of duplicate (after first closing braces)
        if i > 826 and '// Navigate to language-specific page' in line:
            # Check if this is a duplicate
            prev_lines = '\n'.join(lines[max(0, i-20):i])
            if 'window.location.href = \'index-DUAL-ENTRY-de.html\';' in prev_lines:
                # This is a duplicate, skip it
                in_duplicate = True
                skip_duplicate = True
                continue
        
        if skip_duplicate:
            # Skip until we hit closing braces of the duplicate
            if '});' in line and in_duplicate:
                # Count how many closing braces we need
                if line.count('});') > 0:
                    skip_duplicate = False
                    in_duplicate = False
                continue
        
        new_lines.append(line)
    
    # Also clean up any malformed code
    content = '\n'.join(new_lines)
    
    # Remove duplicate if/else blocks
    content = content.replace(
        '''            if (targetLang === 'de') {
                window.location.href = 'index-DUAL-ENTRY-de.html';
            } else {
                window.location.href = 'index-DUAL-ENTRY.html';
            }
            } else {''',
        '''            if (targetLang === 'de') {
                window.location.href = 'index-DUAL-ENTRY-de.html';
            } else {
                window.location.href = 'index-DUAL-ENTRY.html';
            }'''
    )
    
    file_path.write_text(content, encoding='utf-8')
    print("✅ Removed duplicate navigation code")

if __name__ == '__main__':
    remove_duplicate_nav()

