#!/usr/bin/env python3
"""Find all broken bilingual links"""

import os
import re
from pathlib import Path

print("=" * 80)
print("FINDING BROKEN BILINGUAL LINKS")
print("=" * 80)
print()

issues = []

# Check all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('archive')]

for file in html_files:
    is_german = file.endswith('-de.html') or 'de.html' in file.lower()
    
    try:
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # Find all href links
        href_links = re.findall(r'href=[\'"]([^\'"]+)[\'"]', content, re.IGNORECASE)
        onclick_links = re.findall(r'onclick="[^"]*location\.href=[\'"]([^\'"]+)[\'"]', content, re.IGNORECASE)
        all_links = href_links + onclick_links
        
        for link in all_links:
            # Skip external links
            if link.startswith('http') or link.startswith('//'):
                continue
                
            # Check for language mismatches
            link_is_german = '-de.html' in link or link.endswith('de.html')
            link_is_english = link.endswith('.html') and not link_is_german
            
            if is_german and link_is_english and 'belt-assessment' in link.lower():
                if not any(x in link for x in ['index', 'learning-hub', 'gym-dashboard']):
                    issues.append({
                        'file': file,
                        'link': link,
                        'issue': 'German file linking to English version'
                    })
            elif not is_german and link_is_german and 'belt-assessment' in link.lower():
                if not any(x in link for x in ['-de']):
                    issues.append({
                        'file': file,
                        'link': link,
                        'issue': 'English file linking to German version (might be intentional)'
                    })
    
    except Exception as e:
        pass

print(f"Found {len(issues)} potential link issues:\n")
for issue in issues:
    print(f"❌ {issue['file']}")
    print(f"   Link: {issue['link']}")
    print(f"   Issue: {issue['issue']}")
    print()

print("\n" + "=" * 80)
print("SPECIFIC CHECKS")
print("=" * 80)
print()

# Specific checks
checks = [
    ('belt-assessment-sales-landing.html', 'Deutsche Version', 'belt-assessment-v2-de.html'),
    ('belt-assessment-sales-landing-de.html', 'English Version', 'belt-assessment-v2.html'),
]

for file, button_text, expected_link in checks:
    if os.path.exists(file):
        with open(file, 'r') as f:
            content = f.read()
            if button_text in content:
                links = re.findall(rf'{re.escape(button_text)}.*?href=[\'"]([^\'"]+)[\'"]', content, re.IGNORECASE | re.DOTALL)
                if links:
                    actual_link = links[0] if links else 'NOT FOUND'
                    status = "✅" if expected_link in actual_link else "❌"
                    print(f"{status} {file}: '{button_text}' button")
                    print(f"   Expected: {expected_link}")
                    print(f"   Found: {actual_link}")
                    if status == "❌":
                        issues.append({
                            'file': file,
                            'link': actual_link,
                            'issue': f"'{button_text}' button wrong link"
                        })
                    print()

if not issues:
    print("✅ No broken links found!")
else:
    print(f"\n⚠️  Total issues found: {len(issues)}")

