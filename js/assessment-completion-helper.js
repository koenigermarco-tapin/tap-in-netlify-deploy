/**
 * TAP-IN Assessment Completion Helper
 * Add this snippet to assessment pages to automatically award XP and unlock achievements
 * 
 * USAGE:
 * 1. Add this script tag before closing </body>:
 *    <script src="js/gamification.js"></script>
 *    <script src="js/assessment-completion-helper.js"></script>
 * 
 * 2. Call when assessment is completed:
 *    recordAssessmentCompletion('work-life-balance', 72); // name and score
 */

// Award XP and check achievements when assessment is completed
function recordAssessmentCompletion(assessmentName, score) {
    const xpSystem = new window.TapInGamification.XPSystem();
    const achievementSystem = new window.TapInGamification.AchievementSystem();
    
    const completionKey = `assessment_${assessmentName}_completed`;
    const xpKey = `assessment_${assessmentName}_XP_awarded`;
    const scoreKey = `assessment_${assessmentName}_score`;
    const previousScoreKey = `assessment_${assessmentName}_previous_score`;
    
    // Store score
    const previousScore = localStorage.getItem(scoreKey);
    if (previousScore) {
        localStorage.setItem(previousScoreKey, previousScore);
    }
    localStorage.setItem(scoreKey, score.toString());
    
    // Check if this is first completion or retake
    const isFirstTime = !localStorage.getItem(completionKey);
    
    if (isFirstTime) {
        // First time completion
        localStorage.setItem(completionKey, 'true');
        
        // Award assessment XP
        xpSystem.awardXP(
            window.TapInGamification.XP_REWARDS.completeAssessment,
            `Completed ${formatAssessmentName(assessmentName)} assessment`,
            'assessment'
        );
        
        // Check for first assessment achievement
        const totalAssessments = countCompletedAssessments();
        if (totalAssessments === 1) {
            achievementSystem.unlockAchievement('first-look');
        }
        
        // Check for "Honest Look" achievement (score below 50)
        if (score < 50) {
            achievementSystem.unlockAchievement('honest-look');
        }
        
        // Check for perfect score
        if (score === 100) {
            xpSystem.awardXP(
                window.TapInGamification.XP_REWARDS.perfectAssessment,
                `Perfect score on ${formatAssessmentName(assessmentName)}!`,
                'assessment'
            );
        }
    } else {
        // Retake
        xpSystem.awardXP(
            window.TapInGamification.XP_REWARDS.retakeAssessment,
            `Retook ${formatAssessmentName(assessmentName)} assessment`,
            'assessment'
        );
        
        // Check for improvement
        if (previousScore && score > parseInt(previousScore)) {
            achievementSystem.unlockAchievement('growth-mindset');
        }
    }
}

// Format assessment name for display
function formatAssessmentName(name) {
    return name
        .split('-')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
}

// Count total completed assessments
function countCompletedAssessments() {
    const assessments = [
        'work-life-balance',
        'mental-health',
        'worker-type',
        'leadership-profile',
        'team-dynamics',
        'belt-assessment',
        'white-belt-assessment',
        'blue-belt-assessment',
        'purple-belt-assessment',
        'brown-belt-assessment',
        'black-belt-assessment'
    ];
    
    let count = 0;
    assessments.forEach(assessment => {
        const key = `assessment_${assessment}_completed`;
        if (localStorage.getItem(key) === 'true') {
            count++;
        }
    });
    
    return count;
}

// Check if all self-discovery assessments are complete
function checkSelfDiscoveryComplete() {
    const selfDiscovery = [
        'work-life-balance',
        'mental-health',
        'worker-type'
    ];
    
    const allComplete = selfDiscovery.every(assessment => {
        const key = `assessment_${assessment}_completed`;
        return localStorage.getItem(key) === 'true';
    });
    
    if (allComplete) {
        const achievementSystem = new window.TapInGamification.AchievementSystem();
        achievementSystem.unlockAchievement('know-thyself');
    }
}

// Record belt assessment completion
function recordBeltAssessment(beltColor) {
    const xpSystem = new window.TapInGamification.XPSystem();
    const achievementSystem = new window.TapInGamification.AchievementSystem();
    
    const key = `${beltColor}BeltAssessmentComplete`;
    const xpKey = `${key}_XP_awarded`;
    
    localStorage.setItem(key, 'true');
    
    if (!localStorage.getItem(xpKey)) {
        xpSystem.awardXP(
            window.TapInGamification.XP_REWARDS.completeAssessment,
            `Completed ${beltColor} belt assessment`,
            'assessment'
        );
        
        localStorage.setItem(xpKey, 'true');
        
        // Unlock belt-earned achievement on first belt assessment
        if (beltColor === 'white') {
            achievementSystem.unlockAchievement('belt-earned');
        }
    }
}

// Export functions
window.tapinAssessmentHelper = {
    recordAssessmentCompletion,
    recordBeltAssessment,
    countCompletedAssessments,
    checkSelfDiscoveryComplete
};

// Auto-detect assessment completion on page load
document.addEventListener('DOMContentLoaded', function() {
    // Check if we're on a results/completion page
    // Most assessments store their completion in localStorage
    // This helper will pick it up automatically
    
    // Check for self-discovery completion
    checkSelfDiscoveryComplete();
});
