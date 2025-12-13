#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix links to point to found German versions
"""

import os
import re

def fix_found_versions():
    """Fix links to use the German versions that already exist"""
    
    found_mappings = {
        'combined-profile-carousel.html': 'combined-profile-carousel.de.html',
        'team-assessment-enhanced-v2.html': 'team-assessment-enhanced-v2.de.html',
        'worker-type-assessment.html': 'worker-type-assessment.de.html',
    }
    
    # Get all German files
    german_files = [f for f in os.listdir('.') if f.endswith('-de.html') or f.endswith('.de.html') or f == 'index.de.html']
    
    fixes = 0
    
    for german_file in german_files:
        try:
            with open(german_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            
            for eng_file, de_file in found_mappings.items():
                if eng_file in content:
                    content = content.replace(eng_file, de_file)
            
            if content != original:
                with open(german_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"  ✅ Fixed {german_file}")
        except:
            pass
    
    return fixes

if __name__ == '__main__':
    print("Fixing links to use found German versions...")
    fixes = fix_found_versions()
    print(f"\n✅ Fixed {fixes} files")

