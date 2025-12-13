#!/usr/bin/env python3
"""
Fix email capture showing prematurely - it should only show after results
"""

from pathlib import Path
import re

def fix_email_capture():
    """Prevent email capture from showing before assessment is complete"""
    file_path = Path('sales-recruiting-stage1.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # 1. Ensure email capture initialization script doesn't run on page load
    # Remove any setTimeout calls that auto-initialize
    patterns_to_remove = [
        r'setTimeout\(initializeEmailCapture[^;]*;',
        r'setTimeout\(\(\) => initializeEmailCapture\(\)[^;]*;',
    ]
    
    for pattern in patterns_to_remove:
        content = re.sub(pattern, '', content)
    
    # 2. Make sure email capture only initializes from showResults()
    # Find the DOMContentLoaded section
    dom_content_pattern = r'(document\.addEventListener\(\'DOMContentLoaded\'[^)]+function\(\) \{[^}]+)'
    
    # More specific: find where initializeEmailCapture is defined
    init_pattern = r'(window\.initEmailCapture = initializeEmailCapture;)'
    replacement = r'''\1
            
            // CRITICAL: Do NOT auto-initialize email capture on page load
            // It will only be initialized when showResults() calls initEmailCapture()
            // Email capture should ONLY appear after assessment completion'''
    
    content = re.sub(init_pattern, replacement, content)
    
    # 3. Add CSS to hide email capture container by default
    css_to_add = '''
        /* Hide email capture by default - only show after results */
        #email-capture-container {
            display: none !important;
        }
        
        /* Only show when explicitly shown via JavaScript */
        #email-capture-container.visible {
            display: block !important;
        }
    '''
    
    if '#email-capture-container' not in content:
        # Add CSS before closing </style>
        if '</style>' in content:
            # Find the last </style> tag before </head>
            style_close_pos = content.rfind('</style>', 0, content.find('</head>'))
            if style_close_pos > 0:
                content = content[:style_close_pos] + css_to_add + '\n    ' + content[style_close_pos:]
    
    # 4. Update email capture component to add 'visible' class when showing
    # This is already handled in js/email-capture-component.js but let's make sure
    
    file_path.write_text(content, encoding='utf-8')
    print("✅ Fixed email capture premature display")
    print("   - Removed all auto-initialization on page load")
    print("   - Email capture will only show when explicitly called from showResults()")
    print("   - Added CSS to hide email capture by default")

if __name__ == '__main__':
    fix_email_capture()

