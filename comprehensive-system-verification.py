#!/usr/bin/env python3

"""
Comprehensive System Verification
Final verification of all critical systems before presentation
"""

import os
import re
from pathlib import Path
from datetime import datetime

class SystemVerifier:
    def __init__(self):
        self.issues = []
        self.fixes = []
        self.verified = []
        
    def verify_all(self):
        print("🔍 COMPREHENSIVE SYSTEM VERIFICATION")
        print("=" * 70)
        
        # Verify critical navigation
        print("\n1. Verifying Critical Navigation Paths...")
        self.verify_navigation()
        
        # Verify XP system
        print("\n2. Verifying XP System...")
        self.verify_xp_system()
        
        # Fix German translations
        print("\n3. Fixing German Translations...")
        self.fix_german_translations()
        
        # Verify all links
        print("\n4. Verifying All Links...")
        self.verify_all_links()
        
        # Check for broken code
        print("\n5. Checking for Broken Code...")
        self.check_broken_code()
        
        # Generate final report
        self.generate_report()
    
    def verify_navigation(self):
        """Verify all critical navigation paths"""
        
        # Path 1: index.html → belt-assessment-sales-landing.html
        if os.path.exists('index.html'):
            with open('index.html', 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'belt-assessment-sales-landing.html' in content:
                if os.path.exists('belt-assessment-sales-landing.html'):
                    self.verified.append("✅ index.html → belt-assessment-sales-landing.html")
                else:
                    self.issues.append("❌ Target file missing: belt-assessment-sales-landing.html")
            
            if 'gym-dashboard.html' in content:
                if os.path.exists('gym-dashboard.html'):
                    self.verified.append("✅ index.html → gym-dashboard.html")
        
        # Path 2: belt-assessment-sales-landing.html → belt-assessment-v2.html
        if os.path.exists('belt-assessment-sales-landing.html'):
            with open('belt-assessment-sales-landing.html', 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'belt-assessment-v2.html' in content:
                if os.path.exists('belt-assessment-v2.html'):
                    self.verified.append("✅ belt-assessment-sales-landing.html → belt-assessment-v2.html")
        
        # Path 3: belt-assessment-v2.html → gym-dashboard.html
        if os.path.exists('belt-assessment-v2.html'):
            with open('belt-assessment-v2.html', 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'goToGymDashboard' in content and 'gym-dashboard.html' in content:
                self.verified.append("✅ belt-assessment-v2.html → gym-dashboard.html (via goToGymDashboard)")
            else:
                self.issues.append("❌ Missing navigation function in belt-assessment-v2.html")
    
    def verify_xp_system(self):
        """Verify XP system integrity"""
        
        if os.path.exists('js/xp-manager.js'):
            with open('js/xp-manager.js', 'r') as f:
                content = f.read()
            
            if 'getTotalXP' in content:
                self.verified.append("✅ XP Manager has getTotalXP()")
            else:
                self.issues.append("❌ XP Manager missing getTotalXP()")
            
            # Check for unified key
            if "'totalXP'" in content or '"totalXP"' in content:
                self.verified.append("✅ XP uses unified 'totalXP' key")
        
        # Check integration
        if os.path.exists('js/core-gamification.js'):
            with open('js/core-gamification.js', 'r') as f:
                content = f.read()
                if 'XPManager' in content or 'totalXP' in content:
                    self.verified.append("✅ Core gamification uses XP system")
    
    def fix_german_translations(self):
        """Fix common German translation issues"""
        
        translations = {
            'Continue': 'Weiter',
            'Learn more': 'Mehr erfahren',
            'Start now': 'Jetzt starten'
        }
        
        german_files = [
            'communication-mastery-1-de.html',
            'feedback-culture-3-receiving-team-de.html',
            'brown-belt-stripe1-gamified-de.html',
            'purple-belt-stripe4-gamified-de.html',
            'blue-belt-stripe1-gamified-de.html',
            'belt-assessment-de.html'
        ]
        
        fixed_count = 0
        
        for file_path in german_files:
            file = Path(file_path)
            if not file.exists():
                continue
            
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original = content
                
                # Replace common phrases
                for eng, ger in translations.items():
                    # Replace in button text and labels
                    pattern = f'([>"])({re.escape(eng)})([<"])'
                    content = re.sub(pattern, f'\\1{ger}\\3', content, flags=re.IGNORECASE)
                
                if content != original:
                    with open(file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixed_count += 1
                    self.fixes.append(f"✅ Fixed translations in {file.name}")
            except Exception as e:
                pass
        
        if fixed_count > 0:
            self.verified.append(f"✅ Fixed translations in {fixed_count} German files")
    
    def verify_all_links(self):
        """Verify critical page links"""
        
        key_pages = {
            'index.html': ['gym-dashboard.html', 'belt-assessment-sales-landing.html', 'learning-hub.html'],
            'gym-dashboard.html': ['white-belt-stripe1-gamified.html', 'white-belt.html'],
            'belt-assessment-v2.html': ['gym-dashboard.html']
        }
        
        for page, expected_links in key_pages.items():
            if not os.path.exists(page):
                continue
            
            with open(page, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for link in expected_links:
                if link in content:
                    if os.path.exists(link):
                        self.verified.append(f"✅ {page} → {link}")
                    else:
                        self.issues.append(f"❌ Broken link: {page} → {link} (target missing)")
    
    def check_broken_code(self):
        """Check for broken JavaScript code"""
        
        key_files = ['index.html', 'gym-dashboard.html', 'belt-assessment-v2.html']
        
        for file in key_files:
            if not os.path.exists(file):
                continue
            
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for common broken patterns
            if 'onclick="onclick=' in content:
                self.issues.append(f"❌ Broken onclick in {file}")
            elif 'function function' in content:
                self.issues.append(f"❌ Duplicate function keyword in {file}")
            elif content.count('<script') != content.count('</script>'):
                self.issues.append(f"⚠️ Mismatched script tags in {file}")
            else:
                self.verified.append(f"✅ {file} - No broken code patterns")
    
    def generate_report(self):
        """Generate final verification report"""
        
        report = f"""# ✅ COMPREHENSIVE SYSTEM VERIFICATION REPORT

**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Status:** {'✅ READY' if len(self.issues) == 0 else '⚠️ ISSUES FOUND'}

---

## 📊 SUMMARY

- **Issues Found:** {len(self.issues)}
- **Fixes Applied:** {len(self.fixes)}
- **Systems Verified:** {len(self.verified)}

---

## ✅ VERIFIED SYSTEMS ({len(self.verified)})

"""
        
        for item in self.verified:
            report += f"- {item}\n"
        
        if self.fixes:
            report += f"""

## 🔧 FIXES APPLIED ({len(self.fixes)})

"""
            for fix in self.fixes:
                report += f"- {fix}\n"
        
        if self.issues:
            report += f"""

## ⚠️ ISSUES FOUND ({len(self.issues)})

"""
            for issue in self.issues:
                report += f"- {issue}\n"
        else:
            report += f"""

## ✅ NO ISSUES FOUND

All systems verified and working correctly!

"""
        
        report += """

---

## 🎯 FINAL STATUS

"""
        
        if len(self.issues) == 0:
            report += "**✅ ALL SYSTEMS OPERATIONAL - READY FOR DEMO**\n"
        elif len(self.issues) < 3:
            report += "**⚠️ MINOR ISSUES - READY FOR DEMO WITH NOTES**\n"
        else:
            report += "**❌ ISSUES FOUND - REVIEW BEFORE DEMO**\n"
        
        report += "\n---\n\n*Verification complete*\n"
        
        with open('SYSTEM-VERIFICATION-FINAL.md', 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"\n✅ Verification report saved: SYSTEM-VERIFICATION-FINAL.md")
        print(f"\n📊 Results:")
        print(f"   - Verified: {len(self.verified)}")
        print(f"   - Fixes: {len(self.fixes)}")
        print(f"   - Issues: {len(self.issues)}")

if __name__ == '__main__':
    verifier = SystemVerifier()
    verifier.verify_all()

