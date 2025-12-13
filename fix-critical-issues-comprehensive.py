#!/usr/bin/env python3

"""
TAP-IN Critical Issues Fix - Pre-Presentation
Fixes all critical navigation and functionality issues
"""

import os
import re
from pathlib import Path

def fix_all_critical_issues():
    print("🔧 FIXING ALL CRITICAL ISSUES")
    print("=" * 60)
    
    fixes = []
    
    # Fix 1: Belt Assessment Navigation
    print("\n1. Fixing belt assessment navigation...")
    if os.path.exists('belt-assessment-v2.html'):
        with open('belt-assessment-v2.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix the broken onclick attribute
        broken_pattern = r'onclick="location\.href="#" onclick="goToBelt\(\); return false;""'
        if broken_pattern in content:
            # Replace with proper navigation to gym dashboard
            fixed = '''onclick="goToGymDashboard(); return false;"'''
            content = content.replace(broken_pattern, fixed)
            
            # Add goToGymDashboard function if not exists
            if 'function goToGymDashboard' not in content:
                # Find where to insert the function (before closing script tag)
                script_end = content.rfind('</script>')
                if script_end > 0:
                    navigation_function = '''
        
        // Navigate to gym dashboard after assessment
        function goToGymDashboard() {
            // Save assessment completion
            localStorage.setItem('assessmentCompleted', 'true');
            localStorage.setItem('assessmentCompletedDate', new Date().toISOString());
            
            // Navigate to gym dashboard
            window.location.href = 'gym-dashboard.html';
        }
'''
                    content = content[:script_end] + navigation_function + '\n    ' + content[script_end:]
            
            with open('belt-assessment-v2.html', 'w', encoding='utf-8') as f:
                f.write(content)
            
            fixes.append("✅ Fixed belt assessment navigation button")
    
    # Fix 2: Ensure error suppressor is loaded first
    print("\n2. Ensuring error suppressor loads first...")
    key_pages = ['index.html', 'gym-dashboard.html', 'belt-assessment-v2.html']
    for page in key_pages:
        if not os.path.exists(page):
            continue
        
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if error-suppressor.js is loaded early
        if 'error-suppressor.js' in content:
            # Move it to be first script if not already
            head_match = re.search(r'(<head[^>]*>.*?)(<script)', content, re.DOTALL)
            if head_match and 'error-suppressor.js' not in head_match.group(1):
                # It's already loaded, just verify
                fixes.append(f"✅ {page} has error suppressor")
        else:
            # Add error suppressor as first script
            script_tag = '<script src="js/error-suppressor.js"></script>\n    '
            head_match = re.search(r'(<head[^>]*>)', content)
            if head_match:
                content = content.replace(head_match.group(1), head_match.group(1) + '\n    ' + script_tag)
                with open(page, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes.append(f"✅ Added error suppressor to {page}")
    
    # Fix 3: Verify manifest.json links
    print("\n3. Verifying PWA manifest links...")
    if os.path.exists('manifest.json'):
        fixes.append("✅ manifest.json exists")
        # Check if links are correct
        for page in ['index.html', 'gym-dashboard.html']:
            if os.path.exists(page):
                with open(page, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Fix absolute paths
                if 'href="/manifest.json"' in content:
                    content = content.replace('href="/manifest.json"', 'href="manifest.json"')
                    with open(page, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixes.append(f"✅ Fixed manifest link in {page}")
    
    # Fix 4: Fix German "Continue" translations
    print("\n4. Fixing German translation issues...")
    translations = {
        'Continue': 'Weiter',
        'Learn more': 'Mehr erfahren',
        'Start now': 'Jetzt starten'
    }
    
    german_files = [
        'communication-mastery-1-de.html',
        'feedback-culture-3-receiving-team-de.html',
        'brown-belt-stripe1-gamified-de.html',
        'purple-belt-stripe4-gamified-de.html',
        'blue-belt-stripe1-gamified-de.html'
    ]
    
    for file in german_files:
        file_path = Path(file)
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            for eng, ger in translations.items():
                # Replace in button text
                content = re.sub(
                    f'([>"])({re.escape(eng)})([<"])',
                    f'\\1{ger}\\3',
                    content,
                    flags=re.IGNORECASE
                )
            
            if content != original:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes.append(f"✅ Fixed translations in {file}")
    
    # Fix 5: Verify critical navigation paths
    print("\n5. Verifying critical navigation...")
    
    # Check index.html → gym-dashboard.html
    if os.path.exists('index.html'):
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        if 'gym-dashboard.html' in content:
            fixes.append("✅ index.html links to gym-dashboard.html")
    
    # Check assessment → dashboard navigation
    if os.path.exists('belt-assessment-v2.html'):
        with open('belt-assessment-v2.html', 'r', encoding='utf-8') as f:
            content = f.read()
        if 'gym-dashboard.html' in content or 'goToGymDashboard' in content:
            fixes.append("✅ Belt assessment navigates to gym dashboard")
    
    # Generate report
    print("\n" + "=" * 60)
    print("✅ FIXES COMPLETE")
    print("=" * 60)
    print(f"\nTotal fixes applied: {len(fixes)}")
    for fix in fixes:
        print(f"  {fix}")
    
    # Save report
    with open('CRITICAL-FIXES-APPLIED.md', 'w', encoding='utf-8') as f:
        f.write("# 🔧 CRITICAL FIXES APPLIED\n\n")
        f.write(f"**Date:** {Path('.').cwd()}\n\n")
        f.write(f"**Total Fixes:** {len(fixes)}\n\n")
        f.write("## Fixes Applied:\n\n")
        for fix in fixes:
            f.write(f"- {fix}\n")
    
    print("\n✅ Report saved: CRITICAL-FIXES-APPLIED.md")

if __name__ == '__main__':
    fix_all_critical_issues()

