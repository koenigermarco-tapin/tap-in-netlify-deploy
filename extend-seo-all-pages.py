#!/usr/bin/env python3
"""
Extend SEO improvements to all pages
- Add Open Graph tags to all stripe files
- Add structured data to all pages
- Add canonical URLs
"""

from pathlib import Path
import re
import json

def get_page_metadata(filepath):
    """Generate metadata based on filename"""
    
    filename = filepath.name.lower()
    
    # Extract belt and stripe info
    belt_match = re.search(r'(white|blue|purple|brown|black)-belt', filename)
    stripe_match = re.search(r'stripe(\d+)', filename)
    
    if belt_match and stripe_match:
        belt = belt_match.group(1)
        stripe = stripe_match.group(1)
        belt_title = belt.capitalize() + " Belt"
        
        return {
            'title': f'{belt_title} Stripe {stripe} | TAP-IN Leadership Development',
            'description': f'Complete {belt_title} Stripe {stripe} training. Learn leadership skills through embodied practice and progress through the belt system.',
            'og_title': f'{belt_title} Stripe {stripe} Training',
            'og_description': f'Master leadership fundamentals in {belt_title} Stripe {stripe}. Interactive lessons, quizzes, and progress tracking.',
            'type': 'article'
        }
    
    # Assessment pages
    if 'assessment' in filename:
        return {
            'title': f'Assessment | TAP-IN Leadership Development',
            'description': 'Discover your leadership style and current level through comprehensive assessments.',
            'og_title': 'Leadership Assessment | TAP-IN',
            'og_description': 'Take our leadership assessment to discover your strengths and development areas.',
            'type': 'article'
        }
    
    # Default
    return {
        'title': 'TAP-IN Leadership Development',
        'description': 'Transform your leadership through embodied learning. Progress through belt levels and build championship skills.',
        'og_title': 'TAP-IN Leadership Development',
        'og_description': 'Transform teams through embodied leadership training.',
        'type': 'website'
    }

def add_og_tags(content, metadata, filepath):
    """Add Open Graph meta tags"""
    
    base_url = 'https://tap-in-platform.netlify.app'
    canonical_url = f"{base_url}/{filepath.name}"
    
    og_tags = f'''<!-- Open Graph / Facebook -->
<meta property="og:type" content="{metadata.get('type', 'website')}">
<meta property="og:url" content="{canonical_url}">
<meta property="og:title" content="{metadata.get('og_title', metadata.get('title', ''))}">
<meta property="og:description" content="{metadata.get('og_description', metadata.get('description', ''))}">
<meta property="og:image" content="{base_url}/og-image.png">

<!-- Twitter -->
<meta property="twitter:card" content="summary_large_image">
<meta property="twitter:url" content="{canonical_url}">
<meta property="twitter:title" content="{metadata.get('og_title', metadata.get('title', ''))}">
<meta property="twitter:description" content="{metadata.get('og_description', metadata.get('description', ''))}">
<meta property="twitter:image" content="{base_url}/og-image.png">'''
    
    # Check if OG tags already exist
    if 'property="og:type"' in content:
        return content, False
    
    # Find viewport meta tag
    viewport_pattern = r'(<meta[^>]*name="viewport"[^>]*>)'
    
    if re.search(viewport_pattern, content):
        content = re.sub(viewport_pattern, r'\1\n    ' + og_tags, content, count=1)
        return content, True
    
    # Fallback: before </head>
    head_pattern = r'(</head>)'
    if re.search(head_pattern, content):
        content = re.sub(head_pattern, '    ' + og_tags + '\n\1', content, count=1)
        return content, True
    
    return content, False

def add_canonical_url(content, filepath):
    """Add canonical URL"""
    
    base_url = 'https://tap-in-platform.netlify.app'
    canonical_url = f"{base_url}/{filepath.name}"
    canonical_tag = f'<link rel="canonical" href="{canonical_url}">'
    
    if 'rel="canonical"' in content:
        return content, False
    
    head_pattern = r'(</head>)'
    if re.search(head_pattern, content):
        content = re.sub(head_pattern, '    ' + canonical_tag + '\n\1', content, count=1)
        return content, True
    
    return content, False

def add_structured_data(content, metadata, filepath):
    """Add JSON-LD structured data"""
    
    base_url = 'https://tap-in-platform.netlify.app'
    url = f"{base_url}/{filepath.name}"
    
    # Determine type
    filename = filepath.name.lower()
    is_lesson = 'stripe' in filename or 'module' in filename
    is_assessment = 'assessment' in filename
    
    if is_lesson:
        schema = {
            "@context": "https://schema.org",
            "@type": "Course",
            "name": metadata.get('title', ''),
            "description": metadata.get('description', ''),
            "url": url,
            "provider": {
                "@type": "Organization",
                "name": "TAP-IN Leadership Development"
            }
        }
    elif is_assessment:
        schema = {
            "@context": "https://schema.org",
            "@type": "Quiz",
            "name": metadata.get('title', ''),
            "description": metadata.get('description', ''),
            "url": url
        }
    else:
        schema = {
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": metadata.get('title', ''),
            "description": metadata.get('description', ''),
            "url": url
        }
    
    json_ld = f'<script type="application/ld+json">\n{json.dumps(schema, indent=2)}\n</script>'
    
    if 'application/ld+json' in content:
        return content, False
    
    head_pattern = r'(</head>)'
    if re.search(head_pattern, content):
        content = re.sub(head_pattern, '    ' + json_ld + '\n\1', content, count=1)
        return content, True
    
    return content, False

def improve_seo(filepath):
    """Apply SEO improvements to a file"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    metadata = get_page_metadata(filepath)
    
    # 1. Add OG tags
    content, changed = add_og_tags(content, metadata, filepath)
    if changed:
        changes.append("OG tags")
    
    # 2. Add canonical
    content, changed = add_canonical_url(content, filepath)
    if changed:
        changes.append("canonical URL")
    
    # 3. Add structured data
    content, changed = add_structured_data(content, metadata, filepath)
    if changed:
        changes.append("structured data")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes
    
    return False, []

def main():
    print("=" * 80)
    print("🔍 EXTENDING SEO TO ALL PAGES")
    print("=" * 80)
    print()
    
    # Find all stripe files
    stripe_files = list(Path('.').glob('*-stripe*-gamified.html'))
    stripe_files.sort()
    
    # Find assessment files
    assessment_files = list(Path('.').glob('*-assessment*.html'))
    assessment_files = [f for f in assessment_files if 'de.html' not in f.name]
    assessment_files.sort()
    
    # Find module files
    module_files = list(Path('.').glob('*-module*.html'))
    module_files.sort()
    
    all_files = stripe_files + assessment_files + module_files
    all_files = [f for f in all_files if f.exists()]
    
    print(f"Found {len(all_files)} files to update\n")
    
    updated = 0
    skipped = 0
    
    for filepath in all_files:
        print(f"📝 {filepath.name}...")
        try:
            success, changes = improve_seo(filepath)
            if success:
                updated += 1
                print(f"  ✅ Added: {', '.join(changes)}")
            else:
                skipped += 1
                print(f"  ⏭️  Already has SEO tags")
        except Exception as e:
            print(f"  ❌ Error: {e}")
        print()
    
    print("=" * 80)
    print(f"✅ Updated: {updated}/{len(all_files)}")
    print(f"⏭️  Skipped: {skipped}")
    print("=" * 80)

if __name__ == '__main__':
    main()

