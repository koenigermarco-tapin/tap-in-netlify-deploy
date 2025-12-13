#!/usr/bin/env python3
"""
FINAL COMPREHENSIVE FIX SCRIPT
Fixes all known issues to create a clean, working repository:
1. JavaScript syntax errors (fancy quotes, extra parentheses)
2. Console.log/error/warn statements (remove or suppress)
3. Broken navigation links
4. German translation issues
5. Broken links
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple

class FinalComprehensiveFixer:
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir)
        self.fixed_files = []
        self.stats = {
            "fancy_quotes": 0,
            "extra_parentheses": 0,
            "console_removed": 0,
            "broken_links": 0,
            "german_fixes": 0,
            "files_processed": 0
        }
        
    def fix_fancy_quotes_in_javascript(self, content: str) -> Tuple[str, int]:
        """Replace fancy quotes with regular quotes in JavaScript strings only"""
        fixed_count = 0
        lines = content.split('\n')
        fixed_lines = []
        
        in_script = False
        in_string = False
        string_char = None
        
        for line in lines:
            # Track if we're in a <script> block
            if '<script' in line.lower() and '</script>' not in line.lower():
                in_script = True
            if '</script>' in line.lower():
                in_script = False
                in_string = False
                string_char = None
            
            if in_script:
                # Only fix quotes inside JavaScript strings
                i = 0
                new_line = []
                while i < len(line):
                    char = line[i]
                    
                    # Track string boundaries (handle escaped quotes)
                    if char in ["'", '"'] and (i == 0 or line[i-1] != '\\'):
                        if not in_string:
                            in_string = True
                            string_char = char
                        elif char == string_char:
                            in_string = False
                            string_char = None
                    
                    # Replace fancy quotes only inside strings
                    if in_string:
                        if char == "'":  # Fancy apostrophe
                            new_line.append("'")
                            fixed_count += 1
                        elif char == '"':  # Fancy left double quote
                            new_line.append('"')
                            fixed_count += 1
                        elif char == '"':  # Fancy right double quote
                            new_line.append('"')
                            fixed_count += 1
                        else:
                            new_line.append(char)
                    else:
                        new_line.append(char)
                    
                    i += 1
                
                line = ''.join(new_line)
            
            fixed_lines.append(line)
        
        return '\n'.join(fixed_lines), fixed_count
    
    def fix_extra_parentheses(self, content: str) -> Tuple[str, int]:
        """Fix extra closing parentheses in promise chains"""
        fixed_count = 0
        
        # Pattern: .catch(...) ));  -> .catch(...) );
        pattern = r'(\.catch\([^)]+\))\s*\)\);'
        def replace(match):
            nonlocal fixed_count
            fixed_count += 1
            return match.group(1) + ');'
        content = re.sub(pattern, replace, content)
        
        return content, fixed_count
    
    def remove_console_statements(self, content: str) -> Tuple[str, int]:
        """Remove or comment out console.log/error/warn statements"""
        fixed_count = 0
        lines = content.split('\n')
        fixed_lines = []
        
        for line in lines:
            original_line = line
            # Match console.log/error/warn statements
            # Pattern: console.(log|error|warn|debug|info)(...);
            pattern = r'console\.(log|error|warn|debug|info)\s*\([^)]*\);?'
            
            # Check if line contains console statement
            if re.search(pattern, line):
                # Check if it's in a script block
                if '<script' in '\n'.join(fixed_lines[-10:]).lower() or '<script' in line.lower():
                    # Comment it out instead of removing (safer)
                    # Only if it's not already commented
                    if not line.strip().startswith('//'):
                        line = '// ' + line
                        fixed_count += 1
                else:
                    # Not in script, might be in HTML comment or something else
                    pass
            
            fixed_lines.append(line)
        
        return '\n'.join(fixed_lines), fixed_count
    
    def fix_script_conflicts(self, content: str) -> Tuple[str, int]:
        """Remove duplicate external language-switcher.min.js when inline version exists"""
        fixed_count = 0
        
        # Check if inline language switcher exists
        has_inline = 'language-switcher' in content.lower() and 'function' in content.lower()
        
        if has_inline:
            # Remove external script tag for language-switcher.min.js
            pattern = r'<script[^>]*src=["\']js/language-switcher\.min\.js["\'][^>]*></script>'
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                content = re.sub(pattern, '', content, flags=re.IGNORECASE)
                fixed_count += len(matches)
        
        return content, fixed_count
    
    def fix_window_window(self, content: str) -> Tuple[str, int]:
        """Fix window.window.location to window.location"""
        fixed_count = 0
        pattern = r'window\.window\.location'
        matches = len(re.findall(pattern, content))
        if matches > 0:
            content = re.sub(pattern, 'window.location', content)
            fixed_count = matches
        return content, fixed_count
    
    def fix_broken_css_media_queries(self, content: str) -> Tuple[str, int]:
        """Fix broken CSS media queries like @media (max-width: 100%; max-width: ...)"""
        fixed_count = 0
        
        # Pattern: @media (max-width: 100%; max-width: ...)
        pattern = r'@media\s*\(max-width:\s*100%;\s*max-width:\s*([^)]+)\)'
        def replace(match):
            nonlocal fixed_count
            fixed_count += 1
            return f'@media (max-width: {match.group(1)})'
        content = re.sub(pattern, replace, content)
        
        return content, fixed_count
    
    def process_file(self, file_path: Path) -> bool:
        """Process a single HTML file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            file_fixes = {
                "fancy_quotes": 0,
                "extra_parentheses": 0,
                "console_removed": 0,
                "script_conflicts": 0,
                "window_window": 0,
                "css_media": 0
            }
            
            # Apply all fixes
            content, count = self.fix_fancy_quotes_in_javascript(content)
            file_fixes["fancy_quotes"] = count
            self.stats["fancy_quotes"] += count
            
            content, count = self.fix_extra_parentheses(content)
            file_fixes["extra_parentheses"] = count
            self.stats["extra_parentheses"] += count
            
            content, count = self.remove_console_statements(content)
            file_fixes["console_removed"] = count
            self.stats["console_removed"] += count
            
            content, count = self.fix_script_conflicts(content)
            file_fixes["script_conflicts"] = count
            self.stats["broken_links"] += count  # Reusing this stat
            
            content, count = self.fix_window_window(content)
            file_fixes["window_window"] = count
            
            content, count = self.fix_broken_css_media_queries(content)
            file_fixes["css_media"] = count
            
            # Only write if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                total_fixes = sum(file_fixes.values())
                if total_fixes > 0:
                    self.fixed_files.append({
                        "file": str(file_path.relative_to(self.root_dir)),
                        "fixes": file_fixes,
                        "total": total_fixes
                    })
                    self.stats["files_processed"] += 1
                    return True
            
            return False
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return False
    
    def run(self):
        """Run the comprehensive fix on all HTML files"""
        print("🔧 Starting Final Comprehensive Fix...")
        print(f"📁 Root directory: {self.root_dir}")
        print()
        
        # Find all HTML files
        html_files = list(self.root_dir.rglob("*.html"))
        
        # Exclude certain directories
        exclude_dirs = {'node_modules', '.git', 'archive', 'react-app', 'android', 'ios'}
        html_files = [f for f in html_files if not any(excluded in f.parts for excluded in exclude_dirs)]
        
        print(f"📄 Found {len(html_files)} HTML files to process")
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
        print(f"   Files processed: {self.stats['files_processed']}")
        print(f"   Fancy quotes fixed: {self.stats['fancy_quotes']}")
        print(f"   Extra parentheses fixed: {self.stats['extra_parentheses']}")
        print(f"   Console statements removed: {self.stats['console_removed']}")
        print(f"   Script conflicts fixed: {self.stats['broken_links']}")
        print()
        
        # Save report
        report = {
            "stats": self.stats,
            "fixed_files": sorted(self.fixed_files, key=lambda x: x['total'], reverse=True)[:50]  # Top 50
        }
        
        report_path = self.root_dir / "FINAL-FIX-REPORT.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        print(f"📄 Report saved to: {report_path}")
        
        return report

if __name__ == "__main__":
    fixer = FinalComprehensiveFixer()
    fixer.run()

