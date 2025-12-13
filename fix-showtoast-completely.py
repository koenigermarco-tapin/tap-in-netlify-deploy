#!/usr/bin/env python3
"""
Completely block showToast error messages - remove ALL sources
"""

from pathlib import Path
import re

def completely_block_showtoast_errors():
    """Ensure showToast never shows error messages on landing page"""
    file_path = 'index.html'
    
    if not Path(file_path).exists():
        print(f"⚠️  File not found: {file_path}")
        return
    
    content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
    original = content
    
    # Remove any orphaned code blocks
    content = re.sub(r'</script>\s+const container.*?// \.\.\. existing toast logic.*?</script>', '</script>', content, flags=re.DOTALL)
    
    # Ensure showToast blocks errors at the VERY top
    # Replace the global error suppression script to include showToast blocking FIRST
    suppression_pattern = r'(<script src="js/error-suppressor\.js"></script>\s*<!-- Global Error Suppression[^<]*<script>[\s\S]*?)(window\.showToast[^}]*?})([\s\S]*?</script>)'
    
    match = re.search(suppression_pattern, content, re.DOTALL)
    if match:
        # showToast is already there - ensure it's blocking
        before = match.group(1)
        showtoast_block = match.group(2)
        after = match.group(3)
        
        # Ensure it blocks errors
        if 'type === \'error\'' not in showtoast_block or 'return' not in showtoast_block:
            new_showtoast = '''window.showToast = function(message, type, duration) {
            // NEVER show error toasts - completely silent
            if (type === 'error' || message && (message.includes('went wrong') || message.includes('refresh'))) {
                if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
                    console.log('⚠️ Error toast BLOCKED:', message);
                }
                return; // Block immediately
            }
            // Only allow success/info
            const container = document.getElementById('toast-container');
            if (!container) return;
            const toast = document.createElement('div');
            toast.style.cssText = `background: ${type === 'success' ? '#10b981' : '#3b82f6'}; color: white; padding: 1rem 1.5rem; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.2); min-width: 300px; max-width: 500px; animation: slideInRight 0.3s ease; display: flex; align-items: center; gap: 0.75rem; font-weight: 500;`;
            toast.innerHTML = `<span style="font-size: 1.25rem;">${type === 'success' ? '✅' : 'ℹ️'}</span><span>${message}</span>`;
            container.appendChild(toast);
            setTimeout(() => { toast.style.animation = 'slideOutRight 0.3s ease'; setTimeout(() => toast.remove(), 300); }, duration || 3000);
        };'''
            content = before + new_showtoast + after
    
    # Remove duplicate showToast definitions later in the file
    # Keep only the first one at the top
    lines = content.split('\n')
    showtoast_count = 0
    new_lines = []
    in_script = False
    
    for i, line in enumerate(lines):
        if 'window.showToast = function' in line:
            showtoast_count += 1
            if showtoast_count > 1:
                # Skip duplicate definitions - only keep the first one
                continue
        new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    if content != original:
        Path(file_path).write_text(content, encoding='utf-8')
        print(f"✅ Fixed showToast blocking in {file_path}")
    else:
        print(f"ℹ️  {file_path} already has showToast blocking")

def main():
    print("🔧 Completely Blocking showToast Error Messages...\n")
    completely_block_showtoast_errors()
    print("\n✅ showToast error blocking complete!")

if __name__ == '__main__':
    main()

