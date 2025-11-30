#!/usr/bin/env python3
"""
Add error handling wrapper for localStorage operations
Creates a utility to wrap localStorage calls safely
"""

utility_code = '''/**
 * Safe localStorage wrapper with error handling
 * Prevents quota exceeded and other storage errors from breaking the app
 */
(function() {
    'use strict';
    
    if (window.SafeStorage) {
        return; // Already loaded
    }
    
    const SafeStorage = {
        getItem: function(key) {
            try {
                return localStorage.getItem(key);
            } catch (e) {
                console.debug('[Storage] getItem failed:', e.message || e);
                return null;
            }
        },
        
        setItem: function(key, value) {
            try {
                localStorage.setItem(key, value);
                return true;
            } catch (e) {
                // Handle quota exceeded
                if (e.name === 'QuotaExceededError' || e.name === 'NS_ERROR_DOM_QUOTA_REACHED') {
                    console.warn('[Storage] Quota exceeded, attempting cleanup...');
                    this.cleanup();
                    
                    // Try once more after cleanup
                    try {
                        localStorage.setItem(key, value);
                        return true;
                    } catch (e2) {
                        console.error('[Storage] Still failed after cleanup:', e2.message || e2);
                        return false;
                    }
                }
                
                console.debug('[Storage] setItem failed:', e.message || e);
                return false;
            }
        },
        
        removeItem: function(key) {
            try {
                localStorage.removeItem(key);
                return true;
            } catch (e) {
                console.debug('[Storage] removeItem failed:', e.message || e);
                return false;
            }
        },
        
        cleanup: function() {
            // Remove old error logs
            try {
                const errors = JSON.parse(localStorage.getItem('tapin_errors') || '[]');
                if (errors.length > 10) {
                    localStorage.setItem('tapin_errors', JSON.stringify(errors.slice(-10)));
                }
            } catch (e) {
                // Ignore cleanup errors
            }
        }
    };
    
    window.SafeStorage = SafeStorage;
    console.log('✅ SafeStorage utility loaded');
})();
'''

# Write the utility
with open('js/safe-storage.js', 'w', encoding='utf-8') as f:
    f.write(utility_code)

print("✅ Created js/safe-storage.js utility")
print("   Use SafeStorage.getItem/setItem instead of localStorage directly")

