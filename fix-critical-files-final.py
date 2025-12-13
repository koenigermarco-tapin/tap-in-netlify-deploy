#!/usr/bin/env python3
"""
Final fix for critical files with remaining issues
"""

import re
from pathlib import Path

critical_files = [
    "index-DUAL-ENTRY.html",
    "index-DUAL-ENTRY-de.html",
    "gym-dashboard.html",
    "gym-dashboard-de.html",
    "learning-hub.html",
    "learning-hub-de.html",
    "belt-assessment-v2.html",
    "belt-assessment-v2-de.html",
    "black-belt.html"
]

def fix_file(file_path: Path):
    """Fix a single critical file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Fix console statements - comment them out
        # Pattern: console.log/error/warn(...);
        def comment_console(match):
            line = match.group(0)
            # Don't comment if already commented or in a comment block
            if line.strip().startswith('//') or '/*' in line:
                return line
            # Comment it out
            return '// ' + line
        
        # Match console statements that aren't already commented
        pattern = r'^\s*(console\.(log|error|warn|debug|info)\s*\([^)]*\);?)'
        lines = content.split('\n')
        fixed_lines = []
        for line in lines:
            # Check if this is a console statement
            if re.match(pattern, line) and not line.strip().startswith('//'):
                # Comment it out
                fixed_lines.append('// ' + line)
            else:
                fixed_lines.append(line)
        
        content = '\n'.join(fixed_lines)
        
        # Fix fancy quotes in JavaScript strings more aggressively
        # This is a more careful approach that handles template strings
        script_pattern = r'<script[^>]*>(.*?)</script>'
        def fix_script_quotes(match):
            script_content = match.group(1)
            # Replace fancy quotes in string literals only
            # Handle both single and double quotes
            fixed = script_content
            # Replace fancy apostrophes in single-quoted strings
            fixed = re.sub(r"(?<!\\)'(?=.*?')", "'", fixed)
            # Replace fancy double quotes in double-quoted strings  
            fixed = re.sub(r'(?<!\\)"(?=.*?")', '"', fixed)
            fixed = re.sub(r'(?<!\\)"(?=.*?")', '"', fixed)
            return f'<script>{fixed}</script>'
        
        # Only apply if we're in a script tag context
        if '<script' in content:
            # More conservative: only fix obvious cases
            # Replace fancy quotes that are clearly in string contexts
            content = re.sub(r"'([^']*)'", lambda m: "'" + m.group(1).replace("'", "'") + "'", content)
            content = re.sub(r'"([^"]*)"', lambda m: '"' + m.group(1).replace('"', '"').replace('"', '"') + '"', content)
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

if __name__ == "__main__":
    root = Path(".")
    print("🔧 Fixing critical files...")
    print()
    
    fixed_count = 0
    for file_name in critical_files:
        file_path = root / file_name
        if file_path.exists():
            if fix_file(file_path):
                print(f"✅ Fixed: {file_name}")
                fixed_count += 1
            else:
                print(f"ℹ️  No changes needed: {file_name}")
        else:
            print(f"❌ Not found: {file_name}")
    
    print()
    print(f"✅ Fixed {fixed_count} files")

