#!/usr/bin/env python3
"""
Script to generate missing belt stripe files from template
Based on brown-belt-stripe1-carousel-NEW.html
"""

import re
import sys

# File mapping: (stripe_number, title, subtitle, theme_description, next_link)
FILES_TO_CREATE = [
    # Brown Belt files
    (2, "Accountability Depth", "Peer Accountability, Resistance & Politics", 
     "Navigate resistance, politics, ambiguous authority, and cultural norms that prevent accountability.",
     "brown-belt-stripe3-carousel-NEW.html"),
    (3, "Accountability Systems", "Structures That Sustain Accountability",
     "Create systems, rituals, and norms that make accountability automatic, not heroic.",
     "brown-belt-stripe4-carousel-NEW.html"),
    (4, "Accountability Mastery", "High Standards Without Fear",
     "Advanced applications of accountability through exercises, scenarios, reflections, and challenges.",
     "brown-belt-assessment.html"),  # Check if this exists
    
    # Black Belt files  
    (1, "Integration", "Synthesize All Prior Learnings",
     "Synthesize all prior learnings into a cohesive leadership philosophy. Ego management and results orientation.",
     "black-belt-stripe2-carousel-NEW.html"),
    (2, "Teaching Others", "Pass On What You've Mastered",
     "Pass on what you've mastered. Collective focus and team goals over ego.",
     "black-belt-stripe3-carousel-NEW.html"),
    (3, "Leadership Philosophy", "Codify Your Approach",
     "Codify your approach. Results obsession and metrics & measurement.",
     "black-belt-stripe4-carousel-NEW.html"),
    (4, "Legacy", "Create Lasting Impact Beyond Yourself",
     "Create lasting impact beyond yourself. Selfless leadership mastery.",
     "learning-hub.html"),  # Final belt
]

def read_template():
    """Read the template file"""
    try:
        with open('brown-belt-stripe1-carousel-NEW.html', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print("ERROR: Template file brown-belt-stripe1-carousel-NEW.html not found!")
        sys.exit(1)

def generate_stripe_file(template, belt_level, stripe_num, title, subtitle, theme_desc, next_link):
    """Generate a new stripe file from template"""
    
    # Determine belt color and stripe name
    if belt_level == 'brown':
        color = '#92400e'
        belt_name = 'Brown Belt'
        emoji = '🟤'
        stripe_key = f'brownBeltStripe{stripe_num}'
        prev_check = f'brownBeltStripe{stripe_num - 1}Complete' if stripe_num > 1 else 'purpleBeltComplete'
    else:  # black
        color = '#000000'
        belt_name = 'Black Belt'
        emoji = '⚫'
        stripe_key = f'blackBeltStripe{stripe_num}'
        prev_check = f'blackBeltStripe{stripe_num - 1}Complete' if stripe_num > 1 else 'brownBeltComplete'
    
    # Replace key content
    content = template
    
    # Title replacements
    content = content.replace('🟤 Brown Belt Stripe 1: Accountability Foundation', 
                              f'{emoji} {belt_name} Stripe {stripe_num}: {title}')
    content = content.replace('meta name="theme-color" content="#92400e"', 
                              f'meta name="theme-color" content="{color}"')
    content = content.replace('Brown Belt - Stripe 1: Accountability Foundation',
                              f'{belt_name} - Stripe {stripe_num}: {title}')
    content = content.replace('Self-Accountability, Standards & Personal Responsibility', subtitle)
    
    # Intro section updates
    content = content.replace('⚖️ Accountability Starts With You', f'⚖️ {title}')
    content = content.replace('Brown Belt teaches you that accountability starts with yourself.',
                              f'{belt_name} teaches you about {title.lower()}.')
    content = content.replace('accountability starts with yourself', title.lower())
    
    # Stripe name replacements
    content = content.replace('brownBeltStripe1', stripe_key)
    content = content.replace('brown-belt-stripe2-carousel-NEW.html', next_link)
    content = content.replace('purpleBeltComplete', prev_check)
    content = content.replace('brownBeltStripe1Complete', f'{stripe_key}Complete')
    
    # Results section
    content = content.replace('Your Accountability Foundation Profile', 
                              f'Your {title} Profile')
    content = content.replace('Brown Belt Stripe 1 Complete!', 
                              f'{belt_name} Stripe {stripe_num} Complete!')
    
    # Update XP reward (200 for Brown, 250 for Black)
    xp_reward = 250 if belt_level == 'black' else 200
    content = content.replace('const xpReward = 200;', f'const xpReward = {xp_reward};')
    
    return content

def main():
    print("🚀 Generating missing belt stripe files...")
    print(f"Files to create: {len(FILES_TO_CREATE)}")
    
    template = read_template()
    print(f"✓ Template loaded ({len(template)} characters)")
    
    # Create Brown Belt files (stripes 2-4)
    for stripe_num, title, subtitle, theme_desc, next_link in FILES_TO_CREATE[:3]:
        filename = f'brown-belt-stripe{stripe_num}-carousel-NEW.html'
        print(f"\n📝 Creating {filename}...")
        
        content = generate_stripe_file(template, 'brown', stripe_num, title, subtitle, theme_desc, next_link)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Created {filename} ({len(content)} characters)")
    
    # Create Black Belt files (stripes 1-4)
    for stripe_num, title, subtitle, theme_desc, next_link in FILES_TO_CREATE[3:]:
        filename = f'black-belt-stripe{stripe_num}-carousel-NEW.html'
        print(f"\n📝 Creating {filename}...")
        
        content = generate_stripe_file(template, 'black', stripe_num, title, subtitle, theme_desc, next_link)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Created {filename} ({len(content)} characters)")
    
    print(f"\n✅ All {len(FILES_TO_CREATE)} files created successfully!")

if __name__ == '__main__':
    main()

