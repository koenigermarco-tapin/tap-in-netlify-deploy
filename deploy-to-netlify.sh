#!/bin/bash
# TAP-IN Netlify Deployment Script
# Clears cache and deploys fresh version

echo "🚀 TAP-IN Netlify Deployment Script"
echo "===================================="
echo ""

# Check if Netlify CLI is installed
if ! command -v netlify &> /dev/null; then
    echo "❌ Netlify CLI not found. Installing..."
    npm install -g netlify-cli
fi

# Check if logged in
if ! netlify status &> /dev/null; then
    echo "🔐 Please login to Netlify..."
    netlify login
fi

echo "📦 Preparing deployment..."
echo ""

# Update service worker cache version
echo "🔄 Updating service worker cache version..."
CURRENT_TIME=$(date +%s)
sed -i.bak "s/CACHE_VERSION = '.*'/CACHE_VERSION = 'tap-in-v2.0.1-ERROR-FIX-$CURRENT_TIME';/" sw.js
rm sw.js.bak 2>/dev/null
echo "✅ Cache version updated to: tap-in-v2.0.1-ERROR-FIX-$CURRENT_TIME"

echo ""
echo "🚀 Deploying to Netlify..."
echo ""

# Deploy to production
netlify deploy --prod --dir=.

echo ""
echo "✅ Deployment complete!"
echo ""
echo "📋 Next steps:"
echo "  1. Visit your Netlify site URL"
echo "  2. Hard refresh (Cmd+Shift+R / Ctrl+Shift+R)"
echo "  3. Clear service worker in DevTools if needed"
echo ""
echo "🎯 The new cache version will force users to get fresh content!"

