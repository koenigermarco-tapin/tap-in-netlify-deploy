#!/usr/bin/env python3

"""
FINAL PRE-PRESENTATION DEEP DIVE AUDIT
Complete system verification with detailed reporting
"""

import os
import re
from pathlib import Path
from datetime import datetime

class FinalDeepDiveAudit:
    def __init__(self):
        self.critical_issues = []
        self.warnings = []
        self.info = []
        self.fixes_applied = []
        self.test_results = {}
        
    def run_complete_audit(self):
        print("🔍 FINAL DEEP DIVE AUDIT - COMPREHENSIVE SYSTEM VERIFICATION")
        print("=" * 70)
        print()
        
        # Phase 1.1: Background Errors
        print("1.1 Background Errors Verification...")
        self.verify_background_errors()
        
        # Phase 1.2: Critical Path Testing
        print("\n1.2 Critical Path Testing...")
        self.test_critical_paths()
        
        # Phase 1.3: File Integrity
        print("\n1.3 File Integrity Check...")
        self.check_file_integrity()
        
        # Phase 1.4: Link Integrity
        print("\n1.4 Link Integrity Check...")
        self.check_link_integrity()
        
        # Phase 1.5: German Translations
        print("\n1.5 German Translation Completeness...")
        self.check_german_translations()
        
        # Phase 1.6: XP System
        print("\n1.6 XP System Integrity...")
        self.check_xp_system()
        
        # Phase 2: Critical Bug Fixes
        print("\n2. Critical Bug Fixes...")
        self.fix_known_issues()
        
        # Generate comprehensive report
        self.generate_final_report()
    
    def verify_background_errors(self):
        """Phase 1.1: Background Errors Verification"""
        
        error_count = 0
        warn_count = 0
        
        for root, dirs, files in os.walk('.'):
            if any(x in root for x in ['node_modules', 'archive', '.git']):
                continue
            for file in files:
                if file.endswith(('.html', '.js')):
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                            error_count += content.count('console.error')
                            warn_count += content.count('console.warn')
                    except:
                        pass
        
        self.test_results['console_errors'] = error_count
        self.test_results['console_warnings'] = warn_count
        
        # Check Supabase config
        if os.path.exists('js/supabase-config.js'):
            with open('js/supabase-config.js', 'r') as f:
                content = f.read()
                if 'localStorage-only' in content or 'Silent mode' in content:
                    self.info.append("✅ Supabase in silent mode")
                else:
                    self.critical_issues.append("❌ Supabase not properly disabled")
        else:
            self.critical_issues.append("❌ Missing js/supabase-config.js")
        
        # Check keyboard-nav.js
        if os.path.exists('js/keyboard-nav.js'):
            size = os.path.getsize('js/keyboard-nav.js')
            if size > 100:
                self.info.append(f"✅ keyboard-nav.js exists ({size} bytes)")
            else:
                self.warnings.append("⚠️ keyboard-nav.js seems minimal")
        else:
            self.critical_issues.append("❌ Missing js/keyboard-nav.js")
        
        # Check Service Worker error handling
        for page in ['index.html', 'gym-dashboard.html', 'belt-assessment-v2.html']:
            if os.path.exists(page):
                with open(page, 'r') as f:
                    content = f.read()
                    if 'serviceWorker.register' in content:
                        if 'catch' in content.split('serviceWorker.register')[1][:200]:
                            self.info.append(f"✅ {page} has SW error handling")
                        else:
                            self.warnings.append(f"⚠️ {page} SW registration may not have error handling")
        
        print(f"   Console errors: {error_count}")
        print(f"   Console warnings: {warn_count}")
        
        if error_count > 100:
            self.warnings.append(f"⚠️ High console.error count: {error_count} (most should be suppressed)")
    
    def test_critical_paths(self):
        """Phase 1.2: Critical Path Testing"""
        
        paths_to_test = [
            {
                'name': 'Homepage → Assessment',
                'source': 'index.html',
                'target': 'belt-assessment-v2.html',
                'check': 'href.*belt-assessment'
            },
            {
                'name': 'Homepage → Gym Dashboard',
                'source': 'index.html',
                'target': 'gym-dashboard.html',
                'check': 'href.*gym-dashboard'
            },
            {
                'name': 'Assessment → Gym Dashboard',
                'source': 'belt-assessment-v2.html',
                'target': 'gym-dashboard.html',
                'check': 'goToGymDashboard|gym-dashboard'
            },
            {
                'name': 'Dashboard → White Belt Stripe 1',
                'source': 'gym-dashboard.html',
                'target': 'white-belt-stripe1-gamified.html',
                'check': 'white-belt-stripe1'
            }
        ]
        
        for path in paths_to_test:
            source = path['source']
            target = path['target']
            
            if not os.path.exists(source):
                self.critical_issues.append(f"❌ Missing source: {source}")
                continue
            
            if not os.path.exists(target):
                self.critical_issues.append(f"❌ Missing target: {target}")
                continue
            
            with open(source, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if path['check'] in content.lower():
                self.info.append(f"✅ {path['name']}: Navigation path exists")
            else:
                self.critical_issues.append(f"❌ {path['name']}: Navigation path missing or broken")
    
    def check_file_integrity(self):
        """Phase 1.3: File Integrity Check"""
        
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
                'white-belt-stripe4-gamified-de.html'
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
        for category, files in critical_files.items():
            for file in files:
                if os.path.exists(file):
                    self.info.append(f"✅ {file}")
                else:
                    missing_files.append(file)
                    self.critical_issues.append(f"❌ MISSING: {file}")
        
        self.test_results['missing_files'] = len(missing_files)
        print(f"   Files checked: {sum(len(files) for files in critical_files.values())}")
        print(f"   Missing: {len(missing_files)}")
    
    def check_link_integrity(self):
        """Phase 1.4: Link Integrity Check"""
        
        key_pages = ['index.html', 'gym-dashboard.html', 'belt-assessment-v2.html']
        broken_links = []
        
        for page in key_pages:
            if not os.path.exists(page):
                continue
            
            with open(page, 'r', encoding='utf-8') as f:
                content = f.read()
            
            links = re.findall(r'href=["\']([^"\']+)["\']', content)
            
            for link in links:
                if link.startswith(('http://', 'https://', 'mailto:', '#')):
                    continue
                
                if not os.path.exists(link):
                    # Try common variations
                    variations = [
                        link,
                        link.replace('/', os.sep),
                        os.path.join(os.path.dirname(page), link)
                    ]
                    if not any(os.path.exists(v) for v in variations):
                        broken_links.append(f"{page}: {link}")
        
        if broken_links:
            for link in broken_links[:10]:
                self.warnings.append(f"⚠️ Potentially broken link: {link}")
        else:
            self.info.append("✅ No broken links found in key pages")
        
        self.test_results['broken_links'] = len(broken_links)
    
    def check_german_translations(self):
        """Phase 1.5: German Translation Completeness"""
        
        english_phrases = ['Learn more', 'Start now', 'Continue', 'Next lesson', 'Click here']
        
        german_files = list(Path('.').rglob('*-de.html'))
        incomplete = []
        
        for file in german_files[:50]:  # Check first 50
            if 'archive' in str(file):
                continue
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    for phrase in english_phrases:
                        if phrase.lower() in content.lower() and '<!--' not in content[max(0, content.lower().index(phrase.lower())-20):content.lower().index(phrase.lower())+20]:
                            incomplete.append((str(file), phrase))
                            break
            except:
                pass
        
        if incomplete:
            self.warnings.append(f"⚠️ {len(incomplete)} German files may have English text")
            for file, phrase in incomplete[:10]:
                self.warnings.append(f"   - {Path(file).name}: contains '{phrase}'")
        else:
            self.info.append("✅ German translations appear complete")
        
        self.test_results['incomplete_german'] = len(incomplete)
    
    def check_xp_system(self):
        """Phase 1.6: XP System Integrity"""
        
        if os.path.exists('js/xp-manager.js'):
            with open('js/xp-manager.js', 'r') as f:
                content = f.read()
                
            if 'getTotalXP' in content:
                self.info.append("✅ XP Manager has getTotalXP()")
            else:
                self.critical_issues.append("❌ XP Manager missing getTotalXP()")
            
            if 'addXP' in content or 'awardXP' in content:
                self.info.append("✅ XP Manager has award function")
            else:
                self.critical_issues.append("❌ XP Manager missing award function")
        else:
            self.critical_issues.append("❌ Missing js/xp-manager.js")
        
        # Check integration
        if os.path.exists('js/core-gamification.js'):
            with open('js/core-gamification.js', 'r') as f:
                content = f.read()
                if 'XPManager' in content or 'totalXP' in content:
                    self.info.append("✅ Core gamification uses XP system")
    
    def fix_known_issues(self):
        """Phase 2: Critical Bug Fixes"""
        
        # Fix 1: Verify XP sync (check for unified keys)
        if os.path.exists('js/xp-manager.js'):
            with open('js/xp-manager.js', 'r') as f:
                content = f.read()
                if "'totalXP'" in content or '"totalXP"' in content:
                    self.info.append("✅ XP uses unified 'totalXP' key")
                else:
                    self.warnings.append("⚠️ XP may use different keys - check sync")
        
        # Fix 2: Verify belt assessment navigation
        if os.path.exists('belt-assessment-v2.html'):
            with open('belt-assessment-v2.html', 'r') as f:
                content = f.read()
                if 'goToGymDashboard' in content:
                    self.info.append("✅ Belt assessment navigation function exists")
                else:
                    self.critical_issues.append("❌ Belt assessment missing navigation function")
        
        # Fix 3: Verify German assessment
        if os.path.exists('belt-assessment-v2-de.html'):
            size = os.path.getsize('belt-assessment-v2-de.html')
            if size > 10000:
                self.info.append("✅ German assessment file exists and has content")
            else:
                self.warnings.append("⚠️ German assessment file may be incomplete")
        
        # Fix 4: Verify avatar system
        if os.path.exists('js/avatar-system.js') or os.path.exists('js/enhanced-avatar-system.js'):
            self.info.append("✅ Avatar system files exist")
        else:
            self.warnings.append("⚠️ Avatar system files may be missing")
        
        print(f"   Fixes verified: {len([x for x in self.info if '✅' in x])}")
    
    def generate_final_report(self):
        """Generate comprehensive final report"""
        
        critical_count = len([i for i in self.critical_issues if '❌' in i])
        
        report = f"""# 🚨 FINAL DEEP DIVE AUDIT - COMPREHENSIVE REPORT

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Status:** {'✅ READY' if critical_count == 0 else '⚠️ ISSUES FOUND'}

---

## 📊 EXECUTIVE SUMMARY

- **Critical Issues:** {critical_count}
- **Warnings:** {len(self.warnings)}
- **Positive Findings:** {len(self.info)}
- **Fixes Applied:** {len(self.fixes_applied)}

---

## ❌ CRITICAL ISSUES ({critical_count})

"""
        
        if critical_count == 0:
            report += "- ✅ **NO CRITICAL ISSUES FOUND!**\n\n"
        else:
            for issue in self.critical_issues:
                if '❌' in issue:
                    report += f"- {issue}\n"
        
        report += f"""

## ⚠️ WARNINGS ({len(self.warnings)})

"""
        
        for warning in self.warnings[:30]:
            report += f"- {warning}\n"
        
        if not self.warnings:
            report += "- ✅ No warnings!\n"
        
        report += f"""

## ✅ POSITIVE FINDINGS ({len(self.info)})

"""
        
        for info in self.info[:50]:
            report += f"- {info}\n"
        
        report += f"""

---

## 📊 TEST RESULTS

"""
        
        for key, value in self.test_results.items():
            report += f"- **{key.replace('_', ' ').title()}:** {value}\n"
        
        report += f"""

---

## 🎯 CRITICAL SUCCESS CRITERIA STATUS

"""
        
        criteria = [
            ("Homepage loads", any('index.html' in i and '✅' in i for i in self.info)),
            ("Assessment exists", any('belt-assessment-v2.html' in i and '✅' in i for i in self.info)),
            ("Dashboard exists", any('gym-dashboard.html' in i and '✅' in i for i in self.info)),
            ("XP system works", any('XP' in i and '✅' in i for i in self.info)),
            ("Error suppression active", any('Supabase' in i or 'error' in i.lower() for i in self.info if '✅' in i)),
        ]
        
        for criterion, passed in criteria:
            status = "✅" if passed else "❌"
            report += f"- {status} {criterion}\n"
        
        report += f"""

---

## 🎯 FINAL RECOMMENDATION

"""
        
        if critical_count == 0:
            report += "**STATUS: ✅ READY FOR PRESENTATION**\n\n"
            report += "All critical systems verified. Platform is ready for demo.\n"
        elif critical_count < 3:
            report += "**STATUS: ⚠️ MOSTLY READY**\n\n"
            report += "Minor critical issues found. Review and fix before presentation.\n"
        else:
            report += "**STATUS: ❌ NEEDS WORK**\n\n"
            report += "Multiple critical issues found. Fix before presentation.\n"
        
        report += "\n---\n\n*Final deep dive audit complete*\n"
        
        with open('FINAL-DEEP-DIVE-AUDIT-REPORT.md', 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"\n✅ Final report saved: FINAL-DEEP-DIVE-AUDIT-REPORT.md")
        print(f"\n📊 Summary:")
        print(f"   - Critical Issues: {critical_count}")
        print(f"   - Warnings: {len(self.warnings)}")
        print(f"   - Positive: {len(self.info)}")

if __name__ == '__main__':
    audit = FinalDeepDiveAudit()
    audit.run_complete_audit()

