#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aggressive Fix for All German Link Issues
Systematically fixes all link patterns in all German files
"""

import os
import re
from collections import defaultdict

class AggressiveGermanLinkFixer:
    def __init__(self):
        self.fixes = []
        self.files_modified = set()
        
    def get_link_replacements(self):
        """Get comprehensive map of wrong links to correct German versions"""
        replacements = {}
        
        # Main navigation
        replacements.update({
            'index.html': 'index.de.html',
            'gym-dashboard.html': 'gym-dashboard-de.html',
            'learning-hub.html': 'learning-hub-de.html',
        })
        
        # Belt assessments
        replacements.update({
            'belt-assessment-v2.html': 'belt-assessment-v2-de.html',
            'belt-assessment.html': 'belt-assessment-v2-de.html',
            'belt-assessment-sales-landing.html': 'belt-assessment-sales-landing-de.html',
        })
        
        # Belt hubs
        for belt in ['white', 'blue', 'purple', 'brown', 'black']:
            replacements[f'{belt}-belt.html'] = f'{belt}-belt-de.html'
            replacements[f'{belt}-belt-assessment.html'] = f'{belt}-belt-assessment-de.html'
        
        # Stripe files (check what exists)
        for belt in ['white', 'blue', 'purple', 'brown', 'black']:
            for stripe in [1, 2, 3, 4]:
                stripe_de = f'{belt}-belt-stripe{stripe}-gamified-de.html'
                if os.path.exists(stripe_de):
                    # All possible stripe patterns
                    replacements[f'{belt}-belt-stripe{stripe}.html'] = stripe_de
                    replacements[f'{belt}-belt-stripe{stripe}-carousel.html'] = stripe_de
                    replacements[f'{belt}-belt-stripe{stripe}-carousel-NEW.html'] = stripe_de
                    replacements[f'{belt}-belt-stripe{stripe}-interactive-FULL.html'] = stripe_de
        
        return replacements
    
    def fix_file(self, filepath):
        """Fix all links in a single file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"    ⚠️  Error reading {filepath}: {e}")
            return 0
        
        original = content
        replacements = self.get_link_replacements()
        changes_made = 0
        
        # Fix each replacement
        for wrong_link, correct_link in replacements.items():
            if wrong_link not in content:
                continue
            
            # Pattern 1: href="link"
            pattern1 = rf'href=["\']{re.escape(wrong_link)}["\']'
            if re.search(pattern1, content):
                content = re.sub(pattern1, f'href="{correct_link}"', content)
                changes_made += 1
            
            # Pattern 2: window.location.href = "link"
            pattern2 = rf'(?:window\.location|location\.href)\s*=\s*["\']{re.escape(wrong_link)}["\']'
            if re.search(pattern2, content):
                content = re.sub(pattern2, f'window.location.href = "{correct_link}"', content)
                changes_made += 1
            
            # Pattern 3: onclick="...link..."
            pattern3 = rf'onclick=["\'][^"\']*{re.escape(wrong_link)}[^"\']*["\']'
            if re.search(pattern3, content):
                # Replace link in onclick
                def replace_onclick(match):
                    onclick_content = match.group(0)
                    return onclick_content.replace(wrong_link, correct_link)
                content = re.sub(pattern3, replace_onclick, content)
                changes_made += 1
            
            # Pattern 4: String literals 'link' or "link"
            pattern4 = rf'["\']{re.escape(wrong_link)}["\']'
            # But not if it's already in a href or similar
            if re.search(pattern4, content):
                # Only replace if it's not part of a larger URL pattern
                if not re.search(rf'https?://[^"\']*{re.escape(wrong_link)}', content):
                    # Replace standalone string literals
                    def replace_string(match):
                        full_match = match.group(0)
                        # Don't replace if it's already correct or in a comment
                        if correct_link in full_match or '//' in full_match[:full_match.find(wrong_link)]:
                            return full_match
                        return full_match.replace(wrong_link, correct_link)
                    content = re.sub(pattern4, replace_string, content)
                    changes_made += 1
        
        # Special: Fix function calls like tapToBelt('white-belt.html')
        belt_pattern = r"tapToBelt\(['\"]([^'\"]+-belt\.html)['\"]\)"
        def fix_tap_to_belt(match):
            belt_file = match.group(1)
            belt_de = belt_file.replace('.html', '-de.html')
            if os.path.exists(belt_de):
                return match.group(0).replace(belt_file, belt_de)
            return match.group(0)
        
        if re.search(belt_pattern, content):
            content = re.sub(belt_pattern, fix_tap_to_belt, content)
            if content != original:
                changes_made += 1
        
        # Special: Fix data-link attributes
        data_link_pattern = rf'data-link=["\']{re.escape(wrong_link)}["\']'
        for wrong, correct in replacements.items():
            if re.search(data_link_pattern.replace(wrong_link, wrong), content):
                content = re.sub(
                    rf'data-link=["\']{re.escape(wrong)}["\']',
                    f'data-link="{correct}"',
                    content
                )
                changes_made += 1
        
        # Write back if changed
        if content != original:
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.files_modified.add(filepath)
                return changes_made
            except Exception as e:
                print(f"    ⚠️  Error writing {filepath}: {e}")
                return 0
        
        return 0
    
    def fix_all_german_files(self):
        """Fix all German files"""
        print("="*80)
        print("🔧 AGGRESSIVE GERMAN LINK FIX")
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
            changes = self.fix_file(filepath)
            if changes > 0:
                total_changes += changes
                print(f"  ✅ Fixed {filepath} ({changes} changes)")
        
        print(f"\n✅ Total files modified: {len(self.files_modified)}")
        print(f"✅ Total changes applied: {total_changes}")
        
        return total_changes

def main():
    fixer = AggressiveGermanLinkFixer()
    total_changes = fixer.fix_all_german_files()
    
    print("\n" + "="*80)
    if total_changes > 0:
        print(f"✅ FIXED {total_changes} LINK ISSUES")
    else:
        print("✅ NO ADDITIONAL FIXES NEEDED")
    print("="*80)

if __name__ == '__main__':
    main()

