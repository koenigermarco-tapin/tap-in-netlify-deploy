/**
 * TAP-IN Global Gamification System
 * Tracks XP, achievements, streaks, and progress across all modules
 * Version: 1.0.0
 */

// ============================================================================
// XP SYSTEM
// ============================================================================

const XP_REWARDS = {
    // Assessments
    completeAssessment: 100,
    retakeAssessment: 25,
    perfectAssessment: 250,
    
    // Training
    completeLesson: 25,
    completeStripe: 100,     // Bonus on top of lessons
    completeBelt: 500,       // Bonus on top of stripes
    
    // Engagement
    shareResults: 50,
    dailyVisit: 10,
    weekStreak: 100,
    monthStreak: 500,
    
    // Achievements
    firstLook: 50,
    knowThyself: 200,
    honestLook: 100,
    growthMindset: 150
};

class XPSystem {
    constructor() {
        this.storageKey = 'tapinTotalXP';
        this.historyKey = 'tapinXPHistory';
    }

    // Get current total XP
    getTotalXP() {
        return parseInt(localStorage.getItem(this.storageKey) || '0');
    }

    // Award XP and record it
    awardXP(amount, reason, source = 'general') {
        const currentXP = this.getTotalXP();
        const newXP = currentXP + amount;
        
        localStorage.setItem(this.storageKey, newXP.toString());
        
        // Record in history
        this.recordXPHistory(amount, reason, source);
        
        // Trigger XP gain event
        this.triggerXPEvent(amount, reason, newXP);
        
        return newXP;
    }

    // Record XP transaction in history
    recordXPHistory(amount, reason, source) {
        const history = this.getXPHistory();
        const entry = {
            amount,
            reason,
            source,
            timestamp: Date.now(),
            date: new Date().toISOString()
        };
        
        history.push(entry);
        
        // Keep last 100 entries
        if (history.length > 100) {
            history.shift();
        }
        
        localStorage.setItem(this.historyKey, JSON.stringify(history));
    }

    // Get XP history
    getXPHistory() {
        return JSON.parse(localStorage.getItem(this.historyKey) || '[]');
    }

    // Get XP by source
    getXPBySource(source) {
        const history = this.getXPHistory();
        return history
            .filter(entry => entry.source === source)
            .reduce((sum, entry) => sum + entry.amount, 0);
    }

    // Get XP earned today
    getXPToday() {
        const history = this.getXPHistory();
        const today = new Date().toDateString();
        
        return history
            .filter(entry => new Date(entry.timestamp).toDateString() === today)
            .reduce((sum, entry) => sum + entry.amount, 0);
    }

    // Trigger custom event for XP gain (for UI updates)
    triggerXPEvent(amount, reason, totalXP) {
        const event = new CustomEvent('xpGained', {
            detail: { amount, reason, totalXP }
        });
        window.dispatchEvent(event);
    }
}

// ============================================================================
// ACHIEVEMENT SYSTEM
// ============================================================================

const ACHIEVEMENTS = {
    // Discovery
    'first-look': {
        id: 'first-look',
        name: 'First Look',
        description: 'Complete your first assessment',
        icon: '👀',
        xp: 50,
        category: 'discovery'
    },
    'know-thyself': {
        id: 'know-thyself',
        name: 'Know Thyself',
        description: 'Complete all self-discovery assessments',
        icon: '🔮',
        xp: 200,
        category: 'discovery'
    },
    'belt-earned': {
        id: 'belt-earned',
        name: 'Belt Check',
        description: 'Complete the Belt Check assessment',
        icon: '🥋',
        xp: 100,
        category: 'discovery'
    },
    
    // Training
    'first-stripe': {
        id: 'first-stripe',
        name: 'First Stripe',
        description: 'Earn your first belt stripe',
        icon: '➖',
        xp: 100,
        category: 'training'
    },
    'first-belt-complete': {
        id: 'first-belt-complete',
        name: 'Belt Mastery',
        description: 'Complete your first full belt',
        icon: '🎖️',
        xp: 500,
        category: 'training'
    },
    'all-belts': {
        id: 'all-belts',
        name: 'Black Belt Master',
        description: 'Complete all five belts',
        icon: '🏆',
        xp: 2500,
        category: 'training'
    },
    
    // Engagement
    'week-warrior': {
        id: 'week-warrior',
        name: 'Week Warrior',
        description: 'Train 7 days in a row',
        icon: '🔥',
        xp: 100,
        category: 'engagement'
    },
    'month-warrior': {
        id: 'month-warrior',
        name: 'Month Warrior',
        description: 'Train 30 days in a row',
        icon: '💪',
        xp: 500,
        category: 'engagement'
    },
    
    // Character
    'honest-look': {
        id: 'honest-look',
        name: 'Honest Look',
        description: 'Score below 50 and continue anyway',
        icon: '💪',
        xp: 100,
        category: 'character'
    },
    'growth-mindset': {
        id: 'growth-mindset',
        name: 'Growth Mindset',
        description: 'Retake and improve an assessment score',
        icon: '📈',
        xp: 150,
        category: 'character'
    },
    'vulnerability-first': {
        id: 'vulnerability-first',
        name: 'Vulnerability First',
        description: 'Complete White Belt',
        icon: '⚪',
        xp: 300,
        category: 'character'
    }
};

class AchievementSystem {
    constructor() {
        this.storageKey = 'tapinAchievements';
        this.xpSystem = new XPSystem();
    }

    // Get all earned achievements
    getEarnedAchievements() {
        return JSON.parse(localStorage.getItem(this.storageKey) || '[]');
    }

    // Check if achievement is earned
    hasAchievement(achievementId) {
        const earned = this.getEarnedAchievements();
        return earned.some(a => a.id === achievementId);
    }

    // Unlock achievement
    unlockAchievement(achievementId) {
        if (this.hasAchievement(achievementId)) {
            return false; // Already unlocked
        }

        const achievement = ACHIEVEMENTS[achievementId];
        if (!achievement) {
            console.error(`Achievement ${achievementId} not found`);
            return false;
        }

        // Record achievement
        const earned = this.getEarnedAchievements();
        earned.push({
            ...achievement,
            unlockedAt: Date.now(),
            unlockedDate: new Date().toISOString()
        });
        localStorage.setItem(this.storageKey, JSON.stringify(earned));

        // Award XP
        this.xpSystem.awardXP(achievement.xp, `Achievement: ${achievement.name}`, 'achievement');

        // Trigger achievement event
        this.triggerAchievementEvent(achievement);

        return true;
    }

    // Get achievements by category
    getAchievementsByCategory(category) {
        return Object.values(ACHIEVEMENTS).filter(a => a.category === category);
    }

    // Get achievement progress stats
    getStats() {
        const earned = this.getEarnedAchievements();
        const total = Object.keys(ACHIEVEMENTS).length;
        
        return {
            earned: earned.length,
            total: total,
            percentage: Math.round((earned.length / total) * 100),
            recentUnlocks: earned.slice(-5).reverse()
        };
    }

    // Trigger custom event for achievement unlock
    triggerAchievementEvent(achievement) {
        const event = new CustomEvent('achievementUnlocked', {
            detail: achievement
        });
        window.dispatchEvent(event);
    }
}

// ============================================================================
// STREAK SYSTEM
// ============================================================================

class StreakSystem {
    constructor() {
        this.storageKey = 'tapinStreak';
        this.xpSystem = new XPSystem();
    }

    // Get current streak data
    getStreakData() {
        const defaultData = {
            current: 0,
            longest: 0,
            lastVisit: null,
            visitDates: []
        };
        
        const data = localStorage.getItem(this.storageKey);
        return data ? JSON.parse(data) : defaultData;
    }

    // Record today's visit
    recordVisit() {
        const data = this.getStreakData();
        const today = new Date().toDateString();
        
        // Already recorded today
        if (data.lastVisit === today) {
            return data;
        }

        const yesterday = new Date();
        yesterday.setDate(yesterday.getDate() - 1);
        const yesterdayStr = yesterday.toDateString();

        // Check if streak continues
        if (data.lastVisit === yesterdayStr) {
            // Streak continues
            data.current += 1;
        } else if (data.lastVisit === null || data.lastVisit === today) {
            // First visit or same day
            data.current = 1;
        } else {
            // Streak broken
            data.current = 1;
        }

        // Update longest streak
        if (data.current > data.longest) {
            data.longest = data.current;
        }

        // Record visit date
        data.visitDates.push(today);
        if (data.visitDates.length > 90) {
            data.visitDates.shift();
        }

        data.lastVisit = today;
        localStorage.setItem(this.storageKey, JSON.stringify(data));

        // Award XP for daily visit
        this.xpSystem.awardXP(XP_REWARDS.dailyVisit, 'Daily visit', 'streak');

        // Check for streak achievements
        this.checkStreakAchievements(data.current);

        // Trigger streak event
        this.triggerStreakEvent(data);

        return data;
    }

    // Check and unlock streak achievements
    checkStreakAchievements(current) {
        const achievementSystem = new AchievementSystem();
        
        if (current === 7) {
            achievementSystem.unlockAchievement('week-warrior');
            this.xpSystem.awardXP(XP_REWARDS.weekStreak, '7-day streak bonus', 'streak');
        }
        
        if (current === 30) {
            achievementSystem.unlockAchievement('month-warrior');
            this.xpSystem.awardXP(XP_REWARDS.monthStreak, '30-day streak bonus', 'streak');
        }
    }

    // Trigger custom event for streak update
    triggerStreakEvent(data) {
        const event = new CustomEvent('streakUpdated', {
            detail: data
        });
        window.dispatchEvent(event);
    }
}

// ============================================================================
// BELT PROGRESS TRACKING
// ============================================================================

class BeltProgress {
    constructor() {
        this.belts = ['white', 'blue', 'purple', 'brown', 'black'];
    }

    // Get overall belt progress
    getOverallProgress() {
        const progress = this.belts.map(belt => ({
            belt,
            stripes: this.getStripesEarned(belt),
            totalStripes: 4,
            assessmentComplete: this.isAssessmentComplete(belt),
            xp: this.getBeltXP(belt)
        }));

        return progress;
    }

    // Get stripes earned for a belt
    getStripesEarned(belt) {
        const stripesKey = `${belt}StripesEarned`;
        const stripes = JSON.parse(localStorage.getItem(stripesKey) || '[]');
        return stripes.length;
    }

    // Check if belt assessment is complete
    isAssessmentComplete(belt) {
        const assessmentKey = `${belt}BeltAssessmentComplete`;
        return localStorage.getItem(assessmentKey) === 'true';
    }

    // Get total XP earned in a belt
    getBeltXP(belt) {
        let totalXP = 0;
        
        // Add stripe XP
        for (let i = 1; i <= 4; i++) {
            const stripeKey = `${belt}beltStripe${i}ModuleXP`;
            totalXP += parseInt(localStorage.getItem(stripeKey) || '0');
        }
        
        // Add assessment XP
        const assessmentKey = `${belt}BeltAssessmentXP`;
        totalXP += parseInt(localStorage.getItem(assessmentKey) || '0');
        
        return totalXP;
    }

    // Get current belt (highest unlocked)
    getCurrentBelt() {
        const beltsEarned = JSON.parse(localStorage.getItem('beltsEarned') || '[]');
        
        if (beltsEarned.includes('black')) return 'black';
        if (beltsEarned.includes('brown')) return 'brown';
        if (beltsEarned.includes('purple')) return 'purple';
        if (beltsEarned.includes('blue')) return 'blue';
        return 'white';
    }

    // Get next belt to work on
    getNextBelt() {
        const current = this.getCurrentBelt();
        const currentIndex = this.belts.indexOf(current);
        
        if (currentIndex === this.belts.length - 1) {
            return null; // Already at black belt
        }
        
        return this.belts[currentIndex + 1];
    }

    // Get completion percentage across all belts
    getTotalCompletion() {
        const progress = this.getOverallProgress();
        const totalPossible = this.belts.length * 5; // 4 stripes + 1 assessment per belt
        const completed = progress.reduce((sum, belt) => {
            return sum + belt.stripes + (belt.assessmentComplete ? 1 : 0);
        }, 0);
        
        return Math.round((completed / totalPossible) * 100);
    }
}

// ============================================================================
// GLOBAL INITIALIZATION
// ============================================================================

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    // Record daily visit and update streak
    const streakSystem = new StreakSystem();
    streakSystem.recordVisit();
    
    // Check for first-time user
    const isFirstVisit = !localStorage.getItem('tapinFirstVisit');
    if (isFirstVisit) {
        localStorage.setItem('tapinFirstVisit', Date.now());
    }
});

// Export for use in other scripts
window.TapInGamification = {
    XPSystem,
    AchievementSystem,
    StreakSystem,
    BeltProgress,
    XP_REWARDS,
    ACHIEVEMENTS
};
