#!/usr/bin/env python3
"""
Fix German dual entry navigation to properly switch to English
"""

from pathlib import Path
import re

def fix_german_navigation():
    """Fix German version to navigate correctly"""
    file_path = Path('index-DUAL-ENTRY-de.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # Find and replace the navigation handler
    old_handler = '''            // Get current page without language suffix
            let currentPath = window.location.pathname;
            let basePath = currentPath.replace('-de.html', '.html');
            
            // Build new path
            let newPath = basePath.replace('.html', fileSuffix + '.html');
            
            // Navigate to new language version
            window.location.href = newPath;'''
    
    new_handler = '''            // Navigate to language-specific page
            const currentFile = window.location.pathname;
            const isCurrentlyGerman = currentFile.includes('-de.html');
            const wantsGerman = targetLang === 'de';
            
            if (targetLang === 'de') {
                // Switch to German page
                window.location.href = 'index-DUAL-ENTRY-de.html';
            } else {
                // Switch to English page
                window.location.href = 'index-DUAL-ENTRY.html';
            }'''
    
    if old_handler in content:
        content = content.replace(old_handler, new_handler)
        file_path.write_text(content, encoding='utf-8')
        print("✅ Fixed German dual entry navigation")
    else:
        print("⚠️  Handler not found in expected format")

if __name__ == '__main__':
    fix_german_navigation()

