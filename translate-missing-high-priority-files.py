#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate Missing High Priority German Files
Starts with open-mat-inner-game-leadership-de.html
"""

import os
import re

def translate_open_mat_inner_game():
    """Translate open-mat-inner-game-leadership.html to German"""
    print("="*80)
    print("🌍 TRANSLATING: open-mat-inner-game-leadership-de.html")
    print("="*80)
    print()
    
    # Read English file
    with open('open-mat-inner-game-leadership.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Basic translations
    translations = {
        # HTML lang
        'lang="en"': 'lang="de"',
        
        # Title
        'The Inner Game of Leadership | TAP-IN Open Mat': 'Das Innere Spiel der Führung | TAP-IN Open Mat',
        
        # Header
        '← Back to GYM': '← Zurück zum GYM',
        'gym-dashboard.html': 'gym-dashboard-de.html',
        
        # Article meta
        'Featured': 'Featured',
        '📖 Article': '📖 Artikel',
        '⏱️ 8 min read': '⏱️ 8 Min. Lesezeit',
        '🎯 White Belt': '🎯 White Belt',
        
        # Title and subtitle
        'The Inner Game of Leadership': 'Das Innere Spiel der Führung',
        'Why your self-talk determines your ceiling': 'Warum dein Selbstgespräch deine Obergrenze bestimmt',
        
        # Content translations (first section)
        "You're playing two games at once.": "Du spielst zwei Spiele gleichzeitig.",
        "Game 1: The Outer Game": "Spiel 1: Das Äußere Spiel",
        "The strategy you execute. The decisions you make. The results you deliver. The things everyone can see.": 
            "Die Strategie, die du ausführst. Die Entscheidungen, die du triffst. Die Ergebnisse, die du lieferst. Die Dinge, die jeder sehen kann.",
        "Game 2: The Inner Game": "Spiel 2: Das Innere Spiel",
        "The conversation in your head. The doubts you battle. The fear you manage. The things no one sees.": 
            "Das Gespräch in deinem Kopf. Die Zweifel, mit denen du kämpfst. Die Angst, die du verwaltest. Die Dinge, die niemand sieht.",
        
        # Completion section
        'Complete this article to earn 25 XP': 'Schließe diesen Artikel ab, um 25 XP zu verdienen',
        'Mark Complete & Earn XP': 'Als abgeschlossen markieren & XP verdienen',
        '✓ Complete! (+25 XP)': '✓ Abgeschlossen! (+25 XP)',
        '✓ Already Completed': '✓ Bereits abgeschlossen',
        'Great work! You earned 25 XP. Keep going! 💪': 'Großartige Arbeit! Du hast 25 XP verdient. Weiter so! 💪',
    }
    
    # Apply translations
    for eng, de in translations.items():
        content = content.replace(eng, de)
    
    # More complex translations
    content = re.sub(
        r'What the Research Shows',
        'Was die Forschung zeigt',
        content
    )
    
    content = re.sub(
        r'The Inner Game in Leadership',
        'Das Innere Spiel in der Führung',
        content
    )
    
    content = re.sub(
        r'How to Upgrade Your Inner Game',
        'Wie du dein Inneres Spiel verbesserst',
        content
    )
    
    content = re.sub(
        r'Practice This Today',
        'Übe dies heute',
        content
    )
    
    content = re.sub(
        r'The Bottom Line',
        'Das Wichtigste',
        content
    )
    
    # Save German version
    output_file = 'open-mat-inner-game-leadership-de.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    size_kb = os.path.getsize(output_file) / 1024
    print(f"✅ Created: {output_file} ({size_kb:.1f} KB)")
    print(f"\n⚠️  NOTE: This is a basic translation. Full content translation needed.")
    print(f"    Please review and complete the translation following guidelines.")
    
    return output_file

if __name__ == '__main__':
    translate_open_mat_inner_game()

