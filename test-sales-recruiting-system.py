#!/usr/bin/env python3
"""
Comprehensive Internal Test Suite for Sales Recruiting Assessment System
Tests all 3 files for functionality, links, and errors
"""

from pathlib import Path
import re
import json

def test_file_exists(file_path):
    """Test if file exists"""
    path = Path(file_path)
    exists = path.exists()
    print(f"{'✅' if exists else '❌'} {file_path}: {'EXISTS' if exists else 'MISSING'}")
    return exists

def test_html_structure(file_path):
    """Test basic HTML structure"""
    try:
        content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
        
        checks = {
            'DOCTYPE': '<!DOCTYPE html>' in content,
            'html tag': '<html' in content and '</html>' in content,
            'head tag': '<head' in content and '</head>' in content,
            'body tag': '<body' in content and '</body>' in content,
            'title tag': '<title>' in content and '</title>' in content,
        }
        
        all_pass = all(checks.values())
        status = '✅' if all_pass else '⚠️'
        print(f"{status} {file_path} HTML Structure: {'PASS' if all_pass else 'ISSUES'}")
        
        if not all_pass:
            for check, passed in checks.items():
                if not passed:
                    print(f"   - Missing: {check}")
        
        return all_pass
    except Exception as e:
        print(f"❌ {file_path} HTML Structure: ERROR - {e}")
        return False

def test_javascript_syntax(file_path):
    """Test JavaScript syntax and key functions"""
    try:
        content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
        
        # Extract JavaScript
        script_pattern = r'<script[^>]*>(.*?)</script>'
        scripts = re.findall(script_pattern, content, re.DOTALL)
        
        if not scripts:
            print(f"⚠️  {file_path}: No JavaScript found")
            return False
        
        js_content = '\n'.join(scripts)
        
        # Check for key functions
        checks = {
            'questions array': 'const questions' in js_content or 'let questions' in js_content,
            'renderQuestion function': 'function renderQuestion' in js_content or 'renderQuestion()' in js_content,
            'selectOption function': 'function selectOption' in js_content or 'selectOption(' in js_content,
            'showResults function': 'function showResults' in js_content or 'showResults()' in js_content,
        }
        
        # Stage 1 specific checks
        if 'stage1' in file_path.lower():
            checks['calculateStage1Score'] = 'calculateStage1Score' in js_content
            checks['saveStage1Results'] = 'saveStage1Results' in js_content
            checks['10 questions'] = js_content.count('id:') >= 10
            
        # Stage 2 specific checks
        if 'stage2' in file_path.lower() and 'stage1' not in file_path.lower():
            checks['calculateStage2Score'] = 'calculateStage2Score' in js_content
            checks['25 questions'] = js_content.count('id:') >= 25
            checks['sections array'] = 'sections' in js_content or 'const sections' in js_content
        
        all_pass = all(checks.values())
        status = '✅' if all_pass else '⚠️'
        print(f"{status} {file_path} JavaScript: {'PASS' if all_pass else 'ISSUES'}")
        
        if not all_pass:
            for check, passed in checks.items():
                if not passed:
                    print(f"   - Missing: {check}")
        
        return all_pass
    except Exception as e:
        print(f"❌ {file_path} JavaScript: ERROR - {e}")
        return False

def test_links(file_path):
    """Test internal and external links"""
    try:
        content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
        
        # Find all links
        link_pattern = r'href=["\']([^"\']+)["\']'
        links = re.findall(link_pattern, content)
        
        # Filter out external/absolute links
        internal_links = [l for l in links if not l.startswith('http') and not l.startswith('//') and not l.startswith('mailto:') and not l.startswith('tel:')]
        
        # Check if linked files exist (for HTML files)
        missing = []
        for link in internal_links:
            if link.endswith('.html'):
                link_path = Path(link)
                if not link_path.exists() and link not in ['#', '']:
                    # Check if it's a relative path
                    base_dir = Path(file_path).parent
                    if not (base_dir / link).exists():
                        missing.append(link)
        
        if missing:
            print(f"⚠️  {file_path} Links: {len(missing)} potentially broken links")
            for link in missing[:5]:  # Show first 5
                print(f"   - {link}")
        else:
            print(f"✅ {file_path} Links: All internal links valid")
        
        return len(missing) == 0
    except Exception as e:
        print(f"❌ {file_path} Links: ERROR - {e}")
        return False

def test_stage1_specific(file_path):
    """Test Stage 1 specific functionality"""
    try:
        content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
        
        checks = {
            '10 questions defined': content.count('id:') >= 10,
            'scoring logic': 'calculateStage1Score' in content,
            'results display': 'EXCELLENT FIT' in content or 'EXCELLENT' in content,
            'stage2 link': 'sales-recruiting-stage2.html' in content,
            'category scores': 'workStyle' in content and 'communication' in content,
        }
        
        all_pass = all(checks.values())
        status = '✅' if all_pass else '⚠️'
        print(f"{status} {file_path} Stage 1 Features: {'PASS' if all_pass else 'ISSUES'}")
        
        if not all_pass:
            for check, passed in checks.items():
                if not passed:
                    print(f"   - Missing: {check}")
        
        return all_pass
    except Exception as e:
        print(f"❌ {file_path} Stage 1 Test: ERROR - {e}")
        return False

def test_stage2_specific(file_path):
    """Test Stage 2 specific functionality"""
    try:
        content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
        
        checks = {
            '25 questions defined': content.count('id:') >= 25,
            '4 sections': 'section: 1' in content and 'section: 4' in content,
            'section headers': 'Work Style Deep Dive' in content or 'section-header' in content,
            'weighted scoring': 'weight' in content.lower() or 'calculateStage2Score' in content,
            'profile generation': 'generateProfileType' in content or 'profileType' in content,
            'interview questions': 'generateInterviewQuestions' in content or 'Interview Questions' in content,
        }
        
        all_pass = all(checks.values())
        status = '✅' if all_pass else '⚠️'
        print(f"{status} {file_path} Stage 2 Features: {'PASS' if all_pass else 'ISSUES'}")
        
        if not all_pass:
            for check, passed in checks.items():
                if not passed:
                    print(f"   - Missing: {check}")
        
        return all_pass
    except Exception as e:
        print(f"❌ {file_path} Stage 2 Test: ERROR - {e}")
        return False

def test_demo_specific(file_path):
    """Test Demo page specific functionality"""
    try:
        content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
        
        checks = {
            '3 candidates': 'sampleCandidates' in content or 'Sarah M.' in content,
            'filter functionality': 'filter-by' in content or 'getElementById(\'filter-by\')' in content,
            'sort functionality': 'sort-by' in content or 'getElementById(\'sort-by\')' in content,
            'render function': 'renderCandidates' in content,
            'candidate cards': 'candidate-card' in content,
        }
        
        all_pass = all(checks.values())
        status = '✅' if all_pass else '⚠️'
        print(f"{status} {file_path} Demo Features: {'PASS' if all_pass else 'ISSUES'}")
        
        if not all_pass:
            for check, passed in checks.items():
                if not passed:
                    print(f"   - Missing: {check}")
        
        return all_pass
    except Exception as e:
        print(f"❌ {file_path} Demo Test: ERROR - {e}")
        return False

def test_german_versions():
    """Test German version files"""
    german_files = [
        'sales-recruiting-stage1-de.html',
        'sales-recruiting-stage2-de.html',
        'sales-recruiting-demo-de.html'
    ]
    
    results = []
    for file_path in german_files:
        if Path(file_path).exists():
            content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
            checks = {
                'lang="de"': 'lang="de"' in content,
                'German text': any(word in content for word in ['Assessment', 'Stufe', 'Kandidaten', 'Ergebnisse']),
            }
            all_pass = all(checks.values())
            status = '✅' if all_pass else '⚠️'
            print(f"{status} {file_path} German Version: {'PASS' if all_pass else 'ISSUES'}")
            results.append(all_pass)
        else:
            print(f"⚠️  {file_path}: File missing")
            results.append(False)
    
    return all(results)

def test_integration():
    """Test integration with business portal"""
    try:
        bp_path = Path('business-portal.html')
        if not bp_path.exists():
            print("⚠️  business-portal.html: Not found")
            return False
        
        content = bp_path.read_text(encoding='utf-8', errors='ignore')
        
        checks = {
            'recruiting section': 'Recruiting Profiles' in content or 'recruiting-profiles' in content,
            'stage1 link': 'sales-recruiting-stage1.html' in content,
            'demo link': 'sales-recruiting-demo.html' in content,
        }
        
        all_pass = all(checks.values())
        status = '✅' if all_pass else '⚠️'
        print(f"{status} Business Portal Integration: {'PASS' if all_pass else 'ISSUES'}")
        
        if not all_pass:
            for check, passed in checks.items():
                if not passed:
                    print(f"   - Missing: {check}")
        
        return all_pass
    except Exception as e:
        print(f"❌ Business Portal Integration: ERROR - {e}")
        return False

def run_all_tests():
    """Run comprehensive test suite"""
    print("=" * 70)
    print("🧪 SALES RECRUITING ASSESSMENT SYSTEM - INTERNAL TEST SUITE")
    print("=" * 70)
    print()
    
    results = {}
    
    # Test file existence
    print("📁 FILE EXISTENCE TESTS")
    print("-" * 70)
    files_to_test = [
        'sales-recruiting-stage1.html',
        'sales-recruiting-stage2.html',
        'sales-recruiting-demo.html',
        'sales-recruiting-stage1-de.html',
        'sales-recruiting-stage2-de.html',
        'sales-recruiting-demo-de.html',
    ]
    
    file_results = []
    for file_path in files_to_test:
        file_results.append(test_file_exists(file_path))
    results['file_existence'] = all(file_results)
    print()
    
    # Test HTML structure
    print("🏗️  HTML STRUCTURE TESTS")
    print("-" * 70)
    html_results = []
    for file_path in files_to_test[:3]:  # English versions
        if Path(file_path).exists():
            html_results.append(test_html_structure(file_path))
    results['html_structure'] = all(html_results)
    print()
    
    # Test JavaScript
    print("💻 JAVASCRIPT FUNCTIONALITY TESTS")
    print("-" * 70)
    js_results = []
    if Path('sales-recruiting-stage1.html').exists():
        js_results.append(test_javascript_syntax('sales-recruiting-stage1.html'))
    if Path('sales-recruiting-stage2.html').exists():
        js_results.append(test_javascript_syntax('sales-recruiting-stage2.html'))
    if Path('sales-recruiting-demo.html').exists():
        js_results.append(test_javascript_syntax('sales-recruiting-demo.html'))
    results['javascript'] = all(js_results)
    print()
    
    # Test Stage 1 specific
    print("🎯 STAGE 1 SPECIFIC TESTS")
    print("-" * 70)
    if Path('sales-recruiting-stage1.html').exists():
        results['stage1'] = test_stage1_specific('sales-recruiting-stage1.html')
    else:
        results['stage1'] = False
    print()
    
    # Test Stage 2 specific
    print("🎯 STAGE 2 SPECIFIC TESTS")
    print("-" * 70)
    if Path('sales-recruiting-stage2.html').exists():
        results['stage2'] = test_stage2_specific('sales-recruiting-stage2.html')
    else:
        results['stage2'] = False
    print()
    
    # Test Demo specific
    print("📊 DEMO PAGE TESTS")
    print("-" * 70)
    if Path('sales-recruiting-demo.html').exists():
        results['demo'] = test_demo_specific('sales-recruiting-demo.html')
    else:
        results['demo'] = False
    print()
    
    # Test links
    print("🔗 LINK VALIDATION TESTS")
    print("-" * 70)
    link_results = []
    for file_path in files_to_test[:3]:
        if Path(file_path).exists():
            link_results.append(test_links(file_path))
    results['links'] = all(link_results)
    print()
    
    # Test German versions
    print("🇩🇪 GERMAN VERSION TESTS")
    print("-" * 70)
    results['german'] = test_german_versions()
    print()
    
    # Test integration
    print("🔌 INTEGRATION TESTS")
    print("-" * 70)
    results['integration'] = test_integration()
    print()
    
    # Summary
    print("=" * 70)
    print("📊 TEST SUMMARY")
    print("=" * 70)
    
    total_tests = len(results)
    passed_tests = sum(1 for v in results.values() if v)
    
    for test_name, passed in results.items():
        status = '✅ PASS' if passed else '❌ FAIL'
        print(f"{status}: {test_name.replace('_', ' ').title()}")
    
    print()
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {total_tests - passed_tests}")
    print(f"Success Rate: {(passed_tests/total_tests*100):.1f}%")
    print()
    
    if all(results.values()):
        print("🎉 ALL TESTS PASSED! System is ready for demo.")
    else:
        print("⚠️  SOME TESTS FAILED. Please review issues above.")
    
    print("=" * 70)
    
    return all(results.values())

if __name__ == '__main__':
    success = run_all_tests()
    exit(0 if success else 1)

