#!/usr/bin/env python3
"""
Fix numbered option box readability in all carousel assessment files
"""

import os
import re
import glob

# CSS fix to inject
READABILITY_CSS = """
        /* ============= NUMBERED OPTION BOX READABILITY FIX ============= */
        .scale-option,
        .rating-option,
        .numbered-option,
        .option-number,
        [data-value="1"],
        [data-value="2"],
        [data-value="3"],
        [data-value="4"],
        [data-value="5"] {
            color: #FFFFFF !important;
            font-weight: 700 !important;
            font-size: 1.1rem !important;
            background: #1e293b !important;
            border: 2px solid #475569 !important;
            text-shadow: 0 1px 3px rgba(0,0,0,0.5) !important;
        }
        .scale-option:hover,
        .rating-option:hover,
        .numbered-option:hover,
        .option-number:hover,
        [data-value]:hover {
            background: #334155 !important;
            border-color: #667eea !important;
            color: #FFFFFF !important;
            transform: scale(1.05) !important;
        }
        .scale-option.selected,
        .rating-option.selected,
        .numbered-option.selected,
        .option-number.selected,
        [data-value].selected {
            background: #667eea !important;
            border-color: #818cf8 !important;
            color: #FFFFFF !important;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.3) !important;
        }
        .scale-label,
        .rating-label,
        .option-label {
            color: #FFFFFF !important;
            font-weight: 600 !important;
            font-size: 0.9rem !important;
            text-align: center !important;
            margin-top: 0.5rem !important;
        }
        .scale-container,
        .rating-container,
        .options-row {
            display: flex !important;
            justify-content: space-between !important;
            gap: 0.75rem !important;
            margin: 1.5rem 0 !important;
        }
        .scale-container > *,
        .rating-container > *,
        .options-row > * {
            flex: 1 !important;
            min-width: 60px !important;
            text-align: center !important;
            padding: 1rem 0.5rem !important;
            border-radius: 8px !important;
            cursor: pointer !important;
            transition: all 0.2s ease !important;
        }
        @media (max-width: 768px) {
            .scale-option,
            .rating-option,
            .numbered-option,
            .option-number,
            [data-value] {
                font-size: 1rem !important;
                padding: 0.75rem 0.25rem !important;
                min-width: 50px !important;
            }
            .scale-label,
            .rating-label,
            .option-label {
                font-size: 0.75rem !important;
            }
        }
        input[type="range"] {
            -webkit-appearance: none !important;
            width: 100% !important;
            height: 8px !important;
            background: #334155 !important;
            border-radius: 5px !important;
            outline: none !important;
        }
        input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none !important;
            width: 24px !important;
            height: 24px !important;
            background: #667eea !important;
            cursor: pointer !important;
            border-radius: 50% !important;
            border: 3px solid #FFFFFF !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.3) !important;
        }
        input[type="range"]::-moz-range-thumb {
            width: 24px !important;
            height: 24px !important;
            background: #667eea !important;
            cursor: pointer !important;
            border-radius: 50% !important;
            border: 3px solid #FFFFFF !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.3) !important;
        }
        .slider-value,
        .range-value {
            display: block !important;
            text-align: center !important;
            font-size: 1.5rem !important;
            font-weight: 700 !important;
            color: #667eea !important;
            margin-top: 1rem !important;
            text-shadow: 0 1px 2px rgba(0,0,0,0.2) !important;
        }
        .slider-labels {
            display: flex !important;
            justify-content: space-between !important;
            margin-top: 0.5rem !important;
        }
        .slider-labels span {
            font-size: 0.85rem !important;
            color: #cbd5e1 !important;
            font-weight: 600 !important;
        }
"""

def fix_carousel_file(filepath):
    """Add readability CSS to a carousel file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if fix already applied
        if 'NUMBERED OPTION BOX READABILITY FIX' in content:
            return False
        
        # Find closing </style> tag
        if '</style>' in content:
            # Insert before closing style tag
            content = content.replace('</style>', f'{READABILITY_CSS}\n    </style>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Fixed: {filepath}")
            return True
        else:
            print(f"⚠️  No <style> tag found in: {filepath}")
            return False
    except Exception as e:
        print(f"❌ Error fixing {filepath}: {e}")
        return False

def main():
    """Fix all carousel files"""
    # Files to fix - find all carousel and stripe files
    patterns = [
        '*-carousel-NEW.html',
        '*-stripe*-carousel*.html',
        'white-belt-stripe*.html',
        'blue-belt-stripe*.html',
        'purple-belt-stripe*.html',
        'brown-belt-stripe*.html',
        'black-belt-stripe*.html',
        '*-belt-assessment.html',
        '*-graduation-assessment.html'
    ]
    
    fixed_count = 0
    skipped_count = 0
    
    for pattern in patterns:
        files = glob.glob(pattern)
        for filepath in files:
            # Skip archive and node_modules
            if 'archive' in filepath or 'node_modules' in filepath:
                continue
            if fix_carousel_file(filepath):
                fixed_count += 1
            else:
                skipped_count += 1
    
    print(f"\n🎉 Fixed {fixed_count} files!")
    print(f"⏭️  Skipped {skipped_count} files (already fixed or no style tag)")
    print("\n✅ Readability fix applied to all carousel assessment files!")

if __name__ == '__main__':
    main()


