#!/usr/bin/env python3
"""
Create Final Clean Repository Zip
Excludes: node_modules, .git, archive, build artifacts, temp files
"""

import os
import zipfile
from pathlib import Path
from datetime import datetime

def should_exclude(path):
    """Check if path should be excluded from zip"""
    path_str = str(path)
    
    # Exclude patterns
    exclude_patterns = [
        'node_modules',
        '.git',
        '__pycache__',
        '.DS_Store',
        '*.pyc',
        'archive/',
        'backups/',
        'android/',
        'ios/',
        'capacitor/',
        '.idea/',
        '.vscode/',
        'dist/',
        'build/',
        '*.zip',
        '*.log',
        '.env',
        'package-lock.json',
        'yarn.lock',
        'Pods/',
        '*.xcodeproj',
        '*.xcworkspace',
    ]
    
    for pattern in exclude_patterns:
        if pattern in path_str:
            return True
    
    # Exclude hidden files except allowed ones
    if path.name.startswith('.') and path.name not in ['.htaccess', '.gitignore', '.gitattributes']:
        return True
    
    return False

def create_zip():
    """Create comprehensive zip archive"""
    repo_root = Path('.')
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    zip_name = f'TAP-IN-FULL-REPO-{timestamp}.zip'
    downloads_path = Path.home() / 'Downloads'
    zip_path = downloads_path / zip_name
    
    print(f"📦 Creating zip archive: {zip_name}")
    print(f"📍 Destination: {zip_path}")
    print()
    
    files_added = 0
    total_size = 0
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zipf:
        # Walk through all files
        for root, dirs, files in os.walk('.'):
            # Filter out excluded directories
            dirs[:] = [d for d in dirs if not should_exclude(Path(root) / d)]
            
            for file in files:
                file_path = Path(root) / file
                
                # Skip if should be excluded
                if should_exclude(file_path):
                    continue
                
                # Skip zip files
                if file_path.suffix == '.zip':
                    continue
                
                # Get relative path for zip
                try:
                    arcname = file_path.relative_to(repo_root)
                    
                    # Add file to zip
                    zipf.write(file_path, arcname)
                    files_added += 1
                    total_size += file_path.stat().st_size
                    
                    if files_added % 100 == 0:
                        print(f"  Added {files_added} files...")
                        
                except Exception as e:
                    print(f"  ⚠️  Skipped {file_path}: {e}")
                    continue
    
    zip_size = zip_path.stat().st_size
    zip_size_mb = zip_size / (1024 * 1024)
    
    print()
    print(f"✅ Zip created successfully!")
    print(f"   📁 Files added: {files_added}")
    print(f"   💾 Zip size: {zip_size_mb:.2f} MB")
    print(f"   📍 Location: {zip_path}")
    print()
    
    return zip_path

if __name__ == '__main__':
    try:
        zip_path = create_zip()
        print(f"🎉 Final repository zip ready: {zip_path.name}")
    except Exception as e:
        print(f"❌ Error creating zip: {e}")
        exit(1)

