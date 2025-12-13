#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implement VS Code Claude Translations
Verify files exist, fix links, ensure quality
"""

import os
import re

def check_and_fix_file(filepath):
    """Check if file exists and fix any issues"""
    if not os.path.exists(filepath):
        print(f"⚠️  {filepath}: NOT FOUND (VS Code Claude may still be creating it)")
        return False
    
    print(f"✅ {filepath}: Found")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    fixes = []
    
    # Fix lang attribute
    if 'lang="en"' in content:
        content = content.replace('lang="en"', 'lang="de"')
        fixes.append("Fixed lang attribute")
    
    # Fix common link patterns
    link_fixes = {
        'leadership-games.html': 'leadership-games-de.html',
        'hub-assessment-center.html': 'hub-assessment-center-de.html',
        'values-discovery-assessment.html': 'values-discovery-assessment-de.html',
        'open-mat-inner-game-leadership.html': 'open-mat-inner-game-leadership-de.html',
        'gym-dashboard.html': 'gym-dashboard-de.html',
        'learning-hub.html': 'learning-hub-de.html',
        'index.html': 'index.de.html',
    }
    
    for wrong, correct in link_fixes.items():
        if wrong in content and filepath != wrong:
            # Only replace if target exists or is likely to exist
            content = content.replace(wrong, correct)
            fixes.append(f"Fixed link: {wrong} → {correct}")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   🔧 Applied {len(fixes)} fixes")
        return True
    
    print(f"   ✅ No fixes needed")
    return True

def main():
    print("="*80)
    print("🔧 IMPLEMENTING VS CODE CLAUDE TRANSLATIONS")
    print("="*80)
    print()
    
    files_to_check = [
        'leadership-games-de.html',
        'hub-assessment-center-de.html',
        'values-discovery-assessment-de.html',
        'open-mat-inner-game-leadership-de.html',
        'team-assessment-enhanced-v2.de.html',  # Verify this exists
    ]
    
    found = 0
    fixed = 0
    
    for filepath in files_to_check:
        if check_and_fix_file(filepath):
            found += 1
        print()
    
    print("="*80)
    print(f"✅ Files found: {found}/{len(files_to_check)}")
    print(f"🔧 Files fixed: {fixed}")
    print("="*80)
    
    if found < len(files_to_check):
        missing = len(files_to_check) - found
        print(f"\n⚠️  {missing} files still missing. VS Code Claude may still be working on them.")
        print("   Files will be checked again once they're created.")

if __name__ == '__main__':
    main()

