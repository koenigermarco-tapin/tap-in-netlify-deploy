#!/usr/bin/env python3
"""
Complete Stage 1 file with all fixes
"""

from pathlib import Path
import re

def fix_stage1():
    """Complete Stage 1 implementation"""
    file_path = Path('sales-recruiting-stage1.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # Fix updateButtons to work with new structure
    content = re.sub(
        r'nextBtn\.disabled = !answers\.hasOwnProperty\(currentQuestion\);',
        r'nextBtn.disabled = !answers.hasOwnProperty(currentQuestion) || answers[currentQuestion] === undefined;',
        content
    )
    
    # Ensure answers initialization
    if 'let answers = {};' not in content.split('currentQuestion = 0')[1][:500]:
        content = re.sub(
            r'(let currentQuestion = 0;)',
            r'\1\n        let answers = {};',
            content
        )
    
    file_path.write_text(content, encoding='utf-8')
    print("✅ Stage 1 fixes applied")

if __name__ == '__main__':
    fix_stage1()

