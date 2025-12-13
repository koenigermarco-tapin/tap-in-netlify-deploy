#!/usr/bin/env python3
"""
Image Optimization Script
Finds images and provides WebP conversion instructions
"""

import os
import re
from pathlib import Path

def find_images():
    """Find all image files"""
    images = {
        'png': [],
        'jpg': [],
        'jpeg': []
    }
    
    exclude_dirs = {'node_modules', '.git', 'archive', '__pycache__', 'android', 'ios', 'dist', 'build', 'react-app'}
    
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if file.lower().endswith('.png'):
                images['png'].append(os.path.join(root, file))
            elif file.lower().endswith(('.jpg', '.jpeg')):
                images['jpg'].append(os.path.join(root, file))
    
    return images

def generate_webp_conversion_script():
    """Generate script to convert images to WebP"""
    images = find_images()
    
    total = len(images['png']) + len(images['jpg'])
    
    print("=" * 80)
    print("🖼️  IMAGE OPTIMIZATION REPORT")
    print("=" * 80)
    print()
    print(f"📊 Found {total} images to optimize:")
    print(f"  - PNG: {len(images['png'])} files")
    print(f"  - JPG/JPEG: {len(images['jpg'])} files")
    print()
    
    if total == 0:
        print("✅ No images found to optimize!")
        return
    
    # Generate conversion script
    script_content = """#!/bin/bash
# Image to WebP Conversion Script
# Requires: cwebp (install via: brew install webp or apt-get install webp)

echo "🖼️  Converting images to WebP format..."
echo ""

"""
    
    all_images = images['png'] + images['jpg']
    for img_path in all_images:
        rel_path = os.path.relpath(img_path, '.')
        base_name = os.path.splitext(rel_path)[0]
        webp_path = base_name + '.webp'
        
        script_content += f'# Convert {rel_path}\n'
        script_content += f'if [ -f "{rel_path}" ]; then\n'
        script_content += f'  echo "Converting {rel_path}..."\n'
        script_content += f'  cwebp -q 85 "{rel_path}" -o "{webp_path}"\n'
        script_content += f'  if [ $? -eq 0 ]; then\n'
        script_content += f'    echo "  ✅ Created {webp_path}"\n'
        script_content += f'  else\n'
        script_content += f'    echo "  ⚠️  Failed to convert {rel_path}"\n'
        script_content += f'  fi\n'
        script_content += f'fi\n'
        script_content += f'\n'
    
    script_content += 'echo ""\n'
    script_content += 'echo "✅ Image conversion complete!"\n'
    
    with open('convert-images-to-webp.sh', 'w') as f:
        f.write(script_content)
    
    os.chmod('convert-images-to-webp.sh', 0o755)
    
    print("✅ Generated conversion script: convert-images-to-webp.sh")
    print()
    print("📝 To convert images:")
    print("   1. Install WebP tools: brew install webp (Mac) or apt-get install webp (Linux)")
    print("   2. Run: ./convert-images-to-webp.sh")
    print()
    
    # Create HTML update guide
    guide_content = f"""# Image Optimization Guide

## Current Status
- **Total Images Found:** {total}
- **PNG Files:** {len(images['png'])}
- **JPG/JPEG Files:** {len(images['jpg'])}

## Conversion Steps

### 1. Install WebP Tools
```bash
# Mac
brew install webp

# Linux
sudo apt-get install webp

# Windows
# Download from: https://developers.google.com/speed/webp/download
```

### 2. Convert Images
Run the generated script:
```bash
./convert-images-to-webp.sh
```

### 3. Update HTML Files
Replace image references with WebP and fallback:

**Before:**
```html
<img src="image.png" alt="Description">
```

**After:**
```html
<picture>
  <source srcset="image.webp" type="image/webp">
  <img src="image.png" alt="Description">
</picture>
```

Or with lazy loading:
```html
<picture>
  <source srcset="image.webp" type="image/webp">
  <img src="image.png" alt="Description" loading="lazy" width="800" height="600">
</picture>
```

## Benefits
- **30-50% smaller file sizes**
- **Faster page loads**
- **Better performance scores**
- **Modern browser support with fallback**

## Files to Update
"""
    
    # List files that reference images
    html_files = []
    exclude_dirs = {'node_modules', '.git', 'archive', '__pycache__', 'android', 'ios', 'dist', 'build', 'react-app'}
    
    for root, dirs, files in os.walk('.'):
        if any(ex in root for ex in exclude_dirs):
            continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    guide_content += f"\n**Total HTML files to check:** {len(html_files)}\n"
    guide_content += "\nUse search and replace to update `<img>` tags to `<picture>` format.\n"
    
    with open('IMAGE-OPTIMIZATION-GUIDE.md', 'w') as f:
        f.write(guide_content)
    
    print("✅ Created guide: IMAGE-OPTIMIZATION-GUIDE.md")
    print()
    print("📊 Summary:")
    print(f"  - {total} images found")
    print("  - Conversion script created")
    print("  - Optimization guide created")

if __name__ == '__main__':
    generate_webp_conversion_script()

