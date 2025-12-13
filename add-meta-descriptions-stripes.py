#!/usr/bin/env python3
"""
Add meta description tags to all stripe files
"""

import os
import re

# Stripe descriptions
STRIPE_DESCRIPTIONS = {
    'white-belt-stripe1-gamified.html': 'Master leadership fundamentals in White Belt Stripe 1: Trust Foundations. Interactive lessons, quizzes, and progress tracking for developing core leadership skills.',
    'white-belt-stripe2-gamified.html': 'Learn vulnerability and authentic leadership in White Belt Stripe 2. Interactive lessons on building trust through openness and genuine connection.',
    'white-belt-stripe3-gamified.html': 'Develop team trust and collaboration skills in White Belt Stripe 3. Interactive lessons on creating psychological safety and cohesive teams.',
    'white-belt-stripe4-gamified.html': 'Master self-awareness and emotional intelligence in White Belt Stripe 4. Interactive lessons on understanding yourself to lead others effectively.',
    
    'blue-belt-stripe1-gamified.html': 'Learn to handle difficult conversations with confidence in Blue Belt Stripe 1. Master the STATE framework for productive conflict resolution.',
    'blue-belt-stripe2-gamified.html': 'Develop active listening skills in Blue Belt Stripe 2. Learn to truly understand others and create deeper connections in leadership.',
    'blue-belt-stripe3-gamified.html': 'Master feedback systems and Radical Candor in Blue Belt Stripe 3. Learn to give honest, caring feedback that drives growth.',
    'blue-belt-stripe4-gamified.html': 'Set and maintain healthy boundaries in Blue Belt Stripe 4. Learn to protect your energy and create sustainable leadership practices.',
    
    'purple-belt-stripe1-gamified.html': 'Create shared goals and alignment in Purple Belt Stripe 1. Learn OKR frameworks and strategic goal-setting for high-performing teams.',
    'purple-belt-stripe2-gamified.html': 'Master healthy conflict and productive disagreement in Purple Belt Stripe 2. Turn tension into innovation and stronger decisions.',
    'purple-belt-stripe3-gamified.html': 'Build collective accountability in Purple Belt Stripe 3. Learn to create systems where teams hold each other to high standards.',
    'purple-belt-stripe4-gamified.html': 'Drive results and execution excellence in Purple Belt Stripe 4. Learn to focus on outcomes and deliver consistent performance.',
    
    'brown-belt-stripe1-gamified.html': 'Develop systems thinking and strategic leadership in Brown Belt Stripe 1. Learn to see patterns, connections, and long-term implications.',
    'brown-belt-stripe2-gamified.html': 'Design organizational culture and values in Brown Belt Stripe 2. Create environments where people thrive and perform at their best.',
    'brown-belt-stripe3-gamified.html': 'Master strategic leadership and vision in Brown Belt Stripe 3. Learn to set direction and inspire organizations toward ambitious goals.',
    'brown-belt-stripe4-gamified.html': 'Lead transformation and change management in Brown Belt Stripe 4. Master Kotter\'s framework for successful organizational change.',
    
    'black-belt-stripe1-gamified.html': 'Integrate all leadership skills in Black Belt Stripe 1. Synthesize lessons learned and create your unique leadership philosophy.',
    'black-belt-stripe2-gamified.html': 'Teach and develop other leaders in Black Belt Stripe 2. Learn to multiply your impact through coaching and mentorship.',
    'black-belt-stripe3-gamified.html': 'Articulate your leadership philosophy in Black Belt Stripe 3. Define your values, principles, and approach to leading others.',
    'black-belt-stripe4-gamified.html': 'Build lasting legacy and impact in Black Belt Stripe 4. Learn to create systems and culture that outlive your direct leadership.',
}

def add_meta_description(filepath, description):
    """Add meta description tag to HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ❌ Error reading {filepath}: {e}")
        return False
    
    # Check if meta description already exists
    if 'meta name="description"' in content:
        print(f"  ⚠️  {os.path.basename(filepath)} already has meta description")
        return False
    
    # Find where to insert (before Open Graph tags or after viewport)
    pattern = r'(<meta name="viewport"[^>]*>)\s*'
    
    # Insert meta description after viewport
    replacement = rf'\1\n    <meta name="description" content="{description}">'
    
    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content, count=1)
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"  ❌ Error writing {filepath}: {e}")
            return False
    
    # Fallback: insert before Open Graph tags
    pattern2 = r'(<!-- Open Graph / Facebook -->)'
    replacement2 = f'    <meta name="description" content="{description}">\n    \n    \\1'
    
    if re.search(pattern2, content):
        content = re.sub(pattern2, replacement2, content, count=1)
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"  ❌ Error writing {filepath}: {e}")
            return False
    
    print(f"  ⚠️  Could not find insertion point in {os.path.basename(filepath)}")
    return False

def main():
    """Main function"""
    print("=" * 80)
    print("📝 ADDING META DESCRIPTIONS TO STRIPE FILES")
    print("=" * 80)
    print()
    
    updated = 0
    skipped = 0
    errors = 0
    
    for filename, description in STRIPE_DESCRIPTIONS.items():
        filepath = os.path.join('.', filename)
        
        if not os.path.exists(filepath):
            print(f"  ⚠️  {filename} not found, skipping")
            skipped += 1
            continue
        
        print(f"📄 Processing: {filename}")
        
        if add_meta_description(filepath, description):
            print(f"  ✅ Added meta description")
            updated += 1
        else:
            skipped += 1
    
    print()
    print("=" * 80)
    print(f"✅ COMPLETE: Updated {updated} files, Skipped {skipped} files, Errors {errors}")
    print("=" * 80)

if __name__ == '__main__':
    main()

