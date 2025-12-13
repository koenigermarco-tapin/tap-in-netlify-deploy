#!/usr/bin/env python3
"""
Create German versions of Sales Recruiting Assessment files
"""

from pathlib import Path
import re

def create_german_stage1():
    """Create sales-recruiting-stage1-de.html"""
    base_file = Path('sales-recruiting-stage1.html')
    output_file = Path('sales-recruiting-stage1-de.html')
    
    content = base_file.read_text(encoding='utf-8', errors='ignore')
    
    # Change lang to de
    content = content.replace('<html lang="en">', '<html lang="de">')
    
    # Update title and meta
    content = re.sub(
        r'<title>.*?</title>',
        r'<title>Sales Profil Assessment - Stufe 1 | TAP-IN Recruiting</title>',
        content
    )
    
    content = re.sub(
        r'property="og:title" content="[^"]*"',
        r'property="og:title" content="Sales Rekrutierungs-Assessment - Stufe 1"',
        content
    )
    
    # Update header
    content = content.replace(
        '🎯 Sales Profile Assessment - Stage 1',
        '🎯 Sales Profil Assessment - Stufe 1'
    )
    
    # Update intro section
    intro_text = '''<div class="intro-section" id="introSection" style="background: #f8fafc; padding: 25px; border-radius: 12px; margin-bottom: 30px; border-left: 4px solid #1a365d;">
            <h3 style="color: #1e293b; margin-bottom: 15px; font-weight: 600;">📋 Was dich erwartet</h3>
            <p style="color: #64748b; line-height: 1.7; margin-bottom: 15px;">
                Dieses kurze Assessment hilft uns zu bestimmen, ob es eine starke initiale Übereinstimmung 
                zwischen deinem natürlichen Arbeitsstil und unserer Sales-Rolle gibt. Dauert 3 Minuten.
            </p>
            <p style="color: #64748b; line-height: 1.7; margin-bottom: 20px;">
                <strong>Qualifizierte Kandidaten gehen zu Stufe 2</strong> (10-minütiges detailliertes Profil).
            </p>
            
            <div style="text-align: center; margin-top: 25px;">
                <button class="btn btn-primary" onclick="startAssessment()" style="font-size: 1.2em; padding: 18px 40px;">
                    Assessment starten →
                </button>
            </div>
        </div>'''
    
    content = re.sub(
        r'<div class="intro-section"[^>]*>.*?</div>\s*</div>',
        intro_text,
        content,
        flags=re.DOTALL
    )
    
    # Update progress text
    content = content.replace('Question 1 of 10', 'Frage 1 von 10')
    content = content.replace('Question ${currentQuestion + 1} of ${questions.length}', 
                              'Frage ${currentQuestion + 1} von ${questions.length}')
    
    # Translate questions
    questions_translations = {
        "In sales, I perform best with:": "Im Sales performe ich am besten mit:",
        "Fast-paced, quick wins (sprinter)": "Schnelles Tempo, schnelle Erfolge (Sprinter)",
        "Steady rhythm, consistent pipeline (jogger)": "Stetiger Rhythmus, konsistenter Pipeline (Jogger)",
        "Long relationship building (ultra)": "Langfristiger Relationship-Aufbau (Ultrarunner)",
        "My ideal sales cycle is:": "Mein idealer Sales Cycle ist:",
        "1-2 weeks (short)": "1-2 Wochen (kurz)",
        "1-3 months (medium)": "1-3 Monate (mittel)",
        "6+ months (long)": "6+ Monate (lang)",
        "When presenting to potential clients, I naturally:": "Bei Präsentationen vor potenziellen Kunden:",
        "Confidently guide the conversation (assertive)": "Führe selbstbewusst das Gespräch (assertiv)",
        "Listen carefully and adapt (empathetic)": "Höre genau zu und passe mich an (empathetisch)",
        "Present data and facts (analytical)": "Präsentiere Daten und Fakten (analytisch)",
        "After hearing 'no' from a prospect, I typically:": "Nach einem 'Nein' von einem Prospect:",
        "Move to the next opportunity immediately": "Wechsle sofort zur nächsten Gelegenheit",
        "Review what went wrong briefly": "Analysiere kurz, was schiefgelaufen ist",
        "Need time to recharge": "Brauche Zeit zum Aufladen",
        "What excites me most about sales is:": "Am meisten begeistert mich am Sales:",
        "Hitting targets and winning": "Ziele erreichen und gewinnen",
        "Helping customers solve problems": "Kunden helfen, Probleme zu lösen",
        "Building long-term relationships": "Langfristige Beziehungen aufbauen",
        "In a competitive sales environment, I:": "In einer wettbewerbsorientierten Sales-Umgebung:",
        "Thrive and push to be #1": "Gedeihe und strebe nach Platz #1",
        "Perform well but prefer collaboration": "Leiste gut, bevorzuge aber Zusammenarbeit",
        "Feel stressed by competition": "Fühle mich durch Wettbewerb gestresst",
        "When it's time to close, I:": "Wenn es Zeit ist zu closen:",
        "Directly ask for the commitment": "Frage direkt nach dem Commitment",
        "Guide them to the decision gently": "Führe sie sanft zur Entscheidung",
        "Present the logical next step": "Präsentiere den logischen nächsten Schritt",
        "My ideal prospecting approach is:": "Mein idealer Prospecting-Ansatz ist:",
        "High volume, many calls daily": "Hohes Volumen, viele Calls täglich",
        "Targeted, consistent outreach": "Zielgerichteter, konsistenter Outreach",
        "Deep research, few perfect calls": "Tiefe Recherche, wenige perfekte Calls",
        "My energy at work is typically:": "Meine Energie bei der Arbeit ist typischerweise:",
        "High bursts, need variety": "Hohe Energie-Bursts, brauche Abwechslung",
        "Steady and predictable": "Stetig und vorhersehbar",
        "Deep focus for long periods": "Tiefe Konzentration über längere Zeit",
        "When I lose a big deal to a competitor:": "Wenn ich ein großes Deal an einen Competitor verliere:",
        "Analyze quickly and win the next one": "Analysiere schnell und gewinne das nächste",
        "Feel frustrated but recover": "Fühle mich frustriert, erhole mich aber",
        "Question my approach": "Stelle meinen Ansatz in Frage"
    }
    
    for en, de in questions_translations.items():
        content = content.replace(en, de)
    
    # Translate buttons and UI
    content = content.replace('← Previous', '← Zurück')
    content = content.replace('Next →', 'Weiter →')
    content = content.replace('See Results →', 'Ergebnisse anzeigen →')
    content = content.replace('Start Assessment →', 'Assessment starten →')
    
    # Translate results section
    content = content.replace('Your Stage 1 Results', 'Deine Stufe 1 Ergebnisse')
    content = content.replace('out of 100', 'von 100')
    content = content.replace('Next Steps', 'Nächste Schritte')
    content = content.replace('Strong potential match! Please proceed to Stage 2.', 
                             'Starke potenzielle Übereinstimmung! Bitte gehe zu Stufe 2.')
    content = content.replace('Promising profile. We\'ll review your CV and be in touch.', 
                             'Vielversprechendes Profil. Wir prüfen deinen Lebenslauf und melden uns.')
    content = content.replace('Some strengths shown. We\'ll review carefully.', 
                             'Einige Stärken erkennbar. Wir prüfen sorgfältig.')
    content = content.replace('Thank you for your interest. Your profile doesn\'t closely match this role.', 
                             'Vielen Dank für dein Interesse. Dein Profil passt nicht eng zu dieser Rolle.')
    content = content.replace('Proceed to Stage 2 Assessment →', 
                             'Zu Stufe 2 Assessment →')
    content = content.replace('Score Breakdown', 'Score-Aufschlüsselung')
    content = content.replace('Work Style', 'Arbeitsstil')
    content = content.replace('Communication', 'Kommunikation')
    content = content.replace('Motivation', 'Motivation')
    content = content.replace('Resilience', 'Resilienz')
    content = content.replace('← Back to Business Portal', '← Zurück zum Business Portal')
    
    # Translate recommendation badges
    content = content.replace('EXCELLENT FIT', 'HERVORRAGENDE PASSUNG')
    content = content.replace('GOOD FIT', 'GUTE PASSUNG')
    content = content.replace('MAYBE', 'MÖGLICHERWEISE')
    content = content.replace('NOT RECOMMENDED', 'NICHT EMPFOHLEN')
    
    # Add language switcher
    lang_switcher = '''    <!-- language switcher (DE / EN) -->
    <div id="lang-switch" style="position:fixed;top:16px;right:16px;z-index:1200;font-family:inherit;">
        <div style="background:white;border-radius:999px;padding:8px 12px;box-shadow:0 6px 20px rgba(0,0,0,0.15);font-size:0.95em;">
            <a href="sales-recruiting-stage1.html" style="color:#64748b;text-decoration:none;font-weight:700;margin-right:10px;">EN</a>
            <a href="sales-recruiting-stage1-de.html" style="color:#1a365d;text-decoration:none;font-weight:700;border-left:1px solid #eee;padding-left:10px;margin-left:10px;">DE</a>
        </div>
    </div>

'''
    
    body_start = content.find('<body>')
    if body_start > 0:
        content = content[:body_start + 6] + lang_switcher + content[body_start + 6:]
    
    # Also add to English version
    en_file = Path('sales-recruiting-stage1.html')
    en_content = en_file.read_text(encoding='utf-8', errors='ignore')
    en_switcher = '''    <!-- language switcher (EN / DE) -->
    <div id="lang-switch" style="position:fixed;top:16px;right:16px;z-index:1200;font-family:inherit;">
        <div style="background:white;border-radius:999px;padding:8px 12px;box-shadow:0 6px 20px rgba(0,0,0,0.15);font-size:0.95em;">
            <a href="sales-recruiting-stage1.html" style="color:#1a365d;text-decoration:none;font-weight:700;margin-right:10px;">EN</a>
            <a href="sales-recruiting-stage1-de.html" style="color:#64748b;text-decoration:none;font-weight:700;border-left:1px solid #eee;padding-left:10px;margin-left:10px;">DE</a>
        </div>
    </div>

'''
    
    en_body_start = en_content.find('<body>')
    if en_body_start > 0 and 'lang-switch' not in en_content:
        en_content = en_content[:en_body_start + 6] + en_switcher + en_content[en_body_start + 6:]
        en_file.write_text(en_content, encoding='utf-8')
    
    output_file.write_text(content, encoding='utf-8')
    print("✅ Created sales-recruiting-stage1-de.html")

def create_german_stage2():
    """Create sales-recruiting-stage2-de.html"""
    # For now, create a placeholder - can be expanded later
    base_file = Path('sales-recruiting-stage2.html')
    if base_file.exists():
        output_file = Path('sales-recruiting-stage2-de.html')
        content = base_file.read_text(encoding='utf-8', errors='ignore')
        content = content.replace('<html lang="en">', '<html lang="de">')
        content = content.replace('Sales Profile Assessment - Stage 2', 'Sales Profil Assessment - Stufe 2')
        output_file.write_text(content, encoding='utf-8')
        print("✅ Created sales-recruiting-stage2-de.html (placeholder)")
    else:
        print("⚠️  sales-recruiting-stage2.html not found - skipping")

def create_german_demo():
    """Create sales-recruiting-demo-de.html"""
    # For now, create a placeholder
    base_file = Path('sales-recruiting-demo.html')
    if base_file.exists():
        output_file = Path('sales-recruiting-demo-de.html')
        content = base_file.read_text(encoding='utf-8', errors='ignore')
        content = content.replace('<html lang="en">', '<html lang="de">')
        content = content.replace('Sales Candidate Comparison', 'Sales Kandidaten-Vergleich')
        output_file.write_text(content, encoding='utf-8')
        print("✅ Created sales-recruiting-demo-de.html (placeholder)")
    else:
        print("⚠️  sales-recruiting-demo.html not found - skipping")

if __name__ == '__main__':
    print("🔧 Creating German versions of Sales Recruiting Assessments...\n")
    create_german_stage1()
    create_german_stage2()
    create_german_demo()
    print("\n✅ German versions created!")

