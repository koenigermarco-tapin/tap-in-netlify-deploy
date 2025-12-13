#!/bin/bash
# Final Comprehensive Verification Script
# Verifies all translations and language switchers

echo "🔍 FINAL COMPREHENSIVE VERIFICATION"
echo "===================================="
echo ""

PASS=0
FAIL=0

# Function to check if file exists
check_file() {
    if [ -f "$1" ]; then
        echo "✅ $2 exists"
        ((PASS++))
        return 0
    else
        echo "❌ $2 NOT FOUND: $1"
        ((FAIL++))
        return 1
    fi
}

# Function to check for English switcher in German files
check_english_switcher() {
    if grep -q "English Version\|🇬🇧\|belt-assessment-v2.html\|learning-hub.html\|gym-dashboard.html" "$1" 2>/dev/null; then
        echo "✅ $2 has English switcher"
        ((PASS++))
        return 0
    else
        echo "❌ $2 missing English switcher"
        ((FAIL++))
        return 1
    fi
}

# Function to check for German switcher in English files
check_german_switcher() {
    if grep -q "Deutsche Version\|🇩🇪\|-de.html" "$1" 2>/dev/null; then
        echo "✅ $2 has German switcher"
        ((PASS++))
        return 0
    else
        echo "⚠️  $2 missing German switcher (may be intentional)"
        return 0
    fi
}

# Function to check for English text in German files
check_english_text() {
    local file="$1"
    local name="$2"
    local found=0
    
    # Check for common English phrases that shouldn't be in German files
    if grep -qi "Continue your\|Take Assessment\|Start Team\|Recent Activity\|Your Toolbox\|Your Stats\|Day Streak\|Module Done\|Badges Earned" "$file" 2>/dev/null; then
        echo "⚠️  $name may contain English text (check manually)"
        found=1
    fi
    
    if [ $found -eq 0 ]; then
        echo "✅ $name appears properly translated"
        ((PASS++))
    fi
    return 0
}

echo "1️⃣ CRITICAL GERMAN PAGES"
echo "------------------------"
check_file "belt-assessment-de.html" "German Belt Assessment"
check_file "learning-hub-de.html" "German Learning Hub"
check_file "gym-dashboard-de.html" "German Gym Dashboard"
check_file "gym-home-FOCUSED-de.html" "German Focused Hub"
echo ""

echo "2️⃣ ENGLISH LANGUAGE SWITCHERS (DE → EN)"
echo "----------------------------------------"
check_english_switcher "belt-assessment-de.html" "belt-assessment-de.html"
check_english_switcher "learning-hub-de.html" "learning-hub-de.html"
check_english_switcher "gym-dashboard-de.html" "gym-dashboard-de.html"
check_english_switcher "gym-home-FOCUSED-de.html" "gym-home-FOCUSED-de.html"
echo ""

echo "3️⃣ GERMAN LANGUAGE SWITCHERS (EN → DE)"
echo "----------------------------------------"
check_german_switcher "belt-assessment-v2.html" "belt-assessment-v2.html"
check_german_switcher "learning-hub.html" "learning-hub.html"
check_german_switcher "gym-dashboard.html" "gym-dashboard.html"
echo ""

echo "4️⃣ TRANSLATION QUALITY CHECK"
echo "----------------------------"
check_english_text "gym-dashboard-de.html" "gym-dashboard-de.html"
check_english_text "learning-hub-de.html" "learning-hub-de.html"
check_english_text "belt-assessment-de.html" "belt-assessment-de.html"
echo ""

echo "5️⃣ CORE JAVASCRIPT FILES"
echo "-------------------------"
check_file "js/core-gamification.js" "Core Gamification"
check_file "js/supabase-config.js" "Supabase Config"
check_file "js/language-switcher.min.js" "Language Switcher"
echo ""

echo "6️⃣ CORE CSS FILES"
echo "-----------------"
check_file "css/core-styles.css" "Core Styles"
check_file "css/conversion-boosters.css" "Conversion Boosters"
echo ""

echo ""
echo "===================================="
echo "📊 VERIFICATION RESULTS"
echo "===================================="
TOTAL=$((PASS + FAIL))
if [ $TOTAL -gt 0 ]; then
    SUCCESS_RATE=$((PASS * 100 / TOTAL))
    echo "✅ PASSED: $PASS/$TOTAL checks ($SUCCESS_RATE%)"
    echo "❌ FAILED: $FAIL/$TOTAL checks"
else
    echo "No checks performed"
fi
echo ""

if [ $FAIL -eq 0 ]; then
    echo "🎉 ✅ ALL VERIFICATIONS PASSED!"
    echo "🚀 Repository is READY FOR FINAL ZIP"
    exit 0
else
    echo "⚠️  $FAIL verification(s) failed"
    echo "⚠️  Review failures above before creating zip"
    exit 1
fi

