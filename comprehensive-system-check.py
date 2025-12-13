#!/usr/bin/env python3
"""
Comprehensive System Check for TAP-IN Platform
Checks: Error handlers, Language switchers, Navigation, Links, Critical paths
"""

import os
import re
from pathlib import Path
from collections import defaultdict

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

issues = defaultdict(list)
warnings = defaultdict(list)
passed = defaultdict(list)

def check_error_handlers():
    """Check for error toast boxes in HTML files"""
    print(f"\n{Colors.BLUE}=== Checking Error Handlers ==={Colors.END}")
    
    html_files = list(Path('.').rglob('*.html'))
    html_files = [f for f in html_files if 'archive' not in str(f) and 'node_modules' not in str(f)]
    
    error_patterns = [
        (r'showErrorToast\(', 'showErrorToast function call'),
        (r'function\s+showErrorToast', 'showErrorToast function definition'),
        (r'showToast.*error', 'showToast with error type'),
    ]
    
    for html_file in html_files:
        try:
            content = html_file.read_text(encoding='utf-8', errors='ignore')
            for pattern, description in error_patterns:
                matches = re.finditer(pattern, content, re.IGNORECASE)
                for match in matches:
                    line_num = content[:match.start()].count('\n') + 1
                    issues['error_handlers'].append({
                        'file': str(html_file),
                        'line': line_num,
                        'issue': description,
                        'context': content[max(0, match.start()-50):match.end()+50].replace('\n', ' ')
                    })
        except Exception as e:
            warnings['error_handlers'].append(f"Could not read {html_file}: {e}")
    
    if issues['error_handlers']:
        print(f"{Colors.RED}❌ Found {len(issues['error_handlers'])} error handler issues{Colors.END}")
        for issue in issues['error_handlers'][:10]:  # Show first 10
            print(f"  {Colors.YELLOW}{issue['file']}:{issue['line']}{Colors.END} - {issue['issue']}")
    else:
        print(f"{Colors.GREEN}✅ No error toast boxes found{Colors.END}")

def check_language_switchers():
    """Check language switcher links are correct"""
    print(f"\n{Colors.BLUE}=== Checking Language Switchers ==={Colors.END}")
    
    critical_files = [
        'belt-assessment-v2.html',
        'belt-assessment-v2-de.html',
        'gym-dashboard.html',
        'gym-dashboard-de.html',
        'index.html',
        'index-DUAL-ENTRY.html',
        'learning-hub.html',
        'learning-hub-de.html',
    ]
    
    for file_path in critical_files:
        if not os.path.exists(file_path):
            warnings['language_switchers'].append(f"File not found: {file_path}")
            continue
        
        try:
            content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
            
            # Check if it's a German file
            is_german = '-de.html' in file_path or 'lang="de"' in content[:500]
            
            # Check for language switcher links
            if is_german:
                # Should link to English version (without -de)
                english_pattern = r"location\.href\s*=\s*['\"]([^'\"]+)['\"]"
                matches = re.finditer(english_pattern, content)
                found_english_link = False
                for match in matches:
                    link = match.group(1)
                    if '-de.html' not in link and '.html' in link:
                        # Check if it links to correct English version
                        expected_english = file_path.replace('-de.html', '.html')
                        if link == expected_english or link.endswith(expected_english.split('/')[-1]):
                            found_english_link = True
                            passed['language_switchers'].append(f"{file_path} → {link} ✅")
                if not found_english_link:
                    issues['language_switchers'].append({
                        'file': file_path,
                        'issue': 'Missing or incorrect English language switcher link'
                    })
            else:
                # Should link to German version (with -de)
                german_pattern = r"location\.href\s*=\s*['\"]([^'\"]+-de\.html)['\"]"
                matches = re.finditer(german_pattern, content)
                found_german_link = False
                for match in matches:
                    link = match.group(1)
                    expected_german = file_path.replace('.html', '-de.html')
                    if link.endswith(expected_german.split('/')[-1]):
                        found_german_link = True
                        passed['language_switchers'].append(f"{file_path} → {link} ✅")
                if not found_german_link and 'index.html' not in file_path:  # index.html has special switcher
                    issues['language_switchers'].append({
                        'file': file_path,
                        'issue': 'Missing or incorrect German language switcher link'
                    })
        except Exception as e:
            warnings['language_switchers'].append(f"Error reading {file_path}: {e}")
    
    print(f"{Colors.GREEN}✅ Passed: {len(passed['language_switchers'])}{Colors.END}")
    if issues['language_switchers']:
        print(f"{Colors.RED}❌ Issues: {len(issues['language_switchers'])}{Colors.END}")
        for issue in issues['language_switchers']:
            print(f"  {Colors.YELLOW}{issue['file']}{Colors.END} - {issue['issue']}")

def check_critical_navigation():
    """Check critical navigation paths"""
    print(f"\n{Colors.BLUE}=== Checking Critical Navigation ==={Colors.END}")
    
    critical_paths = {
        'index.html': ['gym-dashboard.html', 'learning-hub.html', 'belt-assessment-sales-landing.html'],
        'belt-assessment-v2.html': ['gym-dashboard.html'],
        'belt-assessment-v2-de.html': ['gym-dashboard-de.html'],
        'gym-dashboard.html': ['learning-hub.html'],
    }
    
    for source_file, target_files in critical_paths.items():
        if not os.path.exists(source_file):
            warnings['navigation'].append(f"Source file not found: {source_file}")
            continue
        
        try:
            content = Path(source_file).read_text(encoding='utf-8', errors='ignore')
            for target_file in target_files:
                # Check for links to target file
                patterns = [
                    rf"href\s*=\s*['\"]{re.escape(target_file)}['\"]",
                    rf"location\.href\s*=\s*['\"]{re.escape(target_file)}['\"]",
                    rf"window\.location\s*=\s*['\"]{re.escape(target_file)}['\"]",
                ]
                found = False
                for pattern in patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        found = True
                        passed['navigation'].append(f"{source_file} → {target_file} ✅")
                        break
                if not found:
                    issues['navigation'].append({
                        'source': source_file,
                        'target': target_file,
                        'issue': 'Missing navigation link'
                    })
        except Exception as e:
            warnings['navigation'].append(f"Error reading {source_file}: {e}")
    
    print(f"{Colors.GREEN}✅ Passed: {len(passed['navigation'])}{Colors.END}")
    if issues['navigation']:
        print(f"{Colors.RED}❌ Issues: {len(issues['navigation'])}{Colors.END}")
        for issue in issues['navigation']:
            print(f"  {Colors.YELLOW}{issue['source']}{Colors.END} → {issue['target']} - {issue['issue']}")

def check_assessment_links():
    """Check assessment file links"""
    print(f"\n{Colors.BLUE}=== Checking Assessment Links ==={Colors.END}")
    
    # Check sales landing pages link to correct assessments
    landing_to_assessment = {
        'belt-assessment-sales-landing.html': 'belt-assessment-v2.html',
        'belt-assessment-sales-landing-de.html': 'belt-assessment-v2-de.html',
    }
    
    for landing_file, assessment_file in landing_to_assessment.items():
        if not os.path.exists(landing_file):
            warnings['assessment_links'].append(f"Landing file not found: {landing_file}")
            continue
        
        try:
            content = Path(landing_file).read_text(encoding='utf-8', errors='ignore')
            if assessment_file in content:
                passed['assessment_links'].append(f"{landing_file} → {assessment_file} ✅")
            else:
                issues['assessment_links'].append({
                    'file': landing_file,
                    'expected': assessment_file,
                    'issue': 'Does not link to correct assessment file'
                })
        except Exception as e:
            warnings['assessment_links'].append(f"Error reading {landing_file}: {e}")
    
    print(f"{Colors.GREEN}✅ Passed: {len(passed['assessment_links'])}{Colors.END}")
    if issues['assessment_links']:
        print(f"{Colors.RED}❌ Issues: {len(issues['assessment_links'])}{Colors.END}")
        for issue in issues['assessment_links']:
            print(f"  {Colors.YELLOW}{issue['file']}{Colors.END} - Expected: {issue['expected']}")

def check_service_worker():
    """Check service worker configuration"""
    print(f"\n{Colors.BLUE}=== Checking Service Worker ==={Colors.END}")
    
    sw_file = 'sw.js'
    if os.path.exists(sw_file):
        try:
            content = Path(sw_file).read_text(encoding='utf-8', errors='ignore')
            
            # Check if it bypasses HTML files (especially gym-dashboard)
            if 'gym-dashboard.html' in content and 'bypass' in content.lower():
                passed['service_worker'].append("Service worker bypasses gym-dashboard.html ✅")
            else:
                warnings['service_worker'].append("Service worker might be caching gym-dashboard.html")
            
            # Check cache version
            cache_version_match = re.search(r'CACHE_VERSION\s*=\s*["\']([^"\']+)["\']', content)
            if cache_version_match:
                passed['service_worker'].append(f"Cache version: {cache_version_match.group(1)} ✅")
        except Exception as e:
            warnings['service_worker'].append(f"Error reading sw.js: {e}")
    else:
        warnings['service_worker'].append("Service worker file not found")
    
    print(f"{Colors.GREEN}✅ Passed: {len(passed['service_worker'])}{Colors.END}")
    if warnings['service_worker']:
        for warning in warnings['service_worker']:
            print(f"  {Colors.YELLOW}⚠️  {warning}{Colors.END}")

def generate_report():
    """Generate comprehensive report"""
    total_issues = sum(len(issues[key]) for key in issues)
    total_warnings = sum(len(warnings[key]) for key in warnings)
    
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BLUE}COMPREHENSIVE SYSTEM CHECK REPORT{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}\n")
    
    print(f"Total Issues: {Colors.RED}{total_issues}{Colors.END}")
    print(f"Total Warnings: {Colors.YELLOW}{total_warnings}{Colors.END}\n")
    
    if total_issues == 0 and total_warnings == 0:
        print(f"{Colors.GREEN}✅ ALL CHECKS PASSED!{Colors.END}\n")
        return True
    
    # Detailed issues
    for category, issue_list in issues.items():
        if issue_list:
            print(f"\n{Colors.RED}{category.upper().replace('_', ' ')}:{Colors.END}")
            for issue in issue_list[:5]:  # Show first 5
                if isinstance(issue, dict):
                    if 'file' in issue:
                        print(f"  • {issue['file']}")
                        if 'line' in issue:
                            print(f"    Line {issue['line']}: {issue.get('issue', 'Unknown issue')}")
    
    return False

def main():
    print(f"{Colors.BLUE}TAP-IN Comprehensive System Check{Colors.END}\n")
    
    check_error_handlers()
    check_language_switchers()
    check_critical_navigation()
    check_assessment_links()
    check_service_worker()
    
    all_clear = generate_report()
    
    return 0 if all_clear else 1

if __name__ == '__main__':
    exit(main())

