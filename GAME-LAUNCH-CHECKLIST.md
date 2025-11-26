# 🚀 GAME LAUNCH CHECKLIST

## Pre-Launch Testing (30 minutes)

### ✅ **Game 1: Confession Poker**
- [ ] Open `confession-poker-v2.html` in browser
- [ ] Test Pass & Play mode (add 3 players, play 1 round)
- [ ] Test Multi-Device mode (2 browser windows, different players)
- [ ] Verify card display (should see belt colors)
- [ ] Test rating system (1-5 scale works)
- [ ] Test challenge voting (if implemented)
- [ ] Check mobile responsive (open on phone)
- [ ] Verify game completion screen shows

**Critical Bugs to Check:**
- [ ] Cards load properly (52 total)
- [ ] Scores calculate correctly
- [ ] Timer doesn't break
- [ ] Room code joining works
- [ ] No console errors

---

### ✅ **Game 2: Conflict Cards**
- [ ] Open `conflict-cards.html` in browser
- [ ] Test Pass & Play (4 players, 2 rounds)
- [ ] Test judge rotation (verify judge changes)
- [ ] Test hand management (10 cards, refills work)
- [ ] Test SBIR bonus checkbox
- [ ] Test Multi-Device mode
- [ ] Check mobile card display (readable text)

**Critical Bugs to Check:**
- [ ] Black cards display properly
- [ ] White cards show in hand
- [ ] Judge can select winner
- [ ] Points awarded correctly
- [ ] SBIR bonus adds +2 not +1

---

### ✅ **Game 3: Take the Back**
- [ ] Open `take-the-back.html` in browser
- [ ] Test claiming mechanic (first press wins)
- [ ] Test 30-second claim timer
- [ ] Test 15-second explanation timer
- [ ] Test voting (thumbs up/down)
- [ ] Test DELIVERED vs ABANDONED tracking
- [ ] Check multi-device sync (2 devices)

**Critical Bugs to Check:**
- [ ] Timer countdown visible and accurate
- [ ] First-press detection fair across devices
- [ ] Vote tallying works
- [ ] Score = DELIVERED - ABANDONED
- [ ] Game ends at +10 or 20 rounds

---

### ✅ **Game 4: Disagree & Commit**
- [ ] Open `disagree-commit-roulette.html` in browser
- [ ] Test wheel spin animation
- [ ] Test 30-sec thinking timer
- [ ] Test 60-sec debate timer
- [ ] Test voting (Agree/Disagree)
- [ ] Test block token mechanic
- [ ] Test commitment logging
- [ ] Test consensus detection

**Critical Bugs to Check:**
- [ ] Wheel spins smoothly
- [ ] Timers don't freeze
- [ ] Simultaneous voting works
- [ ] Block tokens decrement properly
- [ ] Commitments save correctly

---

## Deployment Checklist (15 minutes)

### Option A: Netlify Drop (Recommended - Easiest)

**For Each Game:**
1. [ ] Go to https://app.netlify.com/drop
2. [ ] Drag HTML file to upload area
3. [ ] Wait for deployment (10 seconds)
4. [ ] Click URL to verify live site works
5. [ ] Test on mobile device via URL
6. [ ] Save URL to spreadsheet

**Expected URLs:**
- `https://RANDOM-NAME.netlify.app` (for confession-poker-v2.html)
- `https://RANDOM-NAME.netlify.app` (for conflict-cards.html)
- `https://RANDOM-NAME.netlify.app` (for take-the-back.html)
- `https://RANDOM-NAME.netlify.app` (for disagree-commit-roulette.html)

**Optional: Custom Domains**
- [ ] Buy domain: `tap-in-games.com` (optional)
- [ ] Point to Netlify in DNS settings
- [ ] Update to: `tap-in-games.com/confession-poker`

---

### Option B: Vercel CLI

```bash
# Install Vercel
npm i -g vercel

# Deploy each game
vercel --prod confession-poker-v2.html
vercel --prod conflict-cards.html
vercel --prod take-the-back.html
vercel --prod disagree-commit-roulette.html

# Save URLs from terminal output
```

---

### Option C: GitHub Pages

```bash
# Create repo
git init
git add *.html MULTIPLAYER-GAMES-README.md
git commit -m "Launch 4 multiplayer games"
git remote add origin https://github.com/yourusername/tap-in-games.git
git push -u origin main

# Enable Pages in repo Settings → Pages → Source: main branch
# Access at: https://yourusername.github.io/tap-in-games/confession-poker-v2.html
```

---

## Post-Deployment Verification (10 minutes)

### Test Live URLs:

**For Each Game:**
- [ ] Open production URL on desktop
- [ ] Open production URL on mobile phone
- [ ] Test Pass & Play mode (quick 1-round test)
- [ ] Test Multi-Device mode (2 devices, join same room)
- [ ] Share URL with friend → verify they can join
- [ ] Check loading time (<3 seconds on 4G)

**Firebase Check (Multi-Device Mode):**
- [ ] Create room on Device 1
- [ ] Join room on Device 2 with code
- [ ] Make action on Device 1 → verify Device 2 updates
- [ ] Make action on Device 2 → verify Device 1 updates
- [ ] Verify no lag (updates within 1 second)

---

## Initial User Testing (First Week)

### Beta Tester Recruitment:

**Who to ask:**
- [ ] 3 friends (casual test)
- [ ] 1 team from your company (workshop simulation)
- [ ] 1 external team (ideal: HR/L&D professional)
- [ ] Post in relevant Slack/Discord communities

**What to ask them:**

**Email Template:**
```
Subject: Test my new leadership games? (15 min)

Hey [Name],

I just launched 4 multiplayer web games for teams to practice 
giving feedback, handling conflict, and building trust.

Would you test one with your team and give me 2 minutes of feedback?

Pick any game:
🃏 Confession Poker (vulnerability): [URL]
💼 Conflict Cards (feedback): [URL]  
🔥 Take the Back (ownership): [URL]
🎯 Disagree & Commit (decision-making): [URL]

All you need:
- 3+ people (teammates, friends, anyone)
- 20 minutes
- Phones/laptops

After playing, just reply with:
1. What worked? ✅
2. What broke? 🐛
3. What confused you? 🤔

Thanks! - [Your Name]
```

---

## Feedback Collection (Week 1)

### Questions to Ask Testers:

**Game Mechanics:**
- [ ] Did the game rules make sense?
- [ ] Were the timers too short/long?
- [ ] Did scoring feel fair?
- [ ] Were there enough cards/scenarios?

**Technical:**
- [ ] Did it work on your device?
- [ ] Was joining a room easy (multi-device)?
- [ ] Did anything break or freeze?
- [ ] How was the loading speed?

**Experience:**
- [ ] Was it fun?
- [ ] Would you play again?
- [ ] Would you recommend to others?
- [ ] Which game did you like best?

**Workshop Fit:**
- [ ] Could you use this in a team workshop?
- [ ] What would make it better for that?
- [ ] How much would you pay for this?

---

## Analytics Setup (Optional - Week 2)

**If you want data before enhancements:**

1. [ ] Sign up for Google Analytics (free)
2. [ ] Get tracking ID (G-XXXXXXXXXX)
3. [ ] Add tracking snippet to each game (see `game-analytics-snippet.js`)
4. [ ] Deploy updated versions
5. [ ] Verify events appear in GA dashboard

**Events to Track:**
- [ ] Game started (which game, which mode)
- [ ] Round completed (progression tracking)
- [ ] Game finished (completion rate)
- [ ] Room joined (multi-device adoption)

**After 7 days, check:**
- Which game has most starts?
- What's the completion rate?
- Pass & Play vs Multi-Device ratio?
- Where do people drop off?

---

## Launch Announcement (Week 1)

### LinkedIn Post:

- [ ] Write post (template below)
- [ ] Record 30-second demo video (optional but recommended)
- [ ] Post on LinkedIn
- [ ] Share in relevant groups
- [ ] Tag Tap-In company page

**Post Template:** (see `linkedin-launch-post.md`)

---

### Email to Network:

- [ ] Write email (template below)
- [ ] Send to colleagues
- [ ] Send to former clients
- [ ] Send to HR/L&D contacts
- [ ] Send to Tap-In team

**Email Template:** (see `email-launch-template.md`)

---

## Success Metrics (First Week)

### Minimum Viable Success:
- [ ] 10+ people play a game
- [ ] 3+ complete games (start to finish)
- [ ] 5+ pieces of feedback received
- [ ] 0 critical bugs reported
- [ ] 1+ spontaneous share/recommendation

### Ideal Success:
- [ ] 50+ game sessions
- [ ] 20+ completions
- [ ] 1+ team uses in actual workshop
- [ ] Someone asks "Can I buy this?"
- [ ] Post gets 500+ LinkedIn views

---

## Decision Points (End of Week 1)

### If games work well (0-2 minor bugs):
→ **DO:** Focus on marketing and distribution
→ **DON'T:** Add features yet

### If games have bugs (3+ issues):
→ **DO:** Fix critical bugs first
→ **DON'T:** Launch publicly until stable

### If one game dominates (>60% of plays):
→ **DO:** Double down on that game
→ **DON'T:** Invest equally in all 4

### If multi-device mode unused (<20%):
→ **DO:** Improve onboarding for room joining
→ **DON'T:** Build more multi-device features yet

### If completion rate low (<40%):
→ **DO:** Simplify rules or shorten games
→ **DON'T:** Add complexity

---

## Next Steps Decision Tree

```
START HERE ↓

Did 10+ people play? 
├─ NO → Focus on distribution (marketing, outreach)
└─ YES → Did 50%+ complete the game?
    ├─ NO → Simplify mechanics or fix UX issues
    └─ YES → Did anyone ask to pay for it?
        ├─ NO → Add lead capture, build email list
        └─ YES → Create pricing page, enable purchases!

Any critical bugs?
├─ YES → STOP. Fix bugs before marketing.
└─ NO → Green light to promote widely.

Which game was most popular?
└─ Focus 80% of effort on that game for now.
```

---

## Week 2+ Enhancements (Only After User Feedback)

**Don't do these until you have real user data:**

- [ ] Add most-requested feature
- [ ] Fix most-reported bug
- [ ] Improve most confusing UX element
- [ ] Add analytics if conversion matters
- [ ] Add lead capture if building list
- [ ] Add social sharing if viral potential
- [ ] Translate to German if DACH traction

**Golden Rule:** 
**User feedback > Your assumptions**

---

## Emergency Contacts

**If something breaks:**
- Firebase issues: Check console.firebase.google.com
- Deployment issues: Check Netlify/Vercel dashboard
- DNS issues: Check domain registrar settings
- Bug reports: Create GitHub issues or Notion page

**Where to get help:**
- React issues: Stack Overflow
- Firebase issues: Firebase Discord
- Netlify issues: Netlify support chat
- General: Claude/ChatGPT

---

## 🎉 Launch Day Protocol

**Hour 0 (Morning):**
- [ ] Final test of all 4 games
- [ ] Deploy to production
- [ ] Verify all URLs work
- [ ] Screenshot success state of each game

**Hour 1 (Noon):**
- [ ] Post to LinkedIn
- [ ] Email to 10 close contacts
- [ ] Share in Tap-In team Slack

**Hour 2-4 (Afternoon):**
- [ ] Monitor comments/replies
- [ ] Answer questions promptly
- [ ] Thank people who try it
- [ ] Note all feedback

**End of Day:**
- [ ] Compile feedback notes
- [ ] List any bugs discovered
- [ ] Count how many people played
- [ ] Celebrate shipping! 🎉

---

## Final Reminder

**You have working games. The biggest risk now is NOT SHIPPING.**

Launch → Learn → Improve → Repeat

Good luck! 🚀
