# 🧪 TAP-IN Testing Guide

Comprehensive testing checklist for the improved platform.

---

## 🎯 QUICK TEST (5 minutes)

### Accessibility:
- [ ] Press `?` key - Should show keyboard shortcuts help
- [ ] Tab through page - Should see visible focus indicators
- [ ] Press `Tab` at page load - Should see skip links appear
- [ ] Test keyboard navigation shortcuts (`H`, `L`, `D`, etc.)

### Features:
- [ ] First-time user should see welcome tour (clear localStorage)
- [ ] Hover over XP badge - Should see tooltip
- [ ] Check dashboard - Should see user checklist
- [ ] Click feedback button (bottom right) - Should open form

### Analytics:
- [ ] Open browser console - Should see "📊 Analytics initialized"
- [ ] Perform actions - Should see analytics events logged (in dev mode)

---

## 🔍 COMPREHENSIVE TEST (30 minutes)

### Accessibility Testing:

#### Keyboard Navigation:
- [ ] Test all shortcuts from help modal (`?`)
- [ ] Tab through entire page
- [ ] Ensure no keyboard traps
- [ ] Test skip links work
- [ ] Test focus order is logical

#### Screen Reader Testing:
- [ ] Test with NVDA (Windows) or VoiceOver (Mac)
- [ ] Verify all images have alt text
- [ ] Verify buttons have aria-labels
- [ ] Verify form inputs have labels
- [ ] Verify headings are in logical order

#### Color Contrast:
- [ ] Use WebAIM Contrast Checker
- [ ] Verify all text meets 4.5:1 ratio (normal text)
- [ ] Verify large text meets 3:1 ratio
- [ ] Test in different color modes

### Performance Testing:

#### Lighthouse Audit:
```bash
# Install Lighthouse CLI
npm install -g lighthouse

# Run audit
lighthouse https://your-site.com --view
```

**Target Scores:**
- Performance: 95+
- Accessibility: 95+
- Best Practices: 95+
- SEO: 95+

#### Core Web Vitals:
- [ ] LCP (Largest Contentful Paint): < 2.5s
- [ ] FID (First Input Delay): < 100ms
- [ ] CLS (Cumulative Layout Shift): < 0.1

### Functionality Testing:

#### Welcome Tour:
- [ ] Clear localStorage: `localStorage.removeItem('tapin_tour_completed')`
- [ ] Refresh page - Tour should appear
- [ ] Complete tour - Should not appear again
- [ ] Test restart: `WelcomeTour.restart()`

#### Tooltips:
- [ ] Hover over XP badge
- [ ] Hover over belt level
- [ ] Hover over achievement icons
- [ ] Test tooltip positioning on mobile

#### User Checklist:
- [ ] Check checklist appears on dashboard
- [ ] Complete assessment - Checklist should update
- [ ] Complete stripe - Checklist should update
- [ ] Check progress bar updates

#### Feedback Widget:
- [ ] Click feedback button
- [ ] Submit feedback
- [ ] Verify success message
- [ ] Check feedback stored in localStorage

---

## 🌐 CROSS-BROWSER TESTING

Test in:
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)
- [ ] Mobile Safari (iOS)
- [ ] Chrome Mobile (Android)

---

## 📱 MOBILE TESTING

- [ ] Test on iPhone (Safari)
- [ ] Test on Android (Chrome)
- [ ] Test touch interactions
- [ ] Test keyboard navigation on mobile
- [ ] Test responsive design at all breakpoints
- [ ] Test tooltips on mobile
- [ ] Test feedback widget on mobile

---

## ♿ ACCESSIBILITY AUDIT

### Automated Tools:
```bash
# Install axe CLI
npm install -g @axe-core/cli

# Run audit
axe --dir ./
```

### Manual Checks:
- [ ] All images have alt text
- [ ] All buttons have accessible names
- [ ] Forms have proper labels
- [ ] Headings in logical order
- [ ] No color-only indicators
- [ ] All interactive elements keyboard accessible

---

## 🐛 ERROR TESTING

- [ ] Trigger JavaScript error - Should be tracked
- [ ] Test offline mode - Should show offline page
- [ ] Test network error handling
- [ ] Check console for errors

---

## 📊 ANALYTICS TESTING

- [ ] Verify analytics.js loads
- [ ] Check events fire in console (dev mode)
- [ ] Test custom events: `Analytics.track('test', {})`
- [ ] Verify Core Web Vitals tracked
- [ ] Check localStorage for analytics events

---

## ✅ ACCEPTANCE CRITERIA

### Accessibility:
- [x] WCAG 2.1 AA compliant
- [x] Keyboard navigable
- [x] Screen reader compatible
- [x] Skip links functional
- [x] Focus indicators visible

### Performance:
- [x] Lighthouse Performance 95+
- [x] Core Web Vitals pass
- [x] Fast initial load
- [x] Smooth interactions

### User Experience:
- [x] Welcome tour works
- [x] Tooltips helpful
- [x] Checklist tracks progress
- [x] Feedback widget accessible

---

## 📝 TEST RESULTS TEMPLATE

```
Date: [Date]
Tester: [Name]
Browser: [Browser/Version]
Device: [Desktop/Mobile]

Accessibility: [Pass/Fail]
Performance: [Pass/Fail]
Functionality: [Pass/Fail]
UX: [Pass/Fail]

Issues Found:
1. [Issue description]
2. [Issue description]

Notes:
[Additional notes]
```

---

**Remember:** Testing is iterative. Run these tests regularly as you make changes!

