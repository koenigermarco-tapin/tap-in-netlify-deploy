#!/usr/bin/env python3
"""Update gym dashboard files to use XPManager instead of direct localStorage"""

import re

def update_dashboard_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Replace all localStorage.getItem('totalXP') with XPManager.getTotalXP()
    content = re.sub(
        r"localStorage\.getItem\(['\"]totalXP['\"]\)",
        "XPManager.getTotalXP()",
        content
    )
    
    # Replace all localStorage.setItem('totalXP', ...) with XPManager.setTotalXP(...)
    content = re.sub(
        r"localStorage\.setItem\(['\"]totalXP['\"],\s*([^)]+)\)",
        r"XPManager.setTotalXP(\1)",
        content
    )
    
    # Replace parseInt(localStorage.getItem('totalXP') || '0') with XPManager.getTotalXP()
    content = re.sub(
        r"parseInt\(localStorage\.getItem\(['\"]totalXP['\"]\)\s*\|\|\s*['\"]0['\"]\)",
        "XPManager.getTotalXP()",
        content
    )
    
    # Replace data.totalXP += amount with XPManager.addXP(amount)
    # This needs to be context-aware, so we'll be careful
    # Find patterns like: data.totalXP += amount; then data.totalXP = ...
    content = re.sub(
        r"(data\.totalXP\s*\+=\s*)([^;]+)",
        lambda m: f"XPManager.addXP({m.group(2)})",
        content
    )
    
    # Update syncProgressToCloud function to use XPManager
    content = re.sub(
        r"totalXP:\s*parseInt\(localStorage\.getItem\(['\"]totalXP['\"]\)\s*\|\|\s*['\"]0['\"]\)",
        "totalXP: XPManager.getTotalXP()",
        content
    )
    
    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated {filename}")
        return True
    else:
        print(f"⚠️  No changes needed for {filename}")
        return False

# Update both dashboard files
files = ['gym-dashboard.html', 'gym-dashboard-de.html']

for file in files:
    try:
        update_dashboard_file(file)
    except Exception as e:
        print(f"❌ Error updating {file}: {e}")

print("\n✅ Dashboard XP system update complete!")

