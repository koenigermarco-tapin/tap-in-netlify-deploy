#!/usr/bin/env python3
"""
Comprehensive Layout & Design Problem Detection Scan
Scans for CSS, HTML structure, responsive design, and visual issues
"""

import os
import re
from pathlib import Path
from collections import defaultdict

issues = defaultdict(list)

def scan_html_file(filepath):
    """Scan HTML file for layout and design issues"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            filename = os.path.basename(filepath)
            
        # 1. Missing viewport meta tag
        if '<meta name="viewport"' not in content:
            issues[filename].append({
                'severity': 'HIGH',
                'category': 'Responsive Design',
                'issue': 'Missing viewport meta tag - mobile rendering will be broken',
                'line': '~<head> section'
            })
        
        # 2. Check for inline styles that should be in CSS
        inline_styles = re.findall(r'style="[^"]{100,}"', content)
        if len(inline_styles) > 10:
            issues[filename].append({
                'severity': 'MEDIUM',
                'category': 'Code Quality',
                'issue': f'Too many inline styles ({len(inline_styles)}) - should be in CSS file',
                'line': 'Multiple locations'
            })
        
        # 3. Missing alt attributes on images
        img_tags = re.findall(r'<img[^>]*>', content, re.IGNORECASE)
        for img in img_tags:
            if 'alt=' not in img.lower() and 'alt=""' not in img.lower():
                issues[filename].append({
                    'severity': 'HIGH',
                    'category': 'Accessibility',
                    'issue': 'Image missing alt attribute',
                    'line': img[:100]
                })
        
        # 4. Check for broken CSS links
        css_links = re.findall(r'<link[^>]*href=["\']([^"\']+\.css)["\']', content)
        for css_link in css_links:
            if not css_link.startswith('http') and not css_link.startswith('//'):
                css_path = Path(filepath).parent / css_link.replace('/', os.sep)
                if not css_path.exists():
                    issues[filename].append({
                        'severity': 'HIGH',
                        'category': 'Broken Assets',
                        'issue': f'CSS file not found: {css_link}',
                        'line': css_link
                    })
        
        # 5. Check for broken JS links
        js_scripts = re.findall(r'<script[^>]*src=["\']([^"\']+\.js)["\']', content)
        for js_link in js_scripts:
            if not js_link.startswith('http') and not js_link.startswith('//'):
                js_path = Path(filepath).parent / js_link.replace('/', os.sep)
                if not js_path.exists():
                    issues[filename].append({
                        'severity': 'HIGH',
                        'category': 'Broken Assets',
                        'issue': f'JavaScript file not found: {js_link}',
                        'line': js_link
                    })
        
        # 6. Missing closing tags (basic check)
        open_divs = content.count('<div')
        close_divs = content.count('</div>')
        if open_divs != close_divs:
            issues[filename].append({
                'severity': 'HIGH',
                'category': 'HTML Structure',
                'issue': f'Mismatched div tags: {open_divs} open, {close_divs} closed',
                'line': 'File-wide'
            })
        
        # 7. Check for deprecated HTML
        deprecated = [
            ('<center>', 'Use CSS text-align instead'),
            ('<font>', 'Use CSS font properties instead'),
            ('<marquee>', 'Use CSS animations instead'),
            ('align=', 'Use CSS instead'),
            ('bgcolor=', 'Use CSS background-color instead'),
        ]
        for dep, suggestion in deprecated:
            if dep in content:
                issues[filename].append({
                    'severity': 'LOW',
                    'category': 'Deprecated HTML',
                    'issue': f'Found deprecated HTML: {dep} - {suggestion}',
                    'line': 'Multiple locations'
                })
        
        # 8. Check for table layouts (should use CSS Grid/Flexbox)
        if '<table' in content and 'role=' not in content:
            table_count = content.count('<table')
            if table_count > 2:
                issues[filename].append({
                    'severity': 'MEDIUM',
                    'category': 'Layout',
                    'issue': f'Using tables for layout ({table_count} tables) - consider CSS Grid/Flexbox',
                    'line': 'Multiple locations'
                })
        
        # 9. Check for missing media queries
        if '@media' not in content and 'responsive' not in filename.lower():
            # Check if there are layout-related classes that might need responsive design
            if 'grid' in content or 'flex' in content or 'width:' in content:
                issues[filename].append({
                    'severity': 'MEDIUM',
                    'category': 'Responsive Design',
                    'issue': 'No media queries found - may not be mobile-responsive',
                    'line': '<style> section'
                })
        
        # 10. Check for hardcoded widths that might break on mobile
        hardcoded_widths = re.findall(r'width:\s*\d+px', content)
        if len(hardcoded_widths) > 5:
            issues[filename].append({
                'severity': 'MEDIUM',
                'category': 'Responsive Design',
                'issue': f'Multiple hardcoded pixel widths ({len(hardcoded_widths)}) - may break on mobile',
                'line': 'Multiple locations'
            })
        
        # 11. Check for missing semicolons in inline styles
        style_blocks = re.findall(r'style="([^"]+)"', content)
        for style in style_blocks[:10]:  # Check first 10
            if ';' in style and style.count(';') < style.count(':'):
                issues[filename].append({
                    'severity': 'LOW',
                    'category': 'CSS Syntax',
                    'issue': 'Potential missing semicolon in inline style',
                    'line': style[:50]
                })
        
        # 12. Check for z-index issues (very high values)
        high_zindex = re.findall(r'z-index:\s*(\d{4,})', content)
        if high_zindex:
            issues[filename].append({
                'severity': 'LOW',
                'category': 'CSS',
                'issue': f'Very high z-index values found: {", ".join(high_zindex)} - may cause stacking issues',
                'line': 'Multiple locations'
            })
        
        # 13. Check for !important overuse
        important_count = content.count('!important')
        if important_count > 20:
            issues[filename].append({
                'severity': 'MEDIUM',
                'category': 'CSS Quality',
                'issue': f'Too many !important declarations ({important_count}) - suggests CSS specificity issues',
                'line': 'Multiple locations'
            })
        
        # 14. Check for color contrast issues (basic - black text on dark bg)
        dark_bg_patterns = [
            r'background.*#[0-9a-fA-F]{3,6}',
            r'background-color.*#[0-9a-fA-F]{3,6}',
            r'bg-.*dark',
        ]
        dark_bgs = []
        for pattern in dark_bg_patterns:
            dark_bgs.extend(re.findall(pattern, content))
        
        if dark_bgs and '#fff' not in content.lower() and '#ffffff' not in content.lower():
            issues[filename].append({
                'severity': 'MEDIUM',
                'category': 'Accessibility',
                'issue': 'Dark backgrounds detected - ensure sufficient color contrast for text',
                'line': 'Multiple locations'
            })
        
        # 15. Check for missing favicon
        if 'favicon' not in content.lower() and 'icon' not in content.lower() and filename == 'index.html':
            issues[filename].append({
                'severity': 'LOW',
                'category': 'SEO/Branding',
                'issue': 'No favicon link found',
                'line': '<head> section'
            })
        
        # 16. Check for broken image links
        img_srcs = re.findall(r'<img[^>]*src=["\']([^"\']+)["\']', content, re.IGNORECASE)
        for img_src in img_srcs:
            if not img_src.startswith('http') and not img_src.startswith('//') and not img_src.startswith('data:'):
                img_path = Path(filepath).parent / img_src.replace('/', os.sep)
                if not img_path.exists():
                    issues[filename].append({
                        'severity': 'HIGH',
                        'category': 'Broken Assets',
                        'issue': f'Image file not found: {img_src}',
                        'line': img_src
                    })
        
        # 17. Check for unclosed HTML comments
        open_comments = content.count('<!--')
        close_comments = content.count('-->')
        if open_comments != close_comments:
            issues[filename].append({
                'severity': 'MEDIUM',
                'category': 'HTML Structure',
                'issue': f'Unclosed HTML comments: {open_comments} open, {close_comments} closed',
                'line': 'File-wide'
            })
        
        # 18. Check for duplicate IDs (should be unique)
        ids = re.findall(r'id=["\']([^"\']+)["\']', content)
        if len(ids) != len(set(ids)):
            duplicates = [id for id in ids if ids.count(id) > 1]
            issues[filename].append({
                'severity': 'HIGH',
                'category': 'HTML Structure',
                'issue': f'Duplicate IDs found: {", ".join(set(duplicates))}',
                'line': 'Multiple locations'
            })
        
        # 19. Check for empty alt attributes (should have descriptive text)
        empty_alts = re.findall(r'alt=["\']\s*["\']', content)
        if empty_alts:
            issues[filename].append({
                'severity': 'LOW',
                'category': 'Accessibility',
                'issue': f'Empty alt attributes found ({len(empty_alts)}) - consider if images are decorative',
                'line': 'Multiple locations'
            })
        
        # 20. Check for missing aria-labels on interactive elements
        buttons = re.findall(r'<button[^>]*>', content, re.IGNORECASE)
        buttons_without_label = 0
        for btn in buttons:
            if 'aria-label' not in btn and 'aria-labelledby' not in btn:
                # Check if button has text content
                btn_match = re.search(r'<button[^>]*>(.*?)</button>', content, re.DOTALL | re.IGNORECASE)
                if btn_match:
                    btn_text = btn_match.group(1).strip()
                    if not btn_text or len(btn_text) < 2:
                        buttons_without_label += 1
        
        if buttons_without_label > 0:
            issues[filename].append({
                'severity': 'MEDIUM',
                'category': 'Accessibility',
                'issue': f'Buttons without accessible labels: {buttons_without_label}',
                'line': 'Multiple locations'
            })
        
    except Exception as e:
        issues[os.path.basename(filepath)].append({
            'severity': 'HIGH',
            'category': 'File Error',
            'issue': f'Error reading file: {str(e)}',
            'line': 'N/A'
        })


def scan_css_file(filepath):
    """Scan CSS file for issues"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            filename = os.path.basename(filepath)
        
        # 1. Check for missing closing braces
        open_braces = content.count('{')
        close_braces = content.count('}')
        if open_braces != close_braces:
            issues[filename].append({
                'severity': 'HIGH',
                'category': 'CSS Syntax',
                'issue': f'Mismatched braces: {open_braces} open, {close_braces} closed',
                'line': 'File-wide'
            })
        
        # 2. Check for undefined custom properties
        custom_props = re.findall(r'var\(--([^)]+)\)', content)
        defined_props = re.findall(r'--([^:]+):', content)
        undefined = set(custom_props) - set(defined_props)
        if undefined:
            issues[filename].append({
                'severity': 'MEDIUM',
                'category': 'CSS Variables',
                'issue': f'Undefined CSS variables used: {", ".join(list(undefined)[:5])}',
                'line': 'Multiple locations'
            })
        
        # 3. Check for browser-specific prefixes (may need autoprefixer)
        if '-webkit-' in content or '-moz-' in content or '-ms-' in content:
            issues[filename].append({
                'severity': 'LOW',
                'category': 'Browser Compatibility',
                'issue': 'Browser-specific prefixes found - consider using Autoprefixer',
                'line': 'Multiple locations'
            })
        
        # 4. Check for media query issues
        media_queries = re.findall(r'@media[^{]*{', content)
        if media_queries:
            # Check for common breakpoints
            breakpoints = []
            for mq in media_queries:
                if 'max-width' in mq:
                    width = re.search(r'max-width:\s*(\d+)px', mq)
                    if width:
                        breakpoints.append(width.group(1))
            
            # Check if standard breakpoints are used
            standard_breaks = ['320', '480', '768', '1024', '1200']
            non_standard = [b for b in breakpoints if b not in standard_breaks]
            if non_standard and len(non_standard) == len(breakpoints):
                issues[filename].append({
                    'severity': 'LOW',
                    'category': 'Responsive Design',
                    'issue': f'Non-standard breakpoints used: {", ".join(non_standard)}px',
                    'line': '@media queries'
                })
        
    except Exception as e:
        issues[os.path.basename(filepath)].append({
            'severity': 'HIGH',
            'category': 'File Error',
            'issue': f'Error reading CSS file: {str(e)}',
            'line': 'N/A'
        })


def main():
    """Main scan function"""
    print("🔍 COMPREHENSIVE LAYOUT & DESIGN SCAN")
    print("=" * 70)
    print()
    
    # Scan HTML files
    html_files = []
    for root, dirs, files in os.walk('.'):
        # Skip certain directories
        skip_dirs = {'node_modules', '.git', 'android', 'ios', 'dist', 'build', '__pycache__'}
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    print(f"📄 Scanning {len(html_files)} HTML files...")
    for html_file in sorted(html_files):
        scan_html_file(html_file)
    
    # Scan CSS files
    css_files = []
    for root, dirs, files in os.walk('.'):
        skip_dirs = {'node_modules', '.git', 'android', 'ios', 'dist', 'build', '__pycache__'}
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        
        for file in files:
            if file.endswith('.css'):
                css_files.append(os.path.join(root, file))
    
    print(f"🎨 Scanning {len(css_files)} CSS files...")
    for css_file in sorted(css_files):
        scan_css_file(css_file)
    
    # Generate report
    print()
    print("=" * 70)
    print("📊 SCAN RESULTS")
    print("=" * 70)
    print()
    
    if not issues:
        print("✅ No issues found! Your code looks good.")
        return
    
    # Group by severity
    high_issues = []
    medium_issues = []
    low_issues = []
    
    for filename, file_issues in issues.items():
        for issue in file_issues:
            if issue['severity'] == 'HIGH':
                high_issues.append((filename, issue))
            elif issue['severity'] == 'MEDIUM':
                medium_issues.append((filename, issue))
            else:
                low_issues.append((filename, issue))
    
    # Print HIGH severity issues
    if high_issues:
        print("🔴 HIGH SEVERITY ISSUES")
        print("-" * 70)
        for filename, issue in high_issues:
            print(f"\n📄 {filename}")
            print(f"   Category: {issue['category']}")
            print(f"   Issue: {issue['issue']}")
            print(f"   Location: {issue['line']}")
        print()
    
    # Print MEDIUM severity issues
    if medium_issues:
        print("🟡 MEDIUM SEVERITY ISSUES")
        print("-" * 70)
        for filename, issue in medium_issues:
            print(f"\n📄 {filename}")
            print(f"   Category: {issue['category']}")
            print(f"   Issue: {issue['issue']}")
            print(f"   Location: {issue['line']}")
        print()
    
    # Print LOW severity issues (summary)
    if low_issues:
        print("🟢 LOW SEVERITY ISSUES")
        print("-" * 70)
        print(f"   {len(low_issues)} low-priority issues found (see detailed report)")
        print()
    
    # Summary
    print("=" * 70)
    print("📈 SUMMARY")
    print("=" * 70)
    print(f"   🔴 High:   {len(high_issues)}")
    print(f"   🟡 Medium: {len(medium_issues)}")
    print(f"   🟢 Low:    {len(low_issues)}")
    print(f"   📊 Total:  {len(high_issues) + len(medium_issues) + len(low_issues)}")
    print()
    
    # Generate detailed report file
    with open('DESIGN-LAYOUT-ISSUES-REPORT.md', 'w') as f:
        f.write("# 🔍 Comprehensive Layout & Design Issues Report\n\n")
        f.write(f"**Scan Date:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Files Scanned:** {len(html_files)} HTML, {len(css_files)} CSS\n\n")
        f.write("---\n\n")
        
        if high_issues:
            f.write("## 🔴 HIGH SEVERITY ISSUES\n\n")
            for filename, issue in high_issues:
                f.write(f"### 📄 {filename}\n\n")
                f.write(f"- **Category:** {issue['category']}\n")
                f.write(f"- **Issue:** {issue['issue']}\n")
                f.write(f"- **Location:** {issue['line']}\n\n")
            f.write("\n---\n\n")
        
        if medium_issues:
            f.write("## 🟡 MEDIUM SEVERITY ISSUES\n\n")
            for filename, issue in medium_issues:
                f.write(f"### 📄 {filename}\n\n")
                f.write(f"- **Category:** {issue['category']}\n")
                f.write(f"- **Issue:** {issue['issue']}\n")
                f.write(f"- **Location:** {issue['line']}\n\n")
            f.write("\n---\n\n")
        
        if low_issues:
            f.write("## 🟢 LOW SEVERITY ISSUES\n\n")
            for filename, issue in low_issues:
                f.write(f"### 📄 {filename}\n\n")
                f.write(f"- **Category:** {issue['category']}\n")
                f.write(f"- **Issue:** {issue['issue']}\n")
                f.write(f"- **Location:** {issue['line']}\n\n")
    
    print("📄 Detailed report saved to: DESIGN-LAYOUT-ISSUES-REPORT.md")
    print()


if __name__ == '__main__':
    main()

