#!/usr/bin/env python3
"""
Create Clean Deployment Zip
Excludes archives, backups, fix scripts, and unnecessary files
"""

import os
import zipfile
from pathlib import Path
from datetime import datetime

class CleanZipCreator:
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir)
        self.exclude_dirs = {
            'archive',
            'archives',
            'backup',
            'backups',
            'node_modules',
            '.git',
            'react-app',
            'android',
            'ios',
            '__pycache__',
            '.pytest_cache',
            'venv',
            'env',
            '.venv'
        }
        
        self.exclude_patterns = [
            '*.backup.*',
            '*.bak',
            '*.tmp',
            '*.log',
            '*.pyc',
            '__pycache__',
            '.DS_Store',
            'Thumbs.db',
            '*.swp',
            '*.swo',
            '*~'
        ]
        
        self.exclude_files = {
            # Fix scripts
            'final-comprehensive-fix.py',
            'fix-broken-links-and-translations.py',
            'fix-german-translations-comprehensive.py',
            'fix-critical-files-final.py',
            'final-verification.py',
            'auto-fix-all-errors.py',
            'create-clean-zip.py',
            
            # Documentation that's not needed for deployment
            '*.md',  # Will exclude all markdown files except README
            '*.txt',
            
            # Reports
            'FINAL-FIX-REPORT.json',
            'FINAL-VERIFICATION-REPORT.json',
            'FINAL-REPOSITORY-STATUS.json',
            'AUTO-FIX-REPORT.json',
            'COMPREHENSIVE-TEST-REPORT.json',
            '*.json',  # Exclude JSON reports, but keep data JSON files
            
            # Other unnecessary files
            '.env',
            '.env.local',
            '.env.example',
        }
        
        # Keep these important files
        self.keep_files = {
            'README.md',
            'netlify.toml',
            '_headers',
            '_redirects',
            '.gitignore',
            'package.json',
            'package-lock.json'
        }
    
    def should_exclude(self, file_path: Path) -> bool:
        """Check if a file should be excluded"""
        # Check if in excluded directory
        for part in file_path.parts:
            if part in self.exclude_dirs:
                return True
        
        # Check exclude patterns
        for pattern in self.exclude_patterns:
            if file_path.match(pattern):
                return True
        
        # Check specific exclude files
        file_name = file_path.name
        if file_name in self.exclude_files:
            return True
        
        # Check if it's a markdown file (except README)
        if file_path.suffix == '.md' and file_name != 'README.md':
            return True
        
        # Check if it's a JSON report file
        if file_path.suffix == '.json':
            # Keep JSON files in content/ directory
            if 'content' in file_path.parts:
                return False
            # Keep JSON files in data directories
            if 'data' in file_path.parts:
                return False
            # Exclude report JSON files
            if any(keyword in file_name.lower() for keyword in ['report', 'status', 'fix', 'verification', 'audit']):
                return True
        
        # Check if it's a Python script (except if it's needed)
        if file_path.suffix == '.py':
            return True
        
        # Check if it's a backup file
        if 'backup' in file_name.lower() or '.backup.' in file_name:
            return True
        
        return False
    
    def should_include(self, file_path: Path) -> bool:
        """Check if a file should be included"""
        # Always include keep files
        if file_path.name in self.keep_files:
            return True
        
        # Don't include excluded files
        if self.should_exclude(file_path):
            return False
        
        return True
    
    def create_zip(self, output_name: str = None):
        """Create the clean zip file"""
        if output_name is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_name = f"tap-in-clean-deployment-{timestamp}.zip"
        
        output_path = self.root_dir / output_name
        
        print("📦 Creating clean deployment zip...")
        print(f"📁 Root directory: {self.root_dir}")
        print(f"📄 Output file: {output_name}")
        print()
        
        files_added = 0
        files_excluded = 0
        
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Walk through all files
            for root, dirs, files in os.walk(self.root_dir):
                # Skip excluded directories
                dirs[:] = [d for d in dirs if d not in self.exclude_dirs and not d.startswith('.')]
                
                for file in files:
                    file_path = Path(root) / file
                    rel_path = file_path.relative_to(self.root_dir)
                    
                    # Skip if should be excluded
                    if not self.should_include(file_path):
                        files_excluded += 1
                        continue
                    
                    # Add file to zip
                    try:
                        zipf.write(file_path, rel_path)
                        files_added += 1
                        if files_added % 100 == 0:
                            print(f"⏳ Added {files_added} files...")
                    except Exception as e:
                        print(f"⚠️  Error adding {rel_path}: {e}")
                        files_excluded += 1
        
        print()
        print("✅ Zip file created!")
        print()
        print("📊 Statistics:")
        print(f"   Files added: {files_added}")
        print(f"   Files excluded: {files_excluded}")
        print(f"   Zip size: {output_path.stat().st_size / 1024 / 1024:.2f} MB")
        print()
        print(f"📦 Output: {output_path.absolute()}")
        
        return output_path

if __name__ == "__main__":
    creator = CleanZipCreator()
    zip_path = creator.create_zip()
    print()
    print("🎉 Clean deployment zip ready!")

