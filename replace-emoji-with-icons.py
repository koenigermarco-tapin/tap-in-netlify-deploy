#!/usr/bin/env python3
"""
TAP-IN Emoji to Icon Replacement Script
Safely replaces emoji with professional icons in HTML files
"""

import re
import os
from pathlib import Path

# Emoji to Font Awesome icon mapping
EMOJI_TO_ICON = {
    # Common UI emoji
    '🎯': '<i class="fas fa-bullseye icon-md icon-primary"></i>',
    '⚡': '<i class="fas fa-bolt icon-md icon-warning"></i>',
    '🔥': '<i class="fas fa-fire icon-md icon-danger"></i>',
    '⭐': '<i class="fas fa-star icon-md icon-warning"></i>',
    '🏆': '<i class="fas fa-trophy icon-md icon-warning"></i>',
    '🎓': '<i class="fas fa-graduation-cap icon-md icon-primary"></i>',
    '💡': '<i class="fas fa-lightbulb icon-md icon-warning"></i>',
    '📊': '<i class="fas fa-chart-line icon-md icon-success"></i>',
    '✅': '<i class="fas fa-check-circle icon-md icon-success"></i>',
    '❌': '<i class="fas fa-times-circle icon-md icon-danger"></i>',
    '⏰': '<i class="fas fa-clock icon-md icon-info"></i>',
    '🎨': '<i class="fas fa-palette icon-md icon-primary"></i>',
    '🚀': '<i class="fas fa-rocket icon-md icon-primary"></i>',
    
    # Belt-related
    '⚪': '<i class="fas fa-circle icon-md" style="color: #f7fafc;"></i>',
    '🔵': '<i class="fas fa-circle icon-md" style="color: #3b82f6;"></i>',
    '🟣': '<i class="fas fa-circle icon-md" style="color: #7c3aed;"></i>',
    '🟤': '<i class="fas fa-circle icon-md" style="color: #92400e;"></i>',
    '⚫': '<i class="fas fa-circle icon-md" style="color: #1f2937;"></i>',
    
    # Martial arts / learning
    '🥋': '<i class="fas fa-fist-raised icon-md icon-primary"></i>',
    '💪': '<i class="fas fa-dumbbell icon-md icon-primary"></i>',
    '🧠': '<i class="fas fa-brain icon-md icon-info"></i>',
    '💬': '<i class="fas fa-comments icon-md icon-info"></i>',
    '👥': '<i class="fas fa-users icon-md icon-primary"></i>',
    
    # Progress / status
    '📈': '<i class="fas fa-chart-line icon-md icon-success"></i>',
    '📉': '<i class="fas fa-chart-line icon-md icon-danger"></i>',
    '🎉': '<i class="fas fa-party-horn icon-md icon-warning"></i>',
    '🎊': '<i class="fas fa-confetti icon-md icon-warning"></i>',
    
    # Common actions
    '➡️': '<i class="fas fa-arrow-right icon-sm"></i>',
    '⬅️': '<i class="fas fa-arrow-left icon-sm"></i>',
    '⬆️': '<i class="fas fa-arrow-up icon-sm"></i>',
    '⬇️': '<i class="fas fa-arrow-down icon-sm"></i>',
    
    # Navigation
    '🏠': '<i class="fas fa-home icon-md"></i>',
    '⚙️': '<i class="fas fa-cog icon-md"></i>',
    '🔔': '<i class="fas fa-bell icon-md"></i>',
    '👤': '<i class="fas fa-user icon-md"></i>',
}

# Files to process (key pages only - be selective!)
FILES_TO_UPDATE = [
    'index.html',
    'index-DUAL-ENTRY.html',
    'gym-dashboard.html',
    'gym-dashboard-de.html',
    'learning-hub.html',
    'learning-hub-de.html',
]

def replace_emoji_in_content(content, dry_run=False):
    """Replace emoji with icons in HTML content"""
    original = content
    changes = []
    
    # Replace emoji in specific contexts only
    # Don't replace in:
    # - <script> tags
    # - <style> tags
    # - HTML comments
    # - Attributes
    
    # Split content by script/style blocks
    parts = re.split(r'(<script[^>]*>.*?</script>|<style[^>]*>.*?</style>)', content, flags=re.DOTALL | re.IGNORECASE)
    
    result_parts = []
    for i, part in enumerate(parts):
        # Skip script and style tags
        if part.strip().startswith('<script') or part.strip().startswith('<style'):
            result_parts.append(part)
            continue
        
        # Replace emoji in this part
        modified_part = part
        for emoji, icon_html in EMOJI_TO_ICON.items():
            if emoji in modified_part:
                # Count occurrences
                count = modified_part.count(emoji)
                modified_part = modified_part.replace(emoji, icon_html)
                if count > 0:
                    changes.append(f"  - Replaced {count}x '{emoji}' with icon")
        
        result_parts.append(modified_part)
    
    new_content = ''.join(result_parts)
    
    return new_content, changes

def update_file(filepath, dry_run=False):
    """Update a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, changes = replace_emoji_in_content(content, dry_run)
        
        if changes:
            print(f"\n📄 {filepath}:")
            for change in changes:
                print(change)
            
            if not dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"  ✅ Updated!")
            else:
                print(f"  ⚠️  (Dry run - no changes saved)")
            
            return True
        else:
            print(f"📄 {filepath}: No emoji found to replace")
            return False
            
    except FileNotFoundError:
        print(f"⚠️  File not found: {filepath}")
        return False
    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")
        return False

def main():
    print("=" * 80)
    print("TAP-IN EMOJI TO ICON REPLACEMENT")
    print("=" * 80)
    print()
    
    # Check for dry-run flag
    import sys
    dry_run = '--dry-run' in sys.argv or '-d' in sys.argv
    
    if dry_run:
        print("🔍 DRY RUN MODE - No files will be modified")
        print()
    
    # Process files
    updated_count = 0
    
    for filename in FILES_TO_UPDATE:
        if os.path.exists(filename):
            if update_file(filename, dry_run):
                updated_count += 1
        else:
            print(f"⚠️  File not found: {filename}")
    
    print()
    print("=" * 80)
    if dry_run:
        print(f"🔍 DRY RUN COMPLETE - {updated_count} files would be updated")
        print("Run without --dry-run to apply changes")
    else:
        print(f"✅ COMPLETE - {updated_count} files updated")
        print()
        print("📝 Next steps:")
        print("  1. Add Font Awesome CDN to all HTML files")
        print("  2. Add icons.css to all HTML files")
        print("  3. Initialize Lucide icons in <body>")
        print("  4. Test all icons display correctly")
    print("=" * 80)

if __name__ == '__main__':
    main()

