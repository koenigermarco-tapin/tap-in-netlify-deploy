#!/usr/bin/env python3
"""
Complete fix for dual entry language switcher - ensure proper navigation
"""

from pathlib import Path
import re

def fix_english_nav():
    """Fix English version to navigate to German page"""
    file_path = Path('index-DUAL-ENTRY.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # The navigation is already fixed in the previous update
    # Just verify it exists
    if 'index-DUAL-ENTRY-de.html' in content:
        print("✅ English navigation already fixed")
    else:
        print("⚠️  English navigation needs fixing")

def fix_german_nav():
    """Fix German version to navigate to English page"""
    file_path = Path('index-DUAL-ENTRY-de.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # Replace the navigation logic
    old_nav = r'// Get current page without language suffix\s+let currentPath = window\.location\.pathname;\s+let basePath = currentPath\.replace\(\'-de\.html\', \'\.html\'\);\s+// Build new path\s+let newPath = basePath\.replace\(\'\.html\', fileSuffix \+ \'\.html\'\);\s+// Navigate to new language version\s+window\.location\.href = newPath;'
    
    new_nav = '''            // Navigate to language-specific page
            if (targetLang === 'de') {
                window.location.href = 'index-DUAL-ENTRY-de.html';
            } else {
                window.location.href = 'index-DUAL-ENTRY.html';
            }'''
    
    # Use simple replacement instead
    if 'let newPath = basePath.replace' in content:
        lines = content.split('\n')
        new_lines = []
        skip_next = False
        for i, line in enumerate(lines):
            if '// Get current page without language suffix' in line:
                skip_next = True
                new_lines.append('            // Navigate to language-specific page')
                new_lines.append('            if (targetLang === \'de\') {')
                new_lines.append('                window.location.href = \'index-DUAL-ENTRY-de.html\';')
                new_lines.append('            } else {')
                new_lines.append('                window.location.href = \'index-DUAL-ENTRY.html\';')
                new_lines.append('            }')
                # Skip the old navigation lines
                continue
            if skip_next and ('let currentPath' in line or 'let basePath' in line or 'let newPath' in line or '// Build new path' in line or ('// Navigate to new language version' in line and 'window.location.href = newPath;' in lines[i+1] if i+1 < len(lines) else False)):
                if 'window.location.href = newPath;' in line:
                    skip_next = False
                continue
            
            skip_next = False
            new_lines.append(line)
        
        content = '\n'.join(new_lines)
        file_path.write_text(content, encoding='utf-8')
        print("✅ Fixed German navigation")
    else:
        print("⚠️  German navigation pattern not found")

if __name__ == '__main__':
    fix_english_nav()
    fix_german_nav()

