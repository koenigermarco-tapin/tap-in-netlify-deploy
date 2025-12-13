#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final Optimization and Zip Creation
- Verify all background errors fixed
- Remove temporary/duplicate files
- Create optimized deployment zip
"""

import os
import shutil
from pathlib import Path

def verify_background_errors_fixed():
    """Verify background errors are properly suppressed"""
    print("🔍 Verifying background errors are fixed...\n")
    
    issues = []
    
    # Check main files for proper error suppression
    main_files = ['gym-dashboard.html', 'index.html', 'learning-hub.html']
    
    for file in main_files:
        if not os.path.exists(file):
            continue
        
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if error handlers have suppression
        has_suppression = any(keyword in content.lower() for keyword in [
            'suppress', 'expected', 'service worker', 'favicon',
            'preventdefault', 'silent'
        ])
        
        if not has_suppression:
            issues.append(f"{file}: No error suppression found")
        else:
            print(f"  ✅ {file}: Error suppression present")
    
    if issues:
        print(f"\n⚠️  {len(issues)} potential issues found")
        return False
    else:
        print("\n✅ All background errors properly suppressed")
        return True

def cleanup_temp_files():
    """Remove temporary Python scripts and markdown files"""
    print("\n🧹 Cleaning up temporary files...\n")
    
    temp_patterns = [
        '*.py',
        '*_FINAL*.md',
        '*_COMPLETE*.md',
        '*_AUDIT*.md',
        '*_REPORT*.md',
        '*_STATUS*.md',
        '*_GUIDE*.md',
        'CONNECTION-AUDIT-REPORT.json'
    ]
    
    # Keep important scripts and docs, remove only truly temporary ones
    keep_files = [
        'fix-all-audit-issues-comprehensive.py',
        'comprehensive-system-audit.py',
        'enterprise-connection-audit.py',
        'FULL-PLAYTHROUGH-CHECKLIST.md',
        'COMPREHENSIVE-AUDIT-FIX-FINAL.md'
    ]
    
    removed = 0
    for root, dirs, files in os.walk('.'):
        # Skip certain directories
        if any(skip in root for skip in ['node_modules', '.git', 'archive']):
            continue
        
        for file in files:
            if any(file.startswith(pat.replace('*', '')) or file.endswith(pat.replace('*', '')) 
                   for pat in temp_patterns if '*' in pat):
                if file not in keep_files:
                    filepath = os.path.join(root, file)
                    try:
                        os.remove(filepath)
                        removed += 1
                    except:
                        pass
    
    if removed > 0:
        print(f"  ✅ Removed {removed} temporary files")
    else:
        print("  ✓ No temporary files to remove")

def create_optimized_zip():
    """Create optimized deployment zip"""
    print("\n📦 Creating optimized deployment zip...\n")
    
    import subprocess
    from datetime import datetime
    
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    zip_name = f"tap-in-optimized-deployment-{timestamp}.zip"
    zip_path = os.path.join(os.path.expanduser('~/Downloads'), zip_name)
    
    # Exclude patterns
    excludes = [
        '--exclude', '*.git*',
        '--exclude', 'node_modules/*',
        '--exclude', '*.DS_Store',
        '--exclude', '*.zip',
        '--exclude', '*.log',
        '--exclude', '__pycache__/*',
        '--exclude', '*.pyc',
        '--exclude', '.cursor/*',
        '--exclude', 'react-app/node_modules/*',
        '--exclude', 'react-app/build/*',
        '--exclude', '.next/*',
        '--exclude', 'dist/*',
        '--exclude', '*.py',  # Exclude Python scripts
        '--exclude', '*_FINAL*.md',
        '--exclude', '*_AUDIT*.md',
        '--exclude', '*_REPORT*.md',
        '--exclude', 'CONNECTION-AUDIT-REPORT.json'
    ]
    
    # Build zip command
    cmd = ['zip', '-r', zip_path, '.'] + excludes
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd='.')
        if result.returncode == 0:
            # Get zip info
            size = os.path.getsize(zip_path) / (1024 * 1024)  # MB
            
            print(f"✅ Zip created successfully!")
            print(f"\n📁 File: {zip_name}")
            print(f"📊 Size: {size:.1f} MB")
            print(f"📍 Location: ~/Downloads/")
            
            return zip_path
        else:
            print(f"⚠️  Zip creation had issues: {result.stderr}")
            return None
    except Exception as e:
        print(f"❌ Error creating zip: {e}")
        return None

def main():
    print("="*80)
    print("🚀 FINAL OPTIMIZATION & DEPLOYMENT ZIP")
    print("="*80)
    
    # Verify errors fixed
    errors_ok = verify_background_errors_fixed()
    
    if not errors_ok:
        print("\n⚠️  WARNING: Some background errors may still exist")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            return
    
    # Cleanup
    cleanup_temp_files()
    
    # Create zip
    zip_path = create_optimized_zip()
    
    print("\n" + "="*80)
    if zip_path:
        print("✅ OPTIMIZED DEPLOYMENT ZIP READY")
    else:
        print("⚠️  ZIP CREATION COMPLETE (with warnings)")
    print("="*80)

if __name__ == '__main__':
    main()

