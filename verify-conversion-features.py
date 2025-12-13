#!/usr/bin/env python3

"""
Phase 3: Conversion Features Verification
Verify all 5 conversion booster features are working
"""

import os
import re
from pathlib import Path

def verify_conversion_features():
    print("🚀 PHASE 3: CONVERSION FEATURES VERIFICATION")
    print("=" * 60)
    
    results = {
        'index.html': {'features': [], 'issues': []},
        'gym-dashboard.html': {'features': [], 'issues': []}
    }
    
    # Check index.html
    print("\n1. Verifying index.html conversion features...")
    if os.path.exists('index.html'):
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check CSS
        if 'conversion-boosters.css' in content:
            results['index.html']['features'].append("✅ CSS loaded: conversion-boosters.css")
        else:
            results['index.html']['issues'].append("❌ Missing: conversion-boosters.css")
        
        # Check JS
        if 'conversion-boosters.js' in content:
            results['index.html']['features'].append("✅ JS loaded: conversion-boosters.js")
        else:
            results['index.html']['issues'].append("❌ Missing: conversion-boosters.js")
        
        # Check Live Counter
        if 'tapLiveCounter' in content or 'liveCount' in content:
            results['index.html']['features'].append("✅ Live Counter element present")
        else:
            results['index.html']['issues'].append("❌ Missing: Live Counter element")
        
        # Check Activity Feed
        if 'tapActivityFeed' in content or 'activityFeed' in content:
            results['index.html']['features'].append("✅ Activity Feed element present")
        else:
            results['index.html']['issues'].append("❌ Missing: Activity Feed element")
        
        print(f"   Features: {len(results['index.html']['features'])}")
        print(f"   Issues: {len(results['index.html']['issues'])}")
    
    # Check gym-dashboard.html
    print("\n2. Verifying gym-dashboard.html conversion features...")
    if os.path.exists('gym-dashboard.html'):
        with open('gym-dashboard.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check CSS
        if 'conversion-boosters.css' in content:
            results['gym-dashboard.html']['features'].append("✅ CSS loaded: conversion-boosters.css")
        else:
            results['gym-dashboard.html']['issues'].append("❌ Missing: conversion-boosters.css")
        
        # Check JS
        if 'conversion-boosters.js' in content:
            results['gym-dashboard.html']['features'].append("✅ JS loaded: conversion-boosters.js")
        else:
            results['gym-dashboard.html']['issues'].append("❌ Missing: conversion-boosters.js")
        
        # Check all 5 features
        features_check = {
            'Milestone Tracker': 'tapMilestoneTracker',
            'Streak Widget': 'tapStreakWidget',
            'Leaderboard': 'tapLeaderboardWidget',
            'Activity Feed': 'tapActivityFeed',
            'Live Counter': 'tapLiveCounter'
        }
        
        for feature_name, element_id in features_check.items():
            if element_id in content:
                results['gym-dashboard.html']['features'].append(f"✅ {feature_name} element present")
            else:
                results['gym-dashboard.html']['issues'].append(f"❌ Missing: {feature_name} ({element_id})")
        
        print(f"   Features: {len(results['gym-dashboard.html']['features'])}")
        print(f"   Issues: {len(results['gym-dashboard.html']['issues'])}")
    
    # Check conversion-boosters.js exists and has functions
    print("\n3. Verifying conversion-boosters.js functionality...")
    if os.path.exists('js/conversion-boosters.js'):
        with open('js/conversion-boosters.js', 'r', encoding='utf-8') as f:
            content = f.read()
        
        functions = {
            'updateLiveCounter': 'Live Counter',
            'showNextActivity': 'Activity Feed',
            'updateMilestone': 'Milestone Tracker',
            'updateLeaderboard': 'Leaderboard',
            'updateStreak': 'Streak Tracker'
        }
        
        for func_name, feature_name in functions.items():
            if f'function {func_name}' in content or f'{func_name}()' in content:
                print(f"   ✅ {feature_name} function present")
            else:
                print(f"   ⚠️ {feature_name} function may be missing")
    else:
        print("   ❌ conversion-boosters.js file not found!")
    
    # Check CSS file exists
    print("\n4. Verifying conversion-boosters.css...")
    if os.path.exists('css/conversion-boosters.css'):
        with open('css/conversion-boosters.css', 'r', encoding='utf-8') as f:
            content = f.read()
        
        styles_check = {
            'Live Counter': '.live-counter',
            'Activity Feed': '.activity-feed',
            'Milestone Card': '.milestone-card',
            'Leaderboard': '.leaderboard-widget',
            'Streak Widget': '.streak-widget'
        }
        
        for style_name, class_name in styles_check.items():
            if class_name in content:
                print(f"   ✅ {style_name} styles present")
            else:
                print(f"   ⚠️ {style_name} styles may be missing")
    else:
        print("   ❌ conversion-boosters.css file not found!")
    
    # Generate report
    print("\n" + "=" * 60)
    print("✅ CONVERSION FEATURES VERIFICATION COMPLETE")
    print("=" * 60)
    
    total_features = sum(len(r['features']) for r in results.values())
    total_issues = sum(len(r['issues']) for r in results.values())
    
    print(f"\nTotal Features Verified: {total_features}")
    print(f"Total Issues Found: {total_issues}")
    
    # Save detailed report
    report = "# 🚀 PHASE 3: CONVERSION FEATURES VERIFICATION REPORT\n\n"
    report += "## index.html\n\n"
    for feature in results['index.html']['features']:
        report += f"- {feature}\n"
    if results['index.html']['issues']:
        report += "\n**Issues:**\n"
        for issue in results['index.html']['issues']:
            report += f"- {issue}\n"
    
    report += "\n## gym-dashboard.html\n\n"
    for feature in results['gym-dashboard.html']['features']:
        report += f"- {feature}\n"
    if results['gym-dashboard.html']['issues']:
        report += "\n**Issues:**\n"
        for issue in results['gym-dashboard.html']['issues']:
            report += f"- {issue}\n"
    
    with open('PHASE3-CONVERSION-FEATURES-REPORT.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    print("\n✅ Report saved: PHASE3-CONVERSION-FEATURES-REPORT.md")

if __name__ == '__main__':
    verify_conversion_features()

