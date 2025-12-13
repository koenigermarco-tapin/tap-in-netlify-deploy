#!/bin/bash
# Image to WebP Conversion Script
# Requires: cwebp (install via: brew install webp or apt-get install webp)

echo "🖼️  Converting images to WebP format..."
echo ""

# Convert icon-144.png
if [ -f "icon-144.png" ]; then
  echo "Converting icon-144.png..."
  cwebp -q 85 "icon-144.png" -o "icon-144.webp"
  if [ $? -eq 0 ]; then
    echo "  ✅ Created icon-144.webp"
  else
    echo "  ⚠️  Failed to convert icon-144.png"
  fi
fi

# Convert icon-192.png
if [ -f "icon-192.png" ]; then
  echo "Converting icon-192.png..."
  cwebp -q 85 "icon-192.png" -o "icon-192.webp"
  if [ $? -eq 0 ]; then
    echo "  ✅ Created icon-192.webp"
  else
    echo "  ⚠️  Failed to convert icon-192.png"
  fi
fi

# Convert icon-384.png
if [ -f "icon-384.png" ]; then
  echo "Converting icon-384.png..."
  cwebp -q 85 "icon-384.png" -o "icon-384.webp"
  if [ $? -eq 0 ]; then
    echo "  ✅ Created icon-384.webp"
  else
    echo "  ⚠️  Failed to convert icon-384.png"
  fi
fi

# Convert icon-152.png
if [ -f "icon-152.png" ]; then
  echo "Converting icon-152.png..."
  cwebp -q 85 "icon-152.png" -o "icon-152.webp"
  if [ $? -eq 0 ]; then
    echo "  ✅ Created icon-152.webp"
  else
    echo "  ⚠️  Failed to convert icon-152.png"
  fi
fi

# Convert icon-72.png
if [ -f "icon-72.png" ]; then
  echo "Converting icon-72.png..."
  cwebp -q 85 "icon-72.png" -o "icon-72.webp"
  if [ $? -eq 0 ]; then
    echo "  ✅ Created icon-72.webp"
  else
    echo "  ⚠️  Failed to convert icon-72.png"
  fi
fi

# Convert icon-96.png
if [ -f "icon-96.png" ]; then
  echo "Converting icon-96.png..."
  cwebp -q 85 "icon-96.png" -o "icon-96.webp"
  if [ $? -eq 0 ]; then
    echo "  ✅ Created icon-96.webp"
  else
    echo "  ⚠️  Failed to convert icon-96.png"
  fi
fi

# Convert icon-128.png
if [ -f "icon-128.png" ]; then
  echo "Converting icon-128.png..."
  cwebp -q 85 "icon-128.png" -o "icon-128.webp"
  if [ $? -eq 0 ]; then
    echo "  ✅ Created icon-128.webp"
  else
    echo "  ⚠️  Failed to convert icon-128.png"
  fi
fi

# Convert icon-512.png
if [ -f "icon-512.png" ]; then
  echo "Converting icon-512.png..."
  cwebp -q 85 "icon-512.png" -o "icon-512.webp"
  if [ $? -eq 0 ]; then
    echo "  ✅ Created icon-512.webp"
  else
    echo "  ⚠️  Failed to convert icon-512.png"
  fi
fi

# Convert icons/icon-192x192.png
if [ -f "icons/icon-192x192.png" ]; then
  echo "Converting icons/icon-192x192.png..."
  cwebp -q 85 "icons/icon-192x192.png" -o "icons/icon-192x192.webp"
  if [ $? -eq 0 ]; then
    echo "  ✅ Created icons/icon-192x192.webp"
  else
    echo "  ⚠️  Failed to convert icons/icon-192x192.png"
  fi
fi

# Convert icons/icon-384x384.png
if [ -f "icons/icon-384x384.png" ]; then
  echo "Converting icons/icon-384x384.png..."
  cwebp -q 85 "icons/icon-384x384.png" -o "icons/icon-384x384.webp"
  if [ $? -eq 0 ]; then
    echo "  ✅ Created icons/icon-384x384.webp"
  else
    echo "  ⚠️  Failed to convert icons/icon-384x384.png"
  fi
fi

# Convert icons/icon-72x72.png
if [ -f "icons/icon-72x72.png" ]; then
  echo "Converting icons/icon-72x72.png..."
  cwebp -q 85 "icons/icon-72x72.png" -o "icons/icon-72x72.webp"
  if [ $? -eq 0 ]; then
    echo "  ✅ Created icons/icon-72x72.webp"
  else
    echo "  ⚠️  Failed to convert icons/icon-72x72.png"
  fi
fi

# Convert icons/icon-96x96.png
if [ -f "icons/icon-96x96.png" ]; then
  echo "Converting icons/icon-96x96.png..."
  cwebp -q 85 "icons/icon-96x96.png" -o "icons/icon-96x96.webp"
  if [ $? -eq 0 ]; then
    echo "  ✅ Created icons/icon-96x96.webp"
  else
    echo "  ⚠️  Failed to convert icons/icon-96x96.png"
  fi
fi

# Convert icons/icon-152x152.png
if [ -f "icons/icon-152x152.png" ]; then
  echo "Converting icons/icon-152x152.png..."
  cwebp -q 85 "icons/icon-152x152.png" -o "icons/icon-152x152.webp"
  if [ $? -eq 0 ]; then
    echo "  ✅ Created icons/icon-152x152.webp"
  else
    echo "  ⚠️  Failed to convert icons/icon-152x152.png"
  fi
fi

# Convert icons/icon-512x512.png
if [ -f "icons/icon-512x512.png" ]; then
  echo "Converting icons/icon-512x512.png..."
  cwebp -q 85 "icons/icon-512x512.png" -o "icons/icon-512x512.webp"
  if [ $? -eq 0 ]; then
    echo "  ✅ Created icons/icon-512x512.webp"
  else
    echo "  ⚠️  Failed to convert icons/icon-512x512.png"
  fi
fi

# Convert icons/icon-144x144.png
if [ -f "icons/icon-144x144.png" ]; then
  echo "Converting icons/icon-144x144.png..."
  cwebp -q 85 "icons/icon-144x144.png" -o "icons/icon-144x144.webp"
  if [ $? -eq 0 ]; then
    echo "  ✅ Created icons/icon-144x144.webp"
  else
    echo "  ⚠️  Failed to convert icons/icon-144x144.png"
  fi
fi

# Convert icons/icon-128x128.png
if [ -f "icons/icon-128x128.png" ]; then
  echo "Converting icons/icon-128x128.png..."
  cwebp -q 85 "icons/icon-128x128.png" -o "icons/icon-128x128.webp"
  if [ $? -eq 0 ]; then
    echo "  ✅ Created icons/icon-128x128.webp"
  else
    echo "  ⚠️  Failed to convert icons/icon-128x128.png"
  fi
fi

echo ""
echo "✅ Image conversion complete!"
