#!/usr/bin/env python3
"""
Comprehensive TAP-IN Fixer
Fixes language switcher, broken links, and navigation issues
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple

class TapInFixer:
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir)
        self.fixes_applied = []
        self.errors_found = []
        self.files_modified = set()
        
    def log_fix(self, file: str, issue: str, fix: str):
        """Log a fix that was applied"""
        self.fixes_applied.append({
            "file": file,
            "issue": issue,
            "fix": fix
        })
        self.files_modified.add(file)
        print(f"✅ FIXED: {file} - {issue}")
        
    def log_error(self, file: str, error: str):
        """Log an error found"""
        self.errors_found.append({
            "file": file,
            "error": error
        })
        print(f"⚠️  ERROR: {file} - {error}")
        
    def fix_language_switcher(self, file_path: Path) -> bool:
        """Fix language switcher initialization issues"""
        try:
            content = file_path.read_text(encoding='utf-8')
            original = content
            
            # Fix 1: Ensure elements are selected after DOM ready
            if 'const toggle = document.getElementById' in content and 'initLanguageSwitcher' in content:
                # Check if elements are selected before DOM ready
                if 'const toggle = document.getElementById(\'langToggle\')' in content:
                    # Move element selection inside initLanguageSwitcher
                    pattern = r'const (toggle|dropdown|currentFlag|currentLang) = document\.getElementById\([\'"](\w+)[\'"]\);'
                    matches = list(re.finditer(pattern, content))
                    
                    if matches and 'function initLanguageSwitcher()' in content:
                        # Replace const with let declarations at top
                        content = re.sub(
                            r'const (toggle|dropdown|currentFlag|currentLang) = document\.getElementById',
                            r'let \1 = document.getElementById',
                            content
                        )
                        
                        # Ensure elements are selected inside initLanguageSwitcher
                        if 'function initLanguageSwitcher()' in content:
                            init_pattern = r'(function initLanguageSwitcher\(\) \{)\s*// Check if elements exist'
                            replacement = r'\1\n        // Get elements after DOM is ready\n        toggle = document.getElementById(\'langToggle\');\n        dropdown = document.getElementById(\'langDropdown\');\n        currentFlag = document.getElementById(\'currentFlag\');\n        currentLang = document.getElementById(\'currentLang\');\n        \n        // Check if elements exist'
                            
                            if re.search(init_pattern, content):
                                content = re.sub(init_pattern, replacement, content)
                                self.log_fix(str(file_path), "Language switcher DOM selection", "Moved element selection inside initLanguageSwitcher")
            
            # Fix 2: Ensure event listeners are properly attached
            if 'toggle.addEventListener' in content and 'initLanguageSwitcher' in content:
                # Check if toggle is null/undefined check exists
                if 'if (!toggle || !dropdown' not in content:
                    # Add null check
                    pattern = r'(function initLanguageSwitcher\(\) \{)\s*(toggle\.addEventListener)'
                    replacement = r'\1\n        // Get elements after DOM is ready\n        toggle = document.getElementById(\'langToggle\');\n        dropdown = document.getElementById(\'langDropdown\');\n        currentFlag = document.getElementById(\'currentFlag\');\n        currentLang = document.getElementById(\'currentLang\');\n        \n        // Check if elements exist\n        if (!toggle || !dropdown || !currentFlag || !currentLang) {\n            console.error(\'Language switcher elements not found\');\n            return;\n        }\n        \n        \2'
                    content = re.sub(pattern, replacement, content)
                    self.log_fix(str(file_path), "Language switcher null check", "Added element existence check")
            
            if content != original:
                file_path.write_text(content, encoding='utf-8')
                return True
            return False
            
        except Exception as e:
            self.log_error(str(file_path), f"Error fixing language switcher: {str(e)}")
            return False
    
    def fix_broken_links(self, file_path: Path) -> bool:
        """Fix broken links, especially .de-de.html issues"""
        try:
            content = file_path.read_text(encoding='utf-8')
            original = content
            fixes = 0
            
            # Fix 1: Remove .de-de.html (double German extension)
            if '.de-de.html' in content:
                content = content.replace('.de-de.html', '-de.html')
                fixes += content.count('.de-de.html')  # Count remaining
                self.log_fix(str(file_path), "Double .de extension", "Fixed .de-de.html to -de.html")
            
            # Fix 2: Fix incorrect German file references
            german_fixes = [
                ('learning-hub.de-de.html', 'learning-hub-de.html'),
                ('gym-dashboard.de-de.html', 'gym-dashboard-de.html'),
                ('index-DUAL-ENTRY.de-de.html', 'index-DUAL-ENTRY-de.html'),
                ('combined-complete-profile.de-de.html', 'combined-complete-profile.de.html'),
            ]
            
            for old, new in german_fixes:
                if old in content:
                    content = content.replace(old, new)
                    self.log_fix(str(file_path), f"Broken link: {old}", f"Fixed to {new}")
                    fixes += 1
            
            # Fix 3: Ensure language switcher navigates correctly
            if 'index-DUAL-ENTRY' in str(file_path):
                # Ensure German page links to correct files
                if '-de.html' in str(file_path):
                    # German page should link to German versions
                    patterns = [
                        (r'href=["\']gym-dashboard\.html["\']', 'href="gym-dashboard-de.html"'),
                        (r'href=["\']learning-hub\.html["\']', 'href="learning-hub-de.html"'),
                        (r'href=["\']combined-complete-profile\.html["\']', 'href="combined-complete-profile.de.html"'),
                    ]
                    for pattern, replacement in patterns:
                        if re.search(pattern, content):
                            content = re.sub(pattern, replacement, content)
                            self.log_fix(str(file_path), "Incorrect German link", f"Fixed {pattern} to {replacement}")
                            fixes += 1
                else:
                    # English page should link to English versions
                    patterns = [
                        (r'href=["\']gym-dashboard-de\.html["\']', 'href="gym-dashboard.html"'),
                        (r'href=["\']learning-hub-de\.html["\']', 'href="learning-hub.html"'),
                        (r'href=["\']combined-complete-profile\.de\.html["\']', 'href="combined-complete-profile.html"'),
                    ]
                    for pattern, replacement in patterns:
                        if re.search(pattern, content):
                            content = re.sub(pattern, replacement, content)
                            self.log_fix(str(file_path), "Incorrect English link", f"Fixed {pattern} to {replacement}")
                            fixes += 1
            
            if content != original:
                file_path.write_text(content, encoding='utf-8')
                return True
            return False
            
        except Exception as e:
            self.log_error(str(file_path), f"Error fixing links: {str(e)}")
            return False
    
    def fix_navigation_handlers(self, file_path: Path) -> bool:
        """Fix navigation event handlers"""
        try:
            content = file_path.read_text(encoding='utf-8')
            original = content
            
            # Fix: Ensure event.stopPropagation() is used in button handlers
            if 'entry-button' in content and 'onclick' in content:
                # Add stopPropagation to buttons inside clickable cards
                pattern = r'(<button[^>]*class=["\'][^"\']*entry-button[^"\']*["\'][^>]*onclick=["\'])([^"\']+)(["\'])'
                def add_stop_prop(match):
                    onclick = match.group(2)
                    if 'event.stopPropagation' not in onclick:
                        return f'{match.group(1)}event.stopPropagation(); {onclick}{match.group(3)}'
                    return match.group(0)
                
                new_content = re.sub(pattern, add_stop_prop, content)
                if new_content != content:
                    content = new_content
                    self.log_fix(str(file_path), "Navigation event handlers", "Added stopPropagation to prevent conflicts")
            
            if content != original:
                file_path.write_text(content, encoding='utf-8')
                return True
            return False
            
        except Exception as e:
            self.log_error(str(file_path), f"Error fixing navigation: {str(e)}")
            return False
    
    def scan_and_fix(self):
        """Scan all HTML files and apply fixes"""
        print("🔍 Scanning for issues...\n")
        
        html_files = list(self.root_dir.rglob("*.html"))
        print(f"Found {len(html_files)} HTML files\n")
        
        for html_file in html_files:
            # Skip node_modules, archive, etc.
            if any(skip in str(html_file) for skip in ['node_modules', 'archive', 'react-app/dist', '.git']):
                continue
            
            # Fix language switcher issues
            self.fix_language_switcher(html_file)
            
            # Fix broken links
            self.fix_broken_links(html_file)
            
            # Fix navigation handlers
            self.fix_navigation_handlers(html_file)
        
        print(f"\n✅ Scan complete!")
        print(f"📝 Files modified: {len(self.files_modified)}")
        print(f"🔧 Fixes applied: {len(self.fixes_applied)}")
        print(f"⚠️  Errors found: {len(self.errors_found)}")
    
    def generate_report(self):
        """Generate fix report JSON"""
        report = {
            "summary": {
                "files_modified": len(self.files_modified),
                "fixes_applied": len(self.fixes_applied),
                "errors_found": len(self.errors_found)
            },
            "fixes": self.fixes_applied,
            "errors": self.errors_found,
            "files_modified": sorted(list(self.files_modified))
        }
        
        report_path = self.root_dir / "FIX-REPORT.json"
        report_path.write_text(json.dumps(report, indent=2), encoding='utf-8')
        print(f"\n📊 Report saved to: {report_path}")
        
        return report

def main():
    print("=" * 60)
    print("🔧 COMPREHENSIVE TAP-IN FIXER")
    print("=" * 60)
    print()
    
    fixer = TapInFixer()
    fixer.scan_and_fix()
    report = fixer.generate_report()
    
    print("\n" + "=" * 60)
    print("✅ FIX COMPLETE!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Review FIX-REPORT.json")
    print("2. Test the fixes")
    print("3. git add -A")
    print("4. git commit -m 'fix: auto-fixed language switcher and navigation'")
    print("5. git push")
    print()

if __name__ == "__main__":
    main()

