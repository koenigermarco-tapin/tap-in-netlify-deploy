#!/usr/bin/env python3
"""
Optimize font loading - ensure preload, display:swap, and proper fallbacks
"""

from pathlib import Path
import re

PRIORITY_PAGES = [
    'index.html',
    'gym-dashboard.html',
    'learning-hub.html',
    'belt-assessment-v2.html',
]

def optimize_font_loading(content):
    """Optimize Google Fonts loading"""
    changes = False
    
    # Check if Google Fonts link exists
    if 'fonts.googleapis.com' not in content:
        return content, False
    
    # Ensure preconnect exists
    if 'preconnect' not in content or 'fonts.googleapis.com' not in re.search(r'preconnect.*fonts', content, re.IGNORECASE).group(0) if re.search(r'preconnect.*fonts', content, re.IGNORECASE) else '':
        preconnect = '''    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'''
        
        # Add before Google Fonts link
        if '<link href="https://fonts.googleapis.com' in content:
            content = content.replace(
                '<link href="https://fonts.googleapis.com',
                preconnect + '\n    <link href="https://fonts.googleapis.com',
                1
            )
            changes = True
    
    # Ensure font-display:swap in link
    if 'fonts.googleapis.com' in content and 'display=swap' not in content:
        # Add display=swap to Google Fonts URL
        content = re.sub(
            r'(https://fonts\.googleapis\.com/css2[^"]+)(")',
            r'\1&display=swap\2',
            content,
            count=1
        )
        changes = True
    
    # Add font-display:swap to @font-face if exists
    if '@font-face' in content and 'font-display' not in content:
        content = re.sub(
            r'(@font-face\s*\{[^}]*)(\})',
            r'\1  font-display: swap;\2',
            content,
            count=5
        )
        changes = True
    
    # Add system font fallback
    font_fallback = '''
      font-family: Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
'''
    
    # Check if body has font-family without fallback
    body_font_pattern = r'(body\s*\{[^}]*font-family:\s*)([^;]+)(;)'
    match = re.search(body_font_pattern, content)
    if match and 'Inter' in match.group(2) and 'system' not in match.group(2):
        # Add system fallbacks
        new_font = match.group(2) + ', -apple-system, BlinkMacSystemFont, sans-serif'
        content = content.replace(match.group(0), match.group(1) + new_font + match.group(3))
        changes = True
    
    return content, changes

def main():
    print("=" * 80)
    print("🔤 OPTIMIZING FONT LOADING")
    print("=" * 80)
    print()
    
    updated = 0
    
    for filename in PRIORITY_PAGES:
        filepath = Path(filename)
        if not filepath.exists():
            continue
        
        print(f"📝 {filename}...")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            
            content, changed = optimize_font_loading(content)
            
            if changed:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated += 1
                print(f"  ✅ Optimized font loading")
            else:
                print(f"  ⏭️  Font loading already optimized")
        except Exception as e:
            print(f"  ❌ Error: {e}")
        print()
    
    print("=" * 80)
    print(f"✅ Updated: {updated}/{len(PRIORITY_PAGES)}")
    print("=" * 80)

if __name__ == '__main__':
    main()

