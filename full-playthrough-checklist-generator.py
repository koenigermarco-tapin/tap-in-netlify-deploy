#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full English Playthrough Checklist Generator
Documents the complete user journey including all paths, games, assessments
"""

import os
import re
from collections import defaultdict

class PlaythroughDocumenter:
    def __init__(self):
        self.entry_points = []
        self.assessments = []
        self.games = []
        self.belt_stripes = []
        self.tools = []
        self.paths = []
        
    def find_entry_points(self):
        """Find all entry points to the platform"""
        print("📋 Finding entry points...")
        
        entry_files = ['index.html', 'index-DUAL-ENTRY.html']
        
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
    
    def find_all_assessments(self):
        """Find all assessment pages"""
        print("\n📋 Finding all assessments...")
        
        assessment_files = [f for f in os.listdir('.') if 'assessment' in f.lower() and f.endswith('.html') and not f.endswith('-de.html')]
        
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
        
        print(f"\n  Total: {len(self.assessments)} assessments")
    
    def find_all_games(self):
        """Find all game pages"""
        print("\n📋 Finding all games...")
        
        game_keywords = ['game', 'poker', 'roulette', 'cards', 'conflict', 'disagree']
        game_files = []
        
        for file in os.listdir('.'):
            if file.endswith('.html') and not file.endswith('-de.html'):
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
        
        print(f"\n  Total: {len(self.games)} games")
    
    def find_all_belt_stripes(self):
        """Find all belt stripe pages"""
        print("\n📋 Finding all belt stripes...")
        
        belts = ['white', 'blue', 'purple', 'brown', 'black']
        
        for belt in belts:
            belt_stripes = []
            for stripe in [1, 2, 3, 4]:
                # Check multiple naming patterns
                patterns = [
                    f"{belt}-belt-stripe{stripe}-gamified.html",
                    f"{belt}-belt-stripe{stripe}-carousel.html",
                    f"{belt}-belt-stripe{stripe}-carousel-NEW.html",
                    f"{belt}-belt-stripe{stripe}-interactive-FULL.html"
                ]
                
                for pattern in patterns:
                    if os.path.exists(pattern):
                        size = os.path.getsize(pattern) / 1024
                        belt_stripes.append({
                            'stripe': stripe,
                            'file': pattern,
                            'size_kb': round(size, 1)
                        })
                        break
            
            if belt_stripes:
                self.belt_stripes.append({
                    'belt': belt,
                    'stripes': belt_stripes
                })
                print(f"  ✅ {belt.capitalize()} Belt: {len(belt_stripes)} stripes")
    
    def find_all_tools(self):
        """Find all tool pages (Open Mat)"""
        print("\n📋 Finding all tools...")
        
        tool_files = []
        for file in os.listdir('.'):
            if file.endswith('.html') and not file.endswith('-de.html'):
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
        
        print(f"\n  Total: {len(self.tools)} tools")
    
    def document_gym_dashboard_paths(self):
        """Document all paths from gym-dashboard.html"""
        print("\n📋 Documenting gym-dashboard paths...")
        
        if not os.path.exists('gym-dashboard.html'):
            print("  ⚠️  gym-dashboard.html not found")
            return
        
        try:
            with open('gym-dashboard.html', 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract all links
            links = re.findall(r'href=["\']([^"\']+\.html)["\']', content)
            onclick_links = re.findall(r'onclick=["\'].*?location\.href\s*=\s*["\']([^"\']+\.html)["\']', content)
            js_links = re.findall(r'window\.location\.href\s*=\s*["\']([^"\']+\.html)["\']', content)
            
            all_links = list(set(links + onclick_links + js_links))
            
            self.paths.append({
                'from': 'gym-dashboard.html',
                'links_to': sorted(all_links),
                'total': len(all_links)
            })
            
            print(f"  ✅ Found {len(all_links)} links from gym-dashboard")
        except Exception as e:
            print(f"  ⚠️  Error: {e}")
    
    def document_learning_hub_paths(self):
        """Document all paths from learning-hub.html"""
        print("\n📋 Documenting learning-hub paths...")
        
        if not os.path.exists('learning-hub.html'):
            print("  ⚠️  learning-hub.html not found")
            return
        
        try:
            with open('learning-hub.html', 'r', encoding='utf-8') as f:
                content = f.read()
            
            links = re.findall(r'href=["\']([^"\']+\.html)["\']', content)
            all_links = list(set(links))
            
            self.paths.append({
                'from': 'learning-hub.html',
                'links_to': sorted(all_links),
                'total': len(all_links)
            })
            
            print(f"  ✅ Found {len(all_links)} links from learning-hub")
        except Exception as e:
            print(f"  ⚠️  Error: {e}")
    
    def generate_checklist(self):
        """Generate comprehensive playthrough checklist"""
        print("\n" + "="*80)
        print("📝 GENERATING PLAYTHROUGH CHECKLIST")
        print("="*80)
        
        checklist = f"""# 🎯 TAP-IN FULL ENGLISH PLAYTHROUGH CHECKLIST

**Generated:** Comprehensive user journey documentation  
**Status:** Complete path mapping

---

## 🚪 ENTRY POINTS

### Main Entry
- [ ] **index.html** - Landing page
  - [ ] Click "THE GYM" → gym-dashboard.html
  - [ ] Click "THE HUB" → learning-hub.html
  - [ ] Click "Belt Assessment" → belt-assessment-sales-landing.html

---

## 🏋️ THE GYM PATH

### Gym Dashboard (`gym-dashboard.html`)
- [ ] View dashboard overview
- [ ] Check XP and level
- [ ] View streak badge
- [ ] Check current progress

### Belt Assessments
"""
        
        # Add belt assessments
        for assess in self.assessments:
            if assess['type'] == 'belt-assessment':
                checklist += f"- [ ] **{assess['file']}** ({assess['size_kb']} KB)\n"
        
        checklist += "\n### Belt Paths\n\n"
        
        # Add belt stripes
        for belt_info in self.belt_stripes:
            belt = belt_info['belt']
            checklist += f"#### {belt.capitalize()} Belt\n"
            checklist += f"- [ ] **{belt}-belt.html** - Belt hub page\n"
            for stripe in belt_info['stripes']:
                checklist += f"  - [ ] Stripe {stripe['stripe']}: {stripe['file']} ({stripe['size_kb']} KB)\n"
            checklist += f"- [ ] **{belt}-belt-assessment.html** - Assessment\n\n"
        
        checklist += "\n---\n\n## 📚 THE HUB PATH\n\n"
        checklist += "### Learning Hub (`learning-hub.html`)\n"
        checklist += "- [ ] View hub overview\n"
        checklist += "- [ ] Check available modules\n"
        checklist += "- [ ] View tools section\n\n"
        
        checklist += "### Games\n\n"
        for game in self.games:
            checklist += f"- [ ] **{game['file']}** ({game['size_kb']} KB)\n"
        
        checklist += "\n### Tools (Open Mat)\n\n"
        for tool in self.tools:
            checklist += f"- [ ] **{tool['file']}** ({tool['size_kb']} KB)\n"
        
        checklist += "\n### Other Assessments\n\n"
        for assess in self.assessments:
            if assess['type'] == 'other-assessment':
                checklist += f"- [ ] **{assess['file']}** ({assess['size_kb']} KB)\n"
        
        checklist += "\n---\n\n## 🎮 COMPLETE GAME INVENTORY\n\n"
        for game in self.games:
            checklist += f"### {game['file']}\n"
            checklist += f"- [ ] Load game\n"
            checklist += f"- [ ] Test gameplay\n"
            checklist += f"- [ ] Verify scoring/XP\n"
            checklist += f"- [ ] Check mobile responsiveness\n\n"
        
        checklist += "\n---\n\n## 📊 COMPLETE ASSESSMENT INVENTORY\n\n"
        for assess in self.assessments:
            checklist += f"### {assess['file']}\n"
            checklist += f"- [ ] Load assessment\n"
            checklist += f"- [ ] Complete all questions\n"
            checklist += f"- [ ] View results\n"
            checklist += f"- [ ] Verify XP awarded\n"
            checklist += f"- [ ] Check return navigation\n\n"
        
        checklist += "\n---\n\n## 🔄 COMPLETE BELT PATH\n\n"
        for belt_info in self.belt_stripes:
            belt = belt_info['belt']
            checklist += f"### {belt.capitalize()} Belt Complete Path\n"
            checklist += f"1. [ ] Start at {belt}-belt.html\n"
            for i, stripe in enumerate(belt_info['stripes'], 1):
                checklist += f"   {i}. [ ] Complete Stripe {stripe['stripe']}: {stripe['file']}\n"
            checklist += f"   {len(belt_info['stripes'])+1}. [ ] Take {belt}-belt-assessment.html\n"
            checklist += f"   {len(belt_info['stripes'])+2}. [ ] Return to gym-dashboard.html\n\n"
        
        checklist += "\n---\n\n## ✅ COMPLETION VERIFICATION\n\n"
        checklist += "- [ ] All entry points tested\n"
        checklist += "- [ ] All belt paths completed\n"
        checklist += "- [ ] All games playable\n"
        checklist += "- [ ] All tools functional\n"
        checklist += "- [ ] All assessments working\n"
        checklist += "- [ ] Navigation flows correctly\n"
        checklist += "- [ ] XP awards working\n"
        checklist += "- [ ] No broken links\n"
        checklist += "- [ ] No console errors\n"
        checklist += "- [ ] Mobile responsive\n"
        
        return checklist
    
    def save_checklist(self, checklist):
        """Save checklist to file"""
        with open('FULL-PLAYTHROUGH-CHECKLIST.md', 'w', encoding='utf-8') as f:
            f.write(checklist)
        
        print("\n✅ Checklist saved to: FULL-PLAYTHROUGH-CHECKLIST.md")
        print(f"   Length: {len(checklist)} characters")
        print(f"   Lines: {len(checklist.split(chr(10)))}")

def main():
    print("="*80)
    print("🎯 FULL ENGLISH PLAYTHROUGH CHECKLIST GENERATOR")
    print("="*80)
    print()
    
    doc = PlaythroughDocumenter()
    
    # Gather all information
    doc.find_entry_points()
    doc.find_all_assessments()
    doc.find_all_games()
    doc.find_all_belt_stripes()
    doc.find_all_tools()
    doc.document_gym_dashboard_paths()
    doc.document_learning_hub_paths()
    
    # Generate checklist
    checklist = doc.generate_checklist()
    doc.save_checklist(checklist)
    
    print("\n" + "="*80)
    print("✅ CHECKLIST GENERATION COMPLETE")
    print("="*80)

if __name__ == '__main__':
    main()

