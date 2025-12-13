#!/usr/bin/env python3
"""
Comprehensive German Translation Fixer
Fixes English text in German files
"""

import re
from pathlib import Path

class GermanTranslationFixer:
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir)
        self.translations = {
            "Continue": "Weiter",
            "Learn more": "Mehr erfahren",
            "Start": "Start",
            "Next": "Weiter",
            "Previous": "Zurück",
            "Submit": "Absenden",
            "Save": "Speichern",
            "Cancel": "Abbrechen",
            "Close": "Schließen",
            "Back": "Zurück",
            "Skip": "Überspringen",
            "Finish": "Beenden"
        }
        self.fixes = 0
        self.files_processed = 0
        
    def fix_translations(self, content: str) -> tuple[str, int]:
        """Fix English text in German content"""
        fixed_count = 0
        original = content
        
        # Fix in button/link contexts
        for english, german in self.translations.items():
            # Pattern: >Continue< or "Continue" or 'Continue'
            patterns = [
                (rf'>\s*{re.escape(english)}\s*<', f'>{german}<'),
                (rf'["\']{re.escape(english)}["\']', f'"{german}"'),
                (rf'>{re.escape(english)}</', f'>{german}</'),
            ]
            
            for pattern, replacement in patterns:
                matches = len(re.findall(pattern, content, re.IGNORECASE))
                if matches > 0:
                    content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
                    fixed_count += matches
        
        return content, fixed_count
    
    def process_file(self, file_path: Path) -> bool:
        """Process a German HTML file"""
        # Only process German files
        if not (file_path.name.endswith('-de.html') or 
                file_path.name.endswith('.de.html') or
                'de.html' in file_path.name):
            return False
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            content, fixes = self.fix_translations(content)
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.fixes += fixes
                self.files_processed += 1
                return True
            
            return False
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return False
    
    def run(self):
        """Run the fix on all German HTML files"""
        print("🔧 Fixing German translations...")
        print()
        
        # Find all German HTML files
        html_files = list(self.root_dir.rglob("*de.html"))
        html_files += list(self.root_dir.rglob("*-de.html"))
        
        # Exclude certain directories
        exclude_dirs = {'node_modules', '.git', 'archive', 'react-app', 'android', 'ios'}
        html_files = [f for f in html_files if not any(excluded in f.parts for excluded in exclude_dirs)]
        
        # Remove duplicates
        html_files = list(set(html_files))
        
        print(f"📄 Processing {len(html_files)} German HTML files...")
        print()
        
        # Process each file
        for i, file_path in enumerate(html_files, 1):
            if i % 20 == 0:
                print(f"⏳ Processed {i}/{len(html_files)} files...")
            self.process_file(file_path)
        
        print()
        print("✅ Fix complete!")
        print()
        print("📊 Statistics:")
        print(f"   Files processed: {self.files_processed}")
        print(f"   Translations fixed: {self.fixes}")
        print()

if __name__ == "__main__":
    fixer = GermanTranslationFixer()
    fixer.run()

