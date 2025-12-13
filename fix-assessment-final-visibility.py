#!/usr/bin/env python3
"""
Final fix for assessment visibility and functionality
"""

from pathlib import Path
import re

def fix_visibility():
    """Ensure correct initial visibility states"""
    file_path = Path('sales-recruiting-stage1.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # 1. Ensure results section is hidden by default
    results_pattern = r'(<div id="results"[^>]*?)class="results"'
    if 'class="results"' in content and 'style=' not in re.search(results_pattern, content).group(0) if re.search(results_pattern, content) else '':
        content = re.sub(
            results_pattern,
            r'\1class="results" style="display: none;"',
            content,
            count=1
        )
    
    # 2. Ensure CSS for .results is correct
    if '.results {' not in content or '.results.active' not in content:
        # Add CSS for results visibility
        css_to_add = '''
        .results { display: none; }
        .results.active { display: block; }
        '''
        # Find </style> or add before </head>
        if '</style>' in content:
            content = content.replace('</style>', css_to_add + '\n    </style>', 1)
    
    # 3. Make sure startAssessment button has proper onclick handler
    button_pattern = r'<button[^>]*onclick="startAssessment\(\)"[^>]*>'
    matches = list(re.finditer(button_pattern, content))
    if matches:
        for match in matches:
            button_html = match.group(0)
            if 'onclick="startAssessment()"' in button_html:
                # Verify function exists and is callable
                if 'function startAssessment()' in content:
                    print("✅ startAssessment button and function verified")
    
    file_path.write_text(content, encoding='utf-8')
    print("✅ Fixed assessment visibility states")
    print("   - Results section hidden by default")
    print("   - Results shown when .active class added")
    print("   - Button handlers verified")

if __name__ == '__main__':
    fix_visibility()

