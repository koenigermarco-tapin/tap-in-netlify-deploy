#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix All German Link Issues Comprehensively
- Fix wrong language links (German files linking to English)
- Find missing files using modification dates and similar names
- Use latest file dates as quality marker
"""

import os
import re
import json
from datetime import datetime
from collections import defaultdict

class GermanLinkFixer:
    def __init__(self):
        self.fixes_applied = []
        self.files_fixed = set()
        self.missing_files_map = {}
        
    def get_file_info(self, filepath):
        """Get file info including modification date and line count"""
        if not os.path.exists(filepath):
            return None
        stat = os.stat(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            line_count = len(f.readlines())
        return {
            'path': filepath,
            'mtime': stat.st_mtime,
            'size': stat.st_size,
            'lines': line_count,
            'date': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def find_similar_files(self, missing_filename):
        """Find files with similar names (could be the same file with different naming)"""
        base_name = missing_filename.replace('-de.html', '').replace('.html', '').replace('.de.html', '')
        
        # Look for variations
        patterns = [
            f"{base_name}-de.html",
            f"{base_name}.de.html",
            f"{base_name}.html",
            f"{base_name}-v2-de.html",
            f"{base_name}-v2.html",
        ]
        
        found_files = []
        for pattern in patterns:
            if os.path.exists(pattern):
                info = self.get_file_info(pattern)
                if info:
                    found_files.append(info)
        
        # Also search for files containing the base name
        for file in os.listdir('.'):
            if base_name in file and file.endswith('.html'):
                if file not in [f['path'] for f in found_files]:
                    info = self.get_file_info(file)
                    if info:
                        found_files.append(info)
        
        # Sort by modification date (newest first)
        found_files.sort(key=lambda x: x['mtime'], reverse=True)
        return found_files
    
    def find_best_german_version(self, english_path):
        """Find the best German version of an English file"""
        base = english_path.replace('.html', '')
        
        # Common patterns
        patterns = [
            f"{base}-de.html",
            f"{base}.de.html",
        ]
        
        # Special cases
        if 'index' in english_path:
            patterns.append('index.de.html')
        
        for pattern in patterns:
            if os.path.exists(pattern):
                return pattern
        
        # Search for similar
        for file in os.listdir('.'):
            if file.endswith('-de.html') and base.replace('index', '') in file:
                return file
        
        return None
    
    def fix_wrong_language_links(self, filepath, wrong_link, correct_link):
        """Fix a wrong language link in a file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"    ⚠️  Could not read {filepath}: {e}")
            return False
        
        original = content
        changes = 0
        
        # Fix href links
        content = re.sub(
            rf'href=["\']{re.escape(wrong_link)}["\']',
            f'href="{correct_link}"',
            content
        )
        
        # Fix JavaScript links
        content = re.sub(
            rf'(?:window\.location|location\.href)\s*=\s*["\']{re.escape(wrong_link)}["\']',
            f'window.location.href = "{correct_link}"',
            content
        )
        
        # Fix onclick links
        content = re.sub(
            rf'onclick=["\'][^"\']*["\'"]?{re.escape(wrong_link)}["\']',
            f'onclick="window.location.href = \'{correct_link}\'"',
            content
        )
        
        # Fix template strings and function calls
        content = re.sub(
            rf'["\']{re.escape(wrong_link)}["\']',
            f'"{correct_link}"',
            content
        )
        
        if content != original:
            changes = len(re.findall(re.escape(correct_link), content)) - len(re.findall(re.escape(wrong_link), content))
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.fixes_applied.append({
                'file': filepath,
                'old': wrong_link,
                'new': correct_link,
                'changes': changes
            })
            self.files_fixed.add(filepath)
            return True
        
        return False
    
    def fix_all_wrong_language_links(self):
        """Fix all wrong language links"""
        print("\n🔧 Fixing wrong language links...\n")
        
        # Common wrong language link patterns
        wrong_links = [
            ('index.html', 'index.de.html'),
            ('gym-dashboard.html', 'gym-dashboard-de.html'),
            ('learning-hub.html', 'learning-hub-de.html'),
            ('belt-assessment-v2.html', 'belt-assessment-v2-de.html'),
            ('white-belt.html', 'white-belt-de.html'),
            ('blue-belt.html', 'blue-belt-de.html'),
            ('purple-belt.html', 'purple-belt-de.html'),
            ('brown-belt.html', 'brown-belt-de.html'),
            ('black-belt.html', 'black-belt-de.html'),
        ]
        
        # Find all German files
        german_files = [f for f in os.listdir('.') if f.endswith('-de.html') or f.endswith('.de.html') or f == 'index.de.html']
        
        total_fixes = 0
        
        for german_file in german_files:
            if not os.path.isfile(german_file):
                continue
            
            try:
                with open(german_file, 'r', encoding='utf-8') as f:
                    content = f.read()
            except:
                continue
            
            for wrong_link, correct_link in wrong_links:
                if wrong_link in content:
                    if self.fix_wrong_language_links(german_file, wrong_link, correct_link):
                        total_fixes += 1
                        print(f"  ✅ Fixed {german_file}: {wrong_link} → {correct_link}")
        
        # Fix stripe completion links
        stripe_files = [f for f in os.listdir('.') if '-stripe' in f and f.endswith('-de.html')]
        for stripe_file in stripe_files:
            if not os.path.isfile(stripe_file):
                continue
            
            try:
                with open(stripe_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Fix gym-dashboard links
                if 'gym-dashboard.html' in content and 'gym-dashboard-de.html' not in content:
                    if self.fix_wrong_language_links(stripe_file, 'gym-dashboard.html', 'gym-dashboard-de.html'):
                        total_fixes += 1
                        print(f"  ✅ Fixed {stripe_file}: gym-dashboard link")
            except:
                pass
        
        print(f"\n✅ Fixed {total_fixes} wrong language links")
        return total_fixes
    
    def fix_all_assessment_links(self):
        """Fix links in German assessment files"""
        print("\n🔧 Fixing assessment file links...\n")
        
        assessment_files = [f for f in os.listdir('.') if 'assessment' in f.lower() and f.endswith('-de.html')]
        
        fixes = 0
        
        for assess_file in assessment_files:
            if not os.path.isfile(assess_file):
                continue
            
            try:
                with open(assess_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original = content
                
                # Fix common belt links
                belt_fixes = [
                    ('white-belt.html', 'white-belt-de.html'),
                    ('blue-belt.html', 'blue-belt-de.html'),
                    ('purple-belt.html', 'purple-belt-de.html'),
                    ('brown-belt.html', 'brown-belt-de.html'),
                    ('black-belt.html', 'black-belt-de.html'),
                ]
                
                for wrong, correct in belt_fixes:
                    if wrong in content:
                        content = re.sub(
                            rf'\b{re.escape(wrong)}\b',
                            correct,
                            content
                        )
                
                if content != original:
                    with open(assess_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixes += 1
                    print(f"  ✅ Fixed links in {assess_file}")
            except:
                pass
        
        print(f"\n✅ Fixed {fixes} assessment files")
        return fixes
    
    def fix_all_belt_hub_links(self):
        """Fix links in German belt hub files"""
        print("\n🔧 Fixing belt hub file links...\n")
        
        belt_hubs = [f for f in os.listdir('.') if f.endswith('-belt-de.html') and 'stripe' not in f]
        
        fixes = 0
        
        for hub_file in belt_hubs:
            if not os.path.isfile(hub_file):
                continue
            
            try:
                with open(hub_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original = content
                
                # Fix stripe links to German versions
                # Pattern: white-belt-stripe1.html -> white-belt-stripe1-gamified-de.html
                belt = hub_file.replace('-belt-de.html', '').replace('-belt.de.html', '')
                
                for stripe_num in [1, 2, 3, 4]:
                    patterns = [
                        (f'{belt}-belt-stripe{stripe_num}.html', f'{belt}-belt-stripe{stripe_num}-gamified-de.html'),
                        (f'{belt}-belt-stripe{stripe_num}-carousel.html', f'{belt}-belt-stripe{stripe_num}-gamified-de.html'),
                        (f'{belt}-belt-stripe{stripe_num}-carousel-NEW.html', f'{belt}-belt-stripe{stripe_num}-gamified-de.html'),
                    ]
                    
                    for wrong, correct in patterns:
                        if wrong in content and os.path.exists(correct):
                            content = re.sub(
                                rf'\b{re.escape(wrong)}\b',
                                correct,
                                content
                            )
                
                # Fix gym-dashboard links
                if 'gym-dashboard.html' in content:
                    content = content.replace('gym-dashboard.html', 'gym-dashboard-de.html')
                
                if content != original:
                    with open(hub_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixes += 1
                    print(f"  ✅ Fixed links in {hub_file}")
            except Exception as e:
                print(f"  ⚠️  Error fixing {hub_file}: {e}")
        
        print(f"\n✅ Fixed {fixes} belt hub files")
        return fixes

def main():
    print("="*80)
    print("🔧 FIX ALL GERMAN LINK ISSUES")
    print("="*80)
    
    fixer = GermanLinkFixer()
    
    # Step 1: Fix wrong language links
    total_fixes = 0
    total_fixes += fixer.fix_all_wrong_language_links()
    
    # Step 2: Fix assessment links
    total_fixes += fixer.fix_all_assessment_links()
    
    # Step 3: Fix belt hub links
    total_fixes += fixer.fix_all_belt_hub_links()
    
    print("\n" + "="*80)
    print(f"✅ TOTAL FIXES APPLIED: {total_fixes}")
    print(f"✅ FILES MODIFIED: {len(fixer.files_fixed)}")
    print("="*80)
    
    # Save fix log
    if fixer.fixes_applied:
        with open('GERMAN-LINK-FIXES-LOG.json', 'w', encoding='utf-8') as f:
            json.dump(fixer.fixes_applied, f, indent=2, ensure_ascii=False)
        print(f"\n📄 Fix log saved to: GERMAN-LINK-FIXES-LOG.json")

if __name__ == '__main__':
    main()

