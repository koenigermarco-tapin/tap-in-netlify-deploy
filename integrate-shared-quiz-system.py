#!/usr/bin/env python3
"""
Integrate shared-quiz-system.js into all stripe files
Add script tag and ensure compatibility
"""

from pathlib import Path
import re

def integrate_shared_quiz_system(filepath):
    """Add shared quiz system script to stripe file"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Check if already integrated
    if 'js/shared-quiz-system.js' in content:
        return False, "Already integrated"
    
    # Find where to insert the script (before other JS files or before </body>)
    # Look for existing script tags for gamification or before </body>
    
    # Pattern 1: Before other gamification scripts
    pattern1 = r'(<script\s+src=["\']js/(gamification|stripe-completion|shared-utilities)\.js["\'])'
    
    if re.search(pattern1, content):
        # Insert before first gamification script
        content = re.sub(
            pattern1,
            r'<script src="js/shared-quiz-system.js"></script>\n    \1',
            content,
            count=1
        )
    else:
        # Pattern 2: Before </body> tag
        pattern2 = r'(</body>)'
        if re.search(pattern2, content):
            content = re.sub(
                pattern2,
                '    <script src="js/shared-quiz-system.js"></script>\n\1',
                content,
                count=1
            )
        else:
            # Pattern 3: Before </html> tag
            pattern3 = r'(</html>)'
            if re.search(pattern3, content):
                content = re.sub(
                    pattern3,
                    '    <script src="js/shared-quiz-system.js"></script>\n\1',
                    content,
                    count=1
                )
            else:
                return False, "Could not find insertion point"
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "Integrated"
    
    return False, "No changes needed"

def main():
    print("=" * 80)
    print("🔧 INTEGRATING SHARED QUIZ SYSTEM")
    print("=" * 80)
    print()
    
    # Find all stripe files
    stripe_files = []
    for stripe_file in Path('.').rglob('*-stripe*-gamified.html'):
        if any(skip in str(stripe_file) for skip in ['node_modules', '.git', 'react-app']):
            continue
        stripe_files.append(stripe_file)
    
    stripe_files.sort()
    
    print(f"Found {len(stripe_files)} stripe files\n")
    
    integrated = 0
    skipped = 0
    errors = 0
    
    for stripe_file in stripe_files:
        print(f"📝 {stripe_file.name}...")
        try:
            success, message = integrate_shared_quiz_system(stripe_file)
            if success:
                integrated += 1
                print(f"  ✅ {message}")
            else:
                skipped += 1
                print(f"  ⏭️  {message}")
        except Exception as e:
            errors += 1
            print(f"  ❌ Error: {e}")
        print()
    
    print("=" * 80)
    print(f"✅ Integrated: {integrated}/{len(stripe_files)}")
    print(f"⏭️  Skipped: {skipped}")
    print(f"❌ Errors: {errors}")
    print("=" * 80)

if __name__ == '__main__':
    main()

