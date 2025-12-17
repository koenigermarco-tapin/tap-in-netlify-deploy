#!/usr/bin/env python3
"""Fix Sie-form to du-form in German assessment file"""

import re
from pathlib import Path

def fix_sie_to_du(filepath):
    """Convert formal Sie-form to informal du-form"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Fix pronouns (careful with plural "sie")
    # Sie (formal you) -> Du (but not "sie sind" which could be plural "they are")
    content = re.sub(r'\bSie\b(?!\s+sind)', 'Du', content)
    
    # Ihre/Ihr (formal your) -> Deine/Dein
    # But keep "Ihr Team" as it might be "your team" (formal) - actually, change to "Dein Team"
    content = re.sub(r'\bIhre\b', 'Deine', content)
    content = re.sub(r'\bIhr\b(?!\s+Team)', 'Dein', content)
    content = re.sub(r'\bIhr Team\b', 'Dein Team', content)
    
    # Ihnen (formal you, dative) -> Dir
    content = re.sub(r'\bIhnen\b', 'Dir', content)
    
    # Fix verb conjugations
    # "tun Sie" -> "tust Du"
    content = re.sub(r'\btun Sie\b', 'tust Du', content)
    content = re.sub(r'\bTun Sie\b', 'Tust Du', content)
    
    # "werden Sie" -> "wirst Du"
    content = re.sub(r'\bwerden Sie\b', 'wirst Du', content)
    content = re.sub(r'\bWerden Sie\b', 'Wirst Du', content)
    
    # "sind Sie" -> "bist Du" (but careful - "Sie sind" could be plural)
    content = re.sub(r'\bsind Sie\b', 'bist Du', content)
    content = re.sub(r'\bSind Sie\b', 'Bist Du', content)
    
    # "haben Sie" -> "hast Du"
    content = re.sub(r'\bhaben Sie\b', 'hast Du', content)
    content = re.sub(r'\bHaben Sie\b', 'Hast Du', content)
    
    # "gehen Sie" -> "gehst Du"
    content = re.sub(r'\bgehen Sie\b', 'gehst Du', content)
    content = re.sub(r'\bGehen Sie\b', 'Gehst Du', content)
    
    # "sind Sie" -> "bist Du" (in questions)
    content = re.sub(r'\bsind Sie\b', 'bist Du', content)
    
    # "tun Sie" -> "tust Du" (in various contexts)
    content = re.sub(r'\btun Sie\b', 'tust Du', content)
    
    # "sich" with Sie -> "Dich" (reflexive)
    # "sich auf einen Weg festlegen" -> "Dich auf einen Weg festlegen" (when with Sie)
    # Actually, "sich" stays "sich" in du-form, but "Sie sich" -> "Du Dich"
    content = re.sub(r'\bSie sich\b', 'Du Dich', content)
    
    # "sich" -> "Dich" when it's clearly reflexive with Sie
    # But be careful - "sich" can be used with du too
    
    # Fix "Ihres/Ihrem" -> "Deines/Deinem"
    content = re.sub(r'\bIhres\b', 'Deines', content)
    content = re.sub(r'\bIhrem\b', 'Deinem', content)
    
    # Fix "Ihren" -> "Deinen"
    content = re.sub(r'\bIhren\b', 'Deinen', content)
    
    # Fix verb endings for du-form
    # "erklären Sie" -> "erklärst Du"
    # "bevorzugen Sie" -> "bevorzugst Du"
    # This is complex - verbs ending in -en with Sie -> -st with Du
    
    # Common patterns:
    # "stehen Sie" -> "stehst Du"
    content = re.sub(r'\bstehen Sie\b', 'stehst Du', content)
    
    # "sagen Sie" -> "sagst Du"  
    content = re.sub(r'\bsagen Sie\b', 'sagst Du', content)
    
    # "würden Sie" -> "würdest Du"
    content = re.sub(r'\bwürden Sie\b', 'würdest Du', content)
    content = re.sub(r'\bWürden Sie\b', 'Würdest Du', content)
    
    # "können Sie" -> "kannst Du"
    content = re.sub(r'\bkönnen Sie\b', 'kannst Du', content)
    content = re.sub(r'\bKönnen Sie\b', 'Kannst Du', content)
    
    # "möchten Sie" -> "möchtest Du"
    content = re.sub(r'\bmöchten Sie\b', 'möchtest Du', content)
    content = re.sub(r'\bMöchten Sie\b', 'Möchtest Du', content)
    
    # "sollten Sie" -> "solltest Du"
    content = re.sub(r'\bsollten Sie\b', 'solltest Du', content)
    
    # "wollen Sie" -> "willst Du"
    content = re.sub(r'\bwollen Sie\b', 'willst Du', content)
    content = re.sub(r'\bWollen Sie\b', 'Willst Du', content)
    
    # "müssen Sie" -> "musst Du"
    content = re.sub(r'\bmüssen Sie\b', 'musst Du', content)
    content = re.sub(r'\bMüssen Sie\b', 'Musst Du', content)
    
    # "dürfen Sie" -> "darfst Du"
    content = re.sub(r'\bdürfen Sie\b', 'darfst Du', content)
    
    # Fix "Ihres/Ihrem" in insights
    # "Das Verstehen Ihres" -> "Das Verstehen Deines"
    content = re.sub(r'\bIhres\b', 'Deines', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Fixed Sie-form in {filepath.name}")
        return True
    else:
        print(f"⚠️  No changes needed in {filepath.name}")
        return False

# Fix the deep-dive assessment
filepath = Path('src/pages/assessments/deep-dive-assessment-de.html')
if filepath.exists():
    fix_sie_to_du(filepath)
    print("\n✅ Sie-form fix complete!")
else:
    print(f"❌ File not found: {filepath}")

