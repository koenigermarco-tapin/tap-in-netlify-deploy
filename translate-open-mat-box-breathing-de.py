#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create German translation of open-mat-box-breathing.html
Following translation guidelines: Du-Form, energetic tone, English technical terms
"""

import os
import re

def translate_content():
    """Translate the box breathing file to German"""
    
    if not os.path.exists('open-mat-box-breathing.html'):
        print("❌ open-mat-box-breathing.html not found")
        return
    
    # Read English version
    with open('open-mat-box-breathing.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Translation mappings - Du-Form, energetic, English technical terms
    translations = {
        'lang="en"': 'lang="de"',
        'gym-dashboard.html': 'gym-dashboard-de.html',
        'Back to GYM': '← Zurück zum GYM',
        'Box Breathing for Pressure': 'Box Breathing bei Druck',
        "The Navy SEAL technique for staying calm when everything's on fire": 'Die Navy SEAL-Technik, um ruhig zu bleiben, wenn alles brennt',
        'Before You Start': 'Bevor du startest',
        'This exercise is <strong>safe and effective</strong>, but if you experience dizziness or discomfort, stop immediately and breathe normally.': 'Diese Übung ist <strong>sicher und effektiv</strong>, aber wenn du Schwindel oder Unbehagen verspürst, hör sofort auf und atme normal.',
        'Not a replacement for medical treatment. If you have respiratory conditions, consult your doctor before trying breathing exercises.': 'Kein Ersatz für medizinische Behandlung. Wenn du Atemwegserkrankungen hast, konsultiere deinen Arzt, bevor du Atemübungen ausprobierst.',
        'Why This Works': 'Warum das funktioniert',
        'Box breathing (also called "tactical breathing") activates your <strong>parasympathetic nervous system</strong>—the body\'s natural brake pedal.': 'Box Breathing (auch "taktisches Atmen" genannt) aktiviert dein <strong>parasympathisches Nervensystem</strong>—die natürliche Bremse deines Körpers.',
        "When you're under pressure, your body goes into fight-or-flight:": 'Wenn du unter Druck stehst, geht dein Körper in den Kampf-oder-Flucht-Modus:',
        'Heart rate increases': 'Herzfrequenz steigt',
        'Breathing becomes shallow and rapid': 'Atmung wird flach und schnell',
        'Cortisol floods your system': 'Cortisol überschwemmt dein System',
        'Your prefrontal cortex (rational thinking) goes offline': 'Dein präfrontaler Cortex (rationales Denken) schaltet sich ab',
        'You become reactive instead of responsive': 'Du wirst reaktiv statt responsiv',
        'Box breathing reverses this cascade.': 'Box Breathing kehrt diese Kaskade um.',
        'The Science': 'Die Wissenschaft',
        'Research from the Navy SEAL training program and various university studies shows that controlled breathing:': 'Forschung aus dem Navy SEAL Trainingsprogramm und verschiedenen Universitätsstudien zeigt, dass kontrolliertes Atmen:',
        'Reduces cortisol levels by up to 50%': 'Cortisolspiegel um bis zu 50% reduziert',
        'Lowers heart rate within 60-90 seconds': 'Herzfrequenz innerhalb von 60-90 Sekunden senkt',
        'Increases heart rate variability (marker of stress resilience)': 'Herzfrequenzvariabilität erhöht (Marker für Stress-Resilienz)',
        'Restores prefrontal cortex function (better decision-making)': 'Präfrontalen Cortex wiederherstellt (besseres Entscheiden)',
        'Reduces perceived stress and anxiety': 'Wahrgenommenen Stress und Ängste reduziert',
        'Navy SEALs use this before missions. You can use it before meetings, difficult conversations, presentations, or any high-pressure situation.': 'Navy SEALs nutzen das vor Missionen. Du kannst es vor Meetings, schwierigen Gesprächen, Präsentationen oder jeder Hochdruck-Situation nutzen.',
        'How to Do It': 'Wie du es machst',
        'The 4-4-4-4 Pattern': 'Das 4-4-4-4 Muster',
        'Breathe IN': 'Einatmen',
        'Breathe OUT': 'Ausatmen',
        'HOLD': 'Halten',
        'slowly through your nose for <strong>4 counts</strong>': 'langsam durch die Nase für <strong>4 Zählungen</strong>',
        'your breath for <strong>4 counts</strong>': 'deinen Atem für <strong>4 Zählungen</strong>',
        'slowly through your mouth for <strong>4 counts</strong>': 'langsam durch den Mund für <strong>4 Zählungen</strong>',
        'empty for <strong>4 counts</strong>': 'leer für <strong>4 Zählungen</strong>',
        'REPEAT': 'WIEDERHOLEN',
        'for 4 complete rounds (about 2 minutes)': 'für 4 komplette Runden (etwa 2 Minuten)',
        'Try It Now': 'Probiere es jetzt',
        'Ready': 'Bereit',
        'rounds complete': 'Runden abgeschlossen',
        'Start Exercise': 'Übung starten',
        'Stop': 'Stopp',
        'Tips for Success': 'Tipps zum Erfolg',
        'Find your count:': 'Finde deine Zählung:',
        'If 4 feels too long, try 3. If too short, try 5. The pattern matters more than the number.': 'Wenn 4 sich zu lang anfühlt, probiere 3. Wenn zu kurz, probiere 5. Das Muster ist wichtiger als die Zahl.',
        "Don't force it:": 'Erzwinge es nicht:',
        'Breathe smoothly and naturally. You\'re not trying to fill your lungs completely.': 'Atme sanft und natürlich. Du versuchst nicht, deine Lungen komplett zu füllen.',
        'Focus on the count:': 'Konzentriere dich auf die Zählung:',
        "Counting gives your mind something to do instead of spiraling into anxiety.": 'Zählen gibt deinem Geist etwas zu tun, anstatt in Angst zu versinken.',
        'Practice when calm:': 'Übe, wenn du ruhig bist:',
        "Master this when you're NOT stressed so it's available when you ARE.": 'Meistere das, wenn du NICHT gestresst bist, damit es verfügbar ist, wenn du es BIST.',
        'Use it pre-emptively:': 'Nutze es präventiv:',
        "Don't wait until you're panicking. Use it when you feel pressure building.": 'Warte nicht, bis du in Panik gerätst. Nutze es, wenn du spürst, dass Druck aufbaut.',
        'When to Use Box Breathing': 'Wann du Box Breathing nutzt',
        'Before difficult conversations': 'Vor schwierigen Gesprächen',
        '- Reset your nervous system so you can stay calm': '- Setze dein Nervensystem zurück, damit du ruhig bleiben kannst',
        'During conflict': 'Während Konflikten',
        '- Ask for a 2-minute break, do 4 rounds, return grounded': '- Bitte um eine 2-Minuten-Pause, mache 4 Runden, kehre geerdet zurück',
        'Before presentations': 'Vor Präsentationen',
        '- Backstage, right before you go on': '- Backstage, direkt bevor du auftrittst',
        'When making big decisions': 'Bei großen Entscheidungen',
        '- Clear your head before choosing': '- Kläre deinen Kopf, bevor du wählst',
        'After receiving bad news': 'Nach schlechten Nachrichten',
        '- Process the emotion without spiraling': '- Verarbeite die Emotion, ohne zu versinken',
        'Any time you notice tension': 'Jedes Mal, wenn du Spannung bemerkst',
        '- Shoulders tight? Jaw clenched? Breathe.': '- Schultern verspannt? Kiefer angespannt? Atme.',
        'After You Complete': 'Nach dem Abschluss',
        'How do you feel?': 'Wie fühlst du dich?',
        'Most people notice:': 'Die meisten Menschen bemerken:',
        'Heart rate has slowed': 'Herzfrequenz hat sich verlangsamt',
        'Mind feels clearer': 'Geist fühlt sich klarer an',
        'Shoulders have dropped': 'Schultern sind gesunken',
        'Able to think more strategically': 'Kann strategischer denken',
        "That's not placebo. That's your nervous system shifting from fight-or-flight to rest-and-digest.": 'Das ist kein Placebo. Das ist dein Nervensystem, das von Kampf-oder-Flucht zu Ruhe-und-Verdauung wechselt.',
        'Pro tip:': 'Pro-Tipp:',
        'Bookmark this page. When you\'re stressed, you won\'t remember "box breathing"—but you can click a bookmark.': 'Lesezeichen setzen. Wenn du gestresst bist, wirst du dich nicht an "Box Breathing" erinnern—aber du kannst ein Lesezeichen klicken.',
        'Complete 4 rounds to earn 15 XP': 'Schließe 4 Runden ab, um 15 XP zu verdienen',
        'Mark Complete & Earn XP': 'Als abgeschlossen markieren & XP verdienen',
        'Complete!': 'Abgeschlossen!',
        'Great work! You just regulated your nervous system. Notice how you feel. 🧘': 'Großartige Arbeit! Du hast gerade dein Nervensystem reguliert. Achte darauf, wie du dich fühlst. 🧘',
        'You earned 15 XP! Keep this technique in your back pocket. 💪': 'Du hast 15 XP verdient! Behalte diese Technik in deiner Hinterhand. 💪',
        'Already Completed': 'Bereits abgeschlossen',
    }
    
    # Apply translations
    for eng, ger in translations.items():
        content = content.replace(eng, ger)
    
    # Fix specific patterns
    content = re.sub(r'<title>Box Breathing for Pressure \| TAP-IN Open Mat</title>', 
                     '<title>Box Breathing bei Druck | TAP-IN Open Mat</title>', content)
    
    # Update phases for breathing
    content = re.sub(r"name: 'Breathe IN'", "name: 'Einatmen'", content)
    content = re.sub(r"name: 'Breathe OUT'", "name: 'Ausatmen'", content)
    content = re.sub(r"name: 'HOLD'", "name: 'Halten'", content)
    content = re.sub(r"'Box Breathing Exercise'", "'Box Breathing Übung'", content)
    
    # Update alert messages in JavaScript
    content = re.sub(r"'Great work! You just regulated your nervous system\. Notice how you feel\. 🧘'", 
                     "'Großartige Arbeit! Du hast gerade dein Nervensystem reguliert. Achte darauf, wie du dich fühlst. 🧘'", content)
    content = re.sub(r"'You earned 15 XP! Keep this technique in your back pocket\. 💪'", 
                     "'Du hast 15 XP verdient! Behalte diese Technik in deiner Hinterhand. 💪'", content)
    
    # Save German version
    output_file = 'open-mat-box-breathing-de.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Created {output_file}")
    print(f"   Size: {os.path.getsize(output_file) / 1024:.1f} KB")

if __name__ == '__main__':
    translate_content()

