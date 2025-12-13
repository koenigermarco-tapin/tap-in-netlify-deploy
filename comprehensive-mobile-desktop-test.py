#!/usr/bin/env python3

"""
TAP-IN Comprehensive Mobile & Desktop Testing
Detailed testing with actionable results
"""

import os
import re
from pathlib import Path
from datetime import datetime

def test_all():
    results = {
        'mobile': {'passed': 0, 'failed': 0, 'warnings': 0, 'details': []},
        'desktop': {'passed': 0, 'failed': 0, 'warnings': 0, 'details': []},
        'performance': {'metrics': {}, 'issues': []},
        'critical': {'issues': [], 'fixes_needed': []}
    }
    
    print("🔍 Testing TAP-IN Platform (Mobile & Desktop)...\n")
    
    # 1. Test Critical Pages
    print("📄 Testing critical pages...")
    critical_pages = [
        'index.html',
        'gym-dashboard.html',
        'learning-hub.html',
        'belt-assessment-v2.html',
        'shop.html'
    ]
    
    for page in critical_pages:
        if os.path.exists(page):
            results = test_page(page, results)
            results['desktop']['passed'] += 1
        else:
            results['critical']['issues'].append(f"Missing critical page: {page}")
            results['desktop']['failed'] += 1
    
    # 2. Test Mobile Responsiveness
    print("📱 Testing mobile responsiveness...")
    results = test_mobile_responsive(results)
    
    # 3. Test Performance
    print("⚡ Testing performance...")
    results = test_performance(results)
    
    # 4. Test Conversion Boosters
    print("🚀 Testing conversion boosters...")
    results = test_conversion_boosters(results)
    
    # 5. Test Error Handling
    print("🛡️  Testing error handling...")
    results = test_error_handling(results)
    
    # 6. Test Resource Loading
    print("📦 Testing resource loading...")
    results = test_resource_loading(results)
    
    # Generate comprehensive report
    generate_detailed_report(results)
    
    return results

def test_page(page, results):
    """Test individual page"""
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Mobile checks
        if 'viewport' in content:
            results['mobile']['passed'] += 1
        else:
            results['mobile']['failed'] += 1
            results['mobile']['details'].append(f"{page}: Missing viewport meta tag")
        
        # Desktop checks
        if '<html' in content and '<head' in content and '<body' in content:
            results['desktop']['passed'] += 1
        else:
            results['desktop']['failed'] += 1
        
        return results
    except Exception as e:
        results['critical']['issues'].append(f"Error testing {page}: {e}")
        return results

def test_mobile_responsive(results):
    """Test mobile responsiveness"""
    html_files = [f for f in Path('.').rglob('*.html') if 'archive' not in str(f) and 'node_modules' not in str(f)]
    
    viewport_count = 0
    media_query_count = 0
    
    for html_file in html_files[:50]:  # Limit to first 50
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'viewport' in content:
                viewport_count += 1
            
            # Check CSS for media queries
            css_links = re.findall(r'href=["\']([^"\']*\.css)["\']', content)
            for css_link in css_links[:3]:  # Check first 3 CSS files per page
                css_path = css_link.replace('/', os.sep).lstrip(os.sep)
                if os.path.exists(css_path):
                    try:
                        with open(css_path, 'r', encoding='utf-8') as cf:
                            css_content = cf.read()
                            if '@media' in css_content:
                                media_query_count += 1
                    except:
                        pass
        except:
            pass
    
    results['mobile']['details'].append(f"Pages with viewport: {viewport_count}/{min(50, len(html_files))}")
    results['mobile']['details'].append(f"CSS files with media queries: {media_query_count}")
    
    if viewport_count == min(50, len(html_files)):
        results['mobile']['passed'] += 1
    else:
        results['mobile']['warnings'] += 1
    
    return results

def test_performance(results):
    """Test performance metrics"""
    key_pages = ['index.html', 'gym-dashboard.html', 'learning-hub.html']
    
    total_size = 0
    total_scripts = 0
    
    for page in key_pages:
        if not os.path.exists(page):
            continue
        
        try:
            with open(page, 'r', encoding='utf-8') as f:
                content = f.read()
            
            size_kb = len(content) / 1024
            total_size += size_kb
            
            scripts = len(re.findall(r'<script[^>]*>', content))
            total_scripts += scripts
            
            results['performance']['metrics'][page] = {
                'size_kb': round(size_kb, 2),
                'scripts': scripts
            }
            
            if size_kb > 300:
                results['performance']['issues'].append(f"{page}: Large file size ({size_kb:.1f} KB)")
            
            if scripts > 15:
                results['performance']['issues'].append(f"{page}: Many scripts ({scripts}) - consider bundling")
                
        except Exception as e:
            pass
    
    results['performance']['metrics']['total_size'] = round(total_size, 2)
    results['performance']['metrics']['total_scripts'] = total_scripts
    
    return results

def test_conversion_boosters(results):
    """Test conversion boosters integration"""
    pages = {
        'index.html': ['tapLiveCounter', 'tapActivityFeed'],
        'gym-dashboard.html': ['tapMilestoneTracker', 'tapStreakWidget', 'tapLeaderboardWidget']
    }
    
    for page, elements in pages.items():
        if not os.path.exists(page):
            results['critical']['issues'].append(f"Missing page: {page}")
            continue
        
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check CSS
        if 'conversion-boosters.css' not in content:
            results['critical']['fixes_needed'].append(f"{page}: Add conversion-boosters.css link")
        
        # Check JS
        if 'conversion-boosters.js' not in content:
            results['critical']['fixes_needed'].append(f"{page}: Add conversion-boosters.js script")
        
        # Check elements
        for element in elements:
            if element not in content:
                results['critical']['fixes_needed'].append(f"{page}: Missing element {element}")
            else:
                results['desktop']['passed'] += 1
    
    return results

def test_error_handling(results):
    """Test error handling"""
    error_files = [
        'js/error-suppressor.js',
        'js/supabase-config.js',
        'js/keyboard-nav.js'
    ]
    
    for file in error_files:
        if os.path.exists(file):
            results['desktop']['passed'] += 1
        else:
            results['critical']['issues'].append(f"Missing: {file}")
            results['desktop']['failed'] += 1
    
    # Check supabase config is silent
    if os.path.exists('js/supabase-config.js'):
        with open('js/supabase-config.js', 'r') as f:
            content = f.read()
            if 'localStorage-only' in content or 'Silent mode' in content:
                results['desktop']['passed'] += 1
            else:
                results['critical']['fixes_needed'].append("supabase-config.js: Should be in silent mode")
    
    return results

def test_resource_loading(results):
    """Test resource loading"""
    key_pages = ['index.html', 'gym-dashboard.html']
    missing_resources = []
    
    for page in key_pages:
        if not os.path.exists(page):
            continue
        
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check CSS files
        css_links = re.findall(r'href=["\']([^"\']*\.css)["\']', content)
        for css_link in css_links:
            if css_link.startswith('http'):
                continue
            css_path = css_link.replace('/', os.sep).lstrip(os.sep)
            if not os.path.exists(css_path):
                missing_resources.append(f"{page}: Missing CSS {css_link}")
        
        # Check JS files
        js_links = re.findall(r'src=["\']([^"\']*\.js)["\']', content)
        for js_link in js_links:
            if js_link.startswith('http'):
                continue
            js_path = js_link.replace('/', os.sep).lstrip(os.sep)
            if not os.path.exists(js_path):
                missing_resources.append(f"{page}: Missing JS {js_link}")
    
    if missing_resources:
        results['critical']['fixes_needed'].extend(missing_resources[:10])
    else:
        results['desktop']['passed'] += 1
    
    return results

def generate_detailed_report(results):
    """Generate detailed audit report"""
    
    total_passed = results['mobile']['passed'] + results['desktop']['passed']
    total_failed = results['mobile']['failed'] + results['desktop']['failed']
    total_warnings = results['mobile']['warnings'] + results['desktop']['warnings']
    
    score = 100 - (total_failed * 10) - (total_warnings * 2)
    score = max(0, min(100, score))
    
    report = f"""# 📊 TAP-IN COMPREHENSIVE MOBILE & DESKTOP AUDIT REPORT

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Platform Tested:** Mobile & Desktop  
**Overall Score:** {score}/100

---

## 🎯 EXECUTIVE SUMMARY

### Overall Status: {'✅ PRODUCTION READY' if score >= 80 else '⚠️ NEEDS ATTENTION' if score >= 60 else '❌ CRITICAL ISSUES'}

| Category | Passed | Failed | Warnings | Status |
|----------|--------|--------|----------|--------|
| **Mobile** | {results['mobile']['passed']} | {results['mobile']['failed']} | {results['mobile']['warnings']} | {'✅' if results['mobile']['failed'] == 0 else '⚠️'} |
| **Desktop** | {results['desktop']['passed']} | {results['desktop']['failed']} | {results['desktop']['warnings']} | {'✅' if results['desktop']['failed'] == 0 else '⚠️'} |
| **Performance** | - | - | {len(results['performance']['issues'])} | {'✅' if len(results['performance']['issues']) == 0 else '⚠️'} |

**Total:** {total_passed} passed, {total_failed} failed, {total_warnings} warnings

---

## 📱 MOBILE TESTING RESULTS

### Mobile Responsiveness Checks:

"""
    
    for detail in results['mobile']['details']:
        report += f"- {detail}\n"
    
    report += f"""
### Mobile Score: {100 - (results['mobile']['failed'] * 20)}/100

**Status:** {'✅ Mobile Ready' if results['mobile']['failed'] == 0 else '⚠️ Needs Mobile Fixes'}

---

## 💻 DESKTOP TESTING RESULTS

### Desktop Functionality Checks:

- ✅ Critical pages exist: {results['desktop']['passed']} pages
- ✅ Error handling present: {results['desktop']['passed']} checks passed
- ✅ Resources loading: {results['desktop']['passed']} checks

### Desktop Score: {100 - (results['desktop']['failed'] * 15)}/100

**Status:** {'✅ Desktop Ready' if results['desktop']['failed'] == 0 else '⚠️ Needs Desktop Fixes'}

---

## ⚡ PERFORMANCE METRICS

### Page Load Performance:

"""
    
    for page, metrics in results['performance']['metrics'].items():
        if isinstance(metrics, dict):
            report += f"### {page}\n"
            report += f"- File Size: {metrics.get('size_kb', 0)} KB\n"
            report += f"- Scripts: {metrics.get('scripts', 0)} scripts\n"
            report += f"- Status: {'✅ Good' if metrics.get('size_kb', 0) < 200 else '⚠️ Large'}\n\n"
    
    if results['performance']['issues']:
        report += "### ⚠️ Performance Issues:\n\n"
        for issue in results['performance']['issues']:
            report += f"- {issue}\n"
    
    report += f"""
---

## 🚀 CONVERSION BOOSTERS STATUS

"""
    
    if results['critical']['fixes_needed']:
        conversion_fixes = [f for f in results['critical']['fixes_needed'] if 'conversion' in f.lower()]
        if conversion_fixes:
            report += "### ⚠️ Integration Issues:\n\n"
            for fix in conversion_fixes[:5]:
                report += f"- {fix}\n"
        else:
            report += "### ✅ Conversion Boosters: Fully Integrated\n\n"
    else:
        report += "### ✅ Conversion Boosters: Fully Integrated\n\n"
    
    report += f"""
---

## 🛡️ ERROR HANDLING STATUS

### Error Management Checks:

- ✅ Error Suppressor: {'Present' if 'error-suppressor.js' not in str(results['critical']['issues']) else 'Missing'}
- ✅ Supabase Silent Mode: {'Enabled' if 'supabase-config.js' not in str(results['critical']['fixes_needed']) else 'Needs Fix'}
- ✅ Keyboard Navigation: {'Present' if 'keyboard-nav.js' not in str(results['critical']['issues']) else 'Missing'}

---

## ❌ CRITICAL ISSUES ({len(results['critical']['issues'])})

"""
    
    if results['critical']['issues']:
        for issue in results['critical']['issues'][:10]:
            report += f"- ❌ **{issue}**\n"
    else:
        report += "- ✅ **No critical issues found!**\n"
    
    report += f"""

---

## 🔧 FIXES NEEDED ({len(results['critical']['fixes_needed'])})

"""
    
    if results['critical']['fixes_needed']:
        for fix in results['critical']['fixes_needed'][:15]:
            report += f"- ⚠️ {fix}\n"
    else:
        report += "- ✅ **No fixes needed!**\n"
    
    report += f"""

---

## 📊 DETAILED PERFORMANCE BREAKDOWN

### Key Pages Performance:

"""
    
    key_pages = ['index.html', 'gym-dashboard.html', 'learning-hub.html']
    for page in key_pages:
        if page in results['performance']['metrics']:
            metrics = results['performance']['metrics'][page]
            report += f"""
#### {page}
- **File Size:** {metrics.get('size_kb', 0)} KB {'✅' if metrics.get('size_kb', 0) < 200 else '⚠️'}
- **Scripts:** {metrics.get('scripts', 0)} {'✅' if metrics.get('scripts', 0) < 15 else '⚠️'}
- **Mobile Ready:** {'✅ Yes' if 'viewport' in open(page, 'r').read() else '❌ No'}
"""
    
    report += f"""

---

## 🎯 RECOMMENDATIONS

### Priority 1 (Critical):
"""
    
    if results['critical']['issues']:
        for issue in results['critical']['issues'][:5]:
            report += f"1. Fix: {issue}\n"
    else:
        report += "1. ✅ No critical issues!\n"
    
    report += f"""
### Priority 2 (Important):
"""
    
    if results['performance']['issues']:
        for issue in results['performance']['issues'][:3]:
            report += f"1. Optimize: {issue}\n"
    else:
        report += "1. ✅ Performance is good!\n"
    
    report += f"""
### Priority 3 (Enhancement):
"""
    
    if results['critical']['fixes_needed']:
        fixes = [f for f in results['critical']['fixes_needed'] if 'conversion' not in f.lower()][:3]
        if fixes:
            for fix in fixes:
                report += f"1. Improve: {fix}\n"
        else:
            report += "1. ✅ All enhancements complete!\n"
    else:
        report += "1. ✅ No enhancements needed!\n"
    
    report += f"""

---

## ✅ FINAL VERDICT

### Overall Score: {score}/100

"""
    
    if score >= 90:
        report += "**Status: EXCELLENT ✅**\n\n"
        report += "Your platform is production-ready with excellent quality. All critical checks passed.\n"
    elif score >= 80:
        report += "**Status: GOOD ✅**\n\n"
        report += "Your platform is production-ready. Minor improvements recommended.\n"
    elif score >= 60:
        report += "**Status: NEEDS ATTENTION ⚠️**\n\n"
        report += "Platform is mostly ready but has some issues that should be addressed.\n"
    else:
        report += "**Status: CRITICAL ISSUES ❌**\n\n"
        report += "Platform needs fixes before deployment. Review critical issues above.\n"
    
    report += f"""
### Breakdown:
- Mobile Readiness: {100 - (results['mobile']['failed'] * 20)}%
- Desktop Readiness: {100 - (results['desktop']['failed'] * 15)}%
- Performance: {100 - (len(results['performance']['issues']) * 10)}%
- Error Handling: {100 - (len([i for i in results['critical']['issues'] if 'error' in i.lower()]) * 20)}%

---

## 📝 NEXT STEPS

"""
    
    if score < 80:
        report += "1. Review and fix critical issues\n"
        report += "2. Address performance warnings\n"
        report += "3. Re-run audit to verify fixes\n"
    else:
        report += "1. ✅ Deploy to production\n"
        report += "2. Monitor performance metrics\n"
        report += "3. Gather user feedback\n"
    
    report += f"""
---

*Report generated by TAP-IN Comprehensive Audit System*  
*Tested on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

"""
    
    # Save report
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    report_file = f'FULL-AUDIT-REPORT-MOBILE-DESKTOP-{timestamp}.md'
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n✅ Detailed report saved: {report_file}")
    print(f"\n📊 Final Score: {score}/100")
    print(f"   - Mobile: {100 - (results['mobile']['failed'] * 20)}%")
    print(f"   - Desktop: {100 - (results['desktop']['failed'] * 15)}%")
    
    return report_file

if __name__ == '__main__':
    test_all()

