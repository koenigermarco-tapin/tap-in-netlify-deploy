/**
 * TAP-IN Stripe Completion Helper
 * Add this snippet to any belt stripe page to automatically award XP when complete
 * 
 * USAGE:
 * 1. Add this script tag before closing </body>:
 *    <script src="../js/gamification.js"></script>
 *    <script src="../js/stripe-completion-helper.js"></script>
 * 
 * 2. Call when module is marked complete:
 *    markStripeComplete('white', 1); // For white belt stripe 1
 */

// Award XP when a stripe is completed
function markStripeComplete(beltColor, stripeNumber) {
    const key = `${beltColor}BeltStripe${stripeNumber}Complete`;
    const xpKey = `${key}_XP_Awarded`;
    
    // Mark as complete
    localStorage.setItem(key, 'true');
    
    // Award XP if not already awarded
    if (!localStorage.getItem(xpKey)) {
        const xpSystem = new window.TapInGamification.XPSystem();
        const achievementSystem = new window.TapInGamification.AchievementSystem();
        
        // Award stripe completion XP
        xpSystem.awardXP(
            window.TapInGamification.XP_REWARDS.completeStripe,
            `Completed ${beltColor} belt stripe ${stripeNumber}`,
            'training'
        );
        
        localStorage.setItem(xpKey, 'true');
        
        // Check for first stripe achievement
        const totalStripes = countTotalStripes();
        if (totalStripes === 1) {
            achievementSystem.unlockAchievement('first-stripe');
        }
        
        // Check if entire belt is now complete
        checkBeltCompletion(beltColor);
    }
}

// Count total stripes completed
function countTotalStripes() {
    const belts = ['white', 'blue', 'purple', 'brown', 'black'];
    let count = 0;
    
    belts.forEach(belt => {
        for (let i = 1; i <= 4; i++) {
            const key = `${belt}BeltStripe${i}Complete`;
            if (localStorage.getItem(key) === 'true') {
                count++;
            }
        }
    });
    
    return count;
}

// Check if entire belt is complete and award bonus XP
function checkBeltCompletion(beltColor) {
    const allStripesComplete = [1, 2, 3, 4].every(i => {
        return localStorage.getItem(`${beltColor}BeltStripe${i}Complete`) === 'true';
    });
    
    if (allStripesComplete) {
        const beltXpKey = `${beltColor}Belt_Complete_XP_Awarded`;
        
        if (!localStorage.getItem(beltXpKey)) {
            const xpSystem = new window.TapInGamification.XPSystem();
            const achievementSystem = new window.TapInGamification.AchievementSystem();
            
            // Award belt completion bonus
            xpSystem.awardXP(
                window.TapInGamification.XP_REWARDS.completeBelt,
                `🥋 Completed ${beltColor} belt!`,
                'training'
            );
            
            localStorage.setItem(beltXpKey, 'true');
            
            // Check for first belt achievement
            const totalBelts = countCompletedBelts();
            if (totalBelts === 1) {
                achievementSystem.unlockAchievement('first-belt-complete');
            }
            
            // Special achievement for white belt (vulnerability)
            if (beltColor === 'white') {
                achievementSystem.unlockAchievement('vulnerability-first');
            }
            
            // Check for all belts complete
            if (totalBelts === 5) {
                achievementSystem.unlockAchievement('all-belts');
            }
        }
    }
}

// Count completed belts
function countCompletedBelts() {
    const belts = ['white', 'blue', 'purple', 'brown', 'black'];
    let count = 0;
    
    belts.forEach(belt => {
        const allComplete = [1, 2, 3, 4].every(i => {
            return localStorage.getItem(`${belt}BeltStripe${i}Complete`) === 'true';
        });
        if (allComplete) count++;
    });
    
    return count;
}

// Export functions
window.tapinStripeHelper = {
    markStripeComplete,
    countTotalStripes,
    checkBeltCompletion,
    countCompletedBelts
};

// Auto-detect completion based on existing localStorage keys
// This runs on page load to catch any completions that happened before gamification was added
document.addEventListener('DOMContentLoaded', function() {
    // Check current page URL to determine which stripe this is
    const path = window.location.pathname;
    
    // Pattern: /white-belt-stripe1-gamified.html
    const match = path.match(/(white|blue|purple|brown|black)-belt-stripe(\d+)/);
    
    if (match) {
        const [_, beltColor, stripeNum] = match;
        const key = `${beltColor}BeltStripe${stripeNum}Complete`;
        
        // If this stripe is marked complete, ensure XP was awarded
        if (localStorage.getItem(key) === 'true') {
            markStripeComplete(beltColor, parseInt(stripeNum));
        }
    }
});
