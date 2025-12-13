#!/usr/bin/env python3
"""
Fix German dual entry to show DE flag correctly
"""

from pathlib import Path

def fix_german_flag():
    """Fix initial flag display in German version"""
    file_path = Path('index-DUAL-ENTRY-de.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # Fix initial flag - should be DE, not EN
    content = content.replace(
        '<span class="lang-flag" id="currentFlag">🇬🇧</span>',
        '<span class="lang-flag" id="currentFlag">🇩🇪</span>',
        count=1
    )
    
    content = content.replace(
        '<span class="lang-code" id="currentLang">EN</span>',
        '<span class="lang-code" id="currentLang">DE</span>',
        count=1
    )
    
    file_path.write_text(content, encoding='utf-8')
    print("✅ Fixed German flag display")

if __name__ == '__main__':
    fix_german_flag()

