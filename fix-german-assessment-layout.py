#!/usr/bin/env python3
"""
Fix messy layout in German assessment - hide screens properly
"""

from pathlib import Path
import re

def fix_german_assessment_layout():
    """Fix screen visibility and progress container in German assessment"""
    file_path = 'belt-assessment-v2-de.html'
    
    if not Path(file_path).exists():
        print(f"❌ File not found: {file_path}")
        return
    
    content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
    original = content
    
    # 1. Ensure screen visibility CSS is in place
    if '.screen {' not in content or '.screen.active' not in content:
        # Find where to insert it (before progress-container)
        insert_pos = content.find('.progress-container {')
        if insert_pos > 0:
            screen_css = '''
        /* Screen Visibility Control - Hide all screens except active */
        .screen {
            display: none;
        }
        .screen.active {
            display: block;
        }
        
        '''
            content = content[:insert_pos] + screen_css + content[insert_pos:]
    
    # 2. Hide progress container initially
    if 'display: none; /* Hidden initially' not in content:
        content = re.sub(
            r'(\.progress-container\s*\{[^}]*?z-index:\s*50;)',
            r'\1\n            display: none; /* Hidden initially - shown when assessment starts */',
            content,
            flags=re.DOTALL
        )
    
    # 3. Update startAssessment to show progress
    if 'progressContainer' not in content or 'style.display = \'block\'' not in content:
        content = re.sub(
            r'(function startAssessment\(\)\s*\{[^}]*?showFrage\(\);)',
            r'\1\n            // Show progress container when starting\n            document.getElementById(\'progressContainer\').style.display = \'block\';',
            content,
            flags=re.DOTALL
        )
    
    # 4. Hide progress when showing results
    if 'screen-results.*classList.add.*active' in content:
        content = re.sub(
            r'(document\.getElementById\(\'screen-results\'\)\.classList\.add\(\'active\'\);)',
            r'// Hide progress when showing results\n            document.getElementById(\'progressContainer\').style.display = \'none\';\n            \1',
            content
        )
    
    if content != original:
        Path(file_path).write_text(content, encoding='utf-8')
        print(f"✅ Fixed layout in {file_path}")
        print("   - Added screen visibility CSS")
        print("   - Hide progress container initially")
        print("   - Show/hide progress at right times")
    else:
        print(f"ℹ️  {file_path} already has proper layout control")

if __name__ == '__main__':
    print("🔧 Fixing German Assessment Layout...\n")
    fix_german_assessment_layout()
    print("\n✅ Layout fix complete!")

