#!/usr/bin/env python3
"""
Update belt-assessment-v2.html to match the dark theme of belt-assessment-v2-de.html
"""

from pathlib import Path
import re

def update_english_to_dark_theme():
    """Update English assessment to match German dark theme"""
    english_file = 'belt-assessment-v2.html'
    german_file = 'belt-assessment-v2-de.html'
    
    if not Path(english_file).exists():
        print(f"❌ File not found: {english_file}")
        return
    
    if not Path(german_file).exists():
        print(f"❌ Reference file not found: {german_file}")
        return
    
    content = Path(english_file).read_text(encoding='utf-8', errors='ignore')
    german_content = Path(german_file).read_text(encoding='utf-8', errors='ignore')
    
    original = content
    
    # Update body background to dark theme
    content = re.sub(
        r'background:\s*linear-gradient\(135deg,\s*#4a7c9c\s+0%,\s*#3d6680\s+100%\);',
        'background: linear-gradient(135deg, #0f172a 0%, #020617 100%);',
        content
    )
    
    # Add color property to body if missing
    if 'color: #e2e8f0;' not in content:
        content = re.sub(
            r'(background:\s*linear-gradient\(135deg,\s*#0f172a\s+0%,\s*#020617\s+100%\);)',
            r'\1\n            color: #e2e8f0;',
            content
        )
    
    # Update padding to match German version
    content = re.sub(
        r'padding:\s*2rem\s+1rem;',
        'padding: 20px;',
        content
    )
    
    # Remove line-height from body (German version doesn't have it)
    content = re.sub(
        r'line-height:\s*1\.6;\s*\n',
        '',
        content
    )
    
    # Update container to dark theme
    content = re.sub(
        r'\.container\s*\{[^}]*max-width:\s*700px;',
        '.container {\n            max-width: 960px;',
        content,
        flags=re.DOTALL
    )
    
    # Add dark container background
    container_match = re.search(r'\.container\s*\{([^}]+)\}', content, re.DOTALL)
    if container_match:
        container_content = container_match.group(1)
        if 'background: #020617;' not in container_content:
            content = re.sub(
                r'(\.container\s*\{[^}]*?margin:\s*0\s+auto;)',
                r'\1\n            background: #020617;\n            border-radius: 22px;\n            padding: 42px;\n            box-shadow: 0 20px 60px rgba(2, 6, 23, 0.75);\n            border: 1px solid rgba(148, 163, 184, 0.3);',
                content,
                flags=re.DOTALL
            )
    
    # Update assessment-card background from white to dark
    content = re.sub(
        r'\.assessment-card\s*\{[^}]*?background:\s*white;',
        '.assessment-card {\n            background: rgba(255, 255, 255, 0.05);',
        content,
        flags=re.DOTALL
    )
    
    # Update all white backgrounds to dark
    content = re.sub(
        r'background:\s*(white|#ffffff);',
        'background: rgba(255, 255, 255, 0.05);',
        content
    )
    
    # Update text colors to match dark theme
    content = re.sub(
        r'color:\s*(white|#ffffff);',
        'color: #e2e8f0;',
        content
    )
    
    # Update header text colors
    content = re.sub(
        r'\.header\s*\{[^}]*?color:\s*white;',
        '.header {\n            color: #e2e8f0;',
        content,
        flags=re.DOTALL
    )
    
    if content != original:
        Path(english_file).write_text(content, encoding='utf-8')
        print(f"✅ Updated {english_file} to dark theme")
        print("   - Background: Dark gradient")
        print("   - Container: Dark background")
        print("   - Cards: Dark translucent")
        print("   - Text: Light color")
    else:
        print(f"ℹ️  {english_file} already has dark theme or no changes needed")

if __name__ == '__main__':
    print("🎨 Updating English Assessment to Dark Theme...\n")
    update_english_to_dark_theme()
    print("\n✅ Dark theme update complete!")

