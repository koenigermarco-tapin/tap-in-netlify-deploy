#!/usr/bin/env python3
"""
Complete fix: Remove all orphaned code and ensure clean navigation
"""

from pathlib import Path

def fix_german_complete():
    """Remove all orphaned code from German file"""
    file_path = Path('index-DUAL-ENTRY-de.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # Find the language handler section
    handler_start = content.find('// Language switch handler - Navigate to language-specific page')
    
    if handler_start > 0:
        # Find the end of the handler (should be });)
        # The handler should end at the second });
        lines = content[handler_start:].split('\n')
        handler_lines = []
        brace_count = 0
        found_end = False
        
        for i, line in enumerate(lines):
            handler_lines.append(line)
            brace_count += line.count('{') - line.count('}')
            
            # Check if this is the end of the handler
            if '});' in line and brace_count <= 0 and i > 10:
                found_end = True
                break
        
        if found_end:
            # Everything after handler_lines is orphaned code that should be removed
            handler_code = '\n'.join(handler_lines)
            
            # Find where to insert it back
            script_start = content.rfind('<script>', 0, handler_start)
            script_end = content.find('</script>', handler_start)
            
            # Rebuild content: everything before handler + handler code + closing script
            before_handler = content[:handler_start]
            after_script = content[script_end:]
            
            # Ensure handler code ends properly
            if not handler_code.strip().endswith('});'):
                handler_code = handler_code.rstrip() + '\n})();'
            
            new_content = before_handler + handler_code + '\n</script>' + after_script[9:]  # Skip </script>
            
            file_path.write_text(new_content, encoding='utf-8')
            print("✅ Removed all orphaned code from German file")

if __name__ == '__main__':
    fix_german_complete()

