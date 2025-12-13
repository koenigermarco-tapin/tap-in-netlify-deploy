#!/usr/bin/env python3
"""
Clean fix for dual entry language switcher - remove all duplicate code and simplify
"""

from pathlib import Path

def clean_english_file():
    """Clean English file navigation"""
    file_path = Path('index-DUAL-ENTRY.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # Find the navigation section
    nav_start = content.find('// Navigate to language-specific page')
    nav_end = content.find('});', nav_start) + 3
    
    if nav_start > 0 and nav_end > nav_start:
        # Simple, clean navigation code
        clean_nav = '''            // Navigate to language-specific page
            if (targetLang === 'de') {
                window.location.href = 'index-DUAL-ENTRY-de.html';
            } else {
                window.location.href = 'index-DUAL-ENTRY.html';
            }
        });
    });'''
        
        old_nav = content[nav_start:nav_end+10]  # Include closing
        
        # Find the actual end
        lines = content[nav_start:nav_end+100].split('\n')
        actual_end = nav_start
        brace_count = 0
        for i, line in enumerate(lines):
            actual_end += len(line) + 1
            brace_count += line.count('{') - line.count('}')
            if brace_count == 0 and '});' in line:
                break
        
        content = content[:nav_start] + clean_nav + content[actual_end:]
        file_path.write_text(content, encoding='utf-8')
        print("✅ Cleaned English navigation")

def clean_german_file():
    """Clean German file navigation"""
    file_path = Path('index-DUAL-ENTRY-de.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # Find and replace complex navigation with simple
    old_complex = '''                const germanUrl = currentFile.replace('.html', '-de.html').replace('/index-DUAL-ENTRY.html', '/index-DUAL-ENTRY-de.html');
                if (!germanUrl.includes('-de.html')) {
                    window.location.href = 'index-DUAL-ENTRY-de.html';
                } else {
                    window.location.href = germanUrl;
                }'''
    
    new_simple = '''                window.location.href = 'index-DUAL-ENTRY-de.html';'''
    
    if old_complex in content:
        content = content.replace(old_complex, new_simple)
    
    old_complex_en = '''                const englishUrl = currentFile.replace('-de.html', '.html').replace('/index-DUAL-ENTRY-de.html', '/index-DUAL-ENTRY.html');
                if (englishUrl.includes('-de.html')) {
                    window.location.href = 'index-DUAL-ENTRY.html';
                } else {
                    window.location.href = englishUrl;
                }'''
    
    new_simple_en = '''                window.location.href = 'index-DUAL-ENTRY.html';'''
    
    if old_complex_en in content:
        content = content.replace(old_complex_en, new_simple_en)
    
    file_path.write_text(content, encoding='utf-8')
    print("✅ Cleaned German navigation")

if __name__ == '__main__':
    clean_english_file()
    clean_german_file()

