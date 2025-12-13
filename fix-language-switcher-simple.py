#!/usr/bin/env python3
"""
Simplify language switcher to work reliably - direct navigation
"""

from pathlib import Path
import re

def simplify_navigation(file_path_str, is_german=False):
    """Simplify navigation to direct file paths"""
    file_path = Path(file_path_str)
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # Find the language switch handler and simplify it
    pattern = r'(// Navigate to language-specific page[\s\S]*?window\.location\.href = [^;]+;)'
    
    def replace_with_simple(match):
        if is_german:
            return '''            // Navigate to language-specific page
            if (targetLang === 'de') {
                window.location.href = 'index-DUAL-ENTRY-de.html';
            } else {
                window.location.href = 'index-DUAL-ENTRY.html';
            }'''
        else:
            return '''            // Navigate to language-specific page
            if (targetLang === 'de') {
                window.location.href = 'index-DUAL-ENTRY-de.html';
            } else {
                window.location.href = 'index-DUAL-ENTRY.html';
            }'''
    
    # Replace complex navigation with simple direct paths
    content = re.sub(
        r'if \(targetLang === \'de\'\) \{[\s\S]*?window\.location\.href = [^;]+;[\s\S]*?\} else \{[\s\S]*?window\.location\.href = [^;]+;[\s\S]*?\}',
        '''if (targetLang === 'de') {
                window.location.href = 'index-DUAL-ENTRY-de.html';
            } else {
                window.location.href = 'index-DUAL-ENTRY.html';
            }''',
        content
    )
    
    file_path.write_text(content, encoding='utf-8')
    print(f"✅ Simplified navigation in {file_path_str}")

if __name__ == '__main__':
    simplify_navigation('index-DUAL-ENTRY.html', is_german=False)
    simplify_navigation('index-DUAL-ENTRY-de.html', is_german=True)

