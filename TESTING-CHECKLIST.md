# Testing Checklist - Cache Fix Verification

## Before Testing

- [ ] Wait 5 minutes after deploy completes
- [ ] Clear browser cache (Cmd+Shift+Delete)
- [ ] Open incognito/private window (Cmd+Shift+N)

## Test 1: Language Switching (Primary Issue)

1. - [ ] Go to https://tap-in-assessments.netlify.app/worker-type-assessment.html
2. - [ ] Click **DE** in top-right
3. - [ ] Should see German version immediately
4. - [ ] Click **EN** in top-right
5. - [ ] Should see English version immediately
6. - [ ] Repeat 5 times: **EN → DE → EN → DE → EN**
7. - [ ] **NO duplicates should appear**
8. - [ ] **NO stale content should show**

**Expected:** Smooth switching, clean pages every time ✅

## Test 2: Cache Headers (Technical Verification)

1. - [ ] Open DevTools (F12) → **Network** tab
2. - [ ] Enable "Disable cache" checkbox (while DevTools open)
3. - [ ] Reload page
4. - [ ] Click on HTML file in Network tab
5. - [ ] Check **Response Headers:**

```
Cache-Control: no-cache, no-store, must-revalidate, max-age=0
Pragma: no-cache
Expires: 0
```

**Expected:** All 3 headers present ✅

## Test 3: Fresh Content on Refresh

1. - [ ] Go to https://tap-in-assessments.netlify.app/combined-leadership-profile.html
2. - [ ] Answer 5 questions
3. - [ ] **Hard refresh** (Cmd+Shift+R or Ctrl+Shift+R)
4. - [ ] Progress should reset to 0/46
5. - [ ] No saved answers

**Expected:** Fresh state after refresh ✅

## Test 4: Cross-Assessment Navigation

1. - [ ] Go to https://tap-in-assessments.netlify.app/
2. - [ ] Click "Worker Type Assessment" card
3. - [ ] Answer 2 questions
4. - [ ] Click **Back to Assessments** link
5. - [ ] Click "Team Dynamics Assessment" card
6. - [ ] Should see clean Team assessment (not Worker assessment)

**Expected:** No mixed content from different assessments ✅

## Test 5: Multiple Tabs (Edge Case)

1. - [ ] Open https://tap-in-assessments.netlify.app/worker-type-assessment.html in Tab 1
2. - [ ] Open same URL in Tab 2
3. - [ ] Answer different questions in each tab
4. - [ ] Switch between tabs
5. - [ ] Each tab should maintain its own state

**Expected:** Independent state per tab ✅

## Test 6: Mobile Responsiveness

1. - [ ] Open on mobile device or DevTools → Device Mode
2. - [ ] Test language switching on mobile
3. - [ ] Should work same as desktop

**Expected:** No mobile-specific caching issues ✅

## Failure Scenarios (If Issues Still Occur)

### If duplicates still appear:
- [ ] Check Netlify deploy status: https://app.netlify.com/sites/tap-in-assessments/deploys
- [ ] Verify commit `6332072` or newer is deployed
- [ ] Wait additional 10 minutes for edge cache purge
- [ ] Try different browser (Chrome/Firefox/Safari)

### If seeing "from cache" in Network tab:
- [ ] Uncheck "Disable cache" in DevTools and recheck
- [ ] Clear browser cache again (Settings → Clear browsing data)
- [ ] Try incognito window
- [ ] Check Response Headers match expected (see Test 2)

### If language switching doesn't work:
- [ ] Check browser console (F12) for JavaScript errors
- [ ] Verify HTML files deployed (not 404)
- [ ] Check that language links point to correct files:
  - EN: `worker-type-assessment.html`
  - DE: `worker-type-assessment.de.html`

## Pass/Fail Criteria

**PASS ✅** if all tests complete successfully:
- Language switching works smoothly
- No duplicate content
- Proper cache headers
- Fresh content on refresh
- Clean cross-assessment navigation

**FAIL ❌** if any test shows:
- Duplicate assessments appearing
- Stale content after language switch
- Missing cache-control headers
- Content persisting when it shouldn't

## Reporting Issues

If tests fail, collect this info:

1. **Screenshot** of the issue
2. **Browser & Version:** (Chrome 119, Safari 17, etc.)
3. **Network tab screenshot** showing cache headers
4. **Console errors** (F12 → Console tab)
5. **Test that failed:** (e.g., "Test 1, step 6")
6. **Netlify deploy ID:** From https://app.netlify.com/sites/tap-in-assessments/deploys

---

## Quick Test (30 seconds)

Just want to verify the critical fix works?

1. **Incognito window** → https://tap-in-assessments.netlify.app/worker-type-assessment.html
2. **Click:** EN → DE → EN → DE → EN (5 times)
3. **Should see:** Clean page switching, no duplicates

✅ Pass = Fix is working
❌ Fail = Report issue with screenshot
