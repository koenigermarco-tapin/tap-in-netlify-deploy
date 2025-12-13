#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enhance Playthrough Checklist with detailed paths and user journey
"""

import os
import re

def enhance_checklist():
    """Enhance the checklist with more detailed information"""
    
    # Read existing checklist
    with open('FULL-PLAYTHROUGH-CHECKLIST.md', 'r', encoding='utf-8') as f:
        checklist = f.read()
    
    # Add detailed navigation paths
    enhanced_section = """

---

## 🗺️ DETAILED NAVIGATION PATHS

### Path 1: New User Journey
```
1. index.html (Landing Page)
   ↓
2. Click "Belt Assessment" button
   ↓
3. belt-assessment-sales-landing.html
   ↓
4. belt-assessment-v2.html
   ↓
5. Complete 50 questions
   ↓
6. Get belt recommendation (e.g., Blue Belt)
   ↓
7. Click recommended belt → blue-belt.html
   ↓
8. blue-belt-stripe1-gamified.html
   ↓
9. Complete stripe → gym-dashboard.html (return)
```

### Path 2: Gym Dashboard Flow
```
1. gym-dashboard.html
   ↓
2. Select belt (e.g., white-belt.html)
   ↓
3. View stripe cards
   ↓
4. Click stripe → white-belt-stripe1-gamified.html
   ↓
5. Complete lessons & quiz
   ↓
6. Return to gym-dashboard.html
   ↓
7. Continue to next stripe
```

### Path 3: Learning Hub Flow
```
1. learning-hub.html
   ↓
2. Browse modules/games/tools
   ↓
3. Select tool → tool-morning-routine.html
   ↓
4. Use tool & earn XP
   ↓
5. Return to learning-hub.html
   ↓
6. Try game → confession-poker-v2.html
```

### Path 4: Complete Belt Path
```
White Belt:
  1. white-belt.html
  2. white-belt-stripe1-gamified.html
  3. white-belt-stripe2-gamified.html
  4. white-belt-stripe3-gamified.html
  5. white-belt-stripe4-gamified.html
  6. white-belt-assessment.html
  7. → Unlock Blue Belt

Blue Belt:
  1. blue-belt.html
  2. blue-belt-stripe1-gamified.html
  3. blue-belt-stripe2-gamified.html
  4. blue-belt-stripe3-gamified.html
  5. blue-belt-stripe4-gamified.html
  6. blue-belt-assessment.html
  7. → Unlock Purple Belt

... (continues through all 5 belts)
```

---

## 🎮 COMPLETE GAME LIST WITH LOCATIONS

### Leadership Games Hub
- [ ] **leadership-games.html** - Game hub/landing page
  - Links to all games below

### Individual Games
- [ ] **confession-poker-v2.html** - Multiplayer card game
  - Location: Hub → Games section
  - XP: Per game completion
  
- [ ] **conflict-cards.html** - Conflict resolution game
  - Location: Hub → Games section
  - XP: Per scenario completed

- [ ] **disagree-commit-roulette.html** - Disagree & commit practice
  - Location: Hub → Games section
  - XP: Per round completed

- [ ] **take-the-back.html** - Leadership practice game
  - Location: Hub → Games section
  - XP: Per session

---

## 🛠️ COMPLETE TOOL LIST WITH LOCATIONS

### Open Mat Tools (Quick Practice)
- [ ] **open-mat-5-minute-morning-routine.html**
- [ ] **open-mat-box-breathing.html**
- [ ] **open-mat-decision-framework.html**
- [ ] **open-mat-energy-audit.html**
- [ ] **open-mat-inner-game-leadership.html**
- [ ] **open-mat-jiu-jitsu.html**
- [ ] **open-mat-reframe-60.html**
- [ ] **open-mat-weekly-experiment.html**
- [ ] **open-mat-weekly-review.html**

### Full Tools (Detailed Versions)
- [ ] **tool-box-breathing.html**
- [ ] **tool-decision-framework.html**
- [ ] **tool-energy-audit.html**
- [ ] **tool-goal-tracker.html**
- [ ] **tool-inner-game.html**
- [ ] **tool-journal.html**
- [ ] **tool-mood-tracker.html**
- [ ] **tool-morning-routine.html**
- [ ] **tool-weekly-review.html**

---

## 📊 COMPLETE ASSESSMENT CATALOG

### Belt Assessments (Belt-Specific)
- [ ] **white-belt-assessment.html** - Trust & Vulnerability
- [ ] **blue-belt-assessment.html** - Conflict & Debate
- [ ] **purple-belt-assessment.html** - Commitment & Clarity
- [ ] **brown-belt-assessment.html** - Accountability
- [ ] **black-belt-assessment.html** - Results Focus

### Main Belt Assessment (Entry Point)
- [ ] **belt-assessment-v2.html** - 50 questions, recommends starting belt
  - Can be accessed from:
    - index.html → Belt Assessment button
    - gym-dashboard.html → Take Assessment
    - belt-assessment-sales-landing.html

### Other Assessments
- [ ] **worker-type-assessment.html** - Discover your work style
- [ ] **team-assessment-enhanced-v2.html** - Team dynamics
- [ ] **mental-health-assessment.html** - Wellness check
- [ ] **work-life-balance-assessment.html** - Balance assessment
- [ ] **leadership-style-assessment.html** - Leadership style
- [ ] **values-discovery-assessment.html** - Core values
- [ ] **communication-style-assessment.html** - Communication style
- [ ] **decision-making-assessment.html** - Decision framework
- [ ] **360-feedback-assessment.html** - 360 feedback
- [ ] **accountability-audit-assessment.html** - Accountability audit
- [ ] **life-audit-assessment.html** - Life audit
- [ ] **mission-statement-assessment.html** - Mission statement
- [ ] **deep-dive-assessment.html** - Deep dive

---

"""
    
    # Insert enhanced section before completion verification
    if "## ✅ COMPLETION VERIFICATION" in checklist:
        checklist = checklist.replace(
            "## ✅ COMPLETION VERIFICATION",
            enhanced_section + "\n## ✅ COMPLETION VERIFICATION"
        )
    
    # Save enhanced checklist
    with open('FULL-PLAYTHROUGH-CHECKLIST.md', 'w', encoding='utf-8') as f:
        f.write(checklist)
    
    print("✅ Enhanced checklist with detailed paths and catalog")

if __name__ == '__main__':
    enhance_checklist()

