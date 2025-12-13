#!/usr/bin/env python3
"""
Final comprehensive fix for English assessment - readability and functionality
"""

from pathlib import Path
import re

def fix_english_assessment():
    """Fix all readability issues in English assessment"""
    file_path = 'belt-assessment-v2.html'
    
    if not Path(file_path).exists():
        print(f"❌ File not found: {file_path}")
        return
    
    content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
    original = content
    
    # Fix 1: Question text color - must be light
    content = re.sub(
        r'\.question-text\s*\{[^}]*?color:\s*var\(--text-dark\);',
        r'''.question-text {
            font-size: 1.2rem;
            font-weight: 600;
            color: #f8fafc;  /* Light text for dark background */
            margin-bottom: 1.5rem;
            line-height: 1.5;''',
        content,
        flags=re.DOTALL
    )
    
    # Fix 2: Remove duplicate CSS rules in intro-box
    content = re.sub(
        r'\.intro-box\s*\{[^}]*(?:border-radius|padding|margin|background)[^}]*\}',
        r'''.intro-box {
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(148, 163, 184, 0.3);
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1rem 0;
        }''',
        content,
        flags=re.DOTALL
    )
    
    # Fix 3: Replace all var(--text-dark) with light colors
    content = re.sub(
        r'color:\s*var\(--text-dark\);',
        r'color: #f8fafc;  /* Light text for readability */',
        content
    )
    
    # Fix 4: Fix intro box text colors
    content = re.sub(
        r'\.intro-box\s+h3[^}]*?color:\s*var\(--primary-navy\);',
        r'''.intro-box h3 {
            color: #e2e8f0;
            font-size: 1.1rem;
            margin-bottom: 0.75rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;''',
        content,
        flags=re.DOTALL
    )
    
    # Fix 5: Remove duplicate color declarations
    content = re.sub(
        r'color:\s*#cbd5e1;\s*color:\s*#cbd5e1;',
        r'color: #cbd5e1;',
        content
    )
    
    content = re.sub(
        r'color:\s*#e2e8f0;\s*color:\s*#e2e8f0;',
        r'color: #e2e8f0;',
        content
    )
    
    # Fix 6: Remove duplicate font-size
    content = re.sub(
        r'font-size:\s*1\.1rem;\s*font-size:\s*1\.1rem;',
        r'font-size: 1.1rem;',
        content
    )
    
    # Fix 7: Remove duplicate margin-bottom
    content = re.sub(
        r'margin-bottom:\s*0\.75rem;\s*margin-bottom:\s*0\.75rem;',
        r'margin-bottom: 0.75rem;',
        content
    )
    
    # Fix 8: Ensure all choice/scale options have light text
    if 'color: #f8fafc' not in content.split('.choice-option')[1][:500] if '.choice-option' in content else False:
        content = re.sub(
            r'(\.choice-option\s*\{[^}]*?)color:\s*var\(--text-dark\);',
            r'\1color: #f8fafc;',
            content,
            flags=re.DOTALL
        )
    
    if content != original:
        Path(file_path).write_text(content, encoding='utf-8')
        print(f"✅ Fixed all readability issues in {file_path}")
        return True
    else:
        print(f"ℹ️  {file_path} checked")
        return False

if __name__ == '__main__':
    print("🔧 Final English Assessment Fix...\n")
    fix_english_assessment()
    print("\n✅ Complete!")

