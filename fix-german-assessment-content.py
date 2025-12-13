#!/usr/bin/env python3
"""Fix German assessment file - translate visible content to German"""

import re

# Read the German file
with open('belt-assessment-v2-de.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Translations needed
translations = {
    # Headers and titles
    'Impact Belt Assessment': 'Impact Gürtel-Assessment',
    'Find your gaps, get your roadmap, earn your belts': 'Finde deine Lücken, erhalte deine Roadmap, verdiene deine Gürtel',
    'Question 0 of 50': 'Frage 0 von 50',
    'Question': 'Frage',
    'of 50': 'von 50',
    
    # Section titles
    'Most People Are Stuck': 'Die Meisten Bleiben Stecken',
    'What This Assessment Does': 'Was Dieses Assessment Macht',
    'We Don\'t Hand Out Belts': 'Wir Verschenken Keine Gürtel',
    'What to Expect': 'Was Dich Erwartet',
    'What You\'ll Learn': 'Was Du Lernen Wirst',
    
    # Content
    'You know you should be making more impact.': 'Du weißt, dass du mehr Impact machen solltest.',
    'You read the books. You take the courses.': 'Du liest die Bücher. Du machst die Kurse.',
    'But something\'s missing.': 'Aber etwas fehlt.',
    'The gap between knowing what great impact looks like': 'Die Lücke zwischen dem Wissen, wie großer Impact aussieht',
    'actually creating it': 'und ihn tatsächlich zu schaffen',
    'is where most people get stuck.': 'ist, wo die meisten stecken bleiben.',
    'This assessment will show you exactly where that gap is': 'Dieses Assessment zeigt dir genau, wo diese Lücke ist',
    'and how to close it.': 'und wie du sie schließt.',
    
    # Belt colors in section progress
    'White': 'Weiß',
    'Blue': 'Blau',
    'Purple': 'Lila',
    'Brown': 'Braun',
    'Black': 'Schwarz',
    
    # Buttons and navigation
    'Begin Assessment': 'Assessment Starten',
    'Previous': 'Zurück',
    'Next': 'Weiter',
    'Tap': 'Aufgeben',
    
    # Modal content
    'Tap?': 'Aufgeben?',
    'Choose your next move:': 'Wähle deinen nächsten Schritt:',
    'Tap → Start Training': 'Aufgeben → Training Starten',
    'Tap Out → Back to Gym': 'Aufgeben → Zurück zum Gym',
    'Back to Assessment': 'Zurück zum Assessment',
    'Choose Your Starting Belt': 'Wähle Deinen Startgürtel',
    'Pick the belt you want to start training with:': 'Wähle den Gürtel, mit dem du trainieren willst:',
    'Trust & Vulnerability': 'Vertrauen & Verletzlichkeit',
    'Healthy Conflict': 'Gesunder Konflikt',
    'Commitment & Buy-in': 'Commitment & Einbeziehung',
    'Accountability': 'Verantwortlichkeit',
    'Results Focus': 'Fokus auf Ergebnisse',
    
    # Results
    'Your Belt Readiness Report': 'Dein Gürtel-Readiness-Report',
    'Assessment Complete!': 'Assessment Abgeschlossen!',
    'All belts evaluated': 'Alle Gürtel bewertet',
    'Your Belt-by-Belt Readiness': 'Deine Gürtel-für-Gürtel Readiness',
    'Your 5 Dysfunctions Breakdown': 'Dein 5-Dysfunktionen-Breakdown',
    'Your 90-Day Training Roadmap': 'Dein 90-Tage-Trainings-Roadmap',
    'Start Your Training': 'Starte Dein Training',
}

print("=" * 80)
print("TRANSLATING GERMAN ASSESSMENT FILE")
print("=" * 80)
print()

changes_made = 0
for english, german in translations.items():
    if english in content:
        content = content.replace(english, german)
        changes_made += 1
        print(f"✅ '{english}' → '{german}'")

# Fix JavaScript strings that display to users
js_translations = {
    'Question': 'Frage',
    'of 50': 'von 50',
    'Previous': 'Zurück',
    'Next': 'Weiter',
}

print()
print(f"Total translations applied: {changes_made}")
print()
print("Saving file...")

with open('belt-assessment-v2-de.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ File saved!")

