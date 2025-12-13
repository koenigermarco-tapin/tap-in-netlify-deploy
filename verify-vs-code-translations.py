#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verify VS Code Claude Translations
Check quality, links, and completeness
"""

import os
import re

def verify_german_file(filepath):
    """Verify a German translation file"""
    if not os.path.exists(filepath):
        return {'exists': False}
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    good = []
    
    # Check lang="de"
    if 'lang="de"' in content:
        good.append("✅ Has lang='de'")
    elif 'lang="en"' in content:
        issues.append("❌ Still has lang='en'")
    
    # Check for wrong language links
    wrong_links = [
        'href="leadership-games.html"',
        'href="hub-assessment-center.html"',
        'href="values-discovery-assessment.html"',
        'href="open-mat-inner-game-leadership.html"',
        'href="index.html"',
        'href="gym-dashboard.html"',
        'href="learning-hub.html"',
    ]
    
    for link in wrong_links:
        if link in content:
            issues.append(f"❌ Has wrong link: {link}")
    
    # Check for "Sie" violations
    if re.search(r'\bSie\s+(sind|haben|können|sollten|müssen)', content, re.I):
        issues.append("⚠️  Found 'Sie' form (should be Du-form)")
    
    # Check for German links
    if '-de.html' in content:
        good.append("✅ Has German links")
    
    return {
        'exists': True,
        'size': os.path.getsize(filepath) / 1024,
        'issues': issues,
        'good': good
    }

def main():
    print("="*80)
    print("🔍 VERIFYING VS CODE CLAUDE TRANSLATIONS")
    print("="*80)
    print()
    
    files_to_check = [
        'leadership-games-de.html',
        'hub-assessment-center-de.html',
        'values-discovery-assessment-de.html',
        'open-mat-inner-game-leadership-de.html',
    ]
    
    all_issues = []
    
    for filepath in files_to_check:
        result = verify_german_file(filepath)
        
        if not result['exists']:
            print(f"❌ {filepath}: NOT FOUND")
            all_issues.append(f"{filepath}: Missing")
        else:
            print(f"✅ {filepath} ({result['size']:.1f} KB)")
            for good in result.get('good', []):
                print(f"   {good}")
            for issue in result.get('issues', []):
                print(f"   {issue}")
                all_issues.append(f"{filepath}: {issue}")
            print()
    
    print("="*80)
    if all_issues:
        print(f"⚠️  Found {len(all_issues)} issues to fix")
    else:
        print("✅ All translations look good!")
    print("="*80)

if __name__ == '__main__':
    main()

