#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive System Integrity Audit
Tests frontend/backend integrity, module connections, paths, games, languages, and navigation flows
"""

import os
import re
import json
from pathlib import Path

# Color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

class SystemAudit:
    def __init__(self):
        self.issues = []
        self.warnings = []
        self.successes = []
        self.stats = {
            'pages_checked': 0,
            'links_checked': 0,
            'scripts_checked': 0,
            'broken_links': 0,
            'missing_files': 0,
            'broken_connections': 0
        }
        
    def log_success(self, msg):
        self.successes.append(msg)
        print(f"{Colors.GREEN}OK{Colors.RESET} {msg}")
    
    def log_error(self, msg):
        self.issues.append(msg)
        print(f"{Colors.RED}ERROR{Colors.RESET} {msg}")
        self.stats['broken_connections'] += 1
    
    def log_warning(self, msg):
        self.warnings.append(msg)
        print(f"{Colors.YELLOW}WARN{Colors.RESET} {msg}")
    
    def log_info(self, msg):
        print(f"{Colors.BLUE}INFO{Colors.RESET} {msg}")

    def check_file_exists(self, filepath):
        """Check if a file exists"""
        if os.path.exists(filepath):
            return True
        self.stats['missing_files'] += 1
        return False

    def check_dashboard_gym_relationship(self):
        """Verify dashboard and gym relationship"""
        print(f"\n{Colors.BOLD}{'='*80}")
        print("1. DASHBOARD/GYM RELATIONSHIP")
        print(f"{'='*80}{Colors.RESET}\n")
        
        # Check if gym-dashboard.html exists
        if not self.check_file_exists('gym-dashboard.html'):
            self.log_error("gym-dashboard.html does not exist!")
            return
        
        self.log_success("gym-dashboard.html exists")
        
        # Read gym-dashboard.html to check its purpose
        try:
            with open('gym-dashboard.html', 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if it's described as "THE GYM"
            if 'THE GYM' in content or '"THE GYM"' in content:
                self.log_success("gym-dashboard.html is labeled as THE GYM")
            else:
                self.log_warning("gym-dashboard.html may not be clearly labeled as THE GYM")
            
            # Check for belt path navigation
            belt_links = re.findall(r'href=["\']([^"\']*belt[^"\']*)["\']', content, re.I)
            if belt_links:
                self.log_success(f"gym-dashboard.html has {len(belt_links)} belt-related links")
            else:
                self.log_warning("gym-dashboard.html may not have belt path navigation")
                
        except Exception as e:
            self.log_error(f"Could not read gym-dashboard.html: {e}")

    def check_index_navigation(self):
        """Check index.html navigation to gym"""
        print(f"\n{Colors.BOLD}{'='*80}")
        print("2. INDEX.HTML NAVIGATION TO GYM")
        print(f"{'='*80}{Colors.RESET}\n")
        
        if not self.check_file_exists('index.html'):
            self.log_error("index.html does not exist!")
            return
        
        try:
            with open('index.html', 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if THE GYM button/link exists
            if 'THE GYM' in content or 'gym-dashboard.html' in content:
                self.log_success("index.html has THE GYM link")
                
                # Check what it links to
                gym_links = re.findall(r'href=["\']([^"\']*gym-dashboard[^"\']*)["\']', content, re.I)
                if gym_links:
                    self.log_success(f"THE GYM links to: {gym_links[0]}")
                else:
                    # Check onclick
                    onclick_matches = re.findall(r'onclick=["\']([^"\']*gym-dashboard[^"\']*)["\']', content, re.I)
                    if onclick_matches:
                        self.log_success(f"THE GYM uses onclick to navigate to gym-dashboard")
                    else:
                        self.log_warning("THE GYM link found but target unclear")
            else:
                self.log_error("index.html does not link to THE GYM/gym-dashboard.html")
                
        except Exception as e:
            self.log_error(f"Could not read index.html: {e}")

    def check_stripe_completion_navigation(self):
        """Check where stripe pages navigate after completion"""
        print(f"\n{Colors.BOLD}{'='*80}")
        print("3. STRIPE COMPLETION NAVIGATION")
        print(f"{'='*80}{Colors.RESET}\n")
        
        # Check all stripe files
        stripe_files = []
        for belt in ['white', 'blue', 'purple', 'brown', 'black']:
            for stripe in [1, 2, 3, 4]:
                stripe_file = f"{belt}-belt-stripe{stripe}-gamified.html"
                if os.path.exists(stripe_file):
                    stripe_files.append((belt, stripe, stripe_file))
        
        self.log_info(f"Found {len(stripe_files)} stripe files to check")
        
        gym_links = 0
        belt_hub_links = 0
        learning_hub_links = 0
        no_back_link = 0
        
        for belt, stripe, stripe_file in stripe_files[:5]:  # Check first 5 as sample
            try:
                with open(stripe_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check for back navigation
                has_gym_link = 'gym-dashboard.html' in content or 'gym-dashboard' in content
                has_belt_hub = f'{belt}-belt.html' in content
                has_learning_hub = 'learning-hub.html' in content
                has_next_stripe = f'stripe{stripe + 1}' in content if stripe < 4 else False
                
                if has_gym_link:
                    gym_links += 1
                if has_belt_hub:
                    belt_hub_links += 1
                if has_learning_hub:
                    learning_hub_links += 1
                
                # Check completion handler
                completion_handlers = re.findall(r'window\.location\.href\s*=\s*["\']([^"\']+)["\']', content)
                
                if not completion_handlers and not has_gym_link and not has_belt_hub:
                    no_back_link += 1
                    self.log_warning(f"{stripe_file} may not have clear back navigation")
                
            except Exception as e:
                self.log_error(f"Could not read {stripe_file}: {e}")
        
        print()
        self.log_info(f"Navigation patterns found:")
        self.log_info(f"  - Links to gym-dashboard: {gym_links}/{len(stripe_files[:5])}")
        self.log_info(f"  - Links to belt hub: {belt_hub_links}/{len(stripe_files[:5])}")
        self.log_info(f"  - Links to learning-hub: {learning_hub_links}/{len(stripe_files[:5])}")
        
        if no_back_link > 0:
            self.log_warning(f"{no_back_link} stripe files may be missing back navigation")

    def check_language_switching(self):
        """Check language switcher functionality"""
        print(f"\n{Colors.BOLD}{'='*80}")
        print("4. LANGUAGE SWITCHING")
        print(f"{'='*80}{Colors.RESET}\n")
        
        # Check index.html language switcher
        if self.check_file_exists('index.html'):
            try:
                with open('index.html', 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if 'language-switcher' in content or 'lang-toggle' in content:
                    self.log_success("index.html has language switcher")
                else:
                    self.log_error("index.html does not have language switcher")
                
                # Check if German version exists
                german_files = ['index.de.html', 'index-de.html']
                for gf in german_files:
                    if self.check_file_exists(gf):
                        self.log_success(f"German index page exists: {gf}")
                        break
                else:
                    self.log_warning("No German index page found (index.de.html or index-de.html)")
                    
            except Exception as e:
                self.log_error(f"Could not check language switching: {e}")
        
        # Check stripe files have German versions
        stripe_files = []
        for belt in ['white', 'blue', 'purple', 'brown', 'black']:
            for stripe in [1, 2, 3, 4]:
                stripe_file = f"{belt}-belt-stripe{stripe}-gamified.html"
                if os.path.exists(stripe_file):
                    stripe_files.append(stripe_file)
        
        german_stripes = 0
        for stripe_file in stripe_files[:10]:  # Sample
            german_version = stripe_file.replace('.html', '-de.html')
            if self.check_file_exists(german_version):
                german_stripes += 1
        
        print()
        self.log_info(f"German translations: {german_stripes}/{len(stripe_files[:10])} stripe files checked")

    def check_module_connections(self):
        """Check JavaScript module loading"""
        print(f"\n{Colors.BOLD}{'='*80}")
        print("5. MODULE CONNECTIONS")
        print(f"{'='*80}{Colors.RESET}\n")
        
        required_modules = [
            'js/core-gamification.js',
            'js/core-progress-tracker.js',
            'js/belt-progression.js'
        ]
        
        for module in required_modules:
            if self.check_file_exists(module):
                self.log_success(f"{module} exists")
            else:
                self.log_error(f"{module} is missing!")
        
        # Check if modules are loaded in key pages
        key_pages = ['gym-dashboard.html', 'index.html']
        for page in key_pages:
            if self.check_file_exists(page):
                try:
                    with open(page, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    modules_found = []
                    for module in required_modules:
                        module_name = os.path.basename(module)
                        if module_name in content:
                            modules_found.append(module_name)
                    
                    if modules_found:
                        self.log_success(f"{page} loads {len(modules_found)}/{len(required_modules)} core modules")
                    else:
                        self.log_warning(f"{page} may not be loading core modules")
                        
                except Exception as e:
                    self.log_error(f"Could not check {page}: {e}")

    def check_games_functionality(self):
        """Check game files and backend connections"""
        print(f"\n{Colors.BOLD}{'='*80}")
        print("6. GAMES FUNCTIONALITY")
        print(f"{'='*80}{Colors.RESET}\n")
        
        games = [
            'confession-poker-v2.html',
            'conflict-cards.html',
            'take-the-back.html',
            'disagree-commit-roulette.html'
        ]
        
        for game in games:
            if self.check_file_exists(game):
                self.log_success(f"{game} exists")
                
                # Check for backend connection
                try:
                    with open(game, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    has_firebase = 'firebase' in content.lower() or 'Firebase' in content
                    has_supabase = 'supabase' in content.lower()
                    
                    if has_firebase:
                        # Check if it's demo or production
                        if 'demo' in content.lower():
                            self.log_warning(f"{game} uses demo Firebase - needs production backend")
                        else:
                            self.log_success(f"{game} has Firebase connection")
                    
                    if has_supabase:
                        self.log_success(f"{game} has Supabase connection")
                    
                    if not has_firebase and not has_supabase:
                        self.log_warning(f"{game} may not have backend connection")
                        
                except Exception as e:
                    self.log_error(f"Could not check {game}: {e}")
            else:
                self.log_warning(f"{game} does not exist")

    def check_backend_connection(self):
        """Check backend/Supabase configuration"""
        print(f"\n{Colors.BOLD}{'='*80}")
        print("7. BACKEND CONNECTION")
        print(f"{'='*80}{Colors.RESET}\n")
        
        # Check Supabase client
        if self.check_file_exists('js/supabase-client.js'):
            self.log_success("js/supabase-client.js exists")
        else:
            self.log_warning("js/supabase-client.js missing (backend sync not available)")
        
        # Check sync manager
        if self.check_file_exists('js/sync-manager.js'):
            self.log_success("js/sync-manager.js exists")
        else:
            self.log_warning("js/sync-manager.js missing")
        
        # Check Netlify functions
        functions_dir = 'netlify/functions'
        if os.path.exists(functions_dir):
            functions = [f for f in os.listdir(functions_dir) if f.endswith('.js')]
            self.log_success(f"Found {len(functions)} Netlify functions")
            
            # Check for node-fetch issue
            for func in functions[:3]:  # Sample
                func_path = os.path.join(functions_dir, func)
                try:
                    with open(func_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if 'require(\'node-fetch\')' in content:
                        self.log_warning(f"{func} uses node-fetch - check package.json has it")
                except:
                    pass
        else:
            self.log_warning("netlify/functions directory not found")

    def check_belt_path_flow(self):
        """Check complete belt path navigation flow"""
        print(f"\n{Colors.BOLD}{'='*80}")
        print("8. BELT PATH FLOW")
        print(f"{'='*80}{Colors.RESET}\n")
        
        belts = ['white', 'blue', 'purple', 'brown', 'black']
        
        for belt in belts:
            belt_hub = f"{belt}-belt.html"
            if self.check_file_exists(belt_hub):
                self.log_success(f"{belt_hub} exists")
                
                # Check if it links to gym-dashboard
                try:
                    with open(belt_hub, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if 'gym-dashboard.html' in content:
                        self.log_success(f"{belt_hub} links to gym-dashboard")
                    else:
                        self.log_warning(f"{belt_hub} may not link back to gym-dashboard")
                        
                except Exception as e:
                    self.log_error(f"Could not check {belt_hub}: {e}")
            else:
                self.log_error(f"{belt_hub} does not exist!")

    def check_link_integrity(self):
        """Check critical links work"""
        print(f"\n{Colors.BOLD}{'='*80}")
        print("9. LINK INTEGRITY")
        print(f"{'='*80}{Colors.RESET}\n")
        
        critical_links = {
            'index.html': [
                'gym-dashboard.html',
                'learning-hub.html',
                'belt-assessment-sales-landing.html',
                'business-portal.html'
            ],
            'gym-dashboard.html': [
                'white-belt.html',
                'blue-belt.html',
                'purple-belt.html',
                'brown-belt.html',
                'black-belt.html'
            ]
        }
        
        for source, targets in critical_links.items():
            if not self.check_file_exists(source):
                continue
            
            try:
                with open(source, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                for target in targets:
                    if target in content:
                        if self.check_file_exists(target):
                            self.log_success(f"{source} -> {target} (exists)")
                        else:
                            self.log_error(f"{source} -> {target} (LINK BROKEN - file missing)")
                    else:
                        self.log_warning(f"{source} does not link to {target}")
                        
            except Exception as e:
                self.log_error(f"Could not check links in {source}: {e}")

    def generate_report(self):
        """Generate final audit report"""
        print(f"\n{Colors.BOLD}{'='*80}")
        print("AUDIT SUMMARY")
        print(f"{'='*80}{Colors.RESET}\n")
        
        total_checks = len(self.successes) + len(self.warnings) + len(self.issues)
        
        print(f"Total Checks: {total_checks}")
        print(f"{Colors.GREEN}Successes: {len(self.successes)}{Colors.RESET}")
        print(f"{Colors.YELLOW}Warnings: {len(self.warnings)}{Colors.RESET}")
        print(f"{Colors.RED}Errors: {len(self.issues)}{Colors.RESET}")
        
        if self.issues:
            print(f"\n{Colors.RED}{Colors.BOLD}CRITICAL ISSUES:{Colors.RESET}")
            for i, issue in enumerate(self.issues[:10], 1):
                print(f"  {i}. {issue}")
        
        if self.warnings:
            print(f"\n{Colors.YELLOW}{Colors.BOLD}WARNINGS:{Colors.RESET}")
            for i, warning in enumerate(self.warnings[:10], 1):
                print(f"  {i}. {warning}")
        
        print()
        return {
            'successes': len(self.successes),
            'warnings': len(self.warnings),
            'errors': len(self.issues),
            'issues': self.issues,
            'warnings': self.warnings
        }

def main():
    print(f"{Colors.BOLD}{'='*80}")
    print("COMPREHENSIVE SYSTEM INTEGRITY AUDIT")
    print(f"{'='*80}{Colors.RESET}\n")
    
    audit = SystemAudit()
    
    # Run all audit checks
    audit.check_dashboard_gym_relationship()
    audit.check_index_navigation()
    audit.check_stripe_completion_navigation()
    audit.check_language_switching()
    audit.check_module_connections()
    audit.check_games_functionality()
    audit.check_backend_connection()
    audit.check_belt_path_flow()
    audit.check_link_integrity()
    
    # Generate report
    report = audit.generate_report()
    
    # Save report to file
    report_file = 'SYSTEM-AUDIT-REPORT.md'
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# SYSTEM INTEGRITY AUDIT REPORT\n\n")
        f.write(f"**Date:** {Path().cwd()}\n\n")
        f.write(f"**Successes:** {report['successes']}\n")
        f.write(f"**Warnings:** {report['warnings']}\n")
        f.write(f"**Errors:** {report['errors']}\n\n")
        
        if report['issues']:
            f.write("## CRITICAL ISSUES\n\n")
            for issue in report['issues']:
                f.write(f"- {issue}\n")
            f.write("\n")
        
        if report['warnings']:
            f.write("## WARNINGS\n\n")
            for warning in report['warnings']:
                f.write(f"- {warning}\n")
    
    print(f"\n{Colors.BLUE}Report saved to: {report_file}{Colors.RESET}\n")

if __name__ == '__main__':
    main()

