#!/bin/bash
# Setup Capacitor for TAP-IN App Store Publication

echo "🚀 Setting up Capacitor for TAP-IN..."
echo ""

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js first."
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed. Please install npm first."
    exit 1
fi

echo "✅ Node.js version: $(node --version)"
echo "✅ npm version: $(npm --version)"
echo ""

# Install Capacitor CLI globally
echo "📦 Installing Capacitor CLI..."
npm install -g @capacitor/cli

# Install Capacitor core
echo "📦 Installing Capacitor core..."
npm install @capacitor/core @capacitor/cli

# Initialize Capacitor
echo ""
echo "🔧 Initializing Capacitor..."
echo "App name: TAP-IN Leadership"
echo "App ID: com.tapin.leadership"
echo "Web dir: ."
echo ""

npx cap init "TAP-IN Leadership" "com.tapin.leadership" --web-dir="."

# Create capacitor config if it doesn't exist
if [ ! -f "capacitor.config.json" ]; then
    echo "📝 Creating capacitor.config.json..."
    cat > capacitor.config.json << 'EOF'
{
  "appId": "com.tapin.leadership",
  "appName": "TAP-IN Leadership",
  "webDir": ".",
  "bundledWebRuntime": false,
  "server": {
    "androidScheme": "https",
    "iosScheme": "https"
  },
  "ios": {
    "contentInset": "automatic"
  },
  "android": {
    "allowMixedContent": false
  },
  "plugins": {
    "SplashScreen": {
      "launchShowDuration": 2000,
      "backgroundColor": "#1a365d",
      "showSpinner": false
    }
  }
}
EOF
fi

echo ""
echo "✅ Capacitor setup complete!"
echo ""
echo "📋 Next steps:"
echo "  1. Install iOS platform: npm install @capacitor/ios && npx cap add ios"
echo "  2. Install Android platform: npm install @capacitor/android && npx cap add android"
echo "  3. Create app icons (see APP-STORE-PUBLICATION-GUIDE.md)"
echo "  4. Run: npx cap sync"
echo ""
echo "🚀 Ready to build native apps!"

