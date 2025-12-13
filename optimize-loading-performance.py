#!/usr/bin/env python3
"""
Comprehensive Loading Performance Optimizer
Fixes: duplicate resource hints, blocking scripts, font loading, etc.
"""

import re
from pathlib import Path
from typing import List, Tuple

class PerformanceOptimizer:
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.content = file_path.read_text(encoding='utf-8')
        self.original = self.content
        self.changes = []
    
    def remove_duplicate_resource_hints(self):
        """Remove duplicate preconnect/dns-prefetch tags"""
        # Find all resource hints
        preconnect_pattern = r'<link rel="preconnect"[^>]*>'
        dns_prefetch_pattern = r'<link rel="dns-prefetch"[^>]*>'
        
        preconnects = re.findall(preconnect_pattern, self.content)
        dns_prefetches = re.findall(dns_prefetch_pattern, self.content)
        
        # Keep unique ones
        seen_preconnect = set()
        seen_dns_prefetch = set()
        
        unique_preconnects = []
        for pc in preconnects:
            # Extract href
            href_match = re.search(r'href="([^"]+)"', pc)
            if href_match:
                href = href_match.group(1)
                if href not in seen_preconnect:
                    seen_preconnect.add(href)
                    unique_preconnects.append(pc)
        
        unique_dns_prefetches = []
        for dp in dns_prefetches:
            href_match = re.search(r'href="([^"]+)"', dp)
            if href_match:
                href = href_match.group(1)
                if href not in seen_dns_prefetch:
                    seen_dns_prefetch.add(href)
                    unique_dns_prefetches.append(dp)
        
        # Replace all with unique set
        if len(preconnects) > len(unique_preconnects) or len(dns_prefetches) > len(unique_dns_prefetches):
            # Remove all existing
            self.content = re.sub(preconnect_pattern, '', self.content)
            self.content = re.sub(dns_prefetch_pattern, '', self.content)
            
            # Find insertion point (after charset/viewport, before fonts)
            insert_pattern = r'(<meta name="viewport"[^>]*>)'
            if re.search(insert_pattern, self.content):
                # Insert unique resource hints
                resource_hints = '\n'.join(unique_preconnects + unique_dns_prefetches)
                self.content = re.sub(
                    insert_pattern,
                    r'\1\n\n<!-- Performance: Resource Hints -->\n' + resource_hints,
                    self.content,
                    count=1
                )
                self.changes.append(f"Removed {len(preconnects) - len(unique_preconnects)} duplicate preconnect tags")
                self.changes.append(f"Removed {len(dns_prefetches) - len(unique_dns_prefetches)} duplicate dns-prefetch tags")
    
    def optimize_font_loading(self):
        """Ensure fonts load non-blocking"""
        # Check if font loading is optimized
        font_pattern = r'<link[^>]*fonts\.googleapis\.com[^>]*>'
        fonts = re.findall(font_pattern, self.content)
        
        for font in fonts:
            # Should have media="print" onload="this.media='all'"
            if 'media="print"' not in font or 'onload=' not in font:
                # Replace with optimized version
                optimized = re.sub(
                    r'(<link[^>]*fonts\.googleapis\.com[^>]*>)',
                    r'\1'.replace('>', ' media="print" onload="this.media=\'all\'">'),
                    font
                )
                # Add noscript fallback if not present
                if '<noscript>' not in self.content or 'fonts.googleapis.com' not in self.content.split('<noscript>')[1].split('</noscript>')[0]:
                    clean_font = font.replace(' media="print" onload="this.media=\'all\'"', '')
                    noscript_fallback = f'<noscript>\n    {clean_font}\n</noscript>'
                    self.content = self.content.replace(font, optimized + '\n' + noscript_fallback)
                    self.changes.append("Optimized font loading with non-blocking technique")
    
    def defer_non_critical_scripts(self):
        """Add defer to non-critical scripts"""
        # Scripts that should be deferred (not already deferred)
        script_pattern = r'<script([^>]*?)src="([^"]+)"([^>]*?)>'
        
        def should_defer(src: str) -> bool:
            """Determine if script should be deferred"""
            critical_scripts = [
                'cache-buster.js',
                'performance-optimizer',
                'language-switcher',
            ]
            # Don't defer critical scripts
            if any(critical in src for critical in critical_scripts):
                return False
            # Already deferred?
            return True
        
        def add_defer(match):
            full_tag = match.group(0)
            before_src = match.group(1)
            src = match.group(2)
            after_src = match.group(3)
            
            # Skip if already has defer or async
            if 'defer' in full_tag or 'async' in full_tag:
                return full_tag
            
            # Skip critical scripts
            if not should_defer(src):
                return full_tag
            
            # Add defer
            new_tag = f'<script{before_src}src="{src}"{after_src} defer>'
            return new_tag
        
        new_content = re.sub(script_pattern, add_defer, self.content)
        if new_content != self.content:
            self.content = new_content
            self.changes.append("Added defer to non-critical scripts")
    
    def optimize_cache_buster(self):
        """Ensure cache-buster is async"""
        cache_buster_pattern = r'<script([^>]*?)src="cache-buster\.js"([^>]*?)>'
        
        def make_async(match):
            full_tag = match.group(0)
            if 'async' in full_tag:
                return full_tag
            # Replace or add async
            if 'defer' in full_tag:
                return full_tag.replace('defer', 'async')
            return full_tag.replace('>', ' async>')
        
        new_content = re.sub(cache_buster_pattern, make_async, self.content)
        if new_content != self.content:
            self.content = new_content
            self.changes.append("Made cache-buster.js async")
    
    def optimize_css_loading(self):
        """Optimize CSS loading"""
        # Check for blocking CSS
        css_pattern = r'<link[^>]*rel="stylesheet"[^>]*>'
        css_links = re.findall(css_pattern, self.content)
        
        # Critical CSS should load normally
        # Non-critical CSS could be deferred, but let's keep it simple for now
        # Just ensure no duplicate CSS loads
        seen_css = set()
        for css in css_links:
            href_match = re.search(r'href="([^"]+)"', css)
            if href_match:
                href = href_match.group(1)
                if href in seen_css:
                    # Remove duplicate
                    self.content = self.content.replace(css, '', 1)
                    self.changes.append(f"Removed duplicate CSS: {href}")
                else:
                    seen_css.add(href)
    
    def optimize_loading_screen(self):
        """Optimize loading screen to hide faster"""
        # Look for loading screen logic
        loading_patterns = [
            r'window\.addEventListener\([\'"]load[\'"]',
            r'setTimeout\([^,]+,\s*[5-9]\d{3,}',  # Long timeouts (5000+)
        ]
        
        for pattern in loading_patterns:
            if re.search(pattern, self.content):
                # Change window.load to DOMContentLoaded for faster hide
                self.content = re.sub(
                    r'window\.addEventListener\([\'"]load[\'"]',
                    'document.addEventListener(\'DOMContentLoaded\'',
                    self.content
                )
                # Reduce long timeouts
                self.content = re.sub(
                    r'setTimeout\(([^,]+),\s*([5-9]\d{3,})',
                    r'setTimeout(\1, 3000',  # Max 3 seconds
                    self.content
                )
                self.changes.append("Optimized loading screen timing")
    
    def consolidate_resource_hints(self):
        """Consolidate resource hints into single block"""
        # Find all resource hints
        resource_hint_pattern = r'(<!--\s*Performance:.*?-->\s*)?<link rel="(preconnect|dns-prefetch)"[^>]*>'
        
        hints = re.findall(resource_hint_pattern, self.content)
        if len(hints) > 6:  # Too many scattered hints
            # Remove all hints
            self.content = re.sub(resource_hint_pattern, '', self.content)
            
            # Add consolidated block after viewport
            consolidated = '''<!-- Performance: Resource Hints -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="dns-prefetch" href="https://cdn.jsdelivr.net">'''
            
            self.content = re.sub(
                r'(<meta name="viewport"[^>]*>)',
                r'\1\n' + consolidated,
                self.content,
                count=1
            )
            self.changes.append("Consolidated resource hints")
    
    def optimize(self):
        """Run all optimizations"""
        self.remove_duplicate_resource_hints()
        self.optimize_font_loading()
        self.defer_non_critical_scripts()
        self.optimize_cache_buster()
        self.optimize_css_loading()
        self.optimize_loading_screen()
        self.consolidate_resource_hints()
        
        return self.content != self.original
    
    def save(self):
        """Save optimized content"""
        if self.content != self.original:
            self.file_path.write_text(self.content, encoding='utf-8')
            return True
        return False

def main():
    print("🚀 Performance Optimization - Loading Time")
    print("=" * 70)
    print()
    
    # Critical pages to optimize
    pages_to_optimize = [
        Path("index-DUAL-ENTRY.html"),
        Path("index-DUAL-ENTRY-de.html"),
        Path("gym-dashboard.html"),
        Path("gym-dashboard-de.html"),
        Path("learning-hub.html"),
        Path("learning-hub-de.html"),
        Path("index.html"),
    ]
    
    optimized = 0
    total_changes = 0
    
    for page_path in pages_to_optimize:
        if not page_path.exists():
            print(f"⚠️  Not found: {page_path}")
            continue
        
        print(f"📄 Optimizing: {page_path.name}")
        optimizer = PerformanceOptimizer(page_path)
        
        if optimizer.optimize():
            if optimizer.save():
                optimized += 1
                total_changes += len(optimizer.changes)
                print(f"  ✅ Applied {len(optimizer.changes)} optimizations:")
                for change in optimizer.changes:
                    print(f"     - {change}")
            else:
                print(f"  ⚠️  No changes to save")
        else:
            print(f"  ℹ️  Already optimized")
    
    print()
    print("=" * 70)
    print(f"✅ Optimized {optimized} files")
    print(f"📊 Total optimizations: {total_changes}")
    print()
    print("🎯 Performance improvements:")
    print("  - Removed duplicate resource hints")
    print("  - Optimized font loading (non-blocking)")
    print("  - Added defer to non-critical scripts")
    print("  - Made cache-buster async")
    print("  - Optimized loading screen timing")
    print("  - Consolidated resource hints")

if __name__ == "__main__":
    main()

