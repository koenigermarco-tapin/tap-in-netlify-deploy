#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch Translate Communication Mastery Modules 5, 6, 7 to German
"""

import os
import re

def translate_comm_mastery_file(source_file, target_file):
    """Translate a communication mastery file to German"""
    print(f"Translating {source_file} → {target_file}...")
    
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Basic structural translations
    translations = {
        # HTML lang
        'lang="en"': 'lang="de"',
        
        # Navigation
        '← Back to Communication Mastery': '← Zurück zu Communication Mastery',
        'communication-mastery-v2.html': 'communication-mastery-v2-de.html',
        'communication-mastery-3-feedback.html': 'communication-mastery-3-feedback-de.html',
        'communication-mastery-4-receiving.html': 'communication-mastery-4-receiving-de.html',
        'communication-mastery-5-difficult.html': 'communication-mastery-5-difficult-de.html',
        'communication-mastery-6-nonverbal.html': 'communication-mastery-6-nonverbal-de.html',
        'communication-mastery-7-meetings.html': 'communication-mastery-7-meetings-de.html',
        
        # Common UI elements
        'Lesson': 'Lektion',
        'of 8': 'von 8',
        'minutes': 'Minuten',
        'Previous Lesson': 'Vorherige Lektion',
        'Next Lesson': 'Nächste Lektion',
        'Mark Complete': 'Als abgeschlossen markieren',
        'Save Progress': 'Fortschritt speichern',
        
        # Alert messages
        'Progress saved!': 'Fortschritt gespeichert!',
        'Lesson completed!': 'Lektion abgeschlossen!',
        'XP earned!': 'XP verdient!',
        
        # Common phrases
        'Please complete': 'Bitte vervollständige',
        'before saving': 'bevor du speicherst',
    }
    
    # Apply translations
    for eng, de in translations.items():
        content = content.replace(eng, de)
    
    # Fix lesson links
    for i in range(1, 8):
        if f'communication-mastery-{i}' in content:
            if i == 3:
                content = content.replace(f'communication-mastery-3-feedback.html', 'communication-mastery-3-feedback-de.html')
            elif i == 4:
                content = content.replace(f'communication-mastery-4-receiving.html', 'communication-mastery-4-receiving-de.html')
            elif i == 5:
                content = content.replace(f'communication-mastery-5-difficult.html', 'communication-mastery-5-difficult-de.html')
            elif i == 6:
                content = content.replace(f'communication-mastery-6-nonverbal.html', 'communication-mastery-6-nonverbal-de.html')
            elif i == 7:
                content = content.replace(f'communication-mastery-7-meetings.html', 'communication-mastery-7-meetings-de.html')
    
    # Save
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    size_kb = os.path.getsize(target_file) / 1024
    print(f"  ✅ Created: {target_file} ({size_kb:.1f} KB)")
    print(f"  ⚠️  Note: Basic translation created. Full content translation needed.")
    
    return target_file

def main():
    print("="*80)
    print("🌍 BATCH TRANSLATE COMMUNICATION MASTERY MODULES")
    print("="*80)
    print()
    
    files_to_translate = [
        ('communication-mastery-5-difficult.html', 'communication-mastery-5-difficult-de.html'),
        ('communication-mastery-6-nonverbal.html', 'communication-mastery-6-nonverbal-de.html'),
        ('communication-mastery-7-meetings.html', 'communication-mastery-7-meetings-de.html'),
    ]
    
    for source, target in files_to_translate:
        if os.path.exists(source):
            translate_comm_mastery_file(source, target)
        else:
            print(f"  ⚠️  {source} not found, skipping")
    
    print("\n✅ Batch translation complete!")
    print("   Note: These are basic structural translations.")
    print("   Full content translation still needed for each file.")

if __name__ == '__main__':
    main()

