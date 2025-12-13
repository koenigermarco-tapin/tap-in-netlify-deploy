#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive German Link Verification
Check all German files for broken links, missing translations, wrong language versions
"""

import os
import re
from collections import defaultdict

class GermanLinkVerifier:
    def __init__(self):
        self.broken_links = []
        self.wrong_language_links = []
        self.missing_files = []
        self.issues = []
        
    def find_german_files(self):
        """Find all German HTML files"""
        german_files = []
        for file in os.listdir('.'):
            if file.endswith('-de.html') or file.endswith('.de.html') or file == 'index.de.html':
                if os.path.isfile(file):
                    german_files.append(file)
        return sorted(german_files)
    
    def check_file_links(self, filepath):
        """Check all links in a German file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            return
        
        # Find all HTML links
        html_links = re.findall(r'href=["\']([^"\']+\.html)["\']', content)
        
        # Find JavaScript links
        js_links = re.findall(r'(?:window\.location|location\.href)\s*=\s*["\']([^"\']+\.html)["\']', content)
        
        # Find onclick links
        onclick_links = re.findall(r'onclick=["\'][^"\']*["\'"]?([^"\']+\.html)["\']', content)
        
        all_links = set(html_links + js_links + onclick_links)
        
        for link in all_links:
            # Skip external links
            if link.startswith('http://') or link.startswith('https://'):
                continue
            
            # Skip anchors
            if link.startswith('#'):
                continue
            
            # Check if it's an English link in a German file
            if not link.endswith('-de.html') and not link.endswith('.de.html') and not link == 'index.de.html':
                # Allow certain English files that don't have German versions
                allowed_english = [
                    'contact-card-blackbelt.html',
                    'qr-generator-blackbelt.html',
                    'admin-qr-generator.html',
                    'migration-wizard.html',
                    'auth-callback.html'
                ]
                
                if link not in allowed_english:
                    self.wrong_language_links.append({
                        'file': filepath,
                        'link': link,
                        'should_be': link.replace('.html', '-de.html') if not link.endswith('v2.html') else link.replace('.html', '-de.html')
                    })
            
            # Check if target file exists
            if not os.path.exists(link):
                # Check if German version exists
                de_version = link.replace('.html', '-de.html')
                if not os.path.exists(de_version):
                    self.missing_files.append({
                        'file': filepath,
                        'missing': link,
                        'suggested': de_version
                    })
    
    def verify_all_german_files(self):
        """Verify all German files"""
        print("🔍 Verifying all German files for link issues...\n")
        
        german_files = self.find_german_files()
        print(f"Found {len(german_files)} German files to verify\n")
        
        for file in german_files:
            self.check_file_links(file)
            if len(german_files) <= 50:  # Only show progress for reasonable numbers
                print(f"  ✓ Checked {file}")
        
        print(f"\n✅ Verification complete\n")
    
    def generate_report(self):
        """Generate verification report"""
        print("="*80)
        print("🔍 GERMAN LINK VERIFICATION REPORT")
        print("="*80)
        
        print(f"\n📊 Summary:")
        print(f"  - Wrong language links: {len(self.wrong_language_links)}")
        print(f"  - Missing files: {len(self.missing_files)}")
        
        if self.wrong_language_links:
            print(f"\n⚠️  WRONG LANGUAGE LINKS ({len(self.wrong_language_links)}):")
            print("   (German files linking to English versions)\n")
            
            # Group by file
            by_file = defaultdict(list)
            for issue in self.wrong_language_links[:20]:  # Show first 20
                by_file[issue['file']].append(issue)
            
            for file, issues in list(by_file.items())[:10]:
                print(f"  📄 {file}:")
                for issue in issues[:3]:
                    print(f"    - Links to: {issue['link']}")
                    print(f"      Should be: {issue['should_be']}")
        
        if self.missing_files:
            print(f"\n⚠️  MISSING FILES ({len(self.missing_files)}):")
            print("   (Links pointing to non-existent files)\n")
            
            unique_missing = set(issue['missing'] for issue in self.missing_files)
            for missing in list(unique_missing)[:10]:
                print(f"  - {missing}")
        
        if not self.wrong_language_links and not self.missing_files:
            print("\n✅ No link issues found! All German files properly linked.")
        
        return {
            'wrong_language': len(self.wrong_language_links),
            'missing_files': len(self.missing_files)
        }

def main():
    verifier = GermanLinkVerifier()
    verifier.verify_all_german_files()
    stats = verifier.generate_report()
    
    print("\n" + "="*80)
    if stats['wrong_language'] == 0 and stats['missing_files'] == 0:
        print("✅ ALL GERMAN LINKS VERIFIED")
    else:
        print(f"⚠️  FOUND {stats['wrong_language'] + stats['missing_files']} ISSUES")
    print("="*80)

if __name__ == '__main__':
    main()

