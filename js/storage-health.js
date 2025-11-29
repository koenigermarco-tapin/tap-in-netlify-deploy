/**
 * TAP-IN Storage Health Monitor
 * Monitors localStorage health and provides backup/restore
 */

const StorageHealth = {
    /**
     * Check storage health
     */
    checkHealth() {
        const health = {
            available: true,
            usage: 0,
            quota: 0,
            percentage: 0,
            warnings: []
        };

        try {
            // Check if localStorage is available
            const testKey = '__tapin_storage_test__';
            localStorage.setItem(testKey, 'test');
            localStorage.removeItem(testKey);

            // Estimate usage (rough calculation)
            let totalSize = 0;
            for (let key in localStorage) {
                if (localStorage.hasOwnProperty(key)) {
                    totalSize += localStorage[key].length + key.length;
                }
            }

            // Most browsers allow ~5-10MB
            const estimatedQuota = 5 * 1024 * 1024; // 5MB
            const percentage = (totalSize / estimatedQuota) * 100;

            health.usage = totalSize;
            health.quota = estimatedQuota;
            health.percentage = Math.round(percentage);

            // Add warnings
            if (percentage > 80) {
                health.warnings.push('Storage is nearly full. Consider clearing old data.');
            }
            if (percentage > 90) {
                health.warnings.push('Storage is critically full. Backup recommended.');
            }

        } catch (e) {
            health.available = false;
            health.warnings.push('localStorage is not available or full.');
        }

        return health;
    },

    /**
     * Backup user data
     */
    backup() {
        const backup = {
            timestamp: Date.now(),
            data: {}
        };

        try {
            // Backup all TAP-IN related keys
            for (let key in localStorage) {
                if (localStorage.hasOwnProperty(key) && key.startsWith('tapin') || 
                    key.includes('Belt') || key.includes('XP') || key.includes('Streak')) {
                    backup.data[key] = localStorage.getItem(key);
                }
            }

            // Store backup in localStorage
            localStorage.setItem('tapin_backup', JSON.stringify(backup));
            return backup;
        } catch (e) {
            console.error('Backup failed:', e);
            return null;
        }
    },

    /**
     * Restore from backup
     */
    restore(backupData = null) {
        try {
            const backup = backupData || JSON.parse(localStorage.getItem('tapin_backup') || '{}');
            
            if (!backup.data) {
                console.warn('No backup data found');
                return false;
            }

            // Restore all backed up data
            for (let key in backup.data) {
                localStorage.setItem(key, backup.data[key]);
            }

            return true;
        } catch (e) {
            console.error('Restore failed:', e);
            return false;
        }
    },

    /**
     * Clear old data (keep recent)
     */
    cleanup(daysToKeep = 30) {
        const cutoffDate = Date.now() - (daysToKeep * 24 * 60 * 60 * 1000);
        let cleared = 0;

        try {
            for (let key in localStorage) {
                if (localStorage.hasOwnProperty(key)) {
                    // Check if key has timestamp
                    const value = localStorage.getItem(key);
                    try {
                        const parsed = JSON.parse(value);
                        if (parsed.timestamp && parsed.timestamp < cutoffDate) {
                            localStorage.removeItem(key);
                            cleared++;
                        }
                    } catch (e) {
                        // Not JSON, skip
                    }
                }
            }
            return cleared;
        } catch (e) {
            console.error('Cleanup failed:', e);
            return 0;
        }
    },

    /**
     * Get storage stats
     */
    getStats() {
        const stats = {
            totalKeys: 0,
            tapinKeys: 0,
            totalSize: 0,
            tapinSize: 0
        };

        try {
            for (let key in localStorage) {
                if (localStorage.hasOwnProperty(key)) {
                    const size = localStorage[key].length + key.length;
                    stats.totalKeys++;
                    stats.totalSize += size;

                    if (key.startsWith('tapin') || key.includes('Belt') || 
                        key.includes('XP') || key.includes('Streak')) {
                        stats.tapinKeys++;
                        stats.tapinSize += size;
                    }
                }
            }
        } catch (e) {
            console.error('Stats calculation failed:', e);
        }

        return stats;
    }
};

// Auto-backup on page load (once per day)
if (typeof document !== 'undefined') {
    document.addEventListener('DOMContentLoaded', () => {
        const lastBackup = localStorage.getItem('tapin_last_backup');
        const now = Date.now();
        const oneDay = 24 * 60 * 60 * 1000;

        if (!lastBackup || (now - parseInt(lastBackup)) > oneDay) {
            StorageHealth.backup();
            localStorage.setItem('tapin_last_backup', now.toString());
        }
    });
}

// Make available globally
window.StorageHealth = StorageHealth;


