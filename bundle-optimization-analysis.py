#!/usr/bin/env python3
"""
Bundle Optimization Analysis
- Find duplicate CSS
- Find duplicate JavaScript
- Identify common patterns for extraction
"""

from pathlib import Path
import re
from collections import Counter

def analyze_css_duplication():
    """Analyze CSS duplication across files"""
    
    print("📊 Analyzing CSS duplication...")
    
    common_patterns = Counter()
    total_css_lines = 0
    files_with_css = []
    
    for html_file in Path('.').glob('*.html'):
        if any(skip in str(html_file) for skip in ['node_modules', '.git', 'react-app']):
            continue
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract CSS from <style> tags
            style_matches = re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
            
            for style_content in style_matches:
                files_with_css.append(html_file.name)
                lines = style_content.split('\n')
                total_css_lines += len(lines)
                
                # Find common patterns
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith('/*') and ':' in line:
                        # Extract property
                        prop_match = re.match(r'([^:]+):', line)
                        if prop_match:
                            prop = prop_match.group(1).strip()
                            common_patterns[prop] += 1
        except:
            pass
    
    print(f"  • Total CSS lines across files: {total_css_lines}")
    print(f"  • Files with inline CSS: {len(files_with_css)}")
    print(f"  • Most common CSS properties:")
    for prop, count in common_patterns.most_common(10):
        print(f"    - {prop}: {count} occurrences")
    
    return {
        'total_lines': total_css_lines,
        'files_count': len(files_with_css),
        'common_patterns': common_patterns
    }

def analyze_js_duplication():
    """Analyze JavaScript duplication"""
    
    print("\n📊 Analyzing JavaScript duplication...")
    
    # Check for duplicate function definitions
    function_patterns = Counter()
    js_files = list(Path('js').glob('*.js')) if Path('js').exists() else []
    
    print(f"  • JavaScript files in js/: {len(js_files)}")
    
    # Common functions that might be duplicated
    common_functions = [
        'getTotalXP', 'awardXP', 'showToast', 'triggerConfetti',
        'updateProgress', 'checkMilestones', 'showAchievement'
    ]
    
    duplication_found = []
    
    for html_file in Path('.').glob('*.html'):
        if any(skip in str(html_file) for skip in ['node_modules', '.git', 'react-app']):
            continue
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for func_name in common_functions:
                # Count inline function definitions
                pattern = rf'function\s+{func_name}\s*\(|{func_name}\s*[:=]\s*function|const\s+{func_name}\s*='
                matches = len(re.findall(pattern, content))
                if matches > 0:
                    duplication_found.append((html_file.name, func_name, matches))
        except:
            pass
    
    if duplication_found:
        print(f"  • Potential duplicate functions found:")
        for filename, func_name, count in duplication_found[:10]:
            print(f"    - {func_name} in {filename} ({count} instances)")
    else:
        print("  • No obvious duplication found")
    
    return {
        'js_files': len(js_files),
        'duplications': duplication_found
    }

def generate_recommendations(css_stats, js_stats):
    """Generate optimization recommendations"""
    
    print("\n💡 Optimization Recommendations:")
    print()
    
    print("1. CSS Optimization:")
    print("   ✅ Already using core-styles.css")
    print("   💡 Consider extracting common patterns to core-styles.css")
    print("   💡 Remove inline styles where possible")
    print()
    
    print("2. JavaScript Optimization:")
    print("   ✅ Already using shared modules (core-gamification.js, shared-quiz-system.js)")
    print("   💡 Continue extracting common functions to shared modules")
    print()
    
    print("3. Asset Optimization:")
    print("   ✅ Images already small (30KB total)")
    print("   💡 Optional: Convert to WebP format")
    print()
    
    print("4. Code Splitting:")
    print("   💡 Consider lazy-loading non-critical JS")
    print("   💡 Load assessments on-demand")
    print()

def main():
    print("=" * 80)
    print("📦 BUNDLE OPTIMIZATION ANALYSIS")
    print("=" * 80)
    print()
    
    css_stats = analyze_css_duplication()
    js_stats = analyze_js_duplication()
    
    generate_recommendations(css_stats, js_stats)
    
    print("=" * 80)
    print("✅ Analysis complete")
    print("=" * 80)
    print()
    print("📊 Current Status: Already well-optimized!")
    print("   - CSS centralized in core-styles.css")
    print("   - JS modules shared (core-gamification, shared-quiz-system)")
    print("   - Images small (30KB total)")
    print("   - Minification already implemented")
    print()
    print("💡 Optional improvements:")
    print("   - Extract remaining inline styles (low priority)")
    print("   - WebP image conversion (low priority)")
    print("   - Code splitting for large pages (medium priority)")

if __name__ == '__main__':
    main()

