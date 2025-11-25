# TAP-IN Gamification System Integration

## Overview
The GYM dashboard now features a complete gamification system that tracks user progress, awards XP, unlocks achievements, and maintains engagement streaks.

## System Architecture

### Core Components

1. **gamification.js** - Main gamification engine
   - `XPSystem` - Tracks and awards experience points
   - `AchievementSystem` - Manages badge unlocking
   - `StreakSystem` - Daily visit and streak tracking
   - `BeltProgress` - Monitors belt completion across all 5 belts

2. **gym-dashboard-init.js** - Dashboard UI integration
   - Connects gamification.js to dashboard stats
   - Updates UI in real-time when XP/achievements change
   - Shows animated notifications for level-ups and badges

## XP Rewards System

### Training Progress
- **Complete Lesson**: 25 XP
- **Complete Stripe**: 100 XP (bonus on top of lessons)
- **Complete Belt**: 500 XP (bonus on top of stripes)

### Assessments
- **Complete Assessment**: 100 XP
- **Retake Assessment**: 25 XP
- **Perfect Assessment**: 250 XP

### Engagement
- **Daily Visit**: 10 XP
- **7-Day Streak**: 100 XP
- **30-Day Streak**: 500 XP

### Achievements
- **First Look**: 50 XP (complete first assessment)
- **Honest Look**: 100 XP (score below 50 and continue)
- **Growth Mindset**: 150 XP (retake and improve)
- **Know Thyself**: 200 XP (complete all self-discovery)

## Achievement Badges

### Discovery Category
- 🏆 **First Look**: Complete your first assessment
- 🔮 **Know Thyself**: Complete all self-discovery assessments
- 🥋 **Belt Check**: Complete the Belt Check assessment

### Training Category
- ➖ **First Stripe**: Earn your first belt stripe
- 🎖️ **Belt Mastery**: Complete your first full belt
- 🏆 **Black Belt Master**: Complete all five belts (2500 XP!)

### Engagement Category
- 🔥 **Week Warrior**: Train 7 days in a row
- 💪 **Month Warrior**: Train 30 days in a row

### Character Category
- 💪 **Honest Look**: Score below 50 and continue anyway
- 📈 **Growth Mindset**: Retake and improve an assessment
- ⚪ **Vulnerability First**: Complete White Belt

## Level System

- **500 XP per level**
- Level displayed on dashboard
- Animated notification on level-up
- Level 1 starts at 0 XP
- Level 2 at 500 XP
- Level 3 at 1000 XP
- And so on...

## Streak Tracking

### How It Works
- Tracks consecutive days of visits
- Awards 10 XP for daily login
- Awards 100 XP bonus every 7 days
- Awards 500 XP bonus at 30 days
- Unlocks "Week Warrior" badge at 7 days
- Unlocks "Month Warrior" badge at 30 days

### Streak Rules
- Visits must be on consecutive days
- Missing one day breaks the streak
- Streak resets to 1 on break
- Longest streak is always tracked

## Dashboard Integration

### Stats Display
The dashboard shows 4 key metrics:

1. **🔥 Day Streak** - Current consecutive days
2. **⚡ Total XP** - All-time experience points
3. **📚 Modules** - Completed belt stripes (max 20)
4. **🏆 Badges** - Unlocked achievements

### Real-Time Updates
- Stats update automatically when:
  - User earns XP
  - Achievements are unlocked
  - Streak is updated on daily visit
  - Modules are completed

### Notifications
- **Level Up**: Center screen, 3-second display, ⚡ icon
- **Badge Unlocked**: Top-right corner, 4-second display, 🏆 icon
- Smooth animations (slide, scale, fade)

## Event System

The gamification system fires custom events that other pages can listen to:

```javascript
// XP gained event
window.addEventListener('xpGained', (e) => {
    const { amount, reason, totalXP } = e.detail;
    // Handle XP gain
});

// Achievement unlocked event
window.addEventListener('achievementUnlocked', (e) => {
    const achievement = e.detail;
    // Handle badge unlock
});

// Streak updated event
window.addEventListener('streakUpdated', (e) => {
    const streakData = e.detail;
    // Handle streak change
});
```

## For Developers: Awarding XP

### From Any Page

```javascript
// Award XP
const xpSystem = new window.TapInGamification.XPSystem();
xpSystem.awardXP(50, 'Completed stripe 1', 'training');

// Unlock achievement
const achievementSystem = new window.TapInGamification.AchievementSystem();
achievementSystem.unlockAchievement('first-stripe');

// Record visit (automatic on page load)
const streakSystem = new window.TapInGamification.StreakSystem();
streakSystem.recordVisit();
```

### Belt Stripe Completion

When a user completes a stripe module, call:

```javascript
const xpSystem = new window.TapInGamification.XPSystem();
xpSystem.awardXP(25, 'Completed lesson', 'training'); // Per lesson
xpSystem.awardXP(100, 'Completed stripe 1', 'training'); // Stripe bonus
```

### Assessment Completion

When a user completes an assessment:

```javascript
const xpSystem = new window.TapInGamification.XPSystem();
const achievementSystem = new window.TapInGamification.AchievementSystem();

xpSystem.awardXP(100, 'Completed work-life assessment', 'assessment');
achievementSystem.unlockAchievement('first-look'); // If first assessment
```

## Storage

All data is stored in `localStorage`:

- `tapinTotalXP` - Total XP earned
- `tapinXPHistory` - Last 100 XP transactions
- `tapinAchievements` - Array of unlocked achievements
- `tapinStreak` - Streak data and visit history
- `tapinFirstVisit` - Timestamp of first visit

## Next Steps

1. **Leaderboard**: Personal bests comparison (no user-to-user comparison needed)
2. **Badge Display**: Visual badge collection in sidebar
3. **Activity Feed**: Recent XP history with timestamps
4. **Progress Visualization**: XP bar showing progress to next level
5. **Integration**: Add XP awards to all stripe completion pages
6. **Integration**: Add achievement triggers to all assessment pages

## Design Guidelines

### Colors
- Primary Navy: `#1a365d`
- Purple: `#2d1b4e`
- Gold (XP/Achievements): `#f6e05e`
- Success Green: `#38a169`

### Icons
- XP/Lightning: ⚡
- Streak/Fire: 🔥
- Badges/Trophy: 🏆
- Modules/Books: 📚
- Level Up: ⚡
- Achievement Categories:
  - Discovery: 👀 🔮 🥋
  - Training: ➖ 🎖️ 🏆
  - Engagement: 🔥 💪
  - Character: 💪 📈 ⚪

### Animations
- Level up: Scale in/out from center
- Badge unlock: Slide in from right
- Duration: 3-4 seconds
- Smooth easing functions

## Testing

To test the system:

1. Open gym-dashboard.html
2. Check that stats display correctly
3. Complete a stripe module - should award XP
4. Visit daily to build streak
5. Complete assessments to unlock badges
6. Watch for level-up notifications

## Files Modified

- `gym-dashboard.html` - Added script imports
- `js/gamification.js` - Core system (existing)
- `js/gym-dashboard-init.js` - Dashboard integration (new)

---

**Status**: ✅ Core gamification system integrated into GYM dashboard
**Next**: Add XP awards to stripe completion pages and assessment pages
