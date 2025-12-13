#!/usr/bin/env python3
"""
Final fix: Simplify language switcher navigation to direct file paths
"""

from pathlib import Path

def fix_both_files():
    """Fix both English and German files with simple direct navigation"""
    
    # Fix German file
    de_file = Path('index-DUAL-ENTRY-de.html')
    de_content = de_file.read_text(encoding='utf-8', errors='ignore')
    
    # Replace complex navigation with simple
    old_nav_de = '''            } else {
                // Switch to English page
                const englishUrl = currentFile.replace('-de.html', '.html').replace('/index-DUAL-ENTRY-de.html', '/index-DUAL-ENTRY.html');
                if (englishUrl.includes('-de.html')) {
                    window.location.href = 'index-DUAL-ENTRY.html';
                } else {
                    window.location.href = englishUrl;
                }
            }'''
    
    new_nav_de = '''            } else {
                window.location.href = 'index-DUAL-ENTRY.html';
            }'''
    
    if old_nav_de in de_content:
        de_content = de_content.replace(old_nav_de, new_nav_de)
        de_file.write_text(de_content, encoding='utf-8')
        print("✅ Fixed German navigation")
    
    # Also simplify the German navigation
    old_german_nav = '''                // Switch to German page
                const germanUrl = currentFile.replace('.html', '-de.html').replace('/index-DUAL-ENTRY.html', '/index-DUAL-ENTRY-de.html');
                if (!germanUrl.includes('-de.html')) {
                    window.location.href = 'index-DUAL-ENTRY-de.html';
                } else {
                    window.location.href = germanUrl;
                }'''
    
    new_german_nav = '''                window.location.href = 'index-DUAL-ENTRY-de.html';'''
    
    if old_german_nav in de_content:
        de_content = de_content.replace(old_german_nav, new_german_nav)
        de_file.write_text(de_content, encoding='utf-8')
        print("✅ Simplified German navigation")
    
    # Fix English file - ensure it's simple too
    en_file = Path('index-DUAL-ENTRY.html')
    en_content = en_file.read_text(encoding='utf-8', errors='ignore')
    
    # Verify English navigation is simple
    if 'window.location.href = \'index-DUAL-ENTRY-de.html\';' in en_content and \
       'window.location.href = \'index-DUAL-ENTRY.html\';' in en_content:
        print("✅ English navigation already simple")
    else:
        print("⚠️  English navigation might need fixing")

if __name__ == '__main__':
    fix_both_files()

