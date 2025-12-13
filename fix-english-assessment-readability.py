#!/usr/bin/env python3
"""
Fix English assessment readability - update text colors for dark theme
"""

from pathlib import Path
import re

def fix_english_assessment():
    """Fix text colors and readability in English assessment"""
    file_path = 'belt-assessment-v2.html'
    
    if not Path(file_path).exists():
        print(f"❌ File not found: {file_path}")
        return
    
    content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
    original = content
    
    # Fix 1: Question text color (var(--text-dark) -> light color)
    content = re.sub(
        r'\.question-text\s*\{[^}]*?color:\s*var\(--text-dark\);',
        r'''.question-text {
            font-size: 1.2rem;
            font-weight: 600;
            color: #f8fafc;  /* Light color for readability on dark background */
            margin-bottom: 1.5rem;
            line-height: 1.5;''',
        content,
        flags=re.DOTALL
    )
    
    # Fix 2: Intro boxes - dark theme backgrounds
    content = re.sub(
        r'\.intro-box\s*\{[^}]*?background:\s*#f7fafc;',
        r'''.intro-box {
            background: rgba(15, 23, 42, 0.6);  /* Dark translucent background */
            border: 1px solid rgba(148, 163, 184, 0.3);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;''',
        content,
        flags=re.DOTALL
    )
    
    # Fix 3: Intro box text colors
    content = re.sub(
        r'\.intro-box\s+h3[^}]*?color:\s*var\(--primary-navy\);',
        r'''.intro-box h3 {
            color: #e2e8f0;  /* Light text */
            font-size: 1.2rem;
            margin-bottom: 0.75rem;''',
        content,
        flags=re.DOTALL
    )
    
    # Fix 4: Intro box paragraph colors
    if 'intro-box p' not in content or 'color: #' not in content:
        content = re.sub(
            r'(\.intro-box\s+p\s*\{[^}]*?)',
            r'\1\n            color: #cbd5e1;  /* Light text for readability */',
            content,
            flags=re.DOTALL
        )
    
    # Fix 5: Choice option text colors
    content = re.sub(
        r'\.choice-option\s*\{[^}]*?color:\s*var\(--text-dark\);',
        r'''.choice-option {
            padding: 1rem 1.25rem;
            background: rgba(15, 23, 42, 0.9);
            border: 2px solid rgba(148, 163, 184, 0.3);
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.2s;
            text-align: left;
            font-size: 0.95rem;
            color: #f8fafc;  /* Light text for readability */''',
        content,
        flags=re.DOTALL
    )
    
    # Fix 6: Scale option text colors
    content = re.sub(
        r'\.scale-option\s*\{[^}]*?color:\s*var\(--text-dark\);',
        r'''.scale-option {
            flex: 1;
            padding: 1rem 0.5rem;
            background: rgba(15, 23, 42, 0.9);
            border: 2px solid rgba(148, 163, 184, 0.3);
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
            font-weight: 600;
            font-size: 1.1rem;
            color: #f8fafc;  /* Light text for readability */''',
        content,
        flags=re.DOTALL
    )
    
    # Fix 7: Remove light background hovers on dark theme
    content = re.sub(
        r'background:\s*#f7fafc;',
        r'background: rgba(15, 23, 42, 0.7);',
        content
    )
    
    # Fix 8: Insight card text colors
    content = re.sub(
        r'\.insight-content\s*\{[^}]*?color:\s*#4a5568;',
        r'''.insight-content {
            color: #cbd5e1;  /* Light text */
            font-size: 0.9rem;
            margin-bottom: 0.75rem;''',
        content,
        flags=re.DOTALL
    )
    
    # Fix 9: Insight title color
    content = re.sub(
        r'\.insight-title\s*\{[^}]*?color:\s*var\(--primary-navy\);',
        r'''.insight-title {
            font-weight: 700;
            color: #e2e8f0;  /* Light text */
            font-size: 1.05rem;
            margin-bottom: 0.5rem;''',
        content,
        flags=re.DOTALL
    )
    
    # Fix 10: Make sure intro box text is readable
    if 'intro-box' in content and 'color: #' not in content.split('intro-box')[1][:500]:
        # Add color to intro box paragraphs if missing
        content = re.sub(
            r'(\.intro-box\s+p\s*\{[^}]*?)',
            r'\1\n            color: #cbd5e1;',
            content
        )
    
    if content != original:
        Path(file_path).write_text(content, encoding='utf-8')
        print(f"✅ Fixed readability in {file_path}")
        print("   - Question text: Light color (#f8fafc)")
        print("   - Intro boxes: Dark backgrounds")
        print("   - Choice options: Light text")
        print("   - Scale options: Light text")
        print("   - Insight cards: Light text")
    else:
        print(f"ℹ️  {file_path} may already be readable")

if __name__ == '__main__':
    print("🔧 Fixing English Assessment Readability...\n")
    fix_english_assessment()
    print("\n✅ Readability fix complete!")

