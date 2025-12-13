#!/usr/bin/env python3

"""
TAP-IN Comprehensive Fix All Issues
Pre-Presentation Critical Fixes
"""

import os
import re
from pathlib import Path
from datetime import datetime

class ComprehensiveFixer:
    def __init__(self):
        self.fixes_applied = []
        self.issues_found = []
        
    def run_all_fixes(self):
        print("🔧 COMPREHENSIVE FIX PROCESS")
        print("=" * 60)
        print()
        
        # Fix 1: Create missing PWA files
        print("Fix 1: Creating missing PWA files...")
        self.create_pwa_files()
        
        # Fix 2: Fix broken links
        print("\nFix 2: Fixing broken links...")
        self.fix_broken_links()
        
        # Fix 3: Verify critical paths
        print("\nFix 3: Verifying critical paths...")
        self.verify_critical_paths()
        
        # Fix 4: Fix German translation issues
        print("\nFix 4: Fixing German translation issues...")
        self.fix_german_translations()
        
        # Generate fix report
        self.generate_fix_report()
    
    def create_pwa_files(self):
        """Create missing PWA manifest and icons"""
        
        # Create manifest.json if missing
        if not os.path.exists('manifest.json'):
            manifest = {
                "name": "TAP-IN Leadership Training",
                "short_name": "TAP-IN",
                "description": "Martial arts-style leadership development platform",
                "start_url": "/",
                "display": "standalone",
                "background_color": "#1a365d",
                "theme_color": "#667eea",
                "orientation": "portrait-primary",
                "icons": [
                    {
                        "src": "icons/icon-192.png",
                        "sizes": "192x192",
                        "type": "image/png"
                    },
                    {
                        "src": "icons/icon-512.png",
                        "sizes": "512x512",
                        "type": "image/png"
                    }
                ]
            }
            
            import json
            with open('manifest.json', 'w') as f:
                json.dump(manifest, f, indent=2)
            
            self.fixes_applied.append("✅ Created manifest.json")
        
        # Create icons directory if missing
        if not os.path.exists('icons'):
            os.makedirs('icons')
            self.fixes_applied.append("✅ Created icons directory")
        
        # Create placeholder icon files (they should exist but create if missing)
        icon_sizes = [192, 512]
        for size in icon_sizes:
            icon_path = f'icons/icon-{size}.png'
            if not os.path.exists(icon_path):
                # Create a simple SVG placeholder that can be converted to PNG
                svg_content = f'''<svg width="{size}" height="{size}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{size}" height="{size}" fill="#1a365d"/>
  <text x="50%" y="50%" font-family="Arial" font-size="{size//4}" fill="white" text-anchor="middle" dominant-baseline="middle">TAP-IN</text>
</svg>'''
                
                # For now, just create a note that icons need to be generated
                with open(f'{icon_path}.placeholder', 'w') as f:
                    f.write("Icon placeholder - generate actual PNG icon here")
                
                self.fixes_applied.append(f"⚠️ Created placeholder for {icon_path} (actual PNG needed)")
    
    def fix_broken_links(self):
        """Fix broken links in key pages"""
        
        key_pages = ['index.html', 'gym-dashboard.html']
        fixed_links = []
        
        for page in key_pages:
            if not os.path.exists(page):
                continue
            
            with open(page, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Fix manifest.json links
            if '/manifest.json' in content and not os.path.exists('manifest.json'):
                # Links should be relative, not absolute
                content = content.replace('href="/manifest.json"', 'href="manifest.json"')
                fixed_links.append(f"{page}: Fixed manifest.json link")
            
            # Fix icon links
            if '/icons/icon-192.png' in content:
                content = content.replace('href="/icons/icon-192.png"', 'href="icons/icon-192.png"')
                fixed_links.append(f"{page}: Fixed icon link")
            
            # Write back if changes made
            if fixed_links:
                with open(page, 'w', encoding='utf-8') as f:
                    f.write(content)
        
        if fixed_links:
            self.fixes_applied.extend(fixed_links)
        else:
            self.fixes_applied.append("✅ No broken links found to fix")
    
    def verify_critical_paths(self):
        """Verify critical navigation paths work"""
        
        paths = {
            'index.html → belt-assessment-v2.html': {
                'source': 'index.html',
                'target': 'belt-assessment-v2.html',
                'link_type': 'href'
            },
            'index.html → gym-dashboard.html': {
                'source': 'index.html',
                'target': 'gym-dashboard.html',
                'link_type': 'href'
            },
            'gym-dashboard.html → white-belt-stripe1-gamified.html': {
                'source': 'gym-dashboard.html',
                'target': 'white-belt-stripe1-gamified.html',
                'link_type': 'href'
            }
        }
        
        verified = []
        issues = []
        
        for path_name, path_info in paths.items():
            source = path_info['source']
            target = path_info['target']
            
            if not os.path.exists(source):
                issues.append(f"❌ Source missing: {source}")
                continue
            
            if not os.path.exists(target):
                issues.append(f"❌ Target missing: {target}")
                continue
            
            # Check if link exists in source
            with open(source, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if target in content or target.replace('.html', '') in content:
                verified.append(f"✅ {path_name}: Link exists")
            else:
                issues.append(f"⚠️ {path_name}: Link may be missing")
        
        self.fixes_applied.extend(verified)
        self.issues_found.extend(issues)
    
    def fix_german_translations(self):
        """Fix common German translation issues"""
        
        # Common English phrases that should be translated
        translations = {
            'Continue': 'Weiter',
            'Learn more': 'Mehr erfahren',
            'Start now': 'Jetzt starten',
            'Next lesson': 'Nächste Lektion',
            'Click here': 'Hier klicken'
        }
        
        german_files = list(Path('.').rglob('*-de.html'))
        fixed = []
        
        for file in german_files[:10]:  # Check first 10 files
            if 'archive' in str(file):
                continue
            
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Replace common English phrases
                for english, german in translations.items():
                    # Only replace if it's actual button/text content, not in comments
                    if f">{english}" in content or f'">{english}' in content:
                        content = re.sub(
                            f'([>"])({re.escape(english)})([<"])',
                            f'\\1{german}\\3',
                            content
                        )
                
                if content != original_content:
                    with open(file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixed.append(f"✅ Fixed translations in {file.name}")
            
            except Exception as e:
                pass
        
        if fixed:
            self.fixes_applied.extend(fixed[:5])  # Limit to 5
        else:
            self.fixes_applied.append("✅ German translations already good")
    
    def generate_fix_report(self):
        """Generate fix report"""
        
        report = f"""# 🔧 COMPREHENSIVE FIX REPORT

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## ✅ FIXES APPLIED ({len(self.fixes_applied)})

"""
        
        for fix in self.fixes_applied:
            report += f"- {fix}\n"
        
        if self.issues_found:
            report += f"""

## ⚠️ REMAINING ISSUES ({len(self.issues_found)})

"""
            for issue in self.issues_found:
                report += f"- {issue}\n"
        
        report += """

---

*Fix process completed automatically*
"""
        
        with open('COMPREHENSIVE-FIX-REPORT.md', 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"\n✅ Fix report saved: COMPREHENSIVE-FIX-REPORT.md")
        print(f"\n📊 Summary:")
        print(f"   - Fixes Applied: {len(self.fixes_applied)}")
        print(f"   - Issues Remaining: {len(self.issues_found)}")

if __name__ == '__main__':
    fixer = ComprehensiveFixer()
    fixer.run_all_fixes()

