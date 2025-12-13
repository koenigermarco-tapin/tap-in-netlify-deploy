#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full German Playthrough Checklist Generator
Documents the complete German user journey including all paths, games, assessments
"""

import os
import re
from collections import defaultdict

class GermanPlaythroughDocumenter:
    def __init__(self):
        self.entry_points = []
        self.assessments = []
        self.games = []
        self.belt_stripes = []
        self.tools = []
        self.paths = []
        self.belt_hubs = []
        
    def find_german_entry_points(self):
        """Find all German entry points to the platform"""
        print("📋 Finding German entry points...")
        
        entry_files = ['index.de.html', 'index-DUAL-ENTRY-de.html']
        
        for entry in entry_files:
            if os.path.exists(entry):
                try:
                    with open(entry, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Extract links
                    links = re.findall(r'href=["\']([^"\']+\.html)["\']', content)
                    unique_links = list(set(links))
                    
                    self.entry_points.append({
                        'file': entry,
                        'links_to': unique_links
                    })
                    print(f"  ✅ {entry}: {len(unique_links)} links found")
                except Exception as e:
                    print(f"  ⚠️  Error reading {entry}: {e}")
    
    def find_all_german_assessments(self):
        """Find all German assessment pages"""
        print("\n📋 Finding all German assessments...")
        
        assessment_files = [f for f in os.listdir('.') if 'assessment' in f.lower() and f.endswith('-de.html')]
        
        for assess in sorted(assessment_files):
            try:
                size = os.path.getsize(assess) / 1024
                
                # Check if it's a belt assessment or other
                if 'belt' in assess.lower():
                    self.assessments.append({
                        'file': assess,
                        'type': 'belt-assessment',
                        'size_kb': round(size, 1)
                    })
                else:
                    self.assessments.append({
                        'file': assess,
                        'type': 'other-assessment',
                        'size_kb': round(size, 1)
                    })
                
                print(f"  ✅ {assess} ({size:.1f} KB)")
            except:
                pass
        
        print(f"\n  Total: {len(self.assessments)} German assessments")
    
    def find_all_german_games(self):
        """Find all German game pages"""
        print("\n📋 Finding all German games...")
        
        game_keywords = ['game', 'poker', 'roulette', 'cards', 'conflict', 'disagree']
        game_files = []
        
        for file in os.listdir('.'):
            if file.endswith('-de.html'):
                if any(keyword in file.lower() for keyword in game_keywords):
                    game_files.append(file)
        
        for game in sorted(game_files):
            try:
                size = os.path.getsize(game) / 1024
                self.games.append({
                    'file': game,
                    'size_kb': round(size, 1)
                })
                print(f"  ✅ {game} ({size:.1f} KB)")
            except:
                pass
        
        print(f"\n  Total: {len(self.games)} German games")
    
    def find_all_german_belt_stripes(self):
        """Find all German belt stripe pages"""
        print("\n📋 Finding all German belt stripes...")
        
        belts = ['white', 'blue', 'purple', 'brown', 'black']
        
        for belt in belts:
            belt_stripes = []
            for stripe in [1, 2, 3, 4]:
                # Check German gamified naming pattern
                pattern = f"{belt}-belt-stripe{stripe}-gamified-de.html"
                
                if os.path.exists(pattern):
                    size = os.path.getsize(pattern) / 1024
                    belt_stripes.append({
                        'stripe': stripe,
                        'file': pattern,
                        'size_kb': round(size, 1)
                    })
            
            if belt_stripes:
                self.belt_stripes.append({
                    'belt': belt,
                    'stripes': belt_stripes
                })
                print(f"  ✅ {belt.capitalize()} Belt: {len(belt_stripes)} stripes")
    
    def find_all_german_tools(self):
        """Find all German tool pages (Open Mat)"""
        print("\n📋 Finding all German tools...")
        
        tool_files = []
        for file in os.listdir('.'):
            if file.endswith('-de.html'):
                if file.startswith('tool-') or file.startswith('open-mat-'):
                    tool_files.append(file)
        
        for tool in sorted(tool_files):
            try:
                size = os.path.getsize(tool) / 1024
                self.tools.append({
                    'file': tool,
                    'size_kb': round(size, 1)
                })
                print(f"  ✅ {tool} ({size:.1f} KB)")
            except:
                pass
        
        print(f"\n  Total: {len(self.tools)} German tools")
    
    def find_all_german_belt_hubs(self):
        """Find all German belt hub pages"""
        print("\n📋 Finding all German belt hubs...")
        
        belts = ['white', 'blue', 'purple', 'brown', 'black']
        
        for belt in belts:
            hub_file = f"{belt}-belt-de.html"
            if os.path.exists(hub_file):
                size = os.path.getsize(hub_file) / 1024
                self.belt_hubs.append({
                    'belt': belt,
                    'file': hub_file,
                    'size_kb': round(size, 1)
                })
                print(f"  ✅ {hub_file} ({size:.1f} KB)")
    
    def document_gym_dashboard_de_paths(self):
        """Document all paths from gym-dashboard-de.html"""
        print("\n📋 Documenting gym-dashboard-de.html paths...")
        
        if not os.path.exists('gym-dashboard-de.html'):
            print("  ⚠️  gym-dashboard-de.html not found")
            return
        
        try:
            with open('gym-dashboard-de.html', 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract all links
            links = re.findall(r'href=["\']([^"\']+\.html)["\']', content)
            onclick_links = re.findall(r'onclick=["\'].*?location\.href\s*=\s*["\']([^"\']+\.html)["\']', content)
            js_links = re.findall(r'window\.location\.href\s*=\s*["\']([^"\']+\.html)["\']', content)
            
            all_links = list(set(links + onclick_links + js_links))
            
            self.paths.append({
                'from': 'gym-dashboard-de.html',
                'links_to': sorted(all_links),
                'total': len(all_links)
            })
            
            print(f"  ✅ Found {len(all_links)} links from gym-dashboard-de.html")
        except Exception as e:
            print(f"  ⚠️  Error: {e}")
    
    def document_learning_hub_de_paths(self):
        """Document all paths from learning-hub-de.html"""
        print("\n📋 Documenting learning-hub-de.html paths...")
        
        if not os.path.exists('learning-hub-de.html'):
            print("  ⚠️  learning-hub-de.html not found")
            return
        
        try:
            with open('learning-hub-de.html', 'r', encoding='utf-8') as f:
                content = f.read()
            
            links = re.findall(r'href=["\']([^"\']+\.html)["\']', content)
            all_links = list(set(links))
            
            self.paths.append({
                'from': 'learning-hub-de.html',
                'links_to': sorted(all_links),
                'total': len(all_links)
            })
            
            print(f"  ✅ Found {len(all_links)} links from learning-hub-de.html")
        except Exception as e:
            print(f"  ⚠️  Error: {e}")
    
    def generate_checklist(self):
        """Generate comprehensive German playthrough checklist"""
        print("\n" + "="*80)
        print("📝 GENERATING GERMAN PLAYTHROUGH CHECKLIST")
        print("="*80)
        
        checklist = f"""# 🎯 TAP-IN VOLLSTÄNDIGE DEUTSCHE SPIELDURCHGANG-CHECKLISTE

**Generiert:** Umfassende Dokumentation der deutschen Benutzerreise  
**Status:** Vollständige Pfad-Zuordnung  
**Sprache:** Deutsch (Du-Form)

---

## 🚪 EINSTIEGSPUNKTE (ENTRY POINTS)

### Haupt-Einstieg
- [ ] **index.de.html** - Startseite
  - [ ] Klick auf "DAS GYM" → gym-dashboard-de.html
  - [ ] Klick auf "DER HUB" → learning-hub-de.html
  - [ ] Klick auf "Bewertung" → belt-assessment-sales-landing-de.html

- [ ] **index-DUAL-ENTRY-de.html** - Alternative Startseite
  - [ ] Überprüfe alle Navigationslinks
  - [ ] Überprüfe Sprachumschalter

---

## 🏋️ DAS GYM PFAD

### Gym Dashboard (`gym-dashboard-de.html`)
- [ ] Dashboard-Übersicht anzeigen
- [ ] XP und Level überprüfen
- [ ] Streak-Badge anzeigen
- [ ] Aktuellen Fortschritt überprüfen
- [ ] Sprachumschalter testen

### Gürtel-Bewertungen
"""
        
        # Add belt assessments
        for assess in self.assessments:
            if assess['type'] == 'belt-assessment':
                checklist += f"- [ ] **{assess['file']}** ({assess['size_kb']} KB)\n"
        
        checklist += "\n### Gürtel-Pfade\n\n"
        
        # Add belt hubs and stripes
        for belt_info in self.belt_stripes:
            belt = belt_info['belt']
            belt_name_de = {
                'white': 'Weißer',
                'blue': 'Blauer',
                'purple': 'Lila',
                'brown': 'Brauner',
                'black': 'Schwarzer'
            }.get(belt, belt.capitalize())
            
            # Find corresponding hub
            hub = next((h for h in self.belt_hubs if h['belt'] == belt), None)
            
            checklist += f"#### {belt_name_de} Gürtel\n"
            if hub:
                checklist += f"- [ ] **{hub['file']}** - Gürtel-Hub-Seite ({hub['size_kb']} KB)\n"
            else:
                checklist += f"- [ ] **{belt}-belt-de.html** - Gürtel-Hub-Seite (prüfen ob vorhanden)\n"
            
            for stripe in belt_info['stripes']:
                checklist += f"  - [ ] Stripe {stripe['stripe']}: {stripe['file']} ({stripe['size_kb']} KB)\n"
            
            # Find corresponding assessment
            assess = next((a for a in self.assessments if belt in a['file'] and a['type'] == 'belt-assessment'), None)
            if assess:
                checklist += f"- [ ] **{assess['file']}** - Bewertung\n\n"
            else:
                checklist += f"- [ ] **{belt}-belt-assessment-de.html** - Bewertung (prüfen ob vorhanden)\n\n"
        
        checklist += "\n---\n\n## 📚 DER HUB PFAD\n\n"
        checklist += "### Learning Hub (`learning-hub-de.html`)\n"
        checklist += "- [ ] Hub-Übersicht anzeigen\n"
        checklist += "- [ ] Verfügbare Module überprüfen\n"
        checklist += "- [ ] Tools-Bereich anzeigen\n"
        checklist += "- [ ] Sprachumschalter testen\n\n"
        
        checklist += "### Spiele\n\n"
        if self.games:
            for game in self.games:
                checklist += f"- [ ] **{game['file']}** ({game['size_kb']} KB)\n"
        else:
            checklist += "- [ ] Keine deutschen Spiele gefunden (prüfen ob Übersetzung benötigt)\n"
        
        checklist += "\n### Tools (Open Mat)\n\n"
        if self.tools:
            for tool in self.tools:
                checklist += f"- [ ] **{tool['file']}** ({tool['size_kb']} KB)\n"
        else:
            checklist += "- [ ] Keine deutschen Tools gefunden (prüfen ob Übersetzung benötigt)\n"
        
        checklist += "\n### Andere Bewertungen\n\n"
        for assess in self.assessments:
            if assess['type'] == 'other-assessment':
                checklist += f"- [ ] **{assess['file']}** ({assess['size_kb']} KB)\n"
        
        checklist += "\n---\n\n## 🗺️ DETAILLIERTE NAVIGATIONSPFADE\n\n"
        checklist += """### Pfad 1: Neue Benutzerreise
```
1. index.de.html (Startseite)
   ↓
2. Klick auf "Bewertung" Button
   ↓
3. belt-assessment-sales-landing-de.html
   ↓
4. belt-assessment-v2-de.html
   ↓
5. 50 Fragen beantworten
   ↓
6. Gürtel-Empfehlung erhalten (z.B. Blauer Gürtel)
   ↓
7. Klick auf empfohlenen Gürtel → blue-belt-de.html
   ↓
8. blue-belt-stripe1-gamified-de.html
   ↓
9. Stripe abschließen → gym-dashboard-de.html (Rückkehr)
```

### Pfad 2: Gym Dashboard Flow
```
1. gym-dashboard-de.html
   ↓
2. Gürtel auswählen (z.B. white-belt-de.html)
   ↓
3. Stripe-Karten anzeigen
   ↓
4. Klick auf Stripe → white-belt-stripe1-gamified-de.html
   ↓
5. Lektionen & Quiz abschließen
   ↓
6. Zurück zu gym-dashboard-de.html
   ↓
7. Weiter zum nächsten Stripe
```

### Pfad 3: Learning Hub Flow
```
1. learning-hub-de.html
   ↓
2. Module/Spiele/Tools durchsuchen
   ↓
3. Tool auswählen → tool-morning-routine-de.html
   ↓
4. Tool verwenden & XP verdienen
   ↓
5. Zurück zu learning-hub-de.html
   ↓
6. Spiel ausprobieren → confession-poker-de.html (falls vorhanden)
```

### Pfad 4: Vollständiger Gürtel-Pfad
```
Weißer Gürtel:
  1. white-belt-de.html
  2. white-belt-stripe1-gamified-de.html
  3. white-belt-stripe2-gamified-de.html
  4. white-belt-stripe3-gamified-de.html
  5. white-belt-stripe4-gamified-de.html
  6. white-belt-assessment-de.html
  7. → Blauer Gürtel freischalten

Blauer Gürtel:
  1. blue-belt-de.html
  2. blue-belt-stripe1-gamified-de.html
  3. blue-belt-stripe2-gamified-de.html
  4. blue-belt-stripe3-gamified-de.html
  5. blue-belt-stripe4-gamified-de.html
  6. blue-belt-assessment-de.html
  7. → Lila Gürtel freischalten

... (fortsetzt durch alle 5 Gürtel)
```

---

## 🎮 VOLLSTÄNDIGE SPIELE-LISTE MIT STANDORTEN

### Leadership Games Hub (Deutsch)
- [ ] **leadership-games-de.html** - Spiel-Hub/Landing-Seite (prüfen ob vorhanden)
  - Verlinkt zu allen Spielen unten

### Einzelne Spiele
"""
        
        if self.games:
            for game in self.games:
                checklist += f"""- [ ] **{game['file']}** - Spiel ({game['size_kb']} KB)
  - Standort: Hub → Spiele-Bereich
  - XP: Pro Spiel-Abschluss
  - Überprüfe Übersetzung: Du-Form, technische Begriffe auf Englisch
  - Überprüfe Links: Alle internen Links auf -de.html Versionen
  
"""
        else:
            checklist += """- [ ] **confession-poker-de.html** - Multiplayer-Kartenspiel (prüfen ob vorhanden)
- [ ] **conflict-cards-de.html** - Konfliktlösungs-Spiel (prüfen ob vorhanden)
- [ ] **disagree-commit-roulette-de.html** - Disagree & Commit Übung (prüfen ob vorhanden)
- [ ] **take-the-back-de.html** - Leadership-Übungs-Spiel (prüfen ob vorhanden)

"""
        
        checklist += "\n---\n\n## 🛠️ VOLLSTÄNDIGE TOOLS-LISTE MIT STANDORTEN\n\n"
        checklist += "### Open Mat Tools (Schnell-Übung)\n\n"
        
        if self.tools:
            for tool in self.tools:
                if 'open-mat' in tool['file']:
                    checklist += f"- [ ] **{tool['file']}** ({tool['size_kb']} KB)\n"
        else:
            checklist += "- [ ] Keine Open Mat Tools gefunden\n"
        
        checklist += "\n### Vollständige Tools (Detaillierte Versionen)\n\n"
        if self.tools:
            for tool in self.tools:
                if tool['file'].startswith('tool-'):
                    checklist += f"- [ ] **{tool['file']}** ({tool['size_kb']} KB)\n"
        else:
            checklist += "- [ ] Keine vollständigen Tools gefunden\n"
        
        checklist += "\n---\n\n## 📊 VOLLSTÄNDIGER BEWERTUNGSKATALOG\n\n"
        checklist += "### Gürtel-Bewertungen (Gürtel-spezifisch)\n\n"
        
        belt_assessments = [a for a in self.assessments if a['type'] == 'belt-assessment']
        for assess in belt_assessments:
            belt_name = assess['file'].split('-')[0].capitalize()
            checklist += f"- [ ] **{assess['file']}** - {belt_name} Gürtel ({assess['size_kb']} KB)\n"
        
        checklist += "\n### Haupt-Bewertung (Einstiegspunkt)\n\n"
        checklist += """- [ ] **belt-assessment-v2-de.html** - 50 Fragen, empfiehlt Start-Gürtel
  - Kann zugegriffen werden von:
    - index.de.html → Bewertung Button
    - gym-dashboard-de.html → Bewertung starten
    - belt-assessment-sales-landing-de.html

### Andere Bewertungen

"""
        other_assessments = [a for a in self.assessments if a['type'] == 'other-assessment']
        for assess in other_assessments:
            checklist += f"- [ ] **{assess['file']}** ({assess['size_kb']} KB)\n"
        
        checklist += "\n---\n\n## ✅ QUALITÄTSPRÜFUNG FÜR DEUTSCHE SEITEN\n\n"
        checklist += """### Übersetzungs-Qualität
- [ ] Du-Form durchgehend verwendet (kein "Sie")
- [ ] Technische Begriffe auf Englisch (z.B. "White Belt", nicht "Weißer Gürtel" im UI)
- [ ] Energetischer, motivierender Ton
- [ ] Keine gemischten Sprachen (kein Englisch/Deutsch-Mix in Sätzen)
- [ ] Alle Quiz-Fragen übersetzt
- [ ] Alle Erklärungen übersetzt
- [ ] Alle UI-Elemente übersetzt

### Link-Qualität
- [ ] Alle internen Links zeigen auf -de.html Versionen
- [ ] Keine hardcodierten englischen Links
- [ ] Sprachumschalter funktioniert korrekt
- [ ] Zurück-Navigation führt zu deutschen Versionen

### Technische Qualität
- [ ] `lang="de"` Attribut in <html> Tag
- [ ] Korrekte Meta-Tags
- [ ] Alle JavaScript-Variablen übersetzt
- [ ] localStorage Keys korrekt
- [ ] XP-System funktioniert
- [ ] Fortschritts-Tracking funktioniert

---

## 🔄 VOLLSTÄNDIGER GÜRTEL-PFAD (DEUTSCH)

"""
        
        for belt_info in self.belt_stripes:
            belt = belt_info['belt']
            belt_name_de = {
                'white': 'Weißer',
                'blue': 'Blauer',
                'purple': 'Lila',
                'brown': 'Brauner',
                'black': 'Schwarzer'
            }.get(belt, belt.capitalize())
            
            checklist += f"### {belt_name_de} Gürtel Vollständiger Pfad\n"
            checklist += f"1. [ ] Start bei {belt}-belt-de.html\n"
            for i, stripe in enumerate(belt_info['stripes'], 1):
                checklist += f"   {i}. [ ] Stripe {stripe['stripe']} abschließen: {stripe['file']}\n"
            
            assess = next((a for a in self.assessments if belt in a['file'] and a['type'] == 'belt-assessment'), None)
            if assess:
                checklist += f"   {len(belt_info['stripes'])+1}. [ ] {assess['file']} durchführen\n"
            checklist += f"   {len(belt_info['stripes'])+2}. [ ] Zurück zu gym-dashboard-de.html\n\n"
        
        checklist += "\n---\n\n## ✅ ABSCHLUSSVERIFIZIERUNG\n\n"
        checklist += "- [ ] Alle Einstiegspunkte getestet\n"
        checklist += "- [ ] Alle Gürtel-Pfade abgeschlossen\n"
        checklist += "- [ ] Alle Spiele spielbar (falls übersetzt)\n"
        checklist += "- [ ] Alle Tools funktional (falls übersetzt)\n"
        checklist += "- [ ] Alle Bewertungen funktionieren\n"
        checklist += "- [ ] Navigation fließt korrekt\n"
        checklist += "- [ ] XP-Vergabe funktioniert\n"
        checklist += "- [ ] Keine kaputten Links\n"
        checklist += "- [ ] Keine Konsolen-Fehler\n"
        checklist += "- [ ] Mobile responsive\n"
        checklist += "- [ ] Sprachumschalter funktioniert (DE ↔ EN)\n"
        checklist += "- [ ] Alle Links zeigen auf deutsche Versionen\n"
        checklist += "- [ ] Du-Form durchgehend verwendet\n"
        checklist += "- [ ] Keine gemischten Sprachen\n"
        
        checklist += f"\n---\n\n## 📊 STATISTIK\n\n"
        checklist += f"- **Gürtel-Hubs gefunden:** {len(self.belt_hubs)}\n"
        checklist += f"- **Gürtel-Stripes gefunden:** {sum(len(b['stripes']) for b in self.belt_stripes)}\n"
        checklist += f"- **Bewertungen gefunden:** {len(self.assessments)}\n"
        checklist += f"- **Spiele gefunden:** {len(self.games)}\n"
        checklist += f"- **Tools gefunden:** {len(self.tools)}\n"
        
        return checklist
    
    def save_checklist(self, checklist):
        """Save checklist to file"""
        with open('FULL-PLAYTHROUGH-CHECKLIST-DE.md', 'w', encoding='utf-8') as f:
            f.write(checklist)
        
        print("\n✅ Checkliste gespeichert in: FULL-PLAYTHROUGH-CHECKLIST-DE.md")
        print(f"   Länge: {len(checklist)} Zeichen")
        print(f"   Zeilen: {len(checklist.split(chr(10)))}")

def main():
    print("="*80)
    print("🎯 VOLLSTÄNDIGE DEUTSCHE SPIELDURCHGANG-CHECKLISTE GENERATOR")
    print("="*80)
    print()
    
    doc = GermanPlaythroughDocumenter()
    
    # Gather all information
    doc.find_german_entry_points()
    doc.find_all_german_assessments()
    doc.find_all_german_games()
    doc.find_all_german_belt_stripes()
    doc.find_all_german_tools()
    doc.find_all_german_belt_hubs()
    doc.document_gym_dashboard_de_paths()
    doc.document_learning_hub_de_paths()
    
    # Generate checklist
    checklist = doc.generate_checklist()
    doc.save_checklist(checklist)
    
    print("\n" + "="*80)
    print("✅ CHECKLISTE-GENERIERUNG ABGESCHLOSSEN")
    print("="*80)

if __name__ == '__main__':
    main()

