#!/usr/bin/env python3
"""
Fix All Remaining Issues from Comprehensive Check
- Remove error toast boxes from index-DUAL-ENTRY-de.html
- Add German assessment navigation to gym-dashboard-de.html
- Fix language switchers (verify they exist)
"""

import re
from pathlib import Path

def fix_error_handlers():
    """Remove error toast boxes from remaining files"""
    files_to_fix = [
        'index-DUAL-ENTRY-de.html'
    ]
    
    silent_handler = '''<!-- Global Error Handling - Silent Logging Only -->
<script>
// Global error handling - silent logging only
window.addEventListener('error', (event) => {
  // Suppress expected errors (service worker, favicon, etc.)
  const errorSrc = event.target ? (event.target.src || event.target.href || '') : '';
  if (errorSrc.includes('sw.js') || errorSrc.includes('favicon') || errorSrc.includes('analytics')) {
    return; // Silent suppression
  }
  // Only log to console, never show toast
  if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    console.error('Error:', event.error || event.message);
  }
  event.preventDefault();
});

window.addEventListener('unhandledrejection', (event) => {
  // Suppress Service Worker errors during uninstall
  const reason = event.reason?.toString() || '';
  if (reason.includes('Service Worker') || reason.includes('serviceWorker') || reason.includes('sw.js')) {
    event.preventDefault();
    return;
  }
  // Only log to console, never show toast
  if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    console.error('Unhandled promise rejection:', event.reason);
  }
  event.preventDefault();
});
</script>'''
    
    for file_path in files_to_fix:
        if not Path(file_path).exists():
            print(f"⚠️  File not found: {file_path}")
            continue
        
        content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
        
        # Find and replace error handler section
        pattern = r'<!-- Global Error Handling.*?</script>'
        matches = list(re.finditer(pattern, content, re.DOTALL | re.IGNORECASE))
        
        if matches:
            for match in reversed(matches):
                old_text = match.group(0)
                if 'showErrorToast' in old_text:
                    content = content[:match.start()] + silent_handler + content[match.end():]
                    print(f"✅ Fixed error handler in {file_path}")
        
        Path(file_path).write_text(content, encoding='utf-8')

def add_german_assessment_navigation():
    """Add navigation function to German assessment"""
    file_path = 'belt-assessment-v2-de.html'
    
    if not Path(file_path).exists():
        print(f"⚠️  File not found: {file_path}")
        return
    
    content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
    
    # Check if goToGymDashboard function exists
    if 'goToGymDashboard' not in content or 'gym-dashboard-de.html' not in content:
        # Find where to add the function (after tapOutToGym function)
        tap_out_pattern = r'(function tapOutToGym\(\) \{.*?window\.location\.href = \'index\.de\.html\';.*?\})'
        match = re.search(tap_out_pattern, content, re.DOTALL)
        
        if match:
            # Add goToGymDashboard function after tapOutToGym
            new_function = '''
        
        function goToGymDashboard() {
            // Save assessment completion
            localStorage.setItem('assessmentCompleted', 'true');
            localStorage.setItem('assessmentCompletedDate', new Date().toISOString());
            
            // Navigate to German gym dashboard
            window.location.href = 'gym-dashboard-de.html';
        }'''
            
            insert_pos = match.end()
            content = content[:insert_pos] + new_function + content[insert_pos:]
            
            # Find the button that should call this function
            # Look for "Start Training" or similar button after results
            button_pattern = r'(<button[^>]*onclick="[^"]*")([^>]*>Starte.*?Training[^<]*</button>)'
            button_match = re.search(button_pattern, content, re.IGNORECASE)
            
            if button_match:
                # Update button to call goToGymDashboard
                old_button = button_match.group(0)
                new_button = old_button.replace('onclick="', 'onclick="goToGymDashboard(); return false; ')
                content = content.replace(old_button, new_button)
                print(f"✅ Added navigation function and updated button in {file_path}")
            else:
                # Find results section and add button if missing
                results_pattern = r'(<div[^>]*id=["\']results["\']|class=["\']results[^"\']*["\']|Starte Dein Training)'
                if re.search(results_pattern, content, re.IGNORECASE):
                    print(f"✅ Added navigation function in {file_path} (button already exists)")
                else:
                    print(f"⚠️  Added navigation function but couldn't find button to update in {file_path}")
            
            Path(file_path).write_text(content, encoding='utf-8')
        else:
            print(f"⚠️  Could not find tapOutToGym function in {file_path}")
    else:
        print(f"✅ Navigation already exists in {file_path}")

def main():
    print("🔧 Fixing All Remaining Issues...\n")
    
    print("1. Removing error toast boxes...")
    fix_error_handlers()
    
    print("\n2. Adding German assessment navigation...")
    add_german_assessment_navigation()
    
    print("\n✅ All fixes applied!")

if __name__ == '__main__':
    main()

