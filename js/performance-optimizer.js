/**
 * Performance Optimizer
 * Batches localStorage reads and defers non-critical operations
 */

class PerformanceOptimizer {
    constructor() {
        this.cache = {};
        this.pendingWrites = [];
        this.batchTimeout = null;
    }

    // Batch localStorage reads
    batchRead(keys) {
        const results = {};
        keys.forEach(key => {
            if (this.cache[key] === undefined) {
                try {
                    this.cache[key] = localStorage.getItem(key);
                } catch (e) {
                    console.warn('localStorage read failed:', e);
                    this.cache[key] = null;
                }
            }
            results[key] = this.cache[key];
        });
        return results;
    }

    // Batch localStorage writes (debounced)
    batchWrite(key, value) {
        this.cache[key] = value;
        this.pendingWrites.push({ key, value });
        
        if (this.batchTimeout) {
            clearTimeout(this.batchTimeout);
        }
        
        this.batchTimeout = setTimeout(() => {
            this.flushWrites();
        }, 100);
    }

    flushWrites() {
        this.pendingWrites.forEach(({ key, value }) => {
            try {
                localStorage.setItem(key, value);
            } catch (e) {
                console.warn('localStorage write failed:', e);
            }
        });
        this.pendingWrites = [];
    }

    // Clear cache (for logout/refresh)
    clearCache() {
        this.cache = {};
    }
}

// Global instance
window.PerfOpt = new PerformanceOptimizer();

// Optimize gamification data loading
window.getGamificationDataOptimized = function() {
    const keys = [
        'tapinTotalXP',
        'tapinCurrentStreak',
        'tapinLongestStreak',
        'tapinLastVisit',
        'tapinCurrentBelt',
        'tapinCompletedStripes',
        'tapinCompletedLessons'
    ];
    
    const data = window.PerfOpt.batchRead(keys);
    
    return {
        totalXP: parseInt(data.tapinTotalXP || '0'),
        currentStreak: parseInt(data.tapinCurrentStreak || '0'),
        longestStreak: parseInt(data.tapinLongestStreak || '0'),
        lastVisit: data.tapinLastVisit || null,
        currentBelt: data.tapinCurrentBelt || 'white',
        completedStripes: JSON.parse(data.tapinCompletedStripes || '[]'),
        completedLessons: JSON.parse(data.tapinCompletedLessons || '[]')
    };
};

// Defer heavy operations until after page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        // Initialize after DOM is ready
        setTimeout(() => {
            if (window.XPSystem) {
                window.XPSystem.init();
            }
        }, 100);
    });
}

