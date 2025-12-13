#!/usr/bin/env python3
"""
Comprehensive fix for English assessment readability and functionality
"""

from pathlib import Path
import re

def fix_english_assessment():
    """Fix all readability and functionality issues"""
    file_path = 'belt-assessment-v2.html'
    
    if not Path(file_path).exists():
        print(f"❌ File not found: {file_path}")
        return
    
    content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
    original = content
    
    # Fix 1: Question text - make it light and readable
    content = re.sub(
        r'(\.question-text\s*\{[^}]*?)color:\s*var\(--text-dark\);',
        r'\1color: #f8fafc;  /* Light text for dark background */',
        content,
        flags=re.DOTALL
    )
    
    # Fix 2: Intro boxes - dark background with light text
    content = re.sub(
        r'(\.intro-box\s*\{[^}]*?)background:\s*#f7fafc;',
        r'\1background: rgba(15, 23, 42, 0.6);  /* Dark translucent */',
        content,
        flags=re.DOTALL
    )
    
    content = re.sub(
        r'(\.intro-box\s+h3[^}]*?)color:\s*var\(--primary-navy\);',
        r'\1color: #e2e8f0;  /* Light text */',
        content,
        flags=re.DOTALL
    )
    
    content = re.sub(
        r'(\.intro-box\s+p[^}]*?)color:\s*var\(--text-dark\);',
        r'\1color: #cbd5e1;  /* Light text */',
        content,
        flags=re.DOTALL
    )
    
    content = re.sub(
        r'(\.intro-box\s+li[^}]*?)color:\s*var\(--text-dark\);',
        r'\1color: #cbd5e1;  /* Light text */',
        content,
        flags=re.DOTALL
    )
    
    # Fix 3: Choice options - light text
    content = re.sub(
        r'(\.choice-option\s*\{[^}]*?)color:\s*var\(--text-dark\);',
        r'\1color: #f8fafc;  /* Light text */',
        content,
        flags=re.DOTALL
    )
    
    # Fix 4: Scale options - light text
    content = re.sub(
        r'(\.scale-option\s*\{[^}]*?)color:\s*var\(--text-dark\);',
        r'\1color: #f8fafc;  /* Light text */',
        content,
        flags=re.DOTALL
    )
    
    # Fix 5: Remove light backgrounds on hover (dark theme)
    content = re.sub(
        r'\.scale-option:hover\s*\{[^}]*?background:\s*#f7fafc;',
        r'''.scale-option:hover {
            border-color: #38bdf8;
            background: rgba(56, 189, 248, 0.1);  /* Dark theme hover */''',
        content,
        flags=re.DOTALL
    )
    
    content = re.sub(
        r'\.choice-option:hover\s*\{[^}]*?background:\s*#f7fafc;',
        r'''.choice-option:hover {
            border-color: #38bdf8;
            background: rgba(56, 189, 248, 0.1);  /* Dark theme hover */''',
        content,
        flags=re.DOTALL
    )
    
    # Fix 6: Insight card colors
    content = re.sub(
        r'(\.insight-title[^}]*?)color:\s*var\(--primary-navy\);',
        r'\1color: #e2e8f0;  /* Light text */',
        content,
        flags=re.DOTALL
    )
    
    content = re.sub(
        r'(\.insight-content[^}]*?)color:\s*#4a5568;',
        r'\1color: #cbd5e1;  /* Light text */',
        content,
        flags=re.DOTALL
    )
    
    # Fix 7: Border colors for dark theme
    content = re.sub(
        r'border:\s*1px\s+solid\s+var\(--border-light\);',
        r'border: 1px solid rgba(148, 163, 184, 0.3);',
        content
    )
    
    # Fix 8: Scale option and choice option backgrounds
    content = re.sub(
        r'(\.scale-option\s*\{[^}]*?)background:\s*rgba\(255,\s*255,\s*255,\s*0\.05\);',
        r'\1background: rgba(15, 23, 42, 0.9);',
        content,
        flags=re.DOTALL
    )
    
    content = re.sub(
        r'(\.choice-option\s*\{[^}]*?)background:\s*rgba\(255,\s*255,\s*255,\s*0\.05\);',
        r'\1background: rgba(15, 23, 42, 0.9);',
        content,
        flags=re.DOTALL
    )
    
    # Fix 9: Check for any remaining var(--text-dark) references
    if 'var(--text-dark)' in content:
        print("⚠️  Warning: Still found var(--text-dark) references")
        # Try to replace remaining instances
        content = re.sub(
            r'color:\s*var\(--text-dark\);',
            r'color: #f8fafc;  /* Light text for dark background */',
            content
        )
    
    if content != original:
        Path(file_path).write_text(content, encoding='utf-8')
        print(f"✅ Fixed readability in {file_path}")
        return True
    else:
        print(f"ℹ️  {file_path} may already be readable")
        return False

if __name__ == '__main__':
    print("🔧 Comprehensive English Assessment Fix...\n")
    if fix_english_assessment():
        print("\n✅ All fixes applied!")
    else:
        print("\n✅ File checked - may need manual review")

