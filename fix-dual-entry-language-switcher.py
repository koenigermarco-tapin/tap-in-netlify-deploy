#!/usr/bin/env python3
"""
Fix language switcher in dual entry pages to navigate between English and German pages
"""

from pathlib import Path
import re

def fix_language_switcher(file_path_str, is_german=False):
    """Fix language switcher to navigate to correct language page"""
    file_path = Path(file_path_str)
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # Find the language switch handler
    pattern = r'(// Language switch handler[\s\S]*?})(\);)?'
    
    def replace_handler(match):
        old_code = match.group(0)
        
        # New handler that navigates to language-specific pages
        new_code = '''// Language switch handler - Navigate to language-specific page
    document.querySelectorAll('.lang-option').forEach(option => {
        option.addEventListener('click', (e) => {
            e.preventDefault();
            const targetLang = option.dataset.lang;
            const fileSuffix = option.dataset.file || '';
            
            // Get current file path
            const currentFile = window.location.pathname;
            const isCurrentlyGerman = currentFile.includes('-de.html');
            const wantsGerman = targetLang === 'de';
            
            // Don't switch if already on that language
            if ((isCurrentlyGerman && wantsGerman) || (!isCurrentlyGerman && !wantsGerman)) {
                dropdown.classList.remove('show');
                return;
            }
            
            // Navigate to language-specific page
            if (targetLang === 'de') {
                // Switch to German page
                const germanUrl = currentFile.replace('.html', '-de.html').replace('/index-DUAL-ENTRY.html', '/index-DUAL-ENTRY-de.html');
                if (!germanUrl.includes('-de.html')) {
                    window.location.href = 'index-DUAL-ENTRY-de.html';
                } else {
                    window.location.href = germanUrl;
                }
            } else {
                // Switch to English page
                const englishUrl = currentFile.replace('-de.html', '.html').replace('/index-DUAL-ENTRY-de.html', '/index-DUAL-ENTRY.html');
                if (englishUrl.includes('-de.html')) {
                    window.location.href = 'index-DUAL-ENTRY.html';
                } else {
                    window.location.href = englishUrl;
                }
            }
        });
    });'''
        
        return new_code
    
    # Replace the handler
    new_content = re.sub(pattern, replace_handler, content)
    
    # Also ensure the current language indicator is correct
    if is_german:
        # German page should show DE flag
        current_flag_pattern = r'(<span class="lang-flag" id="currentFlag">)[^<]+(</span>)'
        new_content = re.sub(current_flag_pattern, r'\1🇩🇪\2', new_content, count=1)
        
        current_lang_pattern = r'(<span class="lang-code" id="currentLang">)[^<]+(</span>)'
        new_content = re.sub(current_lang_pattern, r'\1DE\2', new_content, count=1)
    
    file_path.write_text(new_content, encoding='utf-8')
    print(f"✅ Fixed language switcher in {file_path_str}")

if __name__ == '__main__':
    fix_language_switcher('index-DUAL-ENTRY.html', is_german=False)
    fix_language_switcher('index-DUAL-ENTRY-de.html', is_german=True)

