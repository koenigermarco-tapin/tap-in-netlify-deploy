#!/usr/bin/env python3
"""
Create Clean Production Repository
Removes all unnecessary files, keeps only production files
Fixes error handlers to prevent background messages
"""

import os
import shutil
import re
from pathlib import Path

# Configuration
SOURCE_DIR = Path(".")
CLEAN_DIR = Path("../tap-in-CLEAN-PRODUCTION")
CLEAN_DIR.mkdir(exist_ok=True)

# Files to exclude (patterns)
EXCLUDE_PATTERNS = [
    # Documentation
    "*.md",
    "*.txt",
    "*.MD",
    
    # Python scripts
    "*.py",
    "__pycache__",
    
    # Git
    ".git",
    ".gitignore",
    
    # Build/Development
    "node_modules",
    ".vscode",
    ".idea",
    "*.swp",
    "*.swo",
    "*~",
    "*.tmp",
    
    # Archives
    "archive",
    "*backup*",
    "*BACKUP*",
    "*temp*",
    "*TEMP*",
    
    # Old/duplicate files
    "*-OLD*.html",
    "*-old*.html",
    "*-TEMP*.html",
    "*-BACKUP*.html",
    "*-test*.html",
    "*-demo*.html",
    
    # Zip files
    "*.zip",
    
    # OS files
    ".DS_Store",
    "*.log",
    
    # React app (if separate)
    "react-app",
    "android",
    "ios",
]

# Essential directories to copy
ESSENTIAL_DIRS = [
    "css",
    "js",
    "icons",
    "images",
    "content",
    "components",
    "netlify",
]

# Essential file patterns to keep
ESSENTIAL_PATTERNS = [
    "*.html",
    "*.css",
    "*.js",
    "*.json",
    "*.png",
    "*.jpg",
    "*.jpeg",
    "*.svg",
    "*.webp",
    "*.woff",
    "*.woff2",
    "*.ttf",
    "*.ico",
    "manifest.json",
    "sw.js",
    "service-worker.js",
    "cache-buster.js",
    "_redirects",
    "_headers",
    "netlify.toml",
    "robots.txt",
]

def should_exclude(path):
    """Check if path should be excluded"""
    path_str = str(path)
    
    for pattern in EXCLUDE_PATTERNS:
        if pattern in path_str or path.name == pattern:
            return True
    
    return False

def should_include(path):
    """Check if path should be included"""
    if should_exclude(path):
        return False
    
    # Always include essential directories
    if path.is_dir() and path.name in ESSENTIAL_DIRS:
        return True
    
    # Check patterns
    for pattern in ESSENTIAL_PATTERNS:
        if path.match(pattern):
            return True
    
    return False

def fix_error_handlers(file_path):
    """Fix error handlers to not show toasts"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Remove toast calls from error handlers
        content = re.sub(
            r'TapInUtils\.showToast\([^)]+\)',
            '// Toast removed - silent error handling',
            content
        )
        
        # Remove showErrorToast calls
        content = re.sub(
            r'showErrorToast\([^)]+\)',
            '// Error toast removed - silent logging only',
            content
        )
        
        # Ensure error handlers only log, don't show
        if 'showToast' in content and 'error' in content.lower():
            content = re.sub(
                r'(console\.error\([^)]+\))',
                r'\1; // Silent error - no user notification',
                content
            )
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
    except Exception as e:
        print(f"  ⚠️  Could not fix {file_path}: {e}")
    
    return False

def copy_essential_files():
    """Copy only essential files to clean directory"""
    print("=== CREATING CLEAN PRODUCTION REPOSITORY ===\n")
    
    copied_files = 0
    copied_dirs = 0
    fixed_files = 0
    
    # Copy essential directories
    print("📁 Copying essential directories...")
    for dir_name in ESSENTIAL_DIRS:
        src_dir = SOURCE_DIR / dir_name
        if src_dir.exists():
            dst_dir = CLEAN_DIR / dir_name
            shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)
            copied_dirs += 1
            print(f"  ✅ {dir_name}/")
    
    # Copy essential files
    print("\n📄 Copying essential files...")
    
    for root, dirs, files in os.walk(SOURCE_DIR):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if not should_exclude(Path(root) / d)]
        
        for file in files:
            file_path = Path(root) / file
            
            # Skip if excluded
            if should_exclude(file_path):
                continue
            
            # Check if should include
            if should_include(file_path):
                # Calculate relative path
                rel_path = file_path.relative_to(SOURCE_DIR)
                dst_path = CLEAN_DIR / rel_path
                
                # Create directory if needed
                dst_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Copy file
                shutil.copy2(file_path, dst_path)
                copied_files += 1
                
                # Fix error handlers in JS files
                if file_path.suffix == '.js' or file_path.suffix == '.html':
                    if fix_error_handlers(dst_path):
                        fixed_files += 1
                        print(f"  ✅ {rel_path} (error handlers fixed)")
                    else:
                        if copied_files % 50 == 0:
                            print(f"  ... {copied_files} files copied")
    
    print(f"\n✅ Complete!")
    print(f"  📁 Directories: {copied_dirs}")
    print(f"  📄 Files: {copied_files}")
    print(f"  🔧 Fixed: {fixed_files} error handlers")
    print(f"\n📦 Clean repository at: {CLEAN_DIR.absolute()}")

if __name__ == "__main__":
    copy_essential_files()

