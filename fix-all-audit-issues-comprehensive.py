#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix All Audit Issues - Comprehensive
Fixes all identified broken links and missing files from enterprise audit
"""

import os
import re
import json
import shutil
from collections import defaultdict

class ComprehensiveFix:
    def __init__(self):
        self.fixes_applied = []
        self.files_modified = set()
        
    def fix_css_core_styles(self):
        """Create css/core-styles.css or fix references"""
        print("\n🔧 Fixing CSS Core Styles...")
        
        css_dir = 'css'
        os.makedirs(css_dir, exist_ok=True)
        
        # Check if similar file exists
        similar_files = [f for f in os.listdir(css_dir) if 'core' in f.lower() or 'style' in f.lower()]
        
        if similar_files:
            print(f"  Found similar files: {similar_files}")
            # Use existing file
            return False
        
        # Create core-styles.css with basic structure
        core_styles = '''/* TAP-IN Core Styles */
/* Centralized styling for consistent design across all pages */

:root {
    /* Colors */
    --tap-primary-navy: #1a365d;
    --tap-primary-purple: #7c3aed;
    --tap-accent-gold: #f59e0b;
    --tap-success-green: #10b981;
    --tap-error-red: #ef4444;
    
    /* Spacing */
    --tap-spacing-xs: 0.25rem;
    --tap-spacing-sm: 0.5rem;
    --tap-spacing-md: 1rem;
    --tap-spacing-lg: 1.5rem;
    --tap-spacing-xl: 2rem;
    
    /* Typography */
    --tap-font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --tap-font-size-base: 16px;
    --tap-line-height-base: 1.6;
    
    /* Border radius */
    --tap-radius-sm: 4px;
    --tap-radius-md: 8px;
    --tap-radius-lg: 12px;
}

/* Base styles */
body {
    font-family: var(--tap-font-family);
    font-size: var(--tap-font-size-base);
    line-height: var(--tap-line-height-base);
}

/* Utility classes */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: var(--tap-spacing-md);
}

.btn {
    padding: var(--tap-spacing-sm) var(--tap-spacing-lg);
    border-radius: var(--tap-radius-md);
    border: none;
    cursor: pointer;
    font-weight: 600;
    transition: all 0.2s;
}

.btn-primary {
    background: var(--tap-primary-navy);
    color: white;
}

.btn-primary:hover {
    background: var(--tap-primary-purple);
}
'''
        
        core_styles_path = os.path.join(css_dir, 'core-styles.css')
        if not os.path.exists(core_styles_path):
            with open(core_styles_path, 'w', encoding='utf-8') as f:
                f.write(core_styles)
            self.fixes_applied.append("✅ Created css/core-styles.css")
            print("  ✅ Created css/core-styles.css")
            return True
        else:
            print("  ✓ css/core-styles.css already exists")
            return False
    
    def fix_keyboard_nav_references(self):
        """Fix keyboard-nav.js → keyboard-navigation.js references"""
        print("\n🔧 Fixing keyboard navigation references...")
        
        # Find all HTML files
        html_files = [f for f in os.listdir('.') if f.endswith('.html') and os.path.isfile(f)]
        
        fixed_count = 0
        for html_file in html_files:
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if 'keyboard-nav.js' in content and 'keyboard-navigation.js' not in content:
                    # Fix references
                    content = content.replace('keyboard-nav.js', 'keyboard-navigation.js')
                    
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    self.files_modified.add(html_file)
                    fixed_count += 1
            except Exception as e:
                print(f"  ⚠️  Error processing {html_file}: {e}")
        
        if fixed_count > 0:
            self.fixes_applied.append(f"✅ Fixed keyboard-nav.js references in {fixed_count} files")
            print(f"  ✅ Fixed {fixed_count} files")
        else:
            print("  ✓ No files needed fixing")
        
        return fixed_count
    
    def fix_storage_manager_references(self):
        """Fix storage-manager.js → safe-storage.js references"""
        print("\n🔧 Fixing storage manager references...")
        
        html_files = [f for f in os.listdir('.') if f.endswith('.html') and os.path.isfile(f)]
        
        fixed_count = 0
        for html_file in html_files:
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if 'storage-manager.js' in content:
                    # Replace with safe-storage.js
                    content = content.replace('storage-manager.js', 'safe-storage.js')
                    
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    self.files_modified.add(html_file)
                    fixed_count += 1
            except Exception as e:
                print(f"  ⚠️  Error processing {html_file}: {e}")
        
        if fixed_count > 0:
            self.fixes_applied.append(f"✅ Fixed storage-manager.js references in {fixed_count} files")
            print(f"  ✅ Fixed {fixed_count} files")
        else:
            print("  ✓ No files needed fixing")
        
        return fixed_count
    
    def create_lazy_confetti(self):
        """Create js/lazy-confetti.js"""
        print("\n🔧 Creating lazy-confetti.js...")
        
        js_dir = 'js'
        os.makedirs(js_dir, exist_ok=True)
        
        lazy_confetti_path = os.path.join(js_dir, 'lazy-confetti.js')
        
        if os.path.exists(lazy_confetti_path):
            print("  ✓ js/lazy-confetti.js already exists")
            return False
        
        # Create lazy confetti loader
        lazy_confetti = '''/**
 * Lazy Confetti Loader
 * Loads confetti library only when needed
 */

(function() {
    'use strict';
    
    let confettiLoaded = false;
    let confettiLib = null;
    
    function loadConfetti() {
        if (confettiLoaded) {
            return Promise.resolve(confettiLib);
        }
        
        return new Promise((resolve, reject) => {
            const script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js';
            script.async = true;
            script.onload = () => {
                confettiLoaded = true;
                confettiLib = window.confetti;
                resolve(confettiLib);
            };
            script.onerror = reject;
            document.head.appendChild(script);
        });
    }
    
    function triggerConfetti(options = {}) {
        return loadConfetti().then(() => {
            if (confettiLib) {
                confettiLib(options);
            }
        }).catch(err => {
            console.warn('Confetti failed to load:', err);
        });
    }
    
    // Export
    window.LazyConfetti = {
        load: loadConfetti,
        trigger: triggerConfetti
    };
    
    // Auto-load if confetti is already requested
    if (typeof window.confetti !== 'undefined') {
        confettiLoaded = true;
        confettiLib = window.confetti;
    }
})();
'''
        
        with open(lazy_confetti_path, 'w', encoding='utf-8') as f:
            f.write(lazy_confetti)
        
        self.fixes_applied.append("✅ Created js/lazy-confetti.js")
        print("  ✅ Created js/lazy-confetti.js")
        return True
    
    def fix_navigation_flows(self):
        """Fix navigation flow issues"""
        print("\n🔧 Fixing navigation flows...")
        
        fixes = []
        
        # Fix 1: Add return link to belt-assessment-v2.html
        if os.path.exists('belt-assessment-v2.html'):
            try:
                with open('belt-assessment-v2.html', 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if return link exists
                if 'gym-dashboard.html' not in content or 'window.location' not in content:
                    # Add return link before closing body or in results section
                    if '</body>' in content:
                        return_link = '\n    <a href="gym-dashboard.html" style="position: fixed; bottom: 20px; left: 20px; padding: 12px 24px; background: #1a365d; color: white; text-decoration: none; border-radius: 8px; z-index: 1000;">← Back to Gym</a>\n'
                        content = content.replace('</body>', return_link + '</body>', 1)
                        
                        with open('belt-assessment-v2.html', 'w', encoding='utf-8') as f:
                            f.write(content)
                        
                        self.files_modified.add('belt-assessment-v2.html')
                        fixes.append("✅ Added return link to belt-assessment-v2.html")
                        print("  ✅ Added return link to belt-assessment-v2.html")
            except Exception as e:
                print(f"  ⚠️  Error fixing belt-assessment-v2.html: {e}")
        
        if fixes:
            self.fixes_applied.extend(fixes)
        
        return len(fixes)
    
    def run_all_fixes(self):
        """Run all fixes"""
        print("="*80)
        print("🚀 COMPREHENSIVE AUDIT FIX - ALL ISSUES")
        print("="*80)
        
        # Run all fixes
        self.fix_css_core_styles()
        self.fix_keyboard_nav_references()
        self.fix_storage_manager_references()
        self.create_lazy_confetti()
        self.fix_navigation_flows()
        
        # Summary
        print("\n" + "="*80)
        print("📊 FIX SUMMARY")
        print("="*80)
        print(f"\nTotal fixes applied: {len(self.fixes_applied)}")
        print(f"Files modified: {len(self.files_modified)}")
        print("\n✅ Fixes:")
        for fix in self.fixes_applied:
            print(f"  {fix}")
        
        print("\n" + "="*80)
        print("✅ ALL FIXES COMPLETE")
        print("="*80)
        
        return len(self.fixes_applied)

def main():
    fixer = ComprehensiveFix()
    fixer.run_all_fixes()

if __name__ == '__main__':
    main()

