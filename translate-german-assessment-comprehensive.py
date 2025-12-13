#!/usr/bin/env python3
"""Comprehensive German translation for belt-assessment-v2-de.html"""

import re

with open('belt-assessment-v2-de.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("=" * 80)
print("COMPREHENSIVE GERMAN TRANSLATION")
print("=" * 80)
print()

# Comprehensive translations
translations = [
    # Header
    ('Impact Belt Assessment', 'Impact Gürtel-Assessment'),
    ('Find your gaps, get your roadmap, earn your belts', 'Finde deine Lücken, erhalte deine Roadmap, verdiene deine Gürtel'),
    
    # Progress
    ('Question 0 of 50', 'Frage 0 von 50'),
    ('Question', 'Frage'),
    ('of 50', 'von 50'),
    
    # Section titles
    ('Most People Are Stuck', 'Die Meisten Bleiben Stecken'),
    ('What This Assessment Does', 'Was Dieses Assessment Macht'),
    ('We Don\'t Hand Out Belts', 'Wir Verschenken Keine Gürtel'),
    ('What to Expect', 'Was Dich Erwartet'),
    ('What You\'ll Learn', 'Was Du Lernen Wirst'),
    
    # Content - intro section
    ('You know you should be making more impact. You read the books. You take the courses. But something\'s missing.', 
     'Du weißt, dass du mehr Impact machen solltest. Du liest die Bücher. Du machst die Kurse. Aber etwas fehlt.'),
    
    ('The gap between knowing what great impact looks like and <em>actually creating it</em> is where most people get stuck.',
     'Die Lücke zwischen dem Wissen, wie großer Impact aussieht, und <em>ihn tatsächlich zu schaffen</em> ist, wo die meisten stecken bleiben.'),
    
    ('This assessment will show you exactly where that gap is—and how to close it.',
     'Dieses Assessment zeigt dir genau, wo diese Lücke ist—und wie du sie schließt.'),
    
    # What this assessment does
    ('In 15 minutes, you\'ll get a comprehensive analysis of your impact potential across 5 critical dimensions:',
     'In 15 Minuten erhältst du eine umfassende Analyse deines Impact-Potenzials über 5 kritische Dimensionen:'),
    
    ('Can you be vulnerable and build real connections?',
     'Kannst du verletzlich sein und echte Verbindungen aufbauen?'),
    
    ('Do you avoid or engage in healthy debate?',
     'Vermeidest du gesunde Debatten oder gehst du sie ein?'),
    
    ('Do you follow through and inspire buy-in?',
     'Hältst du durch und inspirierst Buy-in?'),
    
    ('Do you hold yourself (and others) to standards?',
     'Hältst du dich (und andere) an Standards?'),
    
    ('Does real impact matter more than looking good?',
     'Ist echter Impact wichtiger als gut auszusehen?'),
    
    ('You won\'t just get a label. You\'ll get a personalized roadmap showing exactly what you need to work on to increase your impact.',
     'Du bekommst nicht nur ein Label. Du bekommst eine personalisierte Roadmap, die genau zeigt, woran du arbeiten musst, um deinen Impact zu erhöhen.'),
    
    # Belt philosophy
    ('"A black belt is just a white belt who never gave up."',
     '"Ein Schwarzgurt ist nur ein Weißgurt, der nie aufgegeben hat."'),
    
    ('In Brazilian Jiu-Jitsu, you earn belts through demonstrated mastery—not time served.',
     'Im brasilianischen Jiu-Jitsu verdienst du Gürtel durch demonstrierte Meisterschaft—nicht durch Zeit.'),
    
    ('A purple belt isn\'t "better" than a white belt. They\'ve just mastered different techniques.',
     'Ein Lila-Gurt ist nicht "besser" als ein Weißgurt. Sie haben nur verschiedene Techniken gemeistert.'),
    
    ('This assessment is rigorous. Scoring 60% in Purple Belt doesn\'t unlock it—it shows you what you need to work on before you\'re ready.',
     'Dieses Assessment ist rigoros. 60% im Lila-Gurt-Bereich schaltet ihn nicht frei—es zeigt dir, woran du arbeiten musst, bevor du bereit bist.'),
    
    ('We\'ll tell you exactly what exercises and modules you need to complete first.',
     'Wir sagen dir genau, welche Übungen und Module du zuerst abschließen musst.'),
    
    ('Mastery over speed. Depth over breadth. Real growth over fake credentials.',
     'Meisterschaft über Geschwindigkeit. Tiefe über Breite. Echtes Wachstum über falsche Credentials.'),
    
    # What to expect
    ('50 questions across 5 belt levels', '50 Fragen über 5 Gürtel-Level'),
    ('10 questions per belt', '10 Fragen pro Gürtel'),
    ('Time:', 'Zeit:'),
    ('12-15 minutes', '12-15 Minuten'),
    ('Question types:', 'Fragetypen:'),
    ('Real scenarios, self-assessments, tough choices', 'Echte Szenarien, Selbstbewertungen, schwere Entscheidungen'),
    ('Honesty required:', 'Ehrlichkeit erforderlich:'),
    ('Choose what you <em>actually do</em>, not what you wish you did.',
     'Wähle, was du <em>tatsächlich tust</em>, nicht was du dir wünschst zu tun.'),
    ('The assessment only works if you\'re brutally honest.',
     'Das Assessment funktioniert nur, wenn du brutal ehrlich bist.'),
    
    # Belt colors
    ('White', 'Weiß'),
    ('Blue', 'Blau'),
    ('Purple', 'Lila'),
    ('Brown', 'Braun'),
    ('Black', 'Schwarz'),
    
    # Buttons
    ('Begin Assessment', 'Assessment Starten'),
    ('Previous', 'Zurück'),
    ('Next', 'Weiter'),
    ('Tap', 'Aufgeben'),
    
    # Results
    ('Your Belt Readiness Report', 'Dein Gürtel-Readiness-Report'),
    ('Rigorous Standards. Real Gaps. Clear Path Forward.', 'Rigorose Standards. Echte Lücken. Klarer Weg vorwärts.'),
    ('Assessment Complete!', 'Assessment Abgeschlossen!'),
    ('All belts evaluated', 'Alle Gürtel bewertet'),
    ('Your Belt-by-Belt Readiness', 'Deine Gürtel-für-Gürtel Readiness'),
    ('Your 5 Dysfunctions Breakdown', 'Dein 5-Dysfunktionen-Breakdown'),
    ('Your 90-Day Training Roadmap', 'Dein 90-Tage-Trainings-Roadmap'),
    ('Start Your Training', 'Starte Dein Training'),
]

changes = 0
for eng, de in translations:
    if eng in content:
        content = content.replace(eng, de)
        changes += 1
        print(f"✅ Translated: {eng[:50]}...")

print()
print(f"Total translations: {changes}")

# Also need to translate JavaScript strings
js_translations = [
    ('Question ', 'Frage '),
    (' of 50', ' von 50'),
    ('Previous', 'Zurück'),
    ('Next', 'Weiter'),
]

print()
print("Translating JavaScript strings...")
for eng, de in js_translations:
    # Replace in string literals
    content = re.sub(rf'(["\']){re.escape(eng)}\1', rf'\1{de}\1', content)
    changes += 1

print(f"Total changes: {changes}")

with open('belt-assessment-v2-de.html', 'w', encoding='utf-8') as f:
    f.write(content)

print()
print("✅ File saved!")

