#!/usr/bin/env python3
"""
Update HTML files to use WebP images with PNG fallback
Converts <img> tags to <picture> tags with WebP + fallback
"""

import os
import re
from pathlib import Path

def find_webp_files():
    """Find all .webp files"""
    webp_files = {}
    
    for root, dirs, files in os.walk('.'):
        # Skip certain directories
        if any(excluded in root for excluded in ['node_modules', '.git', 'archive']):
            continue
        
        for file in files:
            if file.endswith('.webp'):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, '.')
                # Get corresponding PNG/JPG path
                base_path = rel_path.replace('.webp', '')
                
                # Check for PNG or JPG version
                png_path = base_path + '.png'
                jpg_path = base_path + '.jpg'
                jpeg_path = base_path + '.jpeg'
                
                if os.path.exists(png_path):
                    webp_files[base_path] = (png_path, rel_path, 'png')
                elif os.path.exists(jpg_path):
                    webp_files[base_path] = (jpg_path, rel_path, 'jpg')
                elif os.path.exists(jpeg_path):
                    webp_files[base_path] = (jpeg_path, rel_path, 'jpeg')
    
    return webp_files

def update_image_tags(content, webp_mapping):
    """Update <img> tags to use <picture> with WebP"""
    updated_content = content
    
    # Pattern to match <img> tags
    img_pattern = r'<img([^>]*?)src=["\']([^"\']+)["\']([^>]*?)>'
    
    def replace_img(match):
        before_src = match.group(1)
        src = match.group(2)
        after_src = match.group(3)
        
        # Extract alt, width, height, loading attributes
        alt_match = re.search(r'alt=["\']([^"\']*)["\']', before_src + after_src)
        alt = alt_match.group(1) if alt_match else ''
        
        width_match = re.search(r'width=["\']?(\d+)["\']?', before_src + after_src)
        width = width_match.group(1) if width_match else ''
        
        height_match = re.search(r'height=["\']?(\d+)["\']?', before_src + after_src)
        height = height_match.group(1) if height_match else ''
        
        loading_match = re.search(r'loading=["\']?(\w+)["\']?', before_src + after_src)
        loading = loading_match.group(1) if loading_match else 'lazy'
        
        # Check if we have WebP version for this image
        src_base = src.rsplit('.', 1)[0] if '.' in src else src
        ext = src.rsplit('.', 1)[1] if '.' in src else ''
        
        if src_base in webp_mapping:
            original_path, webp_path, orig_ext = webp_mapping[src_base]
            
            # Build <picture> tag
            picture = f'<picture>'
            picture += f'\n  <source srcset="{webp_path}" type="image/webp">'
            picture += f'\n  <img src="{original_path}"'
            
            if alt:
                picture += f' alt="{alt}"'
            if width:
                picture += f' width="{width}"'
            if height:
                picture += f' height="{height}"'
            if loading:
                picture += f' loading="{loading}"'
            
            # Preserve other attributes
            other_attrs = re.sub(r'(alt|width|height|loading|src)=["\'][^"\']*["\']', '', before_src + after_src)
            other_attrs = re.sub(r'\s+', ' ', other_attrs).strip()
            if other_attrs:
                picture += f' {other_attrs}'
            
            picture += '>'
            picture += '\n</picture>'
            
            return picture
        
        # No WebP version, keep original but add lazy loading if missing
        if 'loading=' not in (before_src + after_src):
            img_tag = f'<img{before_src}src="{src}"{after_src} loading="lazy">'
            return img_tag
        
        return match.group(0)  # Return original
    
    updated_content = re.sub(img_pattern, replace_img, updated_content)
    
    return updated_content if updated_content != content else None

def update_html_file(filepath, webp_mapping):
    """Update HTML file to use WebP images"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ⚠️  Error reading {filepath}: {e}")
        return False
    
    updated_content = update_image_tags(content, webp_mapping)
    
    if updated_content:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True
        except Exception as e:
            print(f"  ⚠️  Error writing {filepath}: {e}")
            return False
    
    return False

def main():
    """Main function"""
    print("=" * 80)
    print("🖼️  UPDATING HTML FILES TO USE WEBP IMAGES")
    print("=" * 80)
    print()
    
    # Find all WebP files
    webp_mapping = find_webp_files()
    
    if not webp_mapping:
        print("⚠️  No WebP files found!")
        print("   Please convert images to WebP first:")
        print("   ./convert-images-to-webp.sh")
        return
    
    print(f"🖼️  Found {len(webp_mapping)} WebP images")
    print()
    
    # Find HTML files
    html_files = []
    exclude_dirs = {'node_modules', '.git', 'archive', '__pycache__', 'android', 'ios', 'dist', 'build', 'react-app'}
    
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                html_files.append(filepath)
    
    print(f"📋 Found {len(html_files)} HTML files")
    print()
    
    # Update HTML files
    updated = 0
    skipped = 0
    
    for filepath in sorted(html_files):
        rel_path = os.path.relpath(filepath, '.')
        if update_html_file(filepath, webp_mapping):
            print(f"  ✅ Updated: {rel_path}")
            updated += 1
        else:
            skipped += 1
    
    print()
    print("=" * 80)
    print(f"✅ COMPLETE: Updated {updated} files, Skipped {skipped} files")
    print("=" * 80)
    print()
    print("📝 Next steps:")
    print("  1. Test all images load correctly")
    print("  2. Verify WebP fallback works")
    print("  3. Check performance improvements")

if __name__ == '__main__':
    main()

