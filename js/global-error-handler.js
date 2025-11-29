/**
 * TAP-IN Global Error Handler
 * Catches and logs errors across the platform
 */

const ErrorHandler = {
    /**
     * Initialize error handling
     */
    init() {
        // Catch unhandled errors
        window.addEventListener('error', (event) => {
            this.handleError({
                message: event.message,
                filename: event.filename,
                lineno: event.lineno,
                colno: event.colno,
                error: event.error
            });
        });

        // Catch unhandled promise rejections
        window.addEventListener('unhandledrejection', (event) => {
            this.handleError({
                message: event.reason?.message || String(event.reason),
                type: 'Promise Rejection',
                error: event.reason
            });
        });

        console.log('✅ Global Error Handler initialized');
    },

    /**
     * Handle error
     */
    handleError(errorInfo) {
        // Log to console
        console.error('🚨 Error caught:', errorInfo);

        // Store in localStorage for debugging
        try {
            const errors = JSON.parse(localStorage.getItem('tapin_errors') || '[]');
            errors.push({
                ...errorInfo,
                timestamp: Date.now(),
                url: window.location.href,
                userAgent: navigator.userAgent
            });
            // Keep only last 50 errors
            if (errors.length > 50) {
                errors.shift();
            }
            localStorage.setItem('tapin_errors', JSON.stringify(errors));
        } catch (e) {
            console.error('Failed to save error:', e);
        }

        // Show user-friendly message for critical errors
        if (errorInfo.message && !errorInfo.message.includes('Service Worker')) {
            // Only show for non-SW errors
            if (typeof TapInUtils !== 'undefined' && TapInUtils.showToast) {
                TapInUtils.showToast('Something went wrong. Please refresh the page.', 'error');
            }
        }
    },

    /**
     * Get error log
     */
    getErrorLog() {
        try {
            return JSON.parse(localStorage.getItem('tapin_errors') || '[]');
        } catch (e) {
            return [];
        }
    },

    /**
     * Clear error log
     */
    clearErrorLog() {
        localStorage.removeItem('tapin_errors');
    }
};

// Initialize on load
if (typeof document !== 'undefined') {
    document.addEventListener('DOMContentLoaded', () => {
        ErrorHandler.init();
    });
}

// Make available globally
window.ErrorHandler = ErrorHandler;


