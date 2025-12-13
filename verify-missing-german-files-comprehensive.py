#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verify Missing German Files - Check if they exist with different names
If not found, create translation prompt
"""

import os
import re
from collections import defaultdict

class MissingGermanFileVerifier:
    def __init__(self):
        self.missing_list = []
        self.found_alternatives = {}
        self.truly_missing = []
        self.english_files_exist = {}
        
    def load_missing_list(self):
        """Load the list of missing files"""
        if not os.path.exists('MISSING-GERMAN-VERSIONS.txt'):
            return []
        
        missing = []
        with open('MISSING-GERMAN-VERSIONS.txt', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('-') and not line.startswith('='):
                    # Extract filename
                    if line.startswith('- '):
                        line = line[2:]
                    # Remove leading slash if present
                    line = line.lstrip('/')
                    if line.endswith('.html'):
                        missing.append(line)
                elif line.startswith('- '):
                    # Direct list format
                    filename = line[2:].strip()
                    if filename.endswith('.html'):
                        missing.append(filename)
        
        # Also read from the file more directly
        with open('MISSING-GERMAN-VERSIONS.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            for line in content.split('\n'):
                if line.strip().startswith('- '):
                    filename = line.strip()[2:].strip().lstrip('/')
                    if filename.endswith('.html') and filename not in missing:
                        missing.append(filename)
        
        return missing
    
    def find_file_variations(self, filename):
        """Find all variations of a filename that might exist"""
        base = filename.replace('.html', '').replace('-de.html', '').replace('.de.html', '')
        
        # Remove leading slash
        base = base.lstrip('/')
        
        variations = [
            f"{base}-de.html",
            f"{base}.de.html",
            filename,  # Original
        ]
        
        found = []
        for variant in variations:
            if os.path.exists(variant):
                stat = os.stat(variant)
                found.append({
                    'path': variant,
                    'size': stat.st_size,
                    'mtime': stat.st_mtime
                })
        
        # Also search by base name
        for file in os.listdir('.'):
            if file.endswith('.html') and base in file:
                if file not in [f['path'] for f in found]:
                    if os.path.isfile(file):
                        stat = os.stat(file)
                        found.append({
                            'path': file,
                            'size': stat.st_size,
                            'mtime': stat.st_mtime
                        })
        
        return found
    
    def check_english_version_exists(self, filename):
        """Check if English version exists"""
        base = filename.replace('-de.html', '').replace('.de.html', '').lstrip('/')
        english_file = f"{base}.html"
        
        if os.path.exists(english_file):
            stat = os.stat(english_file)
            return {
                'exists': True,
                'path': english_file,
                'size': stat.st_size,
                'mtime': stat.st_mtime
            }
        
        # Try just the filename
        if os.path.exists(filename.lstrip('/')):
            stat = os.stat(filename.lstrip('/'))
            return {
                'exists': True,
                'path': filename.lstrip('/'),
                'size': stat.st_size,
                'mtime': stat.st_mtime
            }
        
        return {'exists': False}
    
    def verify_all_missing_files(self):
        """Verify all missing files"""
        print("="*80)
        print("🔍 VERIFYING MISSING GERMAN FILES")
        print("="*80)
        print()
        
        missing_list = self.load_missing_list()
        
        if not missing_list:
            print("⚠️  No missing files list found. Checking common missing patterns...")
            # Generate from common patterns
            missing_list = [
                'communication-mastery-2-clarity.html',
                'communication-mastery-4-receiving.html',
                'communication-mastery-5-difficult.html',
                'communication-mastery-6-nonverbal.html',
                'communication-mastery-7-meetings.html',
                'communication-mastery-v2.html',
                'open-mat-box-breathing.html',
                'open-mat-inner-game-leadership.html',
                'leadership-games.html',
                'values-discovery-assessment.html',
            ]
        
        print(f"📋 Checking {len(missing_list)} files...\n")
        
        for filename in sorted(missing_list):
            # Check English version
            eng_info = self.check_english_version_exists(filename)
            self.english_files_exist[filename] = eng_info
            
            # Find German variations
            variations = self.find_file_variations(filename)
            
            if variations:
                # Find German versions
                german_versions = [v for v in variations if '-de.html' in v['path'] or '.de.html' in v['path']]
                if german_versions:
                    self.found_alternatives[filename] = german_versions
                    print(f"  ✅ {filename}")
                    print(f"     Found: {german_versions[0]['path']}")
                else:
                    # Found but not German
                    self.truly_missing.append(filename)
                    print(f"  ❌ {filename}")
                    print(f"     English exists: {eng_info.get('exists', False)}")
            else:
                self.truly_missing.append(filename)
                print(f"  ❌ {filename}")
                print(f"     English exists: {eng_info.get('exists', False)}")
        
        print(f"\n✅ Found: {len(self.found_alternatives)}")
        print(f"❌ Truly missing: {len(self.truly_missing)}")
    
    def generate_translation_prompt(self):
        """Generate translation prompt for missing files"""
        print("\n" + "="*80)
        print("📝 GENERATING TRANSLATION PROMPT")
        print("="*80)
        print()
        
        # Group by category
        categories = {
            'Communication Mastery Modules': [],
            'Open Mat Tools': [],
            'Games': [],
            'Assessments': [],
            'Team Features': [],
            'Advanced Features': [],
            'Other': []
        }
        
        for filename in self.truly_missing:
            if 'communication-mastery' in filename:
                categories['Communication Mastery Modules'].append(filename)
            elif 'open-mat' in filename:
                categories['Open Mat Tools'].append(filename)
            elif 'game' in filename.lower():
                categories['Games'].append(filename)
            elif 'assessment' in filename.lower():
                categories['Assessments'].append(filename)
            elif any(word in filename for word in ['team', 'profile', 'dashboard']):
                categories['Team Features'].append(filename)
            elif any(word in filename for word in ['analytics', 'data', 'portal', 'manager']):
                categories['Advanced Features'].append(filename)
            else:
                categories['Other'].append(filename)
        
        prompt = """# 🌍 GERMAN TRANSLATION PROMPT - MISSING FILES

**Date:** November 30, 2024  
**Status:** Files verified missing - Translation needed

---

## 📋 SUMMARY

**Total Files to Translate:** {total}

These German versions are missing and need to be created from their English counterparts.

---

""".format(total=len(self.truly_missing))
        
        # Add each category
        for category, files in categories.items():
            if files:
                prompt += f"\n## {category} ({len(files)} files)\n\n"
                for filename in sorted(files):
                    eng_info = self.english_files_exist.get(filename, {})
                    prompt += f"- [ ] **{filename}**\n"
                    if eng_info.get('exists'):
                        size_kb = eng_info.get('size', 0) / 1024
                        prompt += f"  - English version exists: `{eng_info.get('path')}` ({size_kb:.1f} KB)\n"
                    prompt += f"  - German target: `{filename.replace('.html', '-de.html')}`\n\n"
        
        # Add translation guidelines
        prompt += """
---

## 📝 TRANSLATION GUIDELINES

### Key Requirements:
1. **Du-Form** throughout (never "Sie")
2. **Energetic, motivating tone**
3. **English technical terms** (e.g., "White Belt", "Leadership", "Assessment")
4. **Correct internal links** to `-de.html` versions
5. **lang="de"** attribute in HTML tag

### Translation Pattern:
```html
<!-- English -->
<h1>Welcome to the Assessment</h1>

<!-- German -->
<h1>Willkommen zur Bewertung</h1>
```

### Link Conversion:
- `href="white-belt.html"` → `href="white-belt-de.html"`
- `window.location.href = 'index.html'` → `window.location.href = 'index.de.html'`

---

## 🎯 PRIORITY ORDER

### High Priority (User-Facing Core Features):
"""
        
        high_priority = []
        for cat in ['Open Mat Tools', 'Games', 'Assessments']:
            if categories[cat]:
                high_priority.extend(categories[cat][:3])  # Top 3 from each
        
        for filename in high_priority[:10]:
            prompt += f"1. {filename}\n"
        
        prompt += """
### Medium Priority (Modules):
"""
        
        medium_priority = []
        for cat in ['Communication Mastery Modules']:
            if categories[cat]:
                medium_priority.extend(categories[cat])
        
        for filename in medium_priority[:5]:
            prompt += f"1. {filename}\n"
        
        prompt += """
### Low Priority (Advanced Features):
"""
        
        low_priority = []
        for cat in ['Team Features', 'Advanced Features', 'Other']:
            if categories[cat]:
                low_priority.extend(categories[cat])
        
        for filename in low_priority[:5]:
            prompt += f"1. {filename}\n"
        
        prompt += """
---

## ✅ QUALITY CHECKLIST

After translation, verify:
- [ ] Du-Form used throughout
- [ ] No "Sie" violations
- [ ] All internal links point to `-de.html` versions
- [ ] Technical terms remain in English
- [ ] `lang="de"` attribute present
- [ ] File saved as `*-de.html`
- [ ] All UI elements translated
- [ ] JavaScript strings translated (where applicable)
- [ ] Mobile responsive maintained
- [ ] Functionality preserved

---

**Ready for translation!** Use this as a checklist to systematically create all missing German versions.

"""
        
        return prompt

def main():
    verifier = MissingGermanFileVerifier()
    verifier.verify_all_missing_files()
    
    if verifier.truly_missing:
        prompt = verifier.generate_translation_prompt()
        
        with open('GERMAN-TRANSLATION-PROMPT.md', 'w', encoding='utf-8') as f:
            f.write(prompt)
        
        print("\n✅ Translation prompt saved to: GERMAN-TRANSLATION-PROMPT.md")
        print(f"\n📋 Files found with German versions: {len(verifier.found_alternatives)}")
        print(f"📋 Files truly missing: {len(verifier.truly_missing)}")
        
        # Save found alternatives report
        if verifier.found_alternatives:
            with open('FOUND-GERMAN-VERSIONS.txt', 'w', encoding='utf-8') as f:
                f.write("Found German Versions\n")
                f.write("="*80 + "\n\n")
                for eng_file, german_versions in verifier.found_alternatives.items():
                    f.write(f"{eng_file}:\n")
                    for gv in german_versions:
                        f.write(f"  ✅ {gv['path']}\n")
                    f.write("\n")
            print("✅ Found versions report saved to: FOUND-GERMAN-VERSIONS.txt")
    else:
        print("\n✅ All files found! No translations needed.")

if __name__ == '__main__':
    main()

