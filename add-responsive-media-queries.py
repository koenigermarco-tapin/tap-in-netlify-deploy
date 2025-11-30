#!/usr/bin/env python3
"""
Add responsive media queries to files missing them
"""

import re
from pathlib import Path
import os

def add_media_queries(filepath):
    """Add responsive media queries if missing"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file already has media queries
        if '@media' in content:
            return False
        
        # Check if file has layout-related CSS
        has_layout = 'width:' in content or 'grid' in content or 'flex' in content
        if not has_layout:
            return False
        
        filename = Path(filepath).name
        
        # Find style tag or create one
        style_pattern = r'(<style[^>]*>)(.*?)(</style>)'
        match = re.search(style_pattern, content, re.DOTALL)
        
        if match:
            # Add media queries before closing style tag
            style_content = match.group(2)
            media_queries = '''

/* Responsive Design */
@media (max-width: 768px) {
    /* Mobile styles */
    * {
        box-sizing: border-box;
    }
    
    .container {
        width: 100%;
        padding: 1rem;
    }
    
    /* Make grids single column on mobile */
    [class*="grid"] {
        grid-template-columns: 1fr !important;
    }
    
    /* Ensure images are responsive */
    img {
        max-width: 100%;
        height: auto;
    }
    
    /* Touch-friendly button sizes */
    button, .btn, a.button {
        min-height: 44px;
        min-width: 44px;
    }
}

@media (max-width: 480px) {
    /* Small mobile adjustments */
    body {
        font-size: 14px;
    }
    
    h1 { font-size: 1.5rem; }
    h2 { font-size: 1.25rem; }
    h3 { font-size: 1.1rem; }
}'''
            
            new_content = match.group(1) + style_content + media_queries + match.group(3)
            content = content.replace(match.group(0), new_content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Added media queries to {filename}")
            return True
        else:
            # No style tag found, add one
            if '</head>' in content:
                media_style = '''<style>
/* Responsive Design */
@media (max-width: 768px) {
    .container {
        width: 100%;
        padding: 1rem;
    }
    
    [class*="grid"] {
        grid-template-columns: 1fr !important;
    }
    
    img {
        max-width: 100%;
        height: auto;
    }
    
    button, .btn {
        min-height: 44px;
        min-width: 44px;
    }
}
</style>'''
                content = content.replace('</head>', media_style + '\n</head>')
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✅ Added responsive styles to {filename}")
                return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error fixing {filepath}: {e}")
        return False

# Find files without media queries
files_to_fix = []
for root, dirs, files in os.walk('.'):
    skip_dirs = {'node_modules', '.git', 'android', 'ios', 'dist', 'build', '__pycache__'}
    dirs[:] = [d for d in dirs if d not in skip_dirs]
    
    for file in files:
        if file.endswith('.html') and 'white-label' in file:
            files_to_fix.append(os.path.join(root, file))

fixed_count = 0
for file in files_to_fix:
    if add_media_queries(file):
        fixed_count += 1

print(f"\n✅ Fixed {fixed_count} file(s)")

