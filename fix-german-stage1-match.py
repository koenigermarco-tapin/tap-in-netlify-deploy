#!/usr/bin/env python3
"""
Fix German Stage 1 to match English structure exactly
"""

from pathlib import Path

def fix_german_structure():
    """Fix German file to match English structure"""
    en_file = Path('sales-recruiting-stage1.html')
    de_file = Path('sales-recruiting-stage1-de.html')
    
    en_content = en_file.read_text(encoding='utf-8', errors='ignore')
    de_content = de_file.read_text(encoding='utf-8', errors='ignore')
    
    # Find the intro section in English
    en_intro_start = en_content.find('<!-- Context Section -->')
    en_intro_end = en_content.find('<!-- Progress Bar -->', en_intro_start)
    en_intro = en_content[en_intro_start:en_intro_end]
    
    # Find the intro section in German
    de_intro_start = de_content.find('<!-- Context Section -->')
    de_intro_end = de_content.find('<!-- Progress Bar -->', de_intro_start)
    
    # Replace German intro with properly translated version matching English structure
    new_de_intro = '''        <!-- Context Section -->
        <div class="intro-section" id="introSection" style="background: #f8fafc; padding: 25px; border-radius: 12px; margin-bottom: 30px; border-left: 4px solid #1a365d;">
            <h3 style="color: #1e293b; margin-bottom: 15px; font-weight: 600;">📋 Was dich erwartet</h3>
            <p style="color: #64748b; line-height: 1.7; margin-bottom: 15px;">
                Dieses kurze Assessment hilft uns zu bestimmen, ob es eine starke initiale Übereinstimmung 
                zwischen deinem natürlichen Arbeitsstil und unserer Sales-Rolle gibt. Dauert 3 Minuten.
            </p>
            <p style="color: #64748b; line-height: 1.7; margin-bottom: 20px;">
                <strong>Qualifizierte Kandidaten gehen zu Stufe 2</strong> (10-minütiges detailliertes Profil).
            </p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin: 20px 0;">
                <div style="background: white; padding: 15px; border-radius: 8px; text-align: center; border-top: 3px solid #1a365d;">
                    <div style="font-size: 2em; margin-bottom: 5px;">⚡</div>
                    <strong style="color: #1a365d;">Sprinter</strong><br>
                    <span style="font-size: 0.85em; color: #64748b;">Hohe Intensität, kurze Bursts</span>
                </div>
                <div style="background: white; padding: 15px; border-radius: 8px; text-align: center; border-top: 3px solid #1a365d;">
                    <div style="font-size: 2em; margin-bottom: 5px;">🏃</div>
                    <strong style="color: #1a365d;">Jogger</strong><br>
                    <span style="font-size: 0.85em; color: #64748b;">Stetiger, konsistenter Rhythmus</span>
                </div>
                <div style="background: white; padding: 15px; border-radius: 8px; text-align: center; border-top: 3px solid #1a365d;">
                    <div style="font-size: 2em; margin-bottom: 5px;">🎯</div>
                    <strong style="color: #1a365d;">Ultrarunner</strong><br>
                    <span style="font-size: 0.85em; color: #64748b;">Marathon-Mentalität, lange Vision</span>
                </div>
            </div>

            <p style="margin-top: 15px; font-style: italic; color: #94a3b8; font-size: 0.9em; text-align: center;">"Der Schlüssel ist nicht, zu priorisieren, was auf deinem Zeitplan steht, sondern deine Prioritäten einzuplanen." — Stephen Covey</p>
            
            <div style="text-align: center; margin-top: 25px;">
                <button class="btn btn-primary" onclick="startAssessment()" style="font-size: 1.2em; padding: 18px 40px;">
                    Assessment starten →
                </button>
            </div>
        </div>
'''
    
    if de_intro_start > 0 and de_intro_end > de_intro_start:
        de_content = de_content[:de_intro_start] + new_de_intro + de_content[de_intro_end:]
        de_file.write_text(de_content, encoding='utf-8')
        print("✅ Fixed German Stage 1 structure to match English")
    else:
        print("⚠️  Could not find intro section in German file")

if __name__ == '__main__':
    fix_german_structure()

