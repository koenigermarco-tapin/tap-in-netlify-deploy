# 🎨 TAP-IN App Icons Creation Guide

**Create all required app icons from a single source image**

---

## 📋 REQUIREMENTS

### Source Image:
- **Size**: 1024x1024 pixels
- **Format**: PNG (no transparency for store icons)
- **Background**: Solid color or image
- **Content**: Your app logo/icon
- **Quality**: High resolution, crisp edges

---

## 🛠️ OPTION 1: Online Tools (Easiest)

### Recommended Tools:

1. **AppIcon.co** (https://www.appicon.co)
   - Upload 1024x1024 image
   - Generates all iOS and Android sizes
   - Free (with watermark) or paid

2. **Icon Kitchen** (https://icon.kitchen)
   - Google's official icon generator
   - Generates adaptive icons
   - Free

3. **MakeAppIcon** (https://makeappicon.com)
   - Generates all sizes
   - Free download

### Steps:
1. Create or find your 1024x1024 source icon
2. Upload to one of the tools above
3. Download generated icons
4. Use in Capacitor project

---

## 🛠️ OPTION 2: Capacitor Assets CLI

### Install:
```bash
npm install -g @capacitor/assets
```

### Use:
```bash
# Generate all icons from source
npx @capacitor/assets generate \
  --iconPath ./assets/icon-source.png \
  --splashPath ./assets/splash-source.png \
  --iconBackgroundColor '#1a365d' \
  --splashBackgroundColor '#1a365d' \
  --iconBackgroundColorDark '#0a0a0a' \
  --splashBackgroundColorDark '#0a0a0a'
```

This automatically generates:
- ✅ All iOS icon sizes
- ✅ All Android icon sizes
- ✅ Adaptive icons (Android)
- ✅ Splash screens

---

## 📐 REQUIRED SIZES

### iOS Icons:
- **App Store**: 1024x1024 (required)
- **iPhone**: 180x180, 120x120, 87x87, 80x60, 60x60, 58x58, 40x40
- **iPad**: 167x167, 152x152, 76x76, 29x29, 20x20

### Android Icons:
- **Play Store**: 512x512 (required)
- **Adaptive Icon**: 
  - Foreground: 108dp circle/square
  - Background: 432dp
  - Various densities: mdpi, hdpi, xhdpi, xxhdpi, xxxhdpi

---

## 🎨 DESIGN GUIDELINES

### iOS:
- ✅ No transparency
- ✅ Rounded corners applied automatically by iOS
- ✅ No text (app name shown separately)
- ✅ Simple, recognizable at small sizes
- ✅ High contrast

### Android:
- ✅ Can have transparency (adaptive icons)
- ✅ Material Design guidelines
- ✅ Safe zone: Center 66% (avoid corners)
- ✅ Simple, clear icon

---

## 📁 FILE STRUCTURE

After generating icons:

```
your-project/
├── assets/
│   ├── icon-source.png (1024x1024)
│   └── splash-source.png (2048x2048)
├── ios/App/App/Assets.xcassets/AppIcon.appiconset/
│   └── [iOS icons here]
└── android/app/src/main/res/
    ├── mipmap-mdpi/
    ├── mipmap-hdpi/
    ├── mipmap-xhdpi/
    ├── mipmap-xxhdpi/
    └── mipmap-xxxhdpi/
```

---

## ✅ QUICK START

1. **Create source icon** (1024x1024 PNG)
2. **Use Capacitor Assets CLI**:
   ```bash
   npx @capacitor/assets generate --iconPath ./icon.png
   ```
3. **Done!** Icons automatically placed in correct locations

---

**Need help creating the source icon? I can guide you through the design process!**

