#!/usr/bin/env python3
"""
Remove orphaned duplicate code after language switcher handler
"""

from pathlib import Path

def remove_orphaned():
    """Remove orphaned code that's causing syntax errors"""
    file_path = Path('index-DUAL-ENTRY-de.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # Find the end of the first complete handler (should end with });)
    handler_end = content.find('    });')
    if handler_end > 0:
        # Find the closing script tag
        script_end = content.find('</script>', handler_end)
        
        # Check if there's orphaned code between handler_end and script_end
        between = content[handler_end+6:script_end].strip()
        
        # Remove any orphaned code that looks like duplicate navigation
        lines = content.split('\n')
        new_lines = []
        skip_mode = False
        
        for i, line in enumerate(lines):
            # After the first });, skip orphaned code
            if '    });' in line and not skip_mode:
                new_lines.append(line)
                skip_mode = True
                continue
            
            if skip_mode:
                # Skip until we hit the closing script or meaningful code
                if '</script>' in line:
                    skip_mode = False
                    new_lines.append(line)
                elif '// Auto-redirect' in line or 'document.addEventListener' in line:
                    skip_mode = False
                    new_lines.append(line)
                # Skip orphaned navigation code
                elif '// Store preference' in line or 'localStorage.setItem' in line or \
                     '// Navigate to language-specific page' in line and i < handler_end + 50:
                    continue
                elif '</script>' not in line and '// Auto-redirect' not in line:
                    continue
            else:
                new_lines.append(line)
        
        content = '\n'.join(new_lines)
        file_path.write_text(content, encoding='utf-8')
        print("✅ Removed orphaned duplicate code")

if __name__ == '__main__':
    remove_orphaned()

