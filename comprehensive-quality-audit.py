#!/usr/bin/env python3
"""
Comprehensive Quality Audit for TAP-IN Platform
Tests all paths, connections, links, and navigation flows
"""

import os
import re
from pathlib import Path
from collections import defaultdict
import json

class QualityAuditor:
    def __init__(self):
        self.issues = []
        self.entry_points = []
        self.all_html_files = []
        self.link_map = defaultdict(list)
        self.broken_links = []
        self.missing_files = []
        self.orphaned_files = []
        
    def find_all_html_files(self):
        """Find all HTML files in the repository"""
        exclude_dirs = {'node_modules', '.git', '__pycache__', 'archive', 'android', 'ios', 'dist', 'build', 'react-app', '.netlify'}
        
        for root, dirs, files in os.walk('.'):
            # Filter out excluded directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                if file.endswith('.html'):
                    filepath = os.path.join(root, file)
                    rel_path = os.path.relpath(filepath, '.')
                    self.all_html_files.append(rel_path)
        
        print(f"📁 Found {len(self.all_html_files)} HTML files")
        return self.all_html_files
    
    def identify_entry_points(self):
        """Identify all entry points to the application"""
        entry_patterns = [
            'index.html',
            'index-DUAL-ENTRY.html',
            'gym-dashboard.html',
            'learning-hub.html',
            'belt-assessment-v2.html',
            'hub-home-BUSINESS.html',
            'hub-assessment-center.html',
            'leadership-games.html',
        ]
        
        for pattern in entry_patterns:
            for file in self.all_html_files:
                if pattern in file:
                    self.entry_points.append(file)
        
        # Also check for German entry points
        for file in self.all_html_files:
            if file.endswith('-de.html') and any(ep in file for ep in ['index', 'gym-dashboard', 'learning-hub']):
                self.entry_points.append(file)
        
        print(f"🚪 Found {len(self.entry_points)} entry points")
        return self.entry_points
    
    def extract_links_from_file(self, filepath):
        """Extract all links from an HTML file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.issues.append({
                'type': 'error',
                'file': filepath,
                'message': f'Could not read file: {e}'
            })
            return []
        
        links = []
        
        # Find all href links
        href_pattern = r'href=["\']([^"\']+)["\']'
        for match in re.finditer(href_pattern, content):
            link = match.group(1)
            # Skip external links and anchors
            if not link.startswith('http') and not link.startswith('#') and not link.startswith('mailto:'):
                links.append(link)
        
        # Find onclick navigation
        onclick_pattern = r'(?:window\.location\.href|location\.href)\s*=\s*["\']([^"\']+)["\']'
        for match in re.finditer(onclick_pattern, content):
            link = match.group(1)
            if not link.startswith('http') and not link.startswith('#'):
                links.append(link)
        
        return links
    
    def check_link_exists(self, link, source_file):
        """Check if a linked file exists"""
        # Handle relative paths
        if link.startswith('/'):
            link = link[1:]
        
        # Handle relative paths from source file directory
        source_dir = os.path.dirname(source_file) if os.path.dirname(source_file) else '.'
        
        # Try different path resolutions
        possible_paths = [
            link,
            os.path.join(source_dir, link),
            os.path.join('.', link),
        ]
        
        for path in possible_paths:
            if os.path.exists(path) and path.endswith('.html'):
                return True, path
        
        return False, link
    
    def audit_all_links(self):
        """Audit all links in all HTML files"""
        print("\n🔍 Auditing all links...")
        
        for file in self.all_html_files:
            links = self.extract_links_from_file(file)
            
            for link in links:
                exists, resolved_path = self.check_link_exists(link, file)
                
                if not exists:
                    self.broken_links.append({
                        'source': file,
                        'link': link,
                        'resolved': resolved_path
                    })
                else:
                    self.link_map[file].append({
                        'link': link,
                        'target': resolved_path,
                        'valid': True
                    })
        
        print(f"  ✅ Valid links: {sum(len(links) for links in self.link_map.values())}")
        print(f"  ❌ Broken links: {len(self.broken_links)}")
        
        return self.broken_links
    
    def find_orphaned_files(self):
        """Find files that are not linked from anywhere"""
        print("\n🔍 Finding orphaned files...")
        
        all_targets = set()
        for links in self.link_map.values():
            for link_info in links:
                if link_info['valid']:
                    all_targets.add(link_info['target'])
        
        # Entry points are always considered linked
        for ep in self.entry_points:
            all_targets.add(ep)
        
        for file in self.all_html_files:
            if file not in all_targets and not file.startswith('archive/'):
                # Check if it's a German version - might be linked from language switcher
                if '-de.html' in file:
                    # Check if English version exists and is linked
                    en_version = file.replace('-de.html', '.html')
                    if en_version in all_targets:
                        continue
                
                self.orphaned_files.append(file)
        
        print(f"  ⚠️  Orphaned files: {len(self.orphaned_files)}")
        return self.orphaned_files
    
    def check_belt_paths(self):
        """Check belt stripe navigation paths"""
        print("\n🥋 Checking belt paths...")
        
        belt_issues = []
        
        # Check each belt
        for belt in ['white', 'blue', 'purple', 'brown', 'black']:
            # Check stripe files exist
            for stripe in range(1, 5):
                stripe_file = f'{belt}-belt-stripe{stripe}-gamified.html'
                if stripe_file not in self.all_html_files:
                    belt_issues.append({
                        'type': 'missing',
                        'belt': belt,
                        'stripe': stripe,
                        'file': stripe_file
                    })
            
            # Check belt hub exists
            hub_file = f'{belt}-belt.html'
            if hub_file not in self.all_html_files:
                belt_issues.append({
                    'type': 'missing_hub',
                    'belt': belt,
                    'file': hub_file
                })
        
        print(f"  ⚠️  Belt path issues: {len(belt_issues)}")
        return belt_issues
    
    def check_navigation_flows(self):
        """Check navigation flows between pages"""
        print("\n🧭 Checking navigation flows...")
        
        flow_issues = []
        
        # Check stripe to stripe navigation
        for belt in ['white', 'blue', 'purple', 'brown', 'black']:
            for stripe in range(1, 4):
                stripe_file = f'{belt}-belt-stripe{stripe}-gamified.html'
                next_stripe = f'{belt}-belt-stripe{stripe+1}-gamified.html'
                
                if stripe_file in self.all_html_files:
                    links = self.extract_links_from_file(stripe_file)
                    if next_stripe not in links:
                        flow_issues.append({
                            'type': 'missing_next',
                            'file': stripe_file,
                            'expected': next_stripe
                        })
        
        # Check stripe 4 to assessment
        for belt in ['white', 'blue', 'purple', 'brown', 'black']:
            stripe4 = f'{belt}-belt-stripe4-gamified.html'
            assessment = f'{belt}-belt-assessment.html'
            
            if stripe4 in self.all_html_files:
                links = self.extract_links_from_file(stripe4)
                if assessment not in links:
                    flow_issues.append({
                        'type': 'missing_assessment',
                        'file': stripe4,
                        'expected': assessment
                    })
        
        print(f"  ⚠️  Navigation flow issues: {len(flow_issues)}")
        return flow_issues
    
    def check_back_links(self):
        """Check that pages have back links to dashboard/hub"""
        print("\n↩️  Checking back links...")
        
        back_link_issues = []
        
        # Pages that should link back to dashboard
        dashboard_pages = [
            'gym-dashboard.html',
            'gym-dashboard-de.html'
        ]
        
        # Pages that should link back to hub
        hub_pages = [
            'learning-hub.html',
            'learning-hub-de.html'
        ]
        
        for file in self.all_html_files:
            # Skip entry points themselves
            if file in self.entry_points:
                continue
            
            links = self.extract_links_from_file(file)
            
            # Check if it's a stripe file - should link back to belt hub or dashboard
            if '-stripe' in file and '-gamified.html' in file:
                has_back_link = any(
                    'gym-dashboard' in link or 
                    'belt.html' in link or
                    'learning-hub' in link
                    for link in links
                )
                
                if not has_back_link:
                    back_link_issues.append({
                        'file': file,
                        'type': 'missing_back_link',
                        'suggestion': 'Add link to gym-dashboard.html or belt hub'
                    })
        
        print(f"  ⚠️  Back link issues: {len(back_link_issues)}")
        return back_link_issues
    
    def check_games_and_tools(self):
        """Check games and tools are accessible"""
        print("\n🎮 Checking games and tools...")
        
        game_issues = []
        
        games = [
            'confession-poker.html',
            'confession-poker-v2.html',
            'conflict-cards.html',
            'take-the-back.html',
            'disagree-commit.html',
            'leadership-games.html'
        ]
        
        tools = [
            'open-mat-box-breathing.html',
            'open-mat-5-minute-morning-routine.html',
            'open-mat-decision-framework.html',
            'open-mat-energy-audit.html',
            'open-mat-weekly-review.html',
            'open-mat-inner-game-leadership.html'
        ]
        
        # Check games exist and are linked
        for game in games:
            if game not in self.all_html_files:
                game_issues.append({
                    'type': 'missing',
                    'category': 'game',
                    'file': game
                })
            else:
                # Check if linked from games hub
                if 'leadership-games.html' in self.all_html_files:
                    links = self.extract_links_from_file('leadership-games.html')
                    if game not in links and game != 'leadership-games.html':
                        game_issues.append({
                            'type': 'not_linked',
                            'category': 'game',
                            'file': game,
                            'from': 'leadership-games.html'
                        })
        
        # Check tools exist and are linked
        for tool in tools:
            if tool not in self.all_html_files:
                game_issues.append({
                    'type': 'missing',
                    'category': 'tool',
                    'file': tool
                })
        
        print(f"  ⚠️  Game/tool issues: {len(game_issues)}")
        return game_issues
    
    def generate_report(self):
        """Generate comprehensive audit report"""
        print("\n📊 Generating audit report...")
        
        report = {
            'summary': {
                'total_files': len(self.all_html_files),
                'entry_points': len(self.entry_points),
                'broken_links': len(self.broken_links),
                'orphaned_files': len(self.orphaned_files),
                'total_issues': len(self.broken_links) + len(self.orphaned_files)
            },
            'entry_points': self.entry_points,
            'broken_links': self.broken_links[:50],  # Limit to first 50
            'orphaned_files': self.orphaned_files[:50],
            'belt_issues': self.check_belt_paths(),
            'navigation_issues': self.check_navigation_flows(),
            'back_link_issues': self.check_back_links(),
            'game_tool_issues': self.check_games_and_tools()
        }
        
        # Save JSON report
        with open('QUALITY-AUDIT-REPORT.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        # Generate markdown report
        self.generate_markdown_report(report)
        
        return report
    
    def generate_markdown_report(self, report):
        """Generate markdown audit report"""
        md_content = f"""# 🔍 COMPREHENSIVE QUALITY AUDIT REPORT

**Date:** {os.popen('date').read().strip()}  
**Status:** Complete

---

## 📊 SUMMARY

- **Total HTML Files:** {report['summary']['total_files']}
- **Entry Points:** {report['summary']['entry_points']}
- **Broken Links:** {report['summary']['broken_links']}
- **Orphaned Files:** {report['summary']['orphaned_files']}
- **Total Issues:** {report['summary']['total_issues']}

---

## 🚪 ENTRY POINTS ({len(report['entry_points'])})

"""
        
        for ep in report['entry_points']:
            md_content += f"- `{ep}`\n"
        
        md_content += f"""
---

## ❌ BROKEN LINKS ({len(report['broken_links'])})

"""
        
        for link in report['broken_links'][:30]:  # Show first 30
            md_content += f"- **{link['source']}** → `{link['link']}` (resolved: `{link['resolved']}`)\n"
        
        if len(report['broken_links']) > 30:
            md_content += f"\n*... and {len(report['broken_links']) - 30} more*\n"
        
        md_content += f"""
---

## 🔗 ORPHANED FILES ({len(report['orphaned_files'])})

"""
        
        for file in report['orphaned_files'][:30]:
            md_content += f"- `{file}`\n"
        
        if len(report['orphaned_files']) > 30:
            md_content += f"\n*... and {len(report['orphaned_files']) - 30} more*\n"
        
        md_content += f"""
---

## 🥋 BELT PATH ISSUES ({len(report['belt_issues'])})

"""
        
        for issue in report['belt_issues']:
            md_content += f"- **{issue['type']}**: {issue.get('belt', 'N/A')} belt, stripe {issue.get('stripe', 'N/A')} - `{issue['file']}`\n"
        
        md_content += f"""
---

## 🧭 NAVIGATION FLOW ISSUES ({len(report['navigation_issues'])})

"""
        
        for issue in report['navigation_issues'][:20]:
            md_content += f"- **{issue['type']}**: `{issue['file']}` missing link to `{issue['expected']}`\n"
        
        md_content += f"""
---

## ↩️  BACK LINK ISSUES ({len(report['back_link_issues'])})

"""
        
        for issue in report['back_link_issues'][:20]:
            md_content += f"- `{issue['file']}`: {issue['suggestion']}\n"
        
        md_content += f"""
---

## 🎮 GAME/TOOL ISSUES ({len(report['game_tool_issues'])})

"""
        
        for issue in report['game_tool_issues']:
            md_content += f"- **{issue['type']}** ({issue['category']}): `{issue['file']}`\n"
        
        md_content += """
---

## ✅ RECOMMENDATIONS

1. **Fix Broken Links**: Update or remove broken links
2. **Link Orphaned Files**: Add navigation to orphaned pages
3. **Complete Belt Paths**: Ensure all stripe files exist and link correctly
4. **Add Back Links**: Ensure all pages can navigate back to dashboard/hub
5. **Test Navigation Flows**: Manually test all user journeys

---

**Report Generated:** Quality Audit System
"""
        
        with open('QUALITY-AUDIT-REPORT.md', 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print("  ✅ Report saved to QUALITY-AUDIT-REPORT.md")

def main():
    """Main audit function"""
    print("=" * 80)
    print("🔍 COMPREHENSIVE QUALITY AUDIT - TAP-IN PLATFORM")
    print("=" * 80)
    print()
    
    auditor = QualityAuditor()
    
    # Step 1: Find all files
    auditor.find_all_html_files()
    
    # Step 2: Identify entry points
    auditor.identify_entry_points()
    
    # Step 3: Audit all links
    auditor.audit_all_links()
    
    # Step 4: Find orphaned files
    auditor.find_orphaned_files()
    
    # Step 5: Generate report
    report = auditor.generate_report()
    
    print()
    print("=" * 80)
    print("✅ AUDIT COMPLETE")
    print("=" * 80)
    print()
    print(f"📊 Total Issues Found: {report['summary']['total_issues']}")
    print(f"📄 Report saved to: QUALITY-AUDIT-REPORT.md")
    print(f"📄 JSON report saved to: QUALITY-AUDIT-REPORT.json")
    print()

if __name__ == '__main__':
    main()
