#!/bin/bash
# Create Clean, Optimized Repository for Deployment
# Removes all unnecessary files, keeps only production files

echo "=== CREATING CLEAN REPOSITORY ==="
echo ""

# Create clean directory
CLEAN_DIR="../tap-in-CLEAN-PRODUCTION"
mkdir -p "$CLEAN_DIR"

echo "📁 Creating clean repository structure..."

# Copy essential directories
echo "  Copying essential directories..."
cp -r css "$CLEAN_DIR/" 2>/dev/null
cp -r js "$CLEAN_DIR/" 2>/dev/null
cp -r icons "$CLEAN_DIR/" 2>/dev/null
cp -r images "$CLEAN_DIR/" 2>/dev/null
cp -r content "$CLEAN_DIR/" 2>/dev/null 2>/dev/null || true
cp -r components "$CLEAN_DIR/" 2>/dev/null || true

# Copy essential HTML files (only production files)
echo "  Copying essential HTML files..."

# Core entry points
cp index.html "$CLEAN_DIR/"
cp index-DUAL-ENTRY.html "$CLEAN_DIR/"
cp index-DUAL-ENTRY-de.html "$CLEAN_DIR/"
cp index.de.html "$CLEAN_DIR/" 2>/dev/null || true

# Dashboards
cp gym-dashboard.html "$CLEAN_DIR/"
cp gym-dashboard-de.html "$CLEAN_DIR/"
cp learning-hub.html "$CLEAN_DIR/"
cp learning-hub-de.html "$CLEAN_DIR/" 2>/dev/null || true

# Belt landing pages
cp white-belt.html "$CLEAN_DIR/"
cp blue-belt.html "$CLEAN_DIR/"
cp purple-belt.html "$CLEAN_DIR/"
cp brown-belt.html "$CLEAN_DIR/"
cp black-belt.html "$CLEAN_DIR/"
cp white-belt-de.html "$CLEAN_DIR/" 2>/dev/null || true
cp blue-belt-de.html "$CLEAN_DIR/" 2>/dev/null || true
cp purple-belt-de.html "$CLEAN_DIR/" 2>/dev/null || true
cp brown-belt-de.html "$CLEAN_DIR/" 2>/dev/null || true
cp black-belt-de.html "$CLEAN_DIR/" 2>/dev/null || true

# Belt assessments
cp belt-assessment*.html "$CLEAN_DIR/" 2>/dev/null || true
cp *-belt-assessment*.html "$CLEAN_DIR/" 2>/dev/null || true

# All gamified stripe files (20 files)
cp *-belt-stripe*-gamified*.html "$CLEAN_DIR/" 2>/dev/null || true

# All assessments
cp *-assessment*.html "$CLEAN_DIR/" 2>/dev/null || true

# All modules
cp *-module*.html "$CLEAN_DIR/" 2>/dev/null || true

# All courses
cp course-*.html "$CLEAN_DIR/" 2>/dev/null || true

# All games
cp *-game*.html "$CLEAN_DIR/" 2>/dev/null || true
cp confession-poker*.html "$CLEAN_DIR/" 2>/dev/null || true
cp conflict-cards*.html "$CLEAN_DIR/" 2>/dev/null || true

# All open mat tools
cp open-mat-*.html "$CLEAN_DIR/" 2>/dev/null || true

# Business/Admin
cp business-portal*.html "$CLEAN_DIR/" 2>/dev/null || true
cp profile-*.html "$CLEAN_DIR/" 2>/dev/null || true
cp achievement-*.html "$CLEAN_DIR/" 2>/dev/null || true

# Other essential pages
cp stripe-navigator.html "$CLEAN_DIR/" 2>/dev/null || true
cp offline.html "$CLEAN_DIR/" 2>/dev/null || true
cp manifest.json "$CLEAN_DIR/" 2>/dev/null || true
cp sw.js "$CLEAN_DIR/"
cp service-worker.js "$CLEAN_DIR/" 2>/dev/null || true
cp cache-buster.js "$CLEAN_DIR/" 2>/dev/null || true

# Configuration files
cp _redirects "$CLEAN_DIR/" 2>/dev/null || true
cp _headers "$CLEAN_DIR/" 2>/dev/null || true
cp netlify.toml "$CLEAN_DIR/" 2>/dev/null || true
cp robots.txt "$CLEAN_DIR/" 2>/dev/null || true

# Copy avatar styles
cp avatar-styles.css "$CLEAN_DIR/" 2>/dev/null || true

echo "✅ Clean repository created at: $CLEAN_DIR"
echo ""
echo "📊 Summary:"
echo "  - Essential files only"
echo "  - No documentation"
echo "  - No Python scripts"
echo "  - No backup files"
echo "  - Ready for deployment"

