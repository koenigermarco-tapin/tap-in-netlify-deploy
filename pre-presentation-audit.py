#!/usr/bin/env python3

"""
TAP-IN Pre-Presentation Comprehensive Audit
Phase 1: Complete System Verification
"""

import os
import re
from pathlib import Path
from datetime import datetime

class PrePresentationAudit:
    def __init__(self):
        self.issues = []
        self.warnings = []
        self.info = []
        self.stats = {}
        
    def run_all_checks(self):
        print("🔍 PHASE 1: COMPREHENSIVE SYSTEM AUDIT")
        print("=" * 60)
        print()
        
        # 1.1 Background Errors Verification
        print("1.1 Background Errors Verification...")
        self.check_background_errors()
        
        # 1.2 Critical File Integrity
        print("\n1.2 Critical File Integrity Check...")
        self.check_file_integrity()
        
        # 1.3 Link Integrity
        print("\n1.3 Link Integrity Check...")
        self.check_link_integrity()
        
        # 1.4 German Translation
        print("\n1.4 German Translation Completeness...")
        self.check_german_translations()
        
        # 1.5 XP System
        print("\n1.5 XP System Integrity...")
        self.check_xp_system()
        
        # Generate report
        self.generate_audit_report()
    
    def check_background_errors(self):
        """Check for remaining console errors"""
        
        # Check console.error count
        error_count = 0
        for root, dirs, files in os.walk('.'):
            if 'node_modules' in root or 'archive' in root:
                continue
            for file in files:
                if file.endswith(('.html', '.js')):
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                            error_count += content.count('console.error')
                    except:
                        pass
        
        self.stats['console_errors'] = error_count
        
        # Check Supabase config
        if os.path.exists('js/supabase-config.js'):
            with open('js/supabase-config.js', 'r') as f:
                content = f.read()
                if 'localStorage-only' in content or 'Silent mode' in content:
                    self.info.append("✅ Supabase in silent mode")
                else:
                    self.issues.append("❌ Supabase not in silent mode")
        else:
            self.issues.append("❌ Missing js/supabase-config.js")
        
        # Check keyboard-nav.js
        if os.path.exists('js/keyboard-nav.js'):
            size = os.path.getsize('js/keyboard-nav.js')
            if size > 100:
                self.info.append(f"✅ keyboard-nav.js exists ({size} bytes)")
            else:
                self.warnings.append("⚠️ keyboard-nav.js seems empty or minimal")
        else:
            self.issues.append("❌ Missing js/keyboard-nav.js")
        
        # Check Service Worker error handling
        html_files = ['index.html', 'gym-dashboard.html', 'belt-assessment-v2.html']
        for html_file in html_files:
            if os.path.exists(html_file):
                with open(html_file, 'r') as f:
                    content = f.read()
                    if 'serviceWorker.register' in content:
                        if 'catch' in content or 'try' in content:
                            self.info.append(f"✅ {html_file} has SW error handling")
                        else:
                            self.warnings.append(f"⚠️ {html_file} SW registration not wrapped")
        
        print(f"   Console errors found: {error_count}")
        if error_count < 10:
            self.info.append(f"✅ Low console.error count: {error_count}")
        elif error_count < 50:
            self.warnings.append(f"⚠️ Moderate console.error count: {error_count}")
        else:
            self.issues.append(f"❌ High console.error count: {error_count}")
    
    def check_file_integrity(self):
        """Verify all critical files exist"""
        
        critical_files = {
            'Core Pages': [
                'index.html',
                'gym-dashboard.html',
                'belt-assessment-v2.html',
                'learning-hub.html'
            ],
            'Core JavaScript': [
                'js/conversion-boosters.js',
                'js/keyboard-nav.js',
                'js/supabase-config.js',
                'js/core-gamification.js',
                'js/core-progress-tracker.js',
                'js/error-suppressor.js',
                'js/xp-manager.js'
            ],
            'Core CSS': [
                'css/conversion-boosters.css',
                'css/core-styles.css',
                'css/variables.css'
            ],
            'English Belt Stripes': [
                'white-belt-stripe1-gamified.html',
                'white-belt-stripe2-gamified.html',
                'white-belt-stripe3-gamified.html',
                'white-belt-stripe4-gamified.html',
                'blue-belt-stripe1-gamified.html',
                'blue-belt-stripe2-gamified.html',
                'blue-belt-stripe3-gamified.html',
                'blue-belt-stripe4-gamified.html'
            ],
            'German Belt Stripes': [
                'white-belt-stripe1-gamified-de.html',
                'white-belt-stripe2-gamified-de.html',
                'white-belt-stripe3-gamified-de.html',
                'white-belt-stripe4-gamified-de.html',
                'blue-belt-stripe1-gamified-de.html',
                'blue-belt-stripe2-gamified-de.html',
                'blue-belt-stripe3-gamified-de.html',
                'blue-belt-stripe4-gamified-de.html'
            ],
            'Belt Landing Pages': [
                'white-belt.html',
                'blue-belt.html',
                'purple-belt.html',
                'brown-belt.html',
                'black-belt.html'
            ]
        }
        
        missing_files = []
        existing_files = []
        
        for category, files in critical_files.items():
            for file in files:
                if os.path.exists(file):
                    existing_files.append(file)
                    self.info.append(f"✅ {file}")
                else:
                    missing_files.append(file)
                    self.issues.append(f"❌ MISSING: {file}")
        
        self.stats['existing_files'] = len(existing_files)
        self.stats['missing_files'] = len(missing_files)
        
        print(f"   Files checked: {len(existing_files) + len(missing_files)}")
        print(f"   Existing: {len(existing_files)}")
        print(f"   Missing: {len(missing_files)}")
    
    def check_link_integrity(self):
        """Check for broken internal links"""
        
        key_pages = ['index.html', 'gym-dashboard.html', 'belt-assessment-v2.html']
        broken_links = []
        
        for page in key_pages:
            if not os.path.exists(page):
                continue
            
            with open(page, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all href links
            links = re.findall(r'href=["\']([^"\']+)["\']', content)
            
            for link in links:
                # Skip external links
                if link.startswith('http://') or link.startswith('https://') or link.startswith('mailto:') or link.startswith('#'):
                    continue
                
                # Check if file exists
                if not os.path.exists(link) and not link.endswith('.html'):
                    # Try with common extensions
                    if not any(os.path.exists(f"{link}.{ext}") for ext in ['html', 'css', 'js', 'png', 'jpg', 'svg']):
                        broken_links.append(f"{page}: {link}")
        
        if broken_links:
            self.warnings.append(f"⚠️ Found {len(broken_links)} potentially broken links")
            for link in broken_links[:10]:  # Show first 10
                self.warnings.append(f"   - {link}")
        else:
            self.info.append("✅ No broken links found in key pages")
        
        self.stats['broken_links'] = len(broken_links)
    
    def check_german_translations(self):
        """Check German translation completeness"""
        
        english_phrases = [
            'Learn more',
            'Start now',
            'Continue',
            'Next lesson',
            'Click here',
            'Lorem ipsum'
        ]
        
        german_files = list(Path('.').rglob('*-de.html'))
        incomplete_files = []
        
        for file in german_files:
            if 'archive' in str(file):
                continue
            
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                for phrase in english_phrases:
                    if phrase.lower() in content.lower():
                        incomplete_files.append((str(file), phrase))
                        break
            except:
                pass
        
        if incomplete_files:
            self.warnings.append(f"⚠️ {len(incomplete_files)} German files may have English text")
            for file, phrase in incomplete_files[:5]:
                self.warnings.append(f"   - {file}: contains '{phrase}'")
        else:
            self.info.append("✅ German translations appear complete")
        
        self.stats['incomplete_german'] = len(incomplete_files)
    
    def check_xp_system(self):
        """Check XP system integrity"""
        
        # Check XP Manager exists
        if os.path.exists('js/xp-manager.js'):
            self.info.append("✅ XP Manager exists")
            
            with open('js/xp-manager.js', 'r') as f:
                content = f.read()
                
            # Check for key functions
            if 'getTotalXP' in content:
                self.info.append("✅ XP Manager has getTotalXP()")
            else:
                self.issues.append("❌ XP Manager missing getTotalXP()")
            
            if 'addXP' in content or 'awardXP' in content:
                self.info.append("✅ XP Manager has award function")
            else:
                self.issues.append("❌ XP Manager missing award function")
        else:
            self.issues.append("❌ Missing js/xp-manager.js")
        
        # Check integration in core-gamification
        if os.path.exists('js/core-gamification.js'):
            with open('js/core-gamification.js', 'r') as f:
                content = f.read()
                if 'XPManager' in content or 'totalXP' in content:
                    self.info.append("✅ Core gamification uses XP system")
                else:
                    self.warnings.append("⚠️ Core gamification may not use XP Manager")
        
        self.stats['xp_system_check'] = 'complete'
    
    def generate_audit_report(self):
        """Generate comprehensive audit report"""
        
        report = f"""# 🔍 PRE-PRESENTATION AUDIT REPORT - PHASE 1

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Phase:** Comprehensive System Audit

---

## 📊 SUMMARY

- **Critical Issues:** {len([i for i in self.issues if '❌' in i])}
- **Warnings:** {len(self.warnings)}
- **Positive Findings:** {len(self.info)}

---

## ❌ CRITICAL ISSUES ({len([i for i in self.issues if '❌' in i])})

"""
        
        for issue in self.issues:
            report += f"- {issue}\n"
        
        if not self.issues:
            report += "- ✅ No critical issues found!\n"
        
        report += f"""

## ⚠️ WARNINGS ({len(self.warnings)})

"""
        
        for warning in self.warnings[:20]:  # Limit to 20
            report += f"- {warning}\n"
        
        if not self.warnings:
            report += "- ✅ No warnings!\n"
        
        report += f"""

## ✅ POSITIVE FINDINGS ({len(self.info)})

"""
        
        for info in self.info[:30]:  # Limit to 30
            report += f"- {info}\n"
        
        report += f"""

---

## 📊 STATISTICS

"""
        
        for key, value in self.stats.items():
            report += f"- **{key.replace('_', ' ').title()}:** {value}\n"
        
        report += f"""

---

## 🎯 NEXT STEPS

"""
        
        if len([i for i in self.issues if '❌' in i]) == 0:
            report += "✅ **Phase 1 Complete** - No critical issues found. Proceed to Phase 2.\n"
        else:
            report += "⚠️ **Action Required** - Fix critical issues before proceeding to Phase 2.\n"
        
        report += "\n---\n\n*Audit completed automatically by Pre-Presentation Audit System*\n"
        
        # Save report
        report_file = 'PHASE1-AUDIT-REPORT.md'
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"\n✅ Audit report saved: {report_file}")
        print(f"\n📊 Results:")
        print(f"   - Critical Issues: {len([i for i in self.issues if '❌' in i])}")
        print(f"   - Warnings: {len(self.warnings)}")
        print(f"   - Positive: {len(self.info)}")

if __name__ == '__main__':
    audit = PrePresentationAudit()
    audit.run_all_checks()

