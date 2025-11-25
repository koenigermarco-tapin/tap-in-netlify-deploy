# 🟣 Purple Belt Testing Checklist

## Pre-Testing Setup
- [ ] Ensure all 4 stripe files are in place:
  - `purple-belt-stripe1-gamified.html` (1,529 lines)
  - `purple-belt-stripe2-gamified.html` (1,383 lines)
  - `purple-belt-stripe3-gamified.html` (1,633 lines)
  - `purple-belt-stripe4-gamified-NEW.html` (target: 1,600-1,800 lines)
- [ ] Clear localStorage to test fresh experience: `localStorage.clear()`
- [ ] Open browser console to watch for errors

---

## Stripe 1: Shared Goals (34 questions)

### Navigation
- [ ] Purple Belt hub → Stripe 1 link works
- [ ] Header shows "Purple Belt Stripe 1"
- [ ] Intro section loads properly
- [ ] "Back to Purple Belt" button works

### Question Flow
- [ ] All 34 questions display correctly
- [ ] Progress bar updates as you advance
- [ ] Mixed question types work (5-point scale, yes/no, scenarios, multiple choice)
- [ ] Can't advance without selecting answer
- [ ] Previous button works correctly
- [ ] Answers persist when going back

### Enhancement Boxes (5 total)
- [ ] Box after Q7: OKR research appears
- [ ] Box after Q14: Studies/context appears
- [ ] Box after Q21: Research appears
- [ ] Box after Q28: Studies appears
- [ ] Box after Q34: Final enhancement appears
- [ ] All boxes styled correctly with research citations

### Results Screen
- [ ] Score calculation displays correctly
- [ ] Score interpretation makes sense
- [ ] Recommendations are personalized
- [ ] XP awarded (+100 XP for completion)
- [ ] Stripe 1 marked complete in localStorage
- [ ] Can return to Purple Belt hub
- [ ] Purple Belt hub shows Stripe 1 as complete (green)

---

## Stripe 2: Healthy Conflict (37 questions)

### Navigation
- [ ] Purple Belt hub → Stripe 2 link works
- [ ] Header shows "Purple Belt Stripe 2"
- [ ] Intro section loads properly
- [ ] "Back to Purple Belt" button works

### Question Flow
- [ ] All 37 questions display correctly
- [ ] Progress bar updates
- [ ] Mixed question types work
- [ ] Answer validation works
- [ ] Navigation buttons function

### Enhancement Boxes (4 total)
- [ ] Box after Q9: Conflict research appears
- [ ] Box after Q18: Studies appears
- [ ] Box after Q27: Research appears
- [ ] Box after Q37: Final enhancement appears
- [ ] All boxes have research-backed content

### Results Screen
- [ ] Score calculation correct
- [ ] Interpretation relevant
- [ ] Actionable recommendations
- [ ] XP awarded (+100 XP)
- [ ] Stripe 2 marked complete
- [ ] Hub reflects completion

---

## Stripe 3: Collective Accountability (45 questions)

### Navigation
- [ ] Purple Belt hub → Stripe 3 link works
- [ ] Header displays correctly
- [ ] Intro section renders
- [ ] Back button functions

### Question Flow
- [ ] All 45 questions load
- [ ] Progress tracking accurate
- [ ] Question types varied and functional
- [ ] Answer selection works
- [ ] Navigation smooth

### Enhancement Boxes (11 total: 5 full + 6 mini reflection)
- [ ] Full enhancement box #1 (after batch 1)
- [ ] Mini reflection box #1
- [ ] Full enhancement box #2 (after batch 2)
- [ ] Mini reflection box #2
- [ ] Full enhancement box #3 (after batch 3)
- [ ] Mini reflection box #3
- [ ] Full enhancement box #4 (after batch 4)
- [ ] Mini reflection box #4
- [ ] Full enhancement box #5 (after batch 5)
- [ ] Mini reflection box #5
- [ ] Final reflection box
- [ ] All boxes display correctly with proper spacing

### Results Screen
- [ ] Score accurate
- [ ] Interpretation personalized
- [ ] Recommendations actionable
- [ ] XP awarded (+150 XP for 45 questions)
- [ ] Stripe 3 completion saved
- [ ] Hub updated

---

## Stripe 4: Results Focus (45 questions)

### Navigation
- [ ] Purple Belt hub → Stripe 4 link works (NEW file!)
- [ ] Header correct
- [ ] Intro renders
- [ ] Back button works

### Question Flow
- [ ] All ~45 questions present
- [ ] Progress bar functional
- [ ] Question variety works
- [ ] Answer validation
- [ ] Smooth navigation

### Enhancement Boxes
- [ ] Count total enhancement boxes (target: ~10-12)
- [ ] Verify research citations present
- [ ] Check mini reflection boxes between sections
- [ ] Ensure proper styling and spacing

### Results Screen
- [ ] Score calculation
- [ ] Interpretation
- [ ] Recommendations
- [ ] XP award (+150 XP)
- [ ] Completion marked
- [ ] Hub reflects all 4 stripes complete

---

## Purple Belt Hub Integration

### Visual Progress
- [ ] All 4 stripe progress bars show on hub header
- [ ] Completed stripes show green/check marks
- [ ] Incomplete stripes show default state

### Stripe Cards
- [ ] Stripe 1 card shows complete if done
- [ ] Stripe 2 card shows complete if done
- [ ] Stripe 3 card shows complete if done
- [ ] Stripe 4 card shows complete if done
- [ ] Hover effects work on all cards
- [ ] All links point to correct files

### Content Quality
- [ ] Introduction section compelling
- [ ] Research citations present
- [ ] BJJ philosophy integrated
- [ ] Lencioni reference accurate
- [ ] Quote attribution correct

---

## Gamification Integration

### XP Tracking
- [ ] Total XP accumulates across stripes (100+100+150+150 = 500 XP)
- [ ] XP displays in header/profile if present
- [ ] XP saves to `gamification` localStorage object

### Achievements
- [ ] "Purple Belt Complete" achievement unlocks after all 4 stripes
- [ ] Achievement toast/notification appears
- [ ] Achievement saves to localStorage

### Progress Persistence
- [ ] Closing browser and reopening maintains progress
- [ ] Can complete stripes in any order
- [ ] Progress syncs across all Purple Belt pages

---

## Cross-Browser Testing

### Desktop
- [ ] Chrome/Brave (primary)
- [ ] Safari
- [ ] Firefox
- [ ] Edge

### Mobile
- [ ] iOS Safari (iPhone)
- [ ] Chrome Mobile (Android)
- [ ] Responsive design works (cards stack properly)
- [ ] Touch interactions smooth
- [ ] Progress bar visible and functional

---

## Edge Cases

### Data Persistence
- [ ] Refresh mid-assessment maintains answers
- [ ] localStorage quota not exceeded
- [ ] Data persists across sessions

### Error Handling
- [ ] No console errors throughout flow
- [ ] Graceful handling of missing localStorage
- [ ] Works in incognito/private mode

### Performance
- [ ] Page loads quickly (<2 seconds)
- [ ] No lag when selecting answers
- [ ] Smooth animations and transitions
- [ ] Images/content load properly

---

## Final Deployment Checklist

### File Verification
- [ ] All 4 stripe files committed
- [ ] Purple Belt hub committed
- [ ] No temporary/test files in repo
- [ ] File names consistent (remove -NEW suffix if needed)

### Links & References
- [ ] All internal links work
- [ ] No broken external links
- [ ] Back navigation works from all pages
- [ ] GYM Dashboard link works

### Content Quality
- [ ] No typos in questions
- [ ] All research citations accurate
- [ ] Enhancement boxes provide value
- [ ] Results interpretations helpful

### Git Commit
- [ ] Descriptive commit message
- [ ] All files staged
- [ ] Push to main branch
- [ ] Verify on deployed site

---

## Success Criteria

✅ **All stripes complete and functional**
✅ **Hub accurately reflects progress**
✅ **XP/gamification works correctly**
✅ **No console errors**
✅ **Mobile responsive**
✅ **Content quality matches White/Blue Belt standard**
✅ **Research citations add educational value**
✅ **Navigation seamless throughout**

---

**Ready for Brown Belt rebuild once Purple Belt testing passes!** 🟤
