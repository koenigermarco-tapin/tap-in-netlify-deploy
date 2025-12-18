#!/usr/bin/env python3
"""Properly comment out all minified JS files in White Belt files"""

import re
from pathlib import Path

def fix_file(filepath):
    """Comment out minified JS files"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # Pattern 1: If performance-optimizer is NOT in a comment, comment it out
    if '<script src="../../../js/performance-optimizer.min.js"></script>' in content:
        # Check if it's already commented
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if 'performance-optimizer.min.js' in line and '<script' in line:
                # Check context - is it in a comment?
                is_commented = False
                for j in range(max(0, i-3), i):
                    if '<!--' in lines[j] and '-->' not in lines[j]:
                        is_commented = True
                        break
                    if '-->' in lines[j]:
                        is_commented = False
                        break
                
                if not is_commented:
                    # Need to add comment block
                    # Find where to insert
                    insert_pos = i
                    # Look for comment start before
                    comment_started = False
                    for j in range(max(0, i-5), i):
                        if '<!-- REMOVED' in lines[j] or '<!-- Performance Optimizer' in lines[j]:
                            comment_started = True
                            break
                    
                    if not comment_started:
                        # Insert comment start before this line
                        lines.insert(insert_pos, '<!-- REMOVED: Syntax errors in minified files causing console errors')
                        insert_pos += 1
                        changes.append("Added comment start")
                    
                    # Find storage-health line and add comment end after it
                    for k in range(insert_pos, min(insert_pos+10, len(lines))):
                        if 'storage-health.min.js' in lines[k] and '<script' in lines[k]:
                            # Add comment end after this line
                            if k+1 < len(lines) and '-->' not in lines[k+1]:
                                lines.insert(k+1, '-->')
                                changes.append("Added comment end")
                            break
                    break
        
        content = '\n'.join(lines)
    
    # Pattern 2: Use regex to fix the block properly
    # Find the pattern: <!-- Performance Optimizer --> followed by script tags
    pattern = r'(<!-- Performance Optimizer[^>]*>)\s*(<script src="[^"]*performance-optimizer\.min\.js"></script>)\s*(<script src="[^"]*shared-quiz-system\.js"></script>)'
    
    if re.search(pattern, content):
        # Replace with commented version
        replacement = r'''\1
<!-- REMOVED: Syntax errors in minified files causing console errors
\2
<script src="../../../js/storage-health.min.js"></script>
-->
\3'''
        content = re.sub(pattern, replacement, content)
        changes.append("Fixed comment block with regex")
    
    # Also handle case where storage-health is separate
    if '<script src="../../../js/storage-health.min.js"></script>' in content:
        # Check if it's in a comment
        if '<!-- REMOVED' not in content.split('storage-health.min.js')[0][-200:]:
            # It's not commented, need to comment it
            content = re.sub(
                r'(<script src="[^"]*storage-health\.min\.js"></script>)',
                r'<!-- REMOVED: Syntax errors\n\1\n-->',
                content,
                count=1
            )
            changes.append("Commented out storage-health")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes
    return False, []

files = [
    'src/pages/gym/white-belt-stripe1-gamified.html',
    'src/pages/gym/white-belt-stripe2-gamified.html',
    'src/pages/gym/white-belt-stripe3-gamified.html',
    'src/pages/gym/white-belt-stripe4-gamified.html',
    'src/pages/gym/white-belt-stripe1-gamified-de.html',
    'src/pages/gym/white-belt-stripe2-gamified-de.html',
    'src/pages/gym/white-belt-stripe3-gamified-de.html',
    'src/pages/gym/white-belt-stripe4-gamified-de.html',
]

print("🔧 Fixing minified JS in all White Belt files...")
print("=" * 60)

fixed = 0
for filepath in files:
    path = Path(filepath)
    if path.exists():
        changed, changes = fix_file(path)
        if changed:
            print(f"\n✅ Fixed: {path.name}")
            for change in changes:
                print(f"   {change}")
            fixed += 1
        else:
            # Verify it's actually commented
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            if 'performance-optimizer.min.js' in content:
                # Check if it's in a comment
                idx = content.find('performance-optimizer.min.js')
                before = content[max(0, idx-200):idx]
                if '<!-- REMOVED' in before or '<!--' in before.split('-->')[-1]:
                    print(f"✓ {path.name} - Already properly commented")
                else:
                    print(f"⚠️  {path.name} - Still has active minified JS!")
            else:
                print(f"✓ {path.name} - No minified JS found")

print("\n" + "=" * 60)
print(f"✅ Processed {len(files)} files, {fixed} needed fixes")

