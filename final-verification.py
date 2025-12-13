#!/usr/bin/env python3
"""
Final Verification Script
Verifies all critical files are clean and working
"""

import re
from pathlib import Path
import json

class FinalVerification:
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir)
        self.issues = []
        self.verified = []
        
    def check_file(self, file_path: Path) -> dict:
        """Check a single file for issues"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            issues = []
            
            # Check for fancy quotes in JavaScript
            if '<script' in content:
                # Count fancy quotes in script blocks
                script_pattern = r'<script[^>]*>(.*?)</script>'
                scripts = re.findall(script_pattern, content, re.DOTALL | re.IGNORECASE)
                for script in scripts:
                    fancy_quotes = len(re.findall(r'[''""]', script))
                    if fancy_quotes > 0:
                        issues.append(f"Found {fancy_quotes} fancy quotes in JavaScript")
            
            # Check for window.window
            if 'window.window' in content:
                issues.append("Found window.window (should be window.location)")
            
            # Check for broken CSS media queries
            if '@media (max-width: 100%' in content:
                issues.append("Found broken CSS media query")
            
            # Check for console.log/error/warn (should be commented)
            console_pattern = r'^\s*console\.(log|error|warn)'
            console_lines = [i+1 for i, line in enumerate(content.split('\n')) 
                           if re.match(console_pattern, line) and not line.strip().startswith('//')]
            if console_lines:
                issues.append(f"Found uncommented console statements at lines: {console_lines[:5]}")
            
            return {
                "file": str(file_path.relative_to(self.root_dir)),
                "issues": issues,
                "status": "✅ CLEAN" if not issues else "⚠️ ISSUES"
            }
            
        except Exception as e:
            return {
                "file": str(file_path.relative_to(self.root_dir)),
                "issues": [f"Error reading file: {e}"],
                "status": "❌ ERROR"
            }
    
    def verify_critical_files(self):
        """Verify all critical files"""
        critical_files = [
            "index.html",
            "index-DUAL-ENTRY.html",
            "index-DUAL-ENTRY-de.html",
            "gym-dashboard.html",
            "gym-dashboard-de.html",
            "learning-hub.html",
            "learning-hub-de.html",
            "belt-assessment-v2.html",
            "belt-assessment-v2-de.html",
            "white-belt.html",
            "blue-belt.html",
            "purple-belt.html",
            "brown-belt.html",
            "black-belt.html"
        ]
        
        print("🔍 Verifying critical files...")
        print()
        
        results = []
        for file_name in critical_files:
            file_path = self.root_dir / file_name
            if file_path.exists():
                result = self.check_file(file_path)
                results.append(result)
                if result["issues"]:
                    self.issues.append(result)
                    print(f"⚠️  {file_name}: {len(result['issues'])} issues")
                    for issue in result["issues"][:3]:
                        print(f"   - {issue}")
                else:
                    self.verified.append(result)
                    print(f"✅ {file_name}: CLEAN")
            else:
                print(f"❌ {file_name}: FILE NOT FOUND")
                results.append({
                    "file": file_name,
                    "issues": ["File not found"],
                    "status": "❌ NOT FOUND"
                })
        
        print()
        print(f"✅ Clean files: {len(self.verified)}")
        print(f"⚠️  Files with issues: {len(self.issues)}")
        print()
        
        return results
    
    def generate_report(self, results):
        """Generate final verification report"""
        report = {
            "verification_date": "2025-12-13",
            "status": "✅ READY" if len(self.issues) == 0 else "⚠️ NEEDS ATTENTION",
            "summary": {
                "total_critical_files": len(results),
                "clean_files": len(self.verified),
                "files_with_issues": len(self.issues)
            },
            "verified_files": [r["file"] for r in self.verified],
            "files_with_issues": [r["file"] for r in self.issues],
            "detailed_results": results
        }
        
        report_path = self.root_dir / "FINAL-VERIFICATION-REPORT.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        print(f"📄 Verification report saved to: {report_path}")
        
        return report

if __name__ == "__main__":
    verifier = FinalVerification()
    results = verifier.verify_critical_files()
    report = verifier.generate_report(results)
    
    if len(verifier.issues) == 0:
        print("🎉 ALL CRITICAL FILES ARE CLEAN!")
        print("✅ Repository is ready for deployment")
    else:
        print(f"⚠️  {len(verifier.issues)} files need attention")
        print("Review the verification report for details")

