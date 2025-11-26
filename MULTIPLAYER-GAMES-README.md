# 🎮 TAP-IN MULTIPLAYER GAMES SUITE

## Complete Collection of 4 Trust-Building Games

All games support **both Pass & Play (single device) and Multi-Device (room codes)** modes.

---

## 🃏 GAME 1: CONFESSION POKER
**File:** `confession-poker-v2.html`

### Overview
Players rate their honesty about workplace confessions, then others guess their rating. Build trust through vulnerability and empathy.

### Features
✅ 52 confession cards across 5 belt categories (White, Blue, Purple, Brown, Black)
✅ 1-5 rating system for honesty
✅ Guess other players' ratings to score points
✅ Challenge system (vote to challenge suspicious ratings)
✅ Trust points tracking
✅ 5 rounds per game

### Scoring
- **Exact guess:** +3 points
- **Off by 1:** +2 points
- **Off by 2:** +1 point
- **Off by 3+:** 0 points
- **Challenge succeeds:** Active player -5 points
- **Challenge fails:** Challengers -2 points each

### Players: 3-8
### Duration: 20-30 minutes
### Best For: Building vulnerability-based trust, White Belt workshops

---

## 💼 GAME 2: CONFLICT CARDS AGAINST HUMANITY
**File:** `conflict-cards.html`

### Overview
Cards Against Humanity format for workplace conflicts. Judge picks the best (or funniest) response to difficult scenarios.

### Features
✅ 50+ black cards (conflict scenarios)
✅ 100+ white cards (responses in 4 categories: Professional, Passive-Aggressive, Avoidant, Aggressive/Toxic, Humorous)
✅ Judge rotation system
✅ SBIR bonus checkbox (award 2 points instead of 1 for excellent responses)
✅ 10-card hand management
✅ Auto-refill hands after each round

### Scoring
- **Standard winner:** +1 point
- **SBIR Bonus winner:** +2 points
- **First to 7 points OR 15 rounds wins**

### Players: 4-10
### Duration: 30-45 minutes
### Best For: Blue Belt (conflict), humor + learning, team building

---

## 🔥 GAME 3: TAKE THE BACK
**File:** `take-the-back.html`

### Overview
Fast-paced ownership game. First person to claim a "broken thing" must explain their ownership. Group votes if convincing.

### Features
✅ 60 "broken things" cards across 4 categories (Culture, Communication, Performance, Customer)
✅ 30-second claim timer (tap "I'VE GOT THE BACK!" button fast)
✅ 15-second explanation timer
✅ Thumbs up/down voting system
✅ DELIVERED/ABANDONED score tracking
✅ First-press detection (fair across devices)

### Scoring
- **Delivered (convincing):** +1 point
- **Abandoned (not convincing):** -1 point
- **Final score:** DELIVERED - ABANDONED
- **Win condition:** First to +10 OR highest score after 20 rounds

### Players: 4-8
### Duration: 15-25 minutes
### Best For: Brown Belt (accountability), practicing ownership

---

## 🎯 GAME 4: DISAGREE & COMMIT ROULETTE
**File:** `disagree-commit-roulette.html`

### Overview
Debate controversial business decisions under time pressure. Must reach consensus or burn Block tokens.

### Features
✅ 20 detailed decision scenarios with context and arguments
✅ Spinning wheel animation for scenario selection
✅ 30-second thinking phase (silent)
✅ 60-second debate phase (verbal discussion)
✅ Simultaneous voting (Agree/Disagree)
✅ Block token mechanic (3 per player, costs -1 point to use)
✅ Commitment logging (actions logged for end-game review)
✅ Two debate rounds if first vote is split

### Scoring
- **Unanimous vote (first round):** +2 points each
- **Consensus after debate 2:** +1 point each
- **Using Block token:** -1 point (skips decision)
- **Win condition:** Highest score after 10 decisions

### Players: 3-6
### Duration: 40-60 minutes
### Best For: Purple Belt (commitment), executive teams, strategic decisions

---

## 🛠 TECHNICAL DETAILS

### Tech Stack
- **Frontend:** React 18 (via CDN)
- **Styling:** Tailwind CSS (via CDN)
- **Multiplayer:** Firebase Realtime Database (optional - falls back to LocalStorage)
- **Deployment:** Single HTML file per game (no build process needed)

### Mode Support

**Pass & Play Mode:**
- Uses browser LocalStorage
- Players share one device and take turns
- Perfect for in-person workshops
- No internet required (after page loads)

**Multi-Device Mode:**
- Uses Firebase Realtime Database
- Each player joins on their own phone/computer
- Real-time state synchronization
- Requires internet connection
- Note: Firebase config uses demo credentials - replace with your own for production

### Firebase Setup (Optional - for Multi-Device Mode)

1. Create a Firebase project at https://console.firebase.google.com
2. Enable Realtime Database
3. Set database rules to:
```json
{
  "rules": {
    "rooms": {
      "$roomId": {
        ".read": true,
        ".write": true
      }
    }
  }
}
```
4. Replace the `firebaseConfig` in each HTML file with your credentials:
```javascript
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT.firebaseapp.com",
    databaseURL: "https://YOUR_PROJECT-default-rtdb.firebaseio.com",
    projectId: "YOUR_PROJECT"
};
```

### Deployment Options

**Option 1: Netlify Drop**
1. Drag and drop any HTML file into Netlify
2. Share the URL with players
3. Done!

**Option 2: Vercel**
```bash
vercel --prod confession-poker-v2.html
```

**Option 3: GitHub Pages**
1. Push files to GitHub repo
2. Enable GitHub Pages in Settings
3. Access via `username.github.io/repo-name/confession-poker-v2.html`

**Option 4: Your Own Hosting**
- Upload HTML files to any web server
- No special configuration needed
- Works with any static file host

---

## 📱 USAGE INSTRUCTIONS

### For Facilitators

**Pass & Play Mode:**
1. Open the game HTML file on one device (laptop/tablet works best)
2. Select "Pass & Play" mode
3. Share the room code (display on screen if workshop)
4. Each player enters their name on the shared device
5. Host starts the game
6. Pass device around for each player's turn

**Multi-Device Mode:**
1. Host opens game and selects "Multi-Device"
2. Room code appears (e.g., "ABC123")
3. Share room code with all players
4. Each player:
   - Opens same HTML file on their phone
   - Enters room code
   - Enters their name
5. Host starts game when everyone is ready
6. Everyone plays simultaneously on their own device

### For Players

**Joining a Game:**
1. Open the game HTML file (get link from facilitator)
2. If multi-device: Enter room code when prompted
3. Enter your name
4. Wait for host to start

**During Game:**
- Follow on-screen instructions
- Watch for timer countdowns
- Submit votes/guesses/cards when prompted
- Read scoring updates

---

## 🎨 CUSTOMIZATION

### Adding More Cards

**Confession Poker:**
Edit `CONFESSION_CARDS` array around line 70. Format:
```javascript
{ id: 53, text: "Your confession text", category: "white", intensity: 3 }
```

**Conflict Cards:**
Edit `BLACK_CARDS` (line 65) and `WHITE_CARDS` (line 95) arrays:
```javascript
// Black card
"New conflict scenario with _____ blank."

// White card
"response that fills the blank"
```

**Take the Back:**
Edit `BROKEN_THINGS` array around line 60:
```javascript
{ id: 61, text: "Something broken", category: "culture", intensity: 4 }
```

**Disagree & Commit:**
Edit `SCENARIOS` array around line 60. Format:
```javascript
{
    id: 21,
    title: "Decision Title?",
    context: "Background context...",
    decision: "The choice to make?",
    proOption1: ["Reason 1", "Reason 2", ...],
    proOption2: ["Reason 1", "Reason 2", ...]
}
```

### Styling Changes
Each game uses Tailwind CSS classes. Modify colors by changing gradient classes:
- `from-purple-500` → `from-blue-500`
- `to-pink-500` → `to-green-500`
- etc.

### Game Rules
Adjust scoring, timers, and win conditions by editing the game logic variables:
- Round limits: Search for conditions like `round >= 20`
- Win conditions: Search for `>= 7` or `>= 10`
- Timers: Modify `timeLeft` values (in seconds)
- Point values: Change scoring in relevant functions

---

## 🐛 TROUBLESHOOTING

**Multi-Device mode not syncing:**
- Check internet connection
- Verify Firebase credentials are correct
- Check browser console for errors
- Fall back to Pass & Play mode if needed

**Room code not working:**
- Ensure all players are using the exact same game file
- Check that room code is entered correctly (case-sensitive)
- Try creating a new room

**Timer issues:**
- Refresh the page if timer freezes
- Check that JavaScript is enabled
- Some browsers throttle background tabs - keep game tab active

**Players can't join:**
- Check player limit for the game
- Verify they're entering the correct room code
- Try having them refresh and rejoin

**LocalStorage data persists:**
- Clear browser data to reset
- Or use a new incognito/private window

---

## 📊 GAME COMPARISON MATRIX

| Game | Players | Duration | Complexity | Belt Level | Key Skill |
|------|---------|----------|------------|------------|-----------|
| Confession Poker | 3-8 | 20-30min | Low | White | Vulnerability |
| Conflict Cards | 4-10 | 30-45min | Low | Blue | Productive Conflict |
| Take the Back | 4-8 | 15-25min | Medium | Brown | Accountability |
| Disagree & Commit | 3-6 | 40-60min | High | Purple | Commitment |

---

## 🚀 DEPLOYMENT CHECKLIST

- [ ] Replace Firebase config with your own (for production)
- [ ] Test both Pass & Play and Multi-Device modes
- [ ] Verify all timers work correctly
- [ ] Test with minimum and maximum player counts
- [ ] Check mobile responsiveness
- [ ] Test disconnection/reconnection handling
- [ ] Verify scoring calculations
- [ ] Test win conditions
- [ ] Check all card databases load correctly
- [ ] Review content for appropriateness

---

## 📝 LICENSE & USAGE

These games are built for **Tap-In** workshops and training programs.

**Permitted Use:**
✅ Internal team workshops
✅ Client training sessions
✅ Leadership retreats
✅ Educational purposes

**Customization:**
✅ Modify cards for your industry
✅ Adjust rules and scoring
✅ Rebrand for your organization
✅ Translate to other languages

**Distribution:**
⚠️ Please attribute Tap-In when sharing
⚠️ Don't resell as standalone product
⚠️ Don't remove Tap-In branding without permission

---

## 🎯 WORKSHOP INTEGRATION

### White Belt (Vulnerability-Based Trust)
**Primary Game:** Confession Poker
**Duration:** 30 minutes
**Objective:** Practice vulnerability in low-stakes environment

### Blue Belt (Productive Conflict)
**Primary Game:** Conflict Cards Against Humanity
**Duration:** 45 minutes
**Objective:** Normalize difficult conversations with humor

### Purple Belt (Commitment)
**Primary Game:** Disagree & Commit Roulette
**Duration:** 60 minutes
**Objective:** Practice debating then committing to decisions

### Brown Belt (Accountability)
**Primary Game:** Take the Back
**Duration:** 25 minutes
**Objective:** Practice owning failures immediately

### Black Belt (Results Focus)
**Combination:** All games as mastery assessment
**Duration:** 2-3 hours
**Objective:** Demonstrate mastery across all dysfunctions

---

## 🔄 VERSION HISTORY

**v2.0** (Current)
- ✅ All 4 games complete
- ✅ Multi-device support via Firebase
- ✅ Pass & Play mode
- ✅ 52 Confession cards (expanded from 30)
- ✅ Enhanced scoring displays
- ✅ Mobile-responsive design
- ✅ Timer systems for all games
- ✅ Commitment logging in Disagree & Commit
- ✅ SBIR bonus detection in Conflict Cards

**v1.0**
- Initial Confession Poker release
- LocalStorage only (single-device)

---

## 📧 SUPPORT

**For Technical Issues:**
- Check the Troubleshooting section above
- Review browser console for errors
- Test in incognito mode to rule out cache issues

**For Content Questions:**
- Review the card databases in each file
- Check the customization section for adding content

**For Workshop Integration:**
- See Workshop Integration section
- Reference Belt-level recommendations

---

## 🎉 QUICK START

**Fastest way to test:**
1. Open `confession-poker-v2.html` in your browser
2. Click "Pass & Play"
3. Add 3 test players (Alice, Bob, Charlie)
4. Start game and play through one round
5. See how it works!

**Fastest multiplayer test:**
1. Open `confession-poker-v2.html` in two browser windows
2. First window: "Multi-Device" → Get room code
3. Second window: Enter room code, different name
4. Start game from first window
5. Watch real-time sync!

---

**Built with ❤️ for Tap-In Leadership Development**

*Helping teams build trust, navigate conflict, commit fully, hold accountability, and focus on results.*
