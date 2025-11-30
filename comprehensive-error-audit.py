#!/usr/bin/env python3
"""
Comprehensive error audit - find all error sources and their root causes
"""

import re
import os
from pathlib import Path
from collections import defaultdict

error_sources = defaultdict(list)

def audit_file(filepath):
    """Audit a file for error sources"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(filepath)
        
        # 1. Error event listeners
        error_listeners = re.findall(r"addEventListener\(['\"]error['\"][^\)]*\)", content)
        if error_listeners:
            error_sources['error_listeners'].append({
                'file': filename,
                'count': len(error_listeners),
                'lines': error_listeners[:3]  # First 3 examples
            })
        
        # 2. Unhandled rejection listeners
        rejection_listeners = re.findall(r"addEventListener\(['\"]unhandledrejection['\"][^\)]*\)", content)
        if rejection_listeners:
            error_sources['rejection_listeners'].append({
                'file': filename,
                'count': len(rejection_listeners),
                'lines': rejection_listeners[:3]
            })
        
        # 3. Console.error calls (potential user-facing errors)
        console_errors = re.findall(r'console\.error\([^\)]+\)', content)
        if console_errors:
            error_sources['console_errors'].append({
                'file': filename,
                'count': len(console_errors)
            })
        
        # 4. Service Worker registrations (common error source)
        sw_registrations = re.findall(r'serviceWorker\.register\([^\)]+\)', content)
        if sw_registrations:
            error_sources['service_worker'].append({
                'file': filename,
                'count': len(sw_registrations),
                'has_catch': '.catch' in content[content.find(sw_registrations[0]):content.find(sw_registrations[0])+200] if sw_registrations else False
            })
        
        # 5. Fetch/network errors (unhandled)
        fetch_calls = re.findall(r'fetch\([^\)]+\)', content)
        unhandled_fetch = []
        for fetch_call in fetch_calls:
            # Check if fetch has .catch or try/catch
            fetch_idx = content.find(fetch_call)
            next_200 = content[fetch_idx:fetch_idx+200]
            if '.catch' not in next_200 and 'try' not in content[max(0, fetch_idx-50):fetch_idx]:
                unhandled_fetch.append(fetch_call)
        
        if unhandled_fetch:
            error_sources['unhandled_fetch'].append({
                'file': filename,
                'count': len(unhandled_fetch)
            })
        
        # 6. localStorage operations (can throw errors)
        localStorage_ops = re.findall(r'localStorage\.(getItem|setItem|removeItem)\([^\)]+\)', content)
        unprotected_ls = []
        for ls_op in localStorage_ops:
            ls_idx = content.find(ls_op)
            prev_100 = content[max(0, ls_idx-100):ls_idx]
            if 'try' not in prev_100:
                unprotected_ls.append(ls_op)
        
        if unprotected_ls:
            error_sources['unprotected_storage'].append({
                'file': filename,
                'count': len(unprotected_ls)
            })
        
        # 7. Missing error suppression for expected errors
        expected_error_patterns = ['service-worker', 'sw.js', 'favicon', 'analytics']
        has_error_handler = 'addEventListener' in content and 'error' in content
        if has_error_handler:
            # Check if error handler suppresses expected errors
            error_handler_code = re.search(r"addEventListener\(['\"]error['\"][^}]+", content, re.DOTALL)
            if error_handler_code:
                handler_code = error_handler_code.group(0)
                suppresses_expected = any(pattern in handler_code.lower() for pattern in expected_error_patterns)
                if not suppresses_expected:
                    error_sources['no_suppression'].append({
                        'file': filename,
                        'issue': 'Error handler does not suppress expected errors'
                    })
        
    except Exception as e:
        print(f"Error auditing {filepath}: {e}")

# Audit all HTML and JS files
html_files = []
js_files = []

for root, dirs, files in os.walk('.'):
    skip_dirs = {'.git', 'node_modules', 'android', 'ios', 'dist', 'build', '__pycache__', 'react-app'}
    dirs[:] = [d for d in dirs if d not in skip_dirs]
    
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))
        elif file.endswith('.js') and 'node_modules' not in root:
            js_files.append(os.path.join(root, file))

print("🔍 Auditing files for error sources...")
print(f"HTML files: {len(html_files)}")
print(f"JS files: {len(js_files)}")
print()

# Audit HTML files
for file in html_files[:50]:  # Sample first 50
    audit_file(file)

# Audit JS files
for file in js_files:
    audit_file(file)

# Generate report
report = []
report.append("# 🔍 Comprehensive Error Source Audit Report\n\n")
report.append(f"**Date:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
report.append(f"**Files Audited:** {len(html_files)} HTML, {len(js_files)} JS\n\n")
report.append("---\n\n")

# Error listeners
if error_sources['error_listeners']:
    report.append("## 🔴 Error Event Listeners\n\n")
    report.append(f"**Total:** {sum(e['count'] for e in error_sources['error_listeners'])} listeners found\n\n")
    
    # Count duplicates
    files_with_handlers = {}
    for item in error_sources['error_listeners']:
        if item['file'] not in files_with_handlers:
            files_with_handlers[item['file']] = 0
        files_with_handlers[item['file']] += item['count']
    
    duplicates = {f: c for f, c in files_with_handlers.items() if c > 1}
    if duplicates:
        report.append("### ⚠️ Files with Multiple Error Handlers (DUPLICATES):\n\n")
        for file, count in sorted(duplicates.items(), key=lambda x: x[1], reverse=True):
            report.append(f"- **{file}**: {count} error listener(s)\n")
        report.append("\n")
    report.append("\n")

# Rejection listeners
if error_sources['rejection_listeners']:
    report.append("## 🔴 Unhandled Rejection Listeners\n\n")
    report.append(f"**Total:** {sum(e['count'] for e in error_sources['rejection_listeners'])} listeners\n\n")
    
    duplicates = {}
    for item in error_sources['rejection_listeners']:
        if item['file'] not in duplicates:
            duplicates[item['file']] = 0
        duplicates[item['file']] += item['count']
    
    duplicates = {f: c for f, c in duplicates.items() if c > 1}
    if duplicates:
        report.append("### ⚠️ Files with Multiple Rejection Handlers:\n\n")
        for file, count in sorted(duplicates.items(), key=lambda x: x[1], reverse=True):
            report.append(f"- **{file}**: {count} rejection listener(s)\n")
        report.append("\n")

# Service Worker
if error_sources['service_worker']:
    report.append("## 🔴 Service Worker Registrations\n\n")
    for item in error_sources['service_worker']:
        status = "✅ Has .catch" if item['has_catch'] else "❌ Missing .catch"
        report.append(f"- **{item['file']}**: {item['count']} registration(s) - {status}\n")
    report.append("\n")

# Unhandled fetch
if error_sources['unhandled_fetch']:
    report.append("## ⚠️ Unhandled Fetch Calls\n\n")
    for item in error_sources['unhandled_fetch'][:10]:
        report.append(f"- **{item['file']}**: {item['count']} unhandled fetch call(s)\n")
    report.append("\n")

# Unprotected storage
if error_sources['unprotected_storage']:
    report.append("## ⚠️ Unprotected localStorage Operations\n\n")
    total = sum(item['count'] for item in error_sources['unprotected_storage'])
    report.append(f"**Total:** {total} unprotected localStorage operations\n\n")
    report.append("*Note: localStorage can throw errors (quota exceeded, etc.)*\n\n")

# No suppression
if error_sources['no_suppression']:
    report.append("## ⚠️ Error Handlers Without Expected Error Suppression\n\n")
    for item in error_sources['no_suppression'][:10]:
        report.append(f"- **{item['file']}**: {item['issue']}\n")
    report.append("\n")

# Summary
report.append("## 📊 Summary\n\n")
report.append(f"- Error listeners: {len(error_sources['error_listeners'])} files\n")
report.append(f"- Rejection listeners: {len(error_sources['rejection_listeners'])} files\n")
report.append(f"- Service Worker registrations: {len(error_sources['service_worker'])} files\n")
report.append(f"- Unhandled fetch calls: {len(error_sources['unhandled_fetch'])} files\n")
report.append(f"- Unprotected storage ops: {len(error_sources['unprotected_storage'])} files\n")
report.append(f"- Handlers without suppression: {len(error_sources['no_suppression'])} files\n")

with open('COMPREHENSIVE-ERROR-AUDIT-REPORT.md', 'w') as f:
    f.write(''.join(report))

print("✅ Audit complete!")
print(f"📄 Report saved to: COMPREHENSIVE-ERROR-AUDIT-REPORT.md")

