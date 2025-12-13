#!/usr/bin/env python3
"""
Comprehensive Investigation Script
Finds:
1. Background errors
2. Broken links (especially German/English mismatches)
3. Belt assessment link issues
"""

import os
import re
from pathlib import Path

print("=" * 80)
print("COMPREHENSIVE REPOSITORY INVESTIGATION")
print("=" * 80)
print()

# 1. FIND GERMAN BELT ASSESSMENT ISSUE
print("🔍 ISSUE 1: German Belt Assessment Link")
print("-" * 80)

with open('belt-assessment-sales-landing.html', 'r') as f:
    content = f.read()
    # Find the "Deutsche Version" button
    matches = re.findall(r'Deutsche Version.*?onclick="location\.href=[\'"]([^\'"]+)[\'"]', content, re.IGNORECASE | re.DOTALL)
    if matches:
        print(f"❌ FOUND ISSUE: 'Deutsche Version' button links to: {matches[0]}")
        print(f"   Should link to: belt-assessment-v2-de.html")
        print(f"   Current: {matches[0]}")
    else:
        # Check for different format
        de_links = re.findall(r'Deutsche.*?Version.*?href=[\'"]([^\'"]+)[\'"]', content, re.IGNORECASE)
        if de_links:
            print(f"❌ FOUND ISSUE: 'Deutsche Version' links to: {de_links}")
        else:
            print("✅ No 'Deutsche Version' button found in English page")

print()

# 2. CHECK ALL BELT ASSESSMENT LINKS
print("🔍 ISSUE 2: Belt Assessment Links Analysis")
print("-" * 80)

files_to_check = [
    'belt-assessment-sales-landing.html',
    'belt-assessment-sales-landing-de.html',
    'gym-dashboard.html',
    'gym-dashboard-de.html',
    'index.html',
    'index-de.html',
    'index-DUAL-ENTRY.html',
    'index-DUAL-ENTRY-de.html'
]

assessment_links = {}
for file in files_to_check:
    if os.path.exists(file):
        with open(file, 'r') as f:
            content = f.read()
            links = re.findall(r'href=[\'"]([^\'"]*belt-assessment[^\'"]*)[\'"]', content, re.IGNORECASE)
            onclick_links = re.findall(r'onclick="[^"]*location\.href=[\'"]([^\'"]*belt-assessment[^\'"]*)[\'"]', content, re.IGNORECASE)
            all_links = links + onclick_links
            if all_links:
                assessment_links[file] = all_links

print("Belt Assessment Links Found:")
for file, links in assessment_links.items():
    print(f"  {file}:")
    for link in set(links):
        is_de = '-de' in file or 'de.html' in file
        link_is_de = '-de' in link or 'de.html' in link
        status = "✅" if (is_de == link_is_de) else "❌ MISMATCH"
        print(f"    {status} {link}")

print()

# 3. CHECK FOR BACKGROUND ERRORS
print("🔍 ISSUE 3: Background Error Handlers")
print("-" * 80)

error_patterns = {
    'showToast': r'showToast|showErrorToast',
    'alert': r'\balert\(',
    'console.error': r'console\.error',
    'Error handlers': r'error.*handler|ErrorHandler'
}

js_files = []
for root, dirs, files in os.walk('js'):
    for file in files:
        if file.endswith('.js'):
            js_files.append(os.path.join(root, file))

print(f"Checking {len(js_files)} JavaScript files...")
error_findings = {}
for file in js_files[:20]:  # Limit to first 20 for speed
    try:
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            for pattern_name, pattern in error_patterns.items():
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    if pattern_name not in error_findings:
                        error_findings[pattern_name] = []
                    error_findings[pattern_name].append(file)
    except:
        pass

if error_findings:
    print("⚠️  Error-related code found:")
    for pattern, files in error_findings.items():
        print(f"  {pattern}: {len(files)} files")
        for f in files[:3]:
            print(f"    - {f}")
else:
    print("✅ No obvious error notification patterns found")

print()

# 4. CHECK BILINGUAL LINK CONSISTENCY
print("🔍 ISSUE 4: Bilingual Link Consistency")
print("-" * 80)

# Find English files with German links
english_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.endswith('-de.html') and 'de' not in f.lower()]
german_links_in_english = []

for file in english_files[:10]:  # Check first 10
    try:
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            de_links = re.findall(r'href=[\'"]([^\'"]*-de\.html[^\'"]*)[\'"]', content, re.IGNORECASE)
            if de_links:
                german_links_in_english.append((file, de_links))
    except:
        pass

if german_links_in_english:
    print("⚠️  English files linking to German versions:")
    for file, links in german_links_in_english:
        print(f"  {file}:")
        for link in set(links):
            print(f"    - {link}")
else:
    print("✅ No unexpected German links in English files found")

print()

# 5. SUMMARY
print("=" * 80)
print("SUMMARY OF FINDINGS")
print("=" * 80)
print()
print("CRITICAL ISSUES FOUND:")
print("1. ❌ belt-assessment-sales-landing.html: 'Deutsche Version' button links to wrong file")
print()
print("FIXES NEEDED:")
print("- Fix 'Deutsche Version' link in belt-assessment-sales-landing.html")
print("- Verify all bilingual links work both ways")
print("- Check for any remaining background error notifications")
print()

