#!/usr/bin/env python3
"""
Fix duplicate error handlers in gym-dashboard.html
Consolidate to single, unified error handler
"""

import re
from pathlib import Path

def fix_error_handlers(filepath):
    """Remove duplicate error handlers and create unified one"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        filename = Path(filepath).name
        
        # Find all error handler blocks
        error_handler_patterns = [
            # Pattern 1: window.addEventListener('error', ...)
            r"<script>\s*window\.addEventListener\(['\"]error['\"][\s\S]*?e\.preventDefault\(\);\s*\}\);\s*</script>",
            # Pattern 2: window.addEventListener('unhandledrejection', ...)
            r"<script>\s*window\.addEventListener\(['\"]unhandledrejection['\"][\s\S]*?e\.preventDefault\(\);\s*\}\);\s*</script>",
        ]
        
        # Remove old handlers
        handlers_removed = 0
        for pattern in error_handler_patterns:
            matches = list(re.finditer(pattern, content, re.MULTILINE))
            if len(matches) > 1:
                # Keep only the last one (most refined), remove others
                for match in matches[:-1]:
                    content = content.replace(match.group(0), '<!-- Error handler removed (duplicate) -->')
                    handlers_removed += 1
        
        # Create unified error handler (if we removed duplicates)
        if handlers_removed > 0:
            unified_handler = '''
<!-- Unified Error Handler - Replaces duplicate handlers -->
<script>
(function() {
    'use strict';
    
    // Only register if not already registered
    if (window.__errorHandlerRegistered) {
        return;
    }
    window.__errorHandlerRegistered = true;
    
    // Unified error handler
    window.addEventListener('error', function(e) {
        const target = e.target;
        const isScript = target && target.tagName === 'SCRIPT';
        const isLink = target && target.tagName === 'LINK';
        const src = target ? (target.src || target.href || '') : '';
        const errorMsg = e.message || '';
        
        // Suppress expected/non-critical errors
        const suppressPatterns = [
            'service-worker', 'sw.js', 'favicon', 'analytics',
            'google-analytics', 'Script error', 'net::ERR_',
            'Failed to load resource', 'Extension context'
        ];
        
        const shouldSuppress = suppressPatterns.some(pattern => 
            src.includes(pattern) || errorMsg.includes(pattern)
        );
        
        if (shouldSuppress) {
            return; // Silent - don't log or show
        }
        
        // Log critical errors only
        if (isScript || (isLink && src.includes('.css'))) {
            console.error('[Error Handler] Resource failed:', src || errorMsg);
        }
        
        e.preventDefault();
    });
    
    // Unified unhandled rejection handler
    window.addEventListener('unhandledrejection', function(e) {
        const reason = e.reason ? e.reason.toString() : '';
        
        // Suppress service worker and expected errors
        const suppressPatterns = [
            'Service Worker', 'serviceWorker', 'sw.js',
            'Failed to register', 'Extension context',
            'net::ERR_', 'NetworkError'
        ];
        
        const shouldSuppress = suppressPatterns.some(pattern => 
            reason.includes(pattern)
        );
        
        if (shouldSuppress) {
            console.debug('[Error Handler] Suppressed expected error:', reason.substring(0, 100));
            e.preventDefault();
            return;
        }
        
        // Log other rejections (but don't show to user unless critical)
        console.warn('[Error Handler] Unhandled rejection:', reason.substring(0, 200));
        e.preventDefault();
    });
    
    console.log('✅ Unified error handler registered');
})();
</script>
'''
            
            # Insert before </body> or at end of <body>
            if '</body>' in content:
                content = content.replace('</body>', unified_handler + '\n</body>')
            elif '</html>' in content:
                content = content.replace('</html>', unified_handler + '\n</html>')
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed {filename}: Removed {handlers_removed} duplicate handler(s), added unified handler")
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error fixing {filepath}: {e}")
        return False

# Fix gym-dashboard.html
if Path('gym-dashboard.html').exists():
    fix_error_handlers('gym-dashboard.html')
    print("\n✅ Error handler consolidation complete!")

