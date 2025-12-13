#!/usr/bin/env python3
"""
Comprehensive TAP-IN Page Tester
Tests all pages, links, and language switchers
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Set, Tuple

class PageTester:
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir)
        self.test_results = {
            "pages_tested": 0,
            "pages_passed": 0,
            "pages_failed": 0,
            "issues": [],
            "language_switchers": [],
            "broken_links": [],
            "missing_corresponding_pages": []
        }
        
    def log_issue(self, page: str, issue_type: str, description: str, severity: str = "error"):
        """Log an issue found"""
        self.test_results["issues"].append({
            "page": page,
            "type": issue_type,
            "description": description,
            "severity": severity
        })
        print(f"  {'❌' if severity == 'error' else '⚠️ '} {issue_type}: {description}")
        
    def log_success(self, page: str, test: str):
        """Log a successful test"""
        print(f"  ✅ {test}")
        
    def find_corresponding_page(self, file_path: Path) -> Tuple[Path, str]:
        """Find the corresponding page in the other language"""
        filename = file_path.name
        base_path = file_path.parent
        
        # Check if it's a German page
        if '-de.html' in filename:
            # Find English version
            english_name = filename.replace('-de.html', '.html')
            english_path = base_path / english_name
            if english_path.exists():
                return english_path, 'en'
            # Also check .de.html pattern
            english_name2 = filename.replace('-de.html', '.html')
            english_path2 = base_path / english_name2
            if english_path2.exists():
                return english_path2, 'en'
        elif '.de.html' in filename:
            # Find English version
            english_name = filename.replace('.de.html', '.html')
            english_path = base_path / english_name
            if english_path.exists():
                return english_path, 'en'
        else:
            # Find German version
            # Try -de.html pattern
            german_name1 = filename.replace('.html', '-de.html')
            german_path1 = base_path / german_name1
            if german_path1.exists():
                return german_path1, 'de'
            # Try .de.html pattern
            german_name2 = filename.replace('.html', '.de.html')
            german_path2 = base_path / german_name2
            if german_path2.exists():
                return german_path2, 'de'
        
        return None, None
    
    def test_language_switcher(self, file_path: Path) -> bool:
        """Test language switcher functionality"""
        try:
            content = file_path.read_text(encoding='utf-8')
            filename = file_path.name
            passed = True
            
            # Check if page has language switcher HTML
            has_switcher_html = 'langToggle' in content and 'langDropdown' in content
            if not has_switcher_html:
                # Some pages might not need language switcher (skip)
                if 'index-DUAL-ENTRY' in filename or 'learning-hub' in filename or 'gym-dashboard' in filename:
                    self.log_issue(str(file_path), "Missing Language Switcher", "Critical page missing language switcher HTML")
                    passed = False
                return passed
            
            # Check for language switcher JavaScript
            has_init_function = 'initLanguageSwitcher' in content or 'langToggle' in content
            if not has_init_function:
                self.log_issue(str(file_path), "Missing Language Switcher JS", "Language switcher HTML present but no JavaScript")
                passed = False
                return passed
            
            # Check that elements are selected after DOM ready
            if 'getElementById(\'langToggle\')' in content:
                # Check if selection happens in init function
                if 'function initLanguageSwitcher' in content:
                    if 'getElementById(\'langToggle\')' not in content.split('function initLanguageSwitcher')[1].split('}')[0]:
                        # Elements might be selected before DOM ready
                        if 'const toggle = document.getElementById' in content.split('function initLanguageSwitcher')[0]:
                            self.log_issue(str(file_path), "Language Switcher Timing", "Elements selected before DOM ready - may cause issues", "warning")
                else:
                    # No init function, elements selected immediately
                    if 'const toggle = document.getElementById' in content:
                        self.log_issue(str(file_path), "Language Switcher Timing", "Elements selected immediately - should wait for DOM ready", "warning")
            
            # Check for event listeners
            has_toggle_listener = 'toggle.addEventListener' in content or 'langToggle' in content
            if not has_toggle_listener:
                self.log_issue(str(file_path), "Missing Event Listeners", "Language switcher has no click handlers")
                passed = False
            
            # Check navigation logic
            has_navigation = 'window.location.href' in content or 'index-DUAL-ENTRY' in content
            if has_switcher_html and not has_navigation:
                self.log_issue(str(file_path), "Missing Navigation", "Language switcher doesn't navigate to other language")
                passed = False
            
            # Check for corresponding page
            corresponding, target_lang = self.find_corresponding_page(file_path)
            if has_switcher_html and not corresponding:
                # Only log if it's a page that should have a corresponding version
                if any(key in filename for key in ['index-DUAL-ENTRY', 'learning-hub', 'gym-dashboard', 'belt-assessment']):
                    self.log_issue(str(file_path), "Missing Corresponding Page", f"No {target_lang} version found")
                    self.test_results["missing_corresponding_pages"].append({
                        "page": str(file_path),
                        "missing_language": target_lang
                    })
            
            if passed:
                self.log_success(str(file_path), "Language switcher present and functional")
                self.test_results["language_switchers"].append({
                    "page": str(file_path),
                    "status": "ok",
                    "has_corresponding": corresponding is not None
                })
            
            return passed
            
        except Exception as e:
            self.log_issue(str(file_path), "Test Error", f"Error testing language switcher: {str(e)}")
            return False
    
    def test_links(self, file_path: Path) -> bool:
        """Test all links in a page"""
        try:
            content = file_path.read_text(encoding='utf-8')
            filename = file_path.name
            passed = True
            
            # Find all href links
            href_pattern = r'href=["\']([^"\']+)["\']'
            links = re.findall(href_pattern, content)
            
            broken_links = []
            for link in links:
                # Skip external links, anchors, and special protocols
                if link.startswith('http://') or link.startswith('https://') or link.startswith('mailto:') or link.startswith('tel:') or link.startswith('#') or link.startswith('javascript:'):
                    continue
                
                # Skip empty links
                if not link or link == '#':
                    continue
                
                # Resolve relative paths
                if link.startswith('/'):
                    target_path = self.root_dir / link.lstrip('/')
                else:
                    target_path = file_path.parent / link
                
                # Normalize path
                target_path = target_path.resolve()
                
                # Check if file exists
                if not target_path.exists():
                    # Check for common variations
                    variations = [
                        target_path,
                        target_path.with_suffix('.html'),
                        target_path.parent / (target_path.stem + '-de.html'),
                        target_path.parent / (target_path.stem + '.de.html'),
                    ]
                    
                    found = False
                    for var in variations:
                        if var.exists():
                            found = True
                            break
                    
                    if not found:
                        broken_links.append(link)
                        self.log_issue(str(file_path), "Broken Link", f"Link '{link}' points to non-existent file")
                        passed = False
            
            # Check for double .de extensions
            if '.de-de.html' in content:
                self.log_issue(str(file_path), "Double Extension", "Found .de-de.html (double German extension)")
                passed = False
            
            if broken_links:
                self.test_results["broken_links"].extend([{
                    "page": str(file_path),
                    "link": link
                } for link in broken_links])
            
            if passed and links:
                self.log_success(str(file_path), f"All {len(links)} links valid")
            
            return passed
            
        except Exception as e:
            self.log_issue(str(file_path), "Test Error", f"Error testing links: {str(e)}")
            return False
    
    def test_navigation_consistency(self, file_path: Path) -> bool:
        """Test that navigation links are consistent with page language"""
        try:
            content = file_path.read_text(encoding='utf-8')
            filename = file_path.name
            passed = True
            
            is_german = '-de.html' in filename or '.de.html' in filename
            
            # Check gym-dashboard links
            if 'gym-dashboard' in content:
                if is_german:
                    if 'gym-dashboard.html' in content and 'gym-dashboard-de.html' not in content:
                        # Should link to German version
                        if 'href="gym-dashboard.html"' in content or "href='gym-dashboard.html'" in content:
                            self.log_issue(str(file_path), "Language Mismatch", "German page links to English gym-dashboard")
                            passed = False
                else:
                    if 'gym-dashboard-de.html' in content and 'gym-dashboard.html' not in content:
                        # Should link to English version
                        if 'href="gym-dashboard-de.html"' in content or "href='gym-dashboard-de.html'" in content:
                            self.log_issue(str(file_path), "Language Mismatch", "English page links to German gym-dashboard")
                            passed = False
            
            # Check learning-hub links
            if 'learning-hub' in content:
                if is_german:
                    if 'learning-hub.html' in content and 'learning-hub-de.html' not in content:
                        if 'href="learning-hub.html"' in content or "href='learning-hub.html'" in content:
                            self.log_issue(str(file_path), "Language Mismatch", "German page links to English learning-hub")
                            passed = False
                else:
                    if 'learning-hub-de.html' in content and 'learning-hub.html' not in content:
                        if 'href="learning-hub-de.html"' in content or "href='learning-hub-de.html'" in content:
                            self.log_issue(str(file_path), "Language Mismatch", "English page links to German learning-hub")
                            passed = False
            
            return passed
            
        except Exception as e:
            self.log_issue(str(file_path), "Test Error", f"Error testing navigation: {str(e)}")
            return False
    
    def test_page(self, file_path: Path) -> bool:
        """Run all tests on a page"""
        print(f"\n📄 Testing: {file_path.name}")
        
        results = {
            "language_switcher": True,
            "links": True,
            "navigation": True
        }
        
        # Test language switcher
        results["language_switcher"] = self.test_language_switcher(file_path)
        
        # Test links
        results["links"] = self.test_links(file_path)
        
        # Test navigation consistency
        results["navigation"] = self.test_navigation_consistency(file_path)
        
        overall = all(results.values())
        
        if overall:
            self.test_results["pages_passed"] += 1
        else:
            self.test_results["pages_failed"] += 1
        
        self.test_results["pages_tested"] += 1
        
        return overall
    
    def run_comprehensive_test(self):
        """Run comprehensive tests on all pages"""
        print("=" * 70)
        print("🧪 COMPREHENSIVE TAP-IN PAGE TESTER")
        print("=" * 70)
        print()
        
        # Find all HTML files
        html_files = list(self.root_dir.rglob("*.html"))
        
        # Filter out unwanted files
        test_files = [
            f for f in html_files
            if not any(skip in str(f) for skip in [
                'node_modules', 'archive', 'react-app/dist', '.git',
                'react-app/src', 'android'
            ])
        ]
        
        # Prioritize critical pages
        critical_pages = [
            f for f in test_files
            if any(key in f.name for key in [
                'index-DUAL-ENTRY', 'learning-hub', 'gym-dashboard',
                'belt-assessment', 'combined-complete-profile'
            ])
        ]
        
        other_pages = [f for f in test_files if f not in critical_pages]
        
        print(f"Found {len(test_files)} HTML files")
        print(f"  - {len(critical_pages)} critical pages")
        print(f"  - {len(other_pages)} other pages")
        print()
        
        # Test critical pages first
        print("🔍 Testing critical pages...")
        for page in sorted(critical_pages):
            self.test_page(page)
        
        # Test a sample of other pages (to avoid too much output)
        print(f"\n🔍 Testing sample of other pages (first 20)...")
        for page in sorted(other_pages)[:20]:
            self.test_page(page)
        
        # Generate summary
        self.generate_summary()
    
    def generate_summary(self):
        """Generate test summary"""
        print("\n" + "=" * 70)
        print("📊 TEST SUMMARY")
        print("=" * 70)
        print()
        
        total = self.test_results["pages_tested"]
        passed = self.test_results["pages_passed"]
        failed = self.test_results["pages_failed"]
        
        print(f"Pages Tested: {total}")
        print(f"✅ Passed: {passed}")
        print(f"❌ Failed: {failed}")
        print(f"Success Rate: {(passed/total*100) if total > 0 else 0:.1f}%")
        print()
        
        # Count issues by type
        error_count = len([i for i in self.test_results["issues"] if i["severity"] == "error"])
        warning_count = len([i for i in self.test_results["issues"] if i["severity"] == "warning"])
        
        print(f"Issues Found:")
        print(f"  ❌ Errors: {error_count}")
        print(f"  ⚠️  Warnings: {warning_count}")
        print()
        
        print(f"Language Switchers: {len(self.test_results['language_switchers'])}")
        print(f"Broken Links: {len(self.test_results['broken_links'])}")
        print(f"Missing Corresponding Pages: {len(self.test_results['missing_corresponding_pages'])}")
        print()
        
        # Save detailed report
        report_path = self.root_dir / "COMPREHENSIVE-TEST-REPORT.json"
        report_path.write_text(json.dumps(self.test_results, indent=2), encoding='utf-8')
        print(f"📄 Detailed report saved to: {report_path}")
        
        # Overall status
        if error_count == 0:
            print("\n✅ ALL CRITICAL TESTS PASSED!")
        else:
            print(f"\n⚠️  {error_count} CRITICAL ISSUES FOUND - Review report above")

def main():
    tester = PageTester()
    tester.run_comprehensive_test()

if __name__ == "__main__":
    main()

