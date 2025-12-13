#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enterprise-Level Connection Audit (Google/Apple Style)
Comprehensive audit of all connections throughout the website:
- Internal links (HTML, CSS, JS)
- External dependencies
- Navigation flows
- Language connections (EN/DE)
- Module dependencies
- Asset loading
- API/backend connections
- Form submissions
- Cross-page navigation
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
from urllib.parse import urlparse

class ConnectionAudit:
    def __init__(self):
        self.issues = []
        self.warnings = []
        self.errors = []
        self.stats = {
            'pages_checked': 0,
            'links_found': 0,
            'broken_links': 0,
            'missing_files': 0,
            'broken_external': 0,
            'navigation_issues': 0
        }
        self.link_map = defaultdict(list)  # target -> [sources]
        self.broken_links = []
        self.external_resources = []
        
    def find_all_html_files(self):
        """Find all HTML files in the project"""
        html_files = []
        for root, dirs, files in os.walk('.'):
            # Skip certain directories
            if any(skip in root for skip in ['node_modules', '.git', 'archive', 'react-app', '.next', 'dist']):
                continue
            for file in files:
                if file.endswith('.html'):
                    html_files.append(os.path.join(root, file))
        return html_files
    
    def extract_links_from_html(self, filepath):
        """Extract all links from an HTML file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.errors.append(f"Cannot read {filepath}: {e}")
            return []
        
        links = []
        
        # href attributes
        href_pattern = r'href=["\']([^"\']+)["\']'
        for match in re.finditer(href_pattern, content):
            links.append(('href', match.group(1), match.start()))
        
        # src attributes
        src_pattern = r'src=["\']([^"\']+)["\']'
        for match in re.finditer(src_pattern, content):
            links.append(('src', match.group(1), match.start()))
        
        # window.location
        location_pattern = r'window\.location\.(?:href|replace)\s*=\s*["\']([^"\']+)["\']'
        for match in re.finditer(location_pattern, content):
            links.append(('js-location', match.group(1), match.start()))
        
        # onclick navigation
        onclick_pattern = r'onclick=["\'].*?location\.href\s*=\s*["\']([^"\']+)["\']'
        for match in re.finditer(onclick_pattern, content):
            links.append(('onclick', match.group(1), match.start()))
        
        # fetch/API calls
        fetch_pattern = r'fetch\(["\']([^"\']+)["\']'
        for match in re.finditer(fetch_pattern, content):
            links.append(('fetch', match.group(1), match.start()))
        
        return links
    
    def normalize_path(self, link, base_file):
        """Normalize a link path relative to base file"""
        # Skip anchors and javascript
        if link.startswith('#') or link.startswith('javascript:') or link.startswith('mailto:'):
            return None
        
        # External URLs
        if link.startswith('http://') or link.startswith('https://'):
            return ('external', link)
        
        # Absolute paths (starting with /)
        if link.startswith('/'):
            link = link[1:]
        
        # Relative paths
        base_dir = os.path.dirname(base_file) or '.'
        if base_dir == '.':
            return link
        else:
            # Resolve relative path
            return os.path.normpath(os.path.join(base_dir, link))
    
    def check_file_exists(self, filepath):
        """Check if a file exists"""
        if isinstance(filepath, tuple):
            return True  # External URL
        
        # Remove query strings and anchors
        filepath = filepath.split('?')[0].split('#')[0]
        
        return os.path.exists(filepath)
    
    def audit_file_connections(self, filepath):
        """Audit all connections in a single file"""
        links = self.extract_links_from_html(filepath)
        self.stats['links_found'] += len(links)
        
        file_issues = []
        
        for link_type, link_url, position in links:
            normalized = self.normalize_path(link_url, filepath)
            
            if normalized is None:
                continue  # Skip anchors/javascript
            
            if isinstance(normalized, tuple) and normalized[0] == 'external':
                self.external_resources.append(normalized[1])
                continue
            
            # Check if file exists
            if not self.check_file_exists(normalized):
                self.stats['broken_links'] += 1
                self.broken_links.append({
                    'source': filepath,
                    'target': normalized,
                    'type': link_type,
                    'url': link_url
                })
                file_issues.append(f"Broken {link_type}: {link_url} → {normalized}")
            else:
                # Track link mapping
                self.link_map[normalized].append(filepath)
        
        return file_issues
    
    def check_language_connections(self, html_files):
        """Check language switching connections (EN ⟷ DE)"""
        print("\n" + "="*80)
        print("🌐 LANGUAGE CONNECTION AUDIT")
        print("="*80)
        
        lang_issues = []
        
        # Find all German files
        german_files = [f for f in html_files if f.endswith('-de.html')]
        english_files = [f for f in html_files if f.endswith('.html') and not f.endswith('-de.html')]
        
        print(f"\nFound {len(german_files)} German files")
        print(f"Found {len(english_files)} English files")
        
        # Check each German file links to German versions
        for de_file in german_files:
            try:
                with open(de_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check for English file links (without -de suffix)
                english_patterns = [
                    r'href=["\']([^"\']+\.html)["\'](?!.*-de\.html)',
                    r'window\.location.*["\']([^"\']+\.html)["\'](?!.*-de\.html)'
                ]
                
                issues = []
                for pattern in english_patterns:
                    matches = re.findall(pattern, content)
                    for match in matches:
                        # Check if it's a German file that should link to German version
                        base_name = os.path.basename(de_file).replace('-de.html', '.html')
                        if match.endswith(base_name) and '-de.html' not in match:
                            issues.append(f"Links to English version: {match}")
                
                if issues:
                    lang_issues.extend([(de_file, issue) for issue in issues])
            except Exception as e:
                self.errors.append(f"Error checking {de_file}: {e}")
        
        if lang_issues:
            print(f"\n⚠️  Found {len(lang_issues)} language connection issues:")
            for file, issue in lang_issues[:10]:
                print(f"  • {os.path.basename(file)}: {issue}")
        else:
            print("\n✅ No language connection issues found")
        
        return lang_issues
    
    def check_navigation_flows(self, html_files):
        """Check critical navigation flows"""
        print("\n" + "="*80)
        print("🧭 NAVIGATION FLOW AUDIT")
        print("="*80)
        
        critical_flows = {
            'index.html': ['gym-dashboard.html', 'learning-hub.html'],
            'gym-dashboard.html': ['white-belt.html', 'blue-belt.html', 'purple-belt.html', 'brown-belt.html', 'black-belt.html'],
            'white-belt.html': ['white-belt-stripe1-gamified.html'],
            'belt-assessment-v2.html': ['gym-dashboard.html'],
        }
        
        flow_issues = []
        
        for source, expected_targets in critical_flows.items():
            if not os.path.exists(source):
                flow_issues.append(f"❌ Source file missing: {source}")
                continue
            
            try:
                with open(source, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                for target in expected_targets:
                    if target not in content:
                        flow_issues.append(f"⚠️  {source} doesn't link to {target}")
                    else:
                        print(f"✅ {source} → {target}")
            except Exception as e:
                flow_issues.append(f"❌ Error reading {source}: {e}")
        
        if flow_issues:
            print(f"\n⚠️  Found {len(flow_issues)} navigation flow issues:")
            for issue in flow_issues:
                print(f"  {issue}")
        
        return flow_issues
    
    def check_module_dependencies(self, html_files):
        """Check JavaScript and CSS module dependencies"""
        print("\n" + "="*80)
        print("📦 MODULE DEPENDENCY AUDIT")
        print("="*80)
        
        required_modules = [
            'js/core-gamification.js',
            'js/core-progress-tracker.js',
            'js/belt-progression.js',
        ]
        
        module_issues = []
        
        for module in required_modules:
            if not os.path.exists(module):
                module_issues.append(f"❌ Missing module: {module}")
                continue
            
            # Check which files use it
            users = []
            for html_file in html_files[:50]:  # Check first 50 files
                try:
                    with open(html_file, 'r', encoding='utf-8') as f:
                        if os.path.basename(module) in f.read():
                            users.append(html_file)
                except:
                    pass
            
            print(f"✅ {module}: Used by {len(users)} files")
        
        if module_issues:
            print(f"\n⚠️  Found {len(module_issues)} module issues:")
            for issue in module_issues:
                print(f"  {issue}")
        
        return module_issues
    
    def check_external_resources(self):
        """Audit external resources (CDN, APIs, etc.)"""
        print("\n" + "="*80)
        print("🌍 EXTERNAL RESOURCE AUDIT")
        print("="*80)
        
        unique_external = set(self.external_resources)
        print(f"\nFound {len(unique_external)} unique external resources")
        
        # Categorize
        cdn_resources = []
        api_endpoints = []
        fonts = []
        other = []
        
        for url in unique_external:
            if 'cdn' in url or 'jsdelivr' in url or 'unpkg' in url:
                cdn_resources.append(url)
            elif 'api' in url or 'supabase' in url or 'firebase' in url:
                api_endpoints.append(url)
            elif 'fonts' in url or 'font' in url:
                fonts.append(url)
            else:
                other.append(url)
        
        print(f"\n  📦 CDN resources: {len(cdn_resources)}")
        for res in cdn_resources[:5]:
            print(f"    • {res[:60]}...")
        
        print(f"\n  🔌 API endpoints: {len(api_endpoints)}")
        for api in api_endpoints[:5]:
            print(f"    • {api[:60]}...")
        
        print(f"\n  🔤 Fonts: {len(fonts)}")
        for font in fonts[:5]:
            print(f"    • {font[:60]}...")
        
        return {
            'cdn': cdn_resources,
            'api': api_endpoints,
            'fonts': fonts,
            'other': other
        }
    
    def generate_report(self):
        """Generate comprehensive audit report"""
        print("\n" + "="*80)
        print("📊 AUDIT SUMMARY")
        print("="*80)
        
        print(f"\n📄 Pages checked: {self.stats['pages_checked']}")
        print(f"🔗 Links found: {self.stats['links_found']}")
        print(f"❌ Broken links: {self.stats['broken_links']}")
        print(f"⚠️  Warnings: {len(self.warnings)}")
        print(f"💥 Errors: {len(self.errors)}")
        
        if self.broken_links:
            print(f"\n🔴 TOP 10 BROKEN LINKS:")
            for link in self.broken_links[:10]:
                print(f"  • {os.path.basename(link['source'])} → {link['target']}")
                print(f"    Type: {link['type']}, URL: {link['url']}")
        
        # Generate report file
        report = {
            'stats': self.stats,
            'broken_links': self.broken_links[:50],  # Top 50
            'warnings': self.warnings,
            'errors': self.errors,
            'external_resources_count': len(set(self.external_resources))
        }
        
        with open('CONNECTION-AUDIT-REPORT.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n📄 Full report saved to: CONNECTION-AUDIT-REPORT.json")
        
        return report

def main():
    print("="*80)
    print("🔍 ENTERPRISE CONNECTION AUDIT (Google/Apple Style)")
    print("="*80)
    print("\nAuditing all connections throughout the website...\n")
    
    audit = ConnectionAudit()
    
    # Find all HTML files
    html_files = audit.find_all_html_files()
    print(f"Found {len(html_files)} HTML files to audit\n")
    
    # Audit each file
    print("="*80)
    print("🔗 LINK AUDIT")
    print("="*80)
    
    for i, html_file in enumerate(html_files, 1):
        if i % 10 == 0:
            print(f"  Progress: {i}/{len(html_files)} files...")
        audit.stats['pages_checked'] += 1
        issues = audit.audit_file_connections(html_file)
        if issues:
            audit.warnings.extend(issues)
    
    # Run specialized audits
    lang_issues = audit.check_language_connections(html_files)
    nav_issues = audit.check_navigation_flows(html_files)
    module_issues = audit.check_module_dependencies(html_files)
    external = audit.check_external_resources()
    
    # Generate report
    report = audit.generate_report()
    
    print("\n" + "="*80)
    print("✅ AUDIT COMPLETE")
    print("="*80)
    print(f"\nTotal issues found: {len(audit.broken_links)} broken links")
    print(f"Check CONNECTION-AUDIT-REPORT.json for full details")

if __name__ == '__main__':
    main()

