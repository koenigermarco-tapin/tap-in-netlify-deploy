#!/usr/bin/env python3

"""

Fix Belt Assessment Links - COMPREHENSIVE VERSION

Automatically updates all references from belt-assessment.html to belt-assessment-v2.html
Searches all HTML files in the directory

"""



import os

import re

from pathlib import Path



def fix_belt_assessment_links(directory="."):

    """Find and fix all belt-assessment.html references in HTML files"""

    

    old_link = "belt-assessment.html"

    new_link = "belt-assessment-v2.html"

    

    # Get all HTML files

    html_files = list(Path(directory).glob("*.html"))

    
    # Exclude certain files
    excluded_files = [
        "belt-assessment.html",  # The old file itself
        "belt-assessment-v2.html",  # The new file
        "belt-assessment-de.html",  # German version
    ]
    
    files_updated = []

    total_replacements = 0
    
    
    for filepath in html_files:
        filename = filepath.name
        
        # Skip excluded files
        if filename in excluded_files:
            continue
            
        # Skip archive folder
        if "archive" in str(filepath):
            continue
        
        # Read file
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"⚠️  Error reading {filename}: {e}")
            continue
        
        # Check if old link exists
        if old_link not in content:
            continue
        
        # Count occurrences
        count = content.count(old_link)
        
        # Replace all occurrences
        new_content = content.replace(old_link, new_link)
        
        # Write back
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            files_updated.append(filename)
            total_replacements += count
            print(f"✅ Updated {filename} ({count} reference(s) fixed)")
        except Exception as e:
            print(f"⚠️  Error writing {filename}: {e}")
    
    return files_updated, total_replacements



if __name__ == "__main__":

    print("🔧 Fixing Belt Assessment Links (Comprehensive Search)...\n")
    print("Searching all HTML files for 'belt-assessment.html' references...\n")
    
    # Run the fix
    updated, total = fix_belt_assessment_links()
    
    print(f"\n📊 Summary:")
    print(f"   Files updated: {len(updated)}")
    print(f"   Total replacements: {total}")
    
    if updated:
        print(f"\n✅ Fixed files:")
        for f in updated:
            print(f"   - {f}")
        print(f"\n🚀 All references updated to belt-assessment-v2.html")
    else:
        print(f"\n💡 No files needed updating!")
        print(f"   All files already reference belt-assessment-v2.html or have no belt assessment links")
    
    print("\n" + "="*50)
    print("NOTE:")
    print("This updated references to the main belt-assessment.html file.")
    print("Belt-specific assessments (white-belt-assessment.html, etc.) were not changed.")
    print("="*50)
