#!/usr/bin/env python3
"""
Fix Broken Links and German Translation Issues
"""

import os
import re
from pathlib import Path

class LinkAndTranslationFixer:
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir)
        self.fixes = {
            "broken_links": 0,
            "german_translations": 0,
            "files_processed": 0
        }
        
    def fix_broken_links(self, content: str, file_path: Path) -> tuple[str, int]:
        """Fix broken links"""
        fixed_count = 0
        original = content
        
        # Fix icon paths
        # icons/icon-192.png -> icon-192.png (if file exists at root)
        if 'icons/icon-192.png' in content:
            icon_path = self.root_dir / 'icon-192.png'
            if icon_path.exists():
                content = content.replace('icons/icon-192.png', 'icon-192.png')
                fixed_count += 1
        
        # Fix achievements.html -> achievement-badges.html
        if 'achievements.html' in content and (self.root_dir / 'achievement-badges.html').exists():
            content = re.sub(r'href=["\']achievements\.html["\']', 'href="achievement-badges.html"', content)
            fixed_count += 1
        
        # Fix /gym-dashboard.html -> gym-dashboard.html (remove leading slash)
        content = re.sub(r'href=["\']/gym-dashboard\.html["\']', 'href="gym-dashboard.html"', content)
        if '/gym-dashboard.html' in original and 'gym-dashboard.html' in content and original != content:
            fixed_count += 1
        
        # Fix /belt-assessment-v2.html -> belt-assessment-v2.html
        content = re.sub(r'href=["\']/belt-assessment-v2\.html["\']', 'href="belt-assessment-v2.html"', content)
        if '/belt-assessment-v2.html' in original and 'belt-assessment-v2.html' in content and original != content:
            fixed_count += 1
        
        # Fix article-*.html links - check if files exist, if not, remove or comment
        article_pattern = r'href=["\'](article-[^"\']+\.html)["\']'
        def check_article(match):
            article_file = match.group(1)
            if (self.root_dir / article_file).exists():
                return match.group(0)
            else:
                # File doesn't exist, comment out or remove
                return f'<!-- {match.group(0)} -->'
        
        matches_before = len(re.findall(article_pattern, content))
        content = re.sub(article_pattern, check_article, content)
        matches_after = len(re.findall(article_pattern, content))
        if matches_before != matches_after:
            fixed_count += matches_before - matches_after
        
        return content, fixed_count
    
    def fix_german_translations(self, content: str, file_path: Path) -> tuple[str, int]:
        """Fix English text in German files"""
        fixed_count = 0
        
        # Only process German files
        if not file_path.name.endswith('-de.html') and 'de.html' not in file_path.name:
            return content, 0
        
        original = content
        
        # Fix "Continue" -> "Weiter"
        if 'Continue' in content and '<button' in content or '<a' in content:
            # Only replace in button/link contexts
            content = re.sub(r'>\s*Continue\s*<', '>Weiter<', content, flags=re.IGNORECASE)
            content = re.sub(r'["\']Continue["\']', '"Weiter"', content, flags=re.IGNORECASE)
            if original != content:
                fixed_count += len(re.findall(r'Continue', original, re.IGNORECASE))
        
        # Fix "Learn more" -> "Mehr erfahren"
        if 'Learn more' in content:
            content = re.sub(r'Learn more', 'Mehr erfahren', content, flags=re.IGNORECASE)
            if original != content:
                fixed_count += len(re.findall(r'Learn more', original, re.IGNORECASE))
        
        return content, fixed_count
    
    def process_file(self, file_path: Path) -> bool:
        """Process a single HTML file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Apply fixes
            content, link_fixes = self.fix_broken_links(content, file_path)
            self.fixes["broken_links"] += link_fixes
            
            content, trans_fixes = self.fix_german_translations(content, file_path)
            self.fixes["german_translations"] += trans_fixes
            
            # Only write if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.fixes["files_processed"] += 1
                return True
            
            return False
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return False
    
    def run(self):
        """Run the fix on all HTML files"""
        print("🔧 Fixing broken links and German translations...")
        print()
        
        # Find all HTML files
        html_files = list(self.root_dir.rglob("*.html"))
        
        # Exclude certain directories
        exclude_dirs = {'node_modules', '.git', 'archive', 'react-app', 'android', 'ios'}
        html_files = [f for f in html_files if not any(excluded in f.parts for excluded in exclude_dirs)]
        
        print(f"📄 Processing {len(html_files)} HTML files...")
        print()
        
        # Process each file
        for i, file_path in enumerate(html_files, 1):
            if i % 50 == 0:
                print(f"⏳ Processed {i}/{len(html_files)} files...")
            self.process_file(file_path)
        
        print()
        print("✅ Fix complete!")
        print()
        print("📊 Statistics:")
        print(f"   Files processed: {self.fixes['files_processed']}")
        print(f"   Broken links fixed: {self.fixes['broken_links']}")
        print(f"   German translations fixed: {self.fixes['german_translations']}")
        print()

if __name__ == "__main__":
    fixer = LinkAndTranslationFixer()
    fixer.run()

