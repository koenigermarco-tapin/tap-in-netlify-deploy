#!/usr/bin/env python3
"""
Script to apply upgrades to remaining stripe files
This will be used as a reference - actual changes done via search_replace
"""

REMAINING_FILES = [
    'blue-belt-stripe2-carousel-NEW.html',
    'blue-belt-stripe3-carousel-NEW.html',
    'blue-belt-stripe4-carousel-NEW.html',
    'purple-belt-stripe1-carousel-NEW.html',
    'purple-belt-stripe2-carousel-NEW.html',
    'purple-belt-stripe3-carousel-NEW.html',
    'purple-belt-stripe4-carousel-NEW.html',
    'brown-belt-stripe1-carousel-NEW.html'
]

print(f"Remaining files to upgrade: {len(REMAINING_FILES)}")
print("Files:", REMAINING_FILES)


