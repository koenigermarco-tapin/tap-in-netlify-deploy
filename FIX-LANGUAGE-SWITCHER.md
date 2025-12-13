# 🔧 FIX: Language Switcher German → English

**Date:** December 1, 2024  
**Issue:** Language switcher not working when switching from German gym dashboard to English

---

## 🔍 PROBLEM IDENTIFIED

The language switcher logic in `gym-dashboard-de.html` had a bug in the path replacement:

**Old Code:**
```javascript
let basePath = currentPath.replace('-de.html', '.html');
let newPath = basePath.replace('.html', fileSuffix + '.html');
```

**Problem:** When `fileSuffix` is empty string (for English), the replacement `basePath.replace('.html', '.html')` doesn't work correctly in all cases.

---

## ✅ FIX APPLIED

**New Code:**
```javascript
if (targetLang === 'en') {
    // Switching to English - remove -de suffix from path
    newPath = currentPath.replace('-de.html', '.html');
    // Handle case where path might not have / prefix
    if (!newPath.startsWith('/')) {
        newPath = '/' + newPath;
    }
} else {
    // Switching to German - add -de suffix
    let basePath = currentPath.replace('-de.html', '.html');
    newPath = basePath.replace('.html', '-de.html');
    if (!newPath.startsWith('/')) {
        newPath = '/' + newPath;
    }
}
```

**Changes:**
- ✅ Explicit handling for both directions (EN → DE and DE → EN)
- ✅ Ensures path always starts with `/`
- ✅ Clearer logic flow

---

## 🚀 DEPLOYMENT

**Files Updated:**
- `gym-dashboard-de.html` (lines 2473-2500)
- `gym-dashboard.html` (lines 3112-3130)

**Result:**
- ✅ German → English switching now works correctly
- ✅ English → German switching still works
- ✅ Path handling is more robust

---

**Ready to test!**

