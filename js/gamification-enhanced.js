/**
 * TAP-IN Enhanced Gamification Wrapper
 * Provides simple API for Open Mat tools while leveraging full enhanced system
 * Version: 1.0.0
 * 
 * This file wraps js/tap-in-xp-enhanced.js to provide:
 * - TapInGamification.awardXP(amount, reason) - Simple API for tools
 * - Automatic streaks, combos, achievements, milestones
 * - Enhanced notifications and celebrations
 */

// Ensure the enhanced XP system is loaded first
(function() {
    'use strict';

    // Check if TapInXP (from tap-in-xp-enhanced.js) is available
    // If not, create a simple fallback that will be replaced when tap-in-xp-enhanced.js loads
    window.TapInGamification = window.TapInGamification || {};

    // Create awardXP function that uses the enhanced system
    window.TapInGamification.awardXP = function(amount, reason) {
        // Try to use enhanced system first (tap-in-xp-enhanced.js)
        if (typeof TapInXP !== 'undefined' && TapInXP.awardXP) {
            return TapInXP.awardXP(amount, reason || 'Completed task');
        }
        
        // Fallback to basic gamification.js system
        if (typeof window.TapInGamification !== 'undefined' && 
            window.TapInGamification.XPSystem) {
            try {
                const xpSystem = new window.TapInGamification.XPSystem();
                return xpSystem.awardXP(amount, reason || 'Completed task', 'open-mat-tools');
            } catch (e) {
                console.warn('Gamification system error:', e);
            }
        }
        
        // Last resort: simple localStorage fallback
        const currentXP = parseInt(localStorage.getItem('totalXP') || '0');
        const newXP = currentXP + amount;
        localStorage.setItem('totalXP', newXP.toString());
        
        // Simple notification if enhanced system isn't available
        console.log(`+${amount} XP: ${reason || 'Completed task'}`);
        
        return newXP;
    };

    // Wait for DOM and enhanced system to load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initEnhancedSystem);
    } else {
        initEnhancedSystem();
    }

    function initEnhancedSystem() {
        // Wait a moment for other scripts to load (like tap-in-xp-enhanced.js)
        setTimeout(function() {
            // Check if enhanced system loaded after delay
            if (typeof TapInXP !== 'undefined' && TapInXP.awardXP) {
                // Re-bind awardXP to use enhanced system
                const originalAwardXP = window.TapInGamification.awardXP;
                window.TapInGamification.awardXP = function(amount, reason) {
                    return TapInXP.awardXP(amount, reason || 'Completed task');
                };
            }
        }, 100);
    }

    // Provide additional helper methods
    window.TapInGamification.getTotalXP = function() {
        if (typeof TapInXP !== 'undefined' && TapInXP.getTotalXP) {
            return TapInXP.getTotalXP();
        }
        return parseInt(localStorage.getItem('totalXP') || '0');
    };

    window.TapInGamification.getLevel = function() {
        if (typeof TapInXP !== 'undefined' && TapInXP.calculateLevel) {
            const xp = window.TapInGamification.getTotalXP();
            return TapInXP.calculateLevel(xp);
        }
        const xp = parseInt(localStorage.getItem('totalXP') || '0');
        return Math.floor(xp / 500) + 1;
    };

})();

