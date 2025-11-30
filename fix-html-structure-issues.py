#!/usr/bin/env python3
"""
Fix HTML structure issues - mismatched tags, unclosed divs
"""

import re
from pathlib import Path

def fix_html_structure(filepath):
    """Fix HTML structure issues in a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        filename = Path(filepath).name
        
        # Count divs
        open_divs = content.count('<div')
        close_divs = content.count('</div>')
        
        if open_divs == close_divs:
            return False  # No issues
        
        # Try to fix common issues
        # 1. Check for self-closing divs (invalid HTML)
        content = re.sub(r'<div([^>]*)/>', r'<div\1></div>', content)
        
        # 2. Check for missing closing tags at end of file
        # Count again after first fix
        open_divs = content.count('<div')
        close_divs = content.count('</div>')
        
        diff = open_divs - close_divs
        
        if diff > 0:
            # Add missing closing divs at end of body (before </body>)
            if '</body>' in content:
                closing_divs = '</div>' * diff
                content = content.replace('</body>', closing_divs + '</body>')
            elif '</html>' in content:
                closing_divs = '</div>' * diff
                content = content.replace('</html>', closing_divs + '</html>')
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed {filename}: Added {diff} closing div(s)")
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error fixing {filepath}: {e}")
        return False

# Fix known problematic files
problem_files = [
    '21-day-mood-tracker.html'
]

fixed_count = 0
for file in problem_files:
    if Path(file).exists():
        if fix_html_structure(file):
            fixed_count += 1

print(f"\n✅ Fixed {fixed_count} file(s)")

