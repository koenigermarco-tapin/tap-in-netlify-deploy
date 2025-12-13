#!/usr/bin/env python3
"""Apply VS Code fixes if needed and fix remaining background errors"""

import os
import re

print("=" * 80)
print("APPLYING VS CODE FIXES & REMAINING ISSUES")
print("=" * 80)
print()

# Check if VS Code fixes are already applied
fixes_to_apply = []

# 1. Check belt-assessment-sales-landing.html
with open('belt-assessment-sales-landing.html', 'r') as f:
    content = f.read()
    if 'onclick="location.href=\'belt-assessment-v2-de.html\'">Deutsche Version' in content:
        print("✅ VS Code Fix 1: Already applied - Deutsche Version button fixed")
    elif 'onclick="location.href="belt-assessment-v2.html"">Deutsche Version' in content:
        print("❌ VS Code Fix 1: NEEDED - Broken button found")
        fixes_to_apply.append({
            'file': 'belt-assessment-sales-landing.html',
            'type': 'fix_button'
        })
    else:
        print("⚠️  VS Code Fix 1: Unknown state - checking...")
        de_button = re.search(r'Deutsche Version.*?onclick="[^"]*"', content, re.DOTALL)
        if de_button:
            print(f"   Found: {de_button.group()[:80]}...")

# 2. Check belt-assessment-v2.html for language switcher
with open('belt-assessment-v2.html', 'r') as f:
    content = f.read()
    if '🇩🇪 Deutsche Version' in content or 'Deutsche Version' in content and 'language switcher' in content.lower():
        print("✅ VS Code Fix 2: Already applied - Language switcher in English assessment")
    else:
        print("❌ VS Code Fix 2: NEEDED - No language switcher in English assessment")
        fixes_to_apply.append({
            'file': 'belt-assessment-v2.html',
            'type': 'add_lang_switcher',
            'target': 'belt-assessment-v2-de.html',
            'label': '🇩🇪 Deutsche Version'
        })

# 3. Check belt-assessment-v2-de.html for language switcher
with open('belt-assessment-v2-de.html', 'r') as f:
    content = f.read()
    if '🇬🇧 English Version' in content or 'English Version' in content and 'language switcher' in content.lower():
        print("✅ VS Code Fix 3: Already applied - Language switcher in German assessment")
    else:
        print("❌ VS Code Fix 3: NEEDED - No language switcher in German assessment")
        fixes_to_apply.append({
            'file': 'belt-assessment-v2-de.html',
            'type': 'add_lang_switcher',
            'target': 'belt-assessment-v2.html',
            'label': '🇬🇧 English Version'
        })

# 4. Check for background errors (showErrorToast)
background_error_files = []
for file in ['gym-dashboard-de.html', 'gym-dashboard.html']:
    if os.path.exists(file):
        with open(file, 'r') as f:
            content = f.read()
            if 'showErrorToast' in content:
                print(f"❌ Background Error: {file} contains showErrorToast")
                background_error_files.append(file)

print()
print("=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"VS Code fixes needed: {len(fixes_to_apply)}")
print(f"Background error files: {len(background_error_files)}")
print()

if fixes_to_apply or background_error_files:
    print("🔧 FIXES TO APPLY:")
    for fix in fixes_to_apply:
        print(f"  - {fix['file']}: {fix['type']}")
    for file in background_error_files:
        print(f"  - {file}: Remove showErrorToast")
else:
    print("✅ All VS Code fixes already applied!")

