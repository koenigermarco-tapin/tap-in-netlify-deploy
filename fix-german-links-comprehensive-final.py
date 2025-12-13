#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive Final Fix for All German Links
Uses file modification dates to identify best versions
Fixes all link issues systematically
"""

import os
import re
from datetime import datetime
from collections import defaultdict

class ComprehensiveGermanLinkFixer:
    def __init__(self):
        self.fixes = []
        self.files_modified = set()
        
    def get_all_german_files(self):
        """Get all German HTML files with their info"""
        german_files = []
        
        for file in os.listdir('.'):
            if not file.endswith('.html'):
                continue
            
            if file.endswith('-de.html') or file.endswith('.de.html') or file == 'index.de.html':
                if os.path.isfile(file):
                    stat = os.stat(file)
                    german_files.append({
                        'name': file,
                        'mtime': stat.st_mtime,
                        'size': stat.st_size
                    })
        
        return sorted(german_files, key=lambda x: x['mtime'], reverse=True)
    
    def fix_file_links(self, filepath):
        """Fix all links in a German file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            return 0
        
        original = content
        changes = 0
        
        # Map of wrong links to correct German versions
        link_replacements = {
            # Main pages
            'index.html': 'index.de.html',
            'gym-dashboard.html': 'gym-dashboard-de.html',
            'learning-hub.html': 'learning-hub-de.html',
            
            # Belt assessments
            'belt-assessment-v2.html': 'belt-assessment-v2-de.html',
            'belt-assessment.html': 'belt-assessment-v2-de.html',
            'belt-assessment-sales-landing.html': 'belt-assessment-sales-landing-de.html',
            
            # Belt hubs
            'white-belt.html': 'white-belt-de.html',
            'blue-belt.html': 'blue-belt-de.html',
            'purple-belt.html': 'purple-belt-de.html',
            'brown-belt.html': 'brown-belt-de.html',
            'black-belt.html': 'black-belt-de.html',
        }
        
        # Add belt assessments
        for belt in ['white', 'blue', 'purple', 'brown', 'black']:
            link_replacements[f'{belt}-belt-assessment.html'] = f'{belt}-belt-assessment-de.html'
        
        # Apply replacements
        for wrong, correct in link_replacements.items():
            if wrong in content and os.path.exists(correct):
                # Replace in href
                content = re.sub(
                    rf'href=["\']{re.escape(wrong)}["\']',
                    f'href="{correct}"',
                    content
                )
                # Replace in JavaScript
                content = re.sub(
                    rf'["\']{re.escape(wrong)}["\']',
                    f'"{correct}"',
                    content
                )
        
        # Fix stripe completion redirects
        if 'gym-dashboard.html' in content:
            content = content.replace('gym-dashboard.html', 'gym-dashboard-de.html')
        
        # Fix stripe file links in belt hubs
        if '-belt-de.html' in filepath:
            belt = filepath.replace('-belt-de.html', '').replace('-belt.de.html', '')
            for stripe_num in [1, 2, 3, 4]:
                stripe_de = f'{belt}-belt-stripe{stripe_num}-gamified-de.html'
                if os.path.exists(stripe_de):
                    # Fix various stripe link patterns
                    patterns_to_fix = [
                        f'{belt}-belt-stripe{stripe_num}.html',
                        f'{belt}-belt-stripe{stripe_num}-carousel.html',
                        f'{belt}-belt-stripe{stripe_num}-carousel-NEW.html',
                        f'{belt}-belt-stripe{stripe_num}-interactive-FULL.html',
                    ]
                    for pattern in patterns_to_fix:
                        if pattern in content:
                            content = content.replace(pattern, stripe_de)
        
        if content != original:
            changes = len([c for c in content.split(wrong) if wrong in content]) if wrong in content else 1
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.files_modified.add(filepath)
            return 1
        
        return 0
    
    def fix_all_files(self):
        """Fix all German files"""
        print("="*80)
        print("🔧 COMPREHENSIVE GERMAN LINK FIX")
        print("="*80)
        print()
        
        german_files = self.get_all_german_files()
        print(f"📋 Found {len(german_files)} German files to check\n")
        
        total_fixes = 0
        
        for file_info in german_files:
            filepath = file_info['name']
            fixes = self.fix_file_links(filepath)
            if fixes > 0:
                total_fixes += fixes
                date = datetime.fromtimestamp(file_info['mtime']).strftime('%Y-%m-%d')
                print(f"  ✅ Fixed {filepath} (modified: {date})")
        
        print(f"\n✅ Total files modified: {len(self.files_modified)}")
        print(f"✅ Total fixes applied: {total_fixes}")
        
        return total_fixes

def main():
    fixer = ComprehensiveGermanLinkFixer()
    fixer.fix_all_files()
    
    print("\n" + "="*80)
    print("✅ GERMAN LINK FIX COMPLETE")
    print("="*80)

if __name__ == '__main__':
    main()

