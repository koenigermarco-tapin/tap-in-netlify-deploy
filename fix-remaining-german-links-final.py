#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Remaining German Link Issues - Final Pass
Handles specialized modules and checks if German versions exist
"""

import os
import re
from collections import defaultdict

class FinalGermanLinkFixer:
    def __init__(self):
        self.fixes = []
        self.files_modified = set()
        self.missing_de_versions = set()
        
    def find_german_version(self, english_file):
        """Find if a German version of an English file exists"""
        base = english_file.replace('.html', '')
        
        # Try common patterns
        patterns = [
            f"{base}-de.html",
            f"{base}.de.html",
        ]
        
        for pattern in patterns:
            if os.path.exists(pattern):
                return pattern
        
        # Try to find similar
        for file in os.listdir('.'):
            if file.endswith('-de.html') and base.split('/')[-1] in file:
                # Check if it's the same file
                if base.split('-')[0] in file:
                    return file
        
        return None
    
    def fix_file_links(self, filepath):
        """Fix links in a file, checking if German versions exist"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            return 0
        
        original = content
        changes = 0
        
        # Find all HTML links in the file
        link_pattern = r'(?:href|location\.href|data-link|tapToBelt|window\.location)\s*=\s*["\']([^"\']+\.html)["\']'
        links = re.findall(link_pattern, content)
        
        # Also find in onclick
        onclick_pattern = r'onclick=["\'][^"\']*["\']([^"\']+\.html)["\']'
        onclick_links = re.findall(onclick_pattern, content)
        
        all_links = set(links + onclick_links)
        
        for link in all_links:
            # Skip external links
            if link.startswith('http'):
                continue
            
            # Skip anchors
            if link.startswith('#'):
                continue
            
            # Skip if already German
            if link.endswith('-de.html') or link.endswith('.de.html') or link == 'index.de.html':
                continue
            
            # Find German version
            de_version = self.find_german_version(link)
            
            if de_version:
                # Replace the link
                content = content.replace(link, de_version)
                changes += 1
                self.fixes.append({
                    'file': filepath,
                    'old': link,
                    'new': de_version
                })
            else:
                # Note missing version
                self.missing_de_versions.add(link)
        
        # Also fix common patterns
        common_fixes = {
            'index.html': 'index.de.html',
            'gym-dashboard.html': 'gym-dashboard-de.html',
            'learning-hub.html': 'learning-hub-de.html',
        }
        
        for wrong, correct in common_fixes.items():
            if wrong in content and os.path.exists(correct):
                content = content.replace(wrong, correct)
                changes += 1
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            self.files_modified.add(filepath)
            return changes
        
        return 0
    
    def fix_all_remaining_files(self):
        """Fix all remaining German files"""
        print("="*80)
        print("🔧 FINAL FIX FOR REMAINING GERMAN LINKS")
        print("="*80)
        print()
        
        # Get all German files
        german_files = []
        for file in os.listdir('.'):
            if file.endswith('-de.html') or file.endswith('.de.html') or file == 'index.de.html':
                if os.path.isfile(file):
                    german_files.append(file)
        
        german_files.sort()
        print(f"📋 Checking {len(german_files)} German files...\n")
        
        total_changes = 0
        
        for filepath in german_files:
            changes = self.fix_file_links(filepath)
            if changes > 0:
                total_changes += changes
                print(f"  ✅ Fixed {filepath} ({changes} changes)")
        
        print(f"\n✅ Total files modified: {len(self.files_modified)}")
        print(f"✅ Total changes applied: {total_changes}")
        
        if self.missing_de_versions:
            print(f"\n⚠️  Missing German versions for {len(self.missing_de_versions)} files:")
            for missing in sorted(self.missing_de_versions)[:10]:
                print(f"  - {missing}")
            if len(self.missing_de_versions) > 10:
                print(f"  ... and {len(self.missing_de_versions) - 10} more")
        
        return total_changes

def main():
    fixer = FinalGermanLinkFixer()
    total_changes = fixer.fix_all_remaining_files()
    
    print("\n" + "="*80)
    if total_changes > 0:
        print(f"✅ FIXED {total_changes} ADDITIONAL LINK ISSUES")
    else:
        print("✅ NO ADDITIONAL FIXES NEEDED")
    print("="*80)
    
    # Save report
    if fixer.missing_de_versions:
        with open('MISSING-GERMAN-VERSIONS.txt', 'w', encoding='utf-8') as f:
            f.write("Missing German Versions\n")
            f.write("="*80 + "\n\n")
            for missing in sorted(fixer.missing_de_versions):
                f.write(f"- {missing}\n")
        print(f"\n📄 Report saved to: MISSING-GERMAN-VERSIONS.txt")

if __name__ == '__main__':
    main()

