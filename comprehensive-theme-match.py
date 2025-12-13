#!/usr/bin/env python3
"""
Comprehensively match English assessment styling to German dark theme
"""

from pathlib import Path
import re

def extract_styles_from_german():
    """Extract key style patterns from German version"""
    german_file = 'belt-assessment-v2-de.html'
    
    if not Path(german_file).exists():
        return {}
    
    content = Path(german_file).read_text(encoding='utf-8', errors='ignore')
    
    # Extract key style patterns
    styles = {}
    
    # Body background
    body_match = re.search(r'body\s*\{[^}]*background:[^;]+;', content, re.DOTALL)
    if body_match:
        styles['body_bg'] = re.search(r'background:[^;]+;', body_match.group(0)).group(0)
    
    # Container
    container_match = re.search(r'\.container\s*\{[^}]+\}', content, re.DOTALL)
    if container_match:
        styles['container'] = container_match.group(0)
    
    # Question card
    qcard_match = re.search(r'\.question-card\s*\{[^}]+\}', content, re.DOTALL)
    if qcard_match:
        styles['question_card'] = qcard_match.group(0)
    
    # Scale option
    scale_match = re.search(r'\.scale-option\s*\{[^}]+\}', content, re.DOTALL)
    if scale_match:
        styles['scale_option'] = scale_match.group(0)
    
    # Intro box
    intro_match = re.search(r'\.intro-box\s*\{[^}]+\}', content, re.DOTALL)
    if intro_match:
        styles['intro_box'] = intro_match.group(0)
    
    return styles

def update_english_to_match_german():
    """Update English file to match German styling exactly"""
    english_file = 'belt-assessment-v2.html'
    german_file = 'belt-assessment-v2-de.html'
    
    if not Path(english_file).exists() or not Path(german_file).exists():
        print("❌ Files not found")
        return
    
    english = Path(english_file).read_text(encoding='utf-8', errors='ignore')
    german = Path(german_file).read_text(encoding='utf-8', errors='ignore')
    
    original = english
    
    # Key style replacements based on German version
    
    # 1. Update intro-box to match German dark theme
    # German has: background: rgba(15, 23, 42, 0.85); border-left: 4px solid #4c1d95;
    english = re.sub(
        r'\.intro-box\s*\{[^}]*?background:\s*[^;]+;',
        '.intro-box {\n            background: rgba(15, 23, 42, 0.85);',
        english,
        flags=re.DOTALL
    )
    
    # Add border-left to intro-box if missing
    if 'border-left: 4px solid #4c1d95;' not in english:
        english = re.sub(
            r'(\.intro-box\s*\{[^}]*?background:\s*[^;]+;)',
            r'\1\n            border-left: 4px solid #4c1d95;',
            english,
            flags=re.DOTALL
        )
    
    # Update intro-box text colors
    english = re.sub(
        r'\.intro-box\s+h3\s*\{[^}]*?color:\s*var\(--primary-navy\);',
        '.intro-box h3 {\n            color: #f8fafc;',
        english,
        flags=re.DOTALL
    )
    
    english = re.sub(
        r'\.intro-box\s+p\s*\{[^}]*?color:\s*var\(--text-dark\);',
        '.intro-box p {\n            color: #cbd5f5;',
        english,
        flags=re.DOTALL
    )
    
    # 2. Update question card to match German
    # German has: background: rgba(15, 23, 42, 0.85); border-radius: 18px;
    if '.question-card' in english:
        english = re.sub(
            r'\.question-card\s*\{[^}]*?background:[^;]+;',
            '.question-card {\n            background: rgba(15, 23, 42, 0.85);',
            english,
            flags=re.DOTALL
        )
    
    # 3. Update scale options to match German dark theme
    # German has: background: rgba(15, 23, 42, 0.9); border: 1px solid rgba(255, 255, 255, 0.08);
    english = re.sub(
        r'\.scale-option\s*\{[^}]*?background:\s*rgba\(255,\s*255,\s*255,\s*0\.05\);',
        'background: rgba(15, 23, 42, 0.9);',
        english
    )
    
    english = re.sub(
        r'\.scale-option\s*\{[^}]*?border:\s*2px\s+solid\s+var\(--border-light\);',
        'border: 1px solid rgba(255, 255, 255, 0.08);',
        english,
        flags=re.DOTALL
    )
    
    # 4. Update text colors throughout
    english = re.sub(
        r'color:\s*var\(--text-dark\);',
        'color: #f8fafc;',
        english
    )
    
    english = re.sub(
        r'color:\s*#4a5568;',
        'color: #cbd5f5;',
        english
    )
    
    # 5. Update progress container
    english = re.sub(
        r'\.progress-container\s*\{[^}]*?background:[^;]+;',
        '.progress-container {\n            background: rgba(15, 23, 42, 0.85);',
        english,
        flags=re.DOTALL
    )
    
    # 6. Update all white backgrounds to dark translucent
    english = re.sub(
        r'background:\s*(white|#ffffff|#fff);',
        'background: rgba(255, 255, 255, 0.05);',
        english
    )
    
    # 7. Update result cards
    english = re.sub(
        r'\.result-card\s*\{[^}]*?background:\s*rgba\(255,\s*255,\s*255,\s*0\.05\);',
        'background: rgba(15, 23, 42, 0.85);',
        english,
        flags=re.DOTALL
    )
    
    if english != original:
        Path(english_file).write_text(english, encoding='utf-8')
        print("✅ Updated English assessment to match German dark theme")
        print("   - All backgrounds updated to dark")
        print("   - All text colors updated to light")
        print("   - All cards updated to dark theme")
    else:
        print("ℹ️  No changes needed")

if __name__ == '__main__':
    print("🎨 Matching English Assessment to German Dark Theme...\n")
    update_english_to_match_german()
    print("\n✅ Theme matching complete!")

