#!/usr/bin/env python3
"""
Script to add TAP OUT functionality to all stripe files.
This script adds the TAP OUT button, CSS, and JavaScript to each stripe file.
"""

import os
import re
from pathlib import Path

# Configuration for each stripe
STRIPE_CONFIG = {
    'white-belt-stripe1-gamified.html': {'stripe': 'whiteBeltStripe1', 'questions': 18, 'type': 'carousel'},
    'white-belt-stripe2-gamified.html': {'stripe': 'whiteBeltStripe2', 'questions': 4, 'type': 'lessons'},
    'white-belt-stripe3-gamified.html': {'stripe': 'whiteBeltStripe3', 'questions': 4, 'type': 'lessons'},
    'white-belt-stripe4-gamified.html': {'stripe': 'whiteBeltStripe4', 'questions': 4, 'type': 'lessons'},
    'blue-belt-stripe1-gamified.html': {'stripe': 'blueBeltStripe1', 'questions': 4, 'type': 'lessons'},
    'blue-belt-stripe2-gamified.html': {'stripe': 'blueBeltStripe2', 'questions': 4, 'type': 'lessons'},
    'blue-belt-stripe3-gamified.html': {'stripe': 'blueBeltStripe3', 'questions': 4, 'type': 'lessons'},
    'blue-belt-stripe4-gamified.html': {'stripe': 'blueBeltStripe4', 'questions': 4, 'type': 'lessons'},
    'purple-belt-stripe1-gamified.html': {'stripe': 'purpleBeltStripe1', 'questions': 4, 'type': 'lessons'},
    'purple-belt-stripe2-gamified.html': {'stripe': 'purpleBeltStripe2', 'questions': 4, 'type': 'lessons'},
    'purple-belt-stripe3-gamified.html': {'stripe': 'purpleBeltStripe3', 'questions': 4, 'type': 'lessons'},
    'purple-belt-stripe4-gamified.html': {'stripe': 'purpleBeltStripe4', 'questions': 4, 'type': 'lessons'},
    'brown-belt-stripe1-gamified.html': {'stripe': 'brownBeltStripe1', 'questions': 4, 'type': 'lessons'},
    'brown-belt-stripe2-gamified.html': {'stripe': 'brownBeltStripe2', 'questions': 4, 'type': 'lessons'},
    'brown-belt-stripe3-gamified.html': {'stripe': 'brownBeltStripe3', 'questions': 4, 'type': 'lessons'},
    'brown-belt-stripe4-gamified.html': {'stripe': 'brownBeltStripe4', 'questions': 4, 'type': 'lessons'},
    'black-belt-stripe1-gamified.html': {'stripe': 'blackBeltStripe1', 'questions': 4, 'type': 'lessons'},
    'black-belt-stripe2-gamified.html': {'stripe': 'blackBeltStripe2', 'questions': 4, 'type': 'lessons'},
    'black-belt-stripe3-gamified.html': {'stripe': 'blackBeltStripe3', 'questions': 4, 'type': 'lessons'},
    'black-belt-stripe4-gamified.html': {'stripe': 'blackBeltStripe4', 'questions': 4, 'type': 'lessons'},
}

TAP_OUT_CSS = """
        .tap-out-button {
            position: fixed;
            top: 20px;
            right: 20px;
            background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%);
            color: white;
            padding: 12px 20px;
            border-radius: 30px;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(220, 38, 38, 0.4);
            z-index: 9999;
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 700;
            transition: all 0.3s;
            border: none;
        }
        .tap-out-button:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 20px rgba(220, 38, 38, 0.6);
        }
        @media (max-width: 768px) {
            .tap-out-button {
                top: 10px;
                right: 10px;
                padding: 10px 16px;
                font-size: 0.9em;
            }
        }
"""

TAP_OUT_HTML = """    <!-- TAP OUT Button -->
    <button class="tap-out-button" onclick="tapOut()" id="tapOutBtn" style="display: none;">
        <div class="tap-icon">🥋</div>
        <div class="tap-text">TAP</div>
    </button>
"""

TAP_OUT_JS = """
        // TAP OUT Configuration
        const currentStripeName = '{STRIPE_NAME}';
        const totalQuestions = {TOTAL_QUESTIONS};
        
        // TAP OUT function
        function tapOut() {
            const currentProgress = getCurrentProgress();
            const confirmed = confirm(
                "🥋 TAP OUT\\n\\n" +
                "Your progress will be saved.\\n" +
                "You can continue from where you left off anytime.\\n\\n" +
                "Return to Gym Dashboard?"
            );
            
            if (!confirmed) return;
            
            // Save progress
            const progressData = {
                stripe: currentStripeName,
                currentQuestion: currentProgress.currentQuestion || 1,
                questionIndex: currentProgress.questionIndex || 0,
                answers: currentProgress.answers || {},
                completedLessons: currentProgress.completedLessons || [],
                timestamp: Date.now(),
                partialComplete: true,
                totalQuestions: totalQuestions
            };
            
            localStorage.setItem('currentProgress', JSON.stringify(progressData));
            
            // Show toast
            showToast("✅ Progress saved! See you soon.");
            
            // Redirect to gym
            setTimeout(() => {
                window.location.href = 'gym-dashboard.html';
            }, 1000);
        }
        
        // Get current progress (implement based on file type)
        function getCurrentProgress() {
            // For lesson-based files
            if (typeof STORAGE_KEY !== 'undefined') {
                const completed = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
                return {
                    currentQuestion: completed.length + 1,
                    questionIndex: completed.length,
                    completedLessons: completed,
                    answers: {}
                };
            }
            // For carousel-based files
            if (typeof currentQuestionIndex !== 'undefined' && typeof answers !== 'undefined') {
                return {
                    currentQuestion: currentQuestionIndex + 1,
                    questionIndex: currentQuestionIndex,
                    answers: answers,
                    completedLessons: []
                };
            }
            return { currentQuestion: 1, questionIndex: 0, answers: {}, completedLessons: [] };
        }
        
        // Toast notification
        function showToast(message) {
            const toast = document.createElement('div');
            toast.style.cssText = `
                position: fixed;
                bottom: 30px;
                left: 50%;
                transform: translateX(-50%);
                background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                color: white;
                padding: 16px 32px;
                border-radius: 50px;
                box-shadow: 0 8px 25px rgba(16, 185, 129, 0.4);
                z-index: 10000;
                font-weight: 600;
            `;
            toast.textContent = message;
            document.body.appendChild(toast);
            
            setTimeout(() => toast.remove(), 3000);
        }
        
        // Check for saved progress on load
        function checkForSavedProgress() {
            const saved = localStorage.getItem('currentProgress');
            if (!saved) return false;
            
            try {
                const progress = JSON.parse(saved);
                
                // Check if this is the right stripe
                if (progress.stripe !== currentStripeName) return false;
                
                // Check if recent (within 7 days)
                const daysSince = (Date.now() - progress.timestamp) / (1000 * 60 * 60 * 24);
                if (daysSince > 7) {
                    localStorage.removeItem('currentProgress');
                    return false;
                }
                
                // Ask to resume
                const resume = confirm(
                    "🥋 WELCOME BACK!\\n\\n" +
                    "You were on " + (progress.completedLessons ? `Lesson ${progress.currentQuestion}` : `Question ${progress.currentQuestion}`) + " of " + (progress.totalQuestions || totalQuestions) + ".\\n" +
                    "Resume where you left off?"
                );
                
                if (resume) {
                    // Restore progress based on file type
                    if (progress.completedLessons && progress.completedLessons.length > 0) {
                        // Lesson-based: restore completed lessons
                        if (typeof STORAGE_KEY !== 'undefined') {
                            localStorage.setItem(STORAGE_KEY, JSON.stringify(progress.completedLessons));
                            // Trigger UI update
                            if (typeof updateAllStats === 'function') {
                                updateAllStats();
                            }
                        }
                    } else if (progress.answers && Object.keys(progress.answers).length > 0) {
                        // Carousel-based: restore answers and question index
                        if (typeof currentQuestionIndex !== 'undefined') {
                            currentQuestionIndex = progress.questionIndex || 0;
                        }
                        if (typeof answers !== 'undefined') {
                            answers = progress.answers || {};
                        }
                        // Jump to saved question
                        if (typeof renderQuestion === 'function') {
                            renderQuestion(currentQuestionIndex);
                        }
                    }
                    return true;
                } else {
                    localStorage.removeItem('currentProgress');
                    return false;
                }
            } catch (e) {
                console.error('Error loading saved progress:', e);
                return false;
            }
        }
        
        // Save progress
        function saveProgress() {
            const currentProgress = getCurrentProgress();
            const progressData = {
                stripe: currentStripeName,
                currentQuestion: currentProgress.currentQuestion || 1,
                questionIndex: currentProgress.questionIndex || 0,
                answers: currentProgress.answers || {},
                completedLessons: currentProgress.completedLessons || [],
                timestamp: Date.now(),
                partialComplete: true,
                totalQuestions: totalQuestions
            };
            localStorage.setItem('currentProgress', JSON.stringify(progressData));
        }
        
        // Clear progress on completion
        function clearProgress() {
            localStorage.removeItem('currentProgress');
        }
        
        // Show TAP OUT button when content is visible
        function showTapOutButton() {
            const btn = document.getElementById('tapOutBtn');
            if (btn) {
                btn.style.display = 'flex';
            }
        }
        
        // Initialize on page load
        document.addEventListener('DOMContentLoaded', function() {
            // Check for saved progress
            const resumed = checkForSavedProgress();
            
            // Show TAP OUT button after a short delay (when content is loaded)
            setTimeout(showTapOutButton, 500);
        });
"""

def add_tap_out_to_file(filepath, config):
    """Add TAP OUT functionality to a stripe file."""
    print(f"Processing {filepath}...")
    
    if not os.path.exists(filepath):
        print(f"  ⚠️  File not found: {filepath}")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if TAP OUT already exists
    if 'tap-out-button' in content:
        print(f"  ✓ TAP OUT already exists in {filepath}")
        return True
    
    # Add CSS (before closing </style> tag)
    if '</style>' in content and TAP_OUT_CSS not in content:
        content = content.replace('</style>', TAP_OUT_CSS + '\n    </style>')
    
    # Add HTML button (after <body> tag)
    if '<body>' in content and TAP_OUT_HTML not in content:
        # Find <body> tag and add button after it
        body_match = re.search(r'(<body[^>]*>)', content)
        if body_match:
            insert_pos = body_match.end()
            content = content[:insert_pos] + '\n' + TAP_OUT_HTML + '\n' + content[insert_pos:]
    
    # Add JavaScript (before closing </script> tag or before </body>)
    js_code = TAP_OUT_JS.replace('{STRIPE_NAME}', config['stripe']).replace('{TOTAL_QUESTIONS}', str(config['questions']))
    
    # Try to insert before last </script> tag
    if '</script>' in content:
        # Find last </script> tag
        last_script_pos = content.rfind('</script>')
        if last_script_pos > 0:
            content = content[:last_script_pos] + js_code + '\n    </script>'
    elif '</body>' in content:
        # Insert before </body> if no script tag found
        content = content.replace('</body>', '<script>' + js_code + '</script>\n</body>')
    
    # Update completion functions to call clearProgress()
    # For lesson-based files
    if 'function completeLesson' in content and 'clearProgress()' not in content:
        content = re.sub(
            r'(function completeLesson\([^)]+\)\s*\{[^}]*localStorage\.setItem\([^)]+\);)',
            r'\1\n            clearProgress();',
            content,
            flags=re.DOTALL
        )
    
    # For carousel-based files - update showResults to call clearProgress
    if 'function showResults' in content and 'clearProgress()' not in content:
        # Find where completion is saved and add clearProgress before it
        content = re.sub(
            r'(localStorage\.setItem\([\'"]whiteBeltStripe\d+Complete[\'"],\s*[\'"]true[\'"];)',
            r'clearProgress();\n            \1',
            content
        )
        # Also handle other belt completions
        for belt in ['blue', 'purple', 'brown', 'black']:
            content = re.sub(
                rf'(localStorage\.setItem\([\'"]{belt}BeltStripe\d+Complete[\'"],\s*[\'"]true[\'"];)',
                r'clearProgress();\n            \1',
                content
            )
    
    # Update answer selection to call saveProgress()
    # For lesson completion
    if 'completeLesson(' in content and 'saveProgress()' not in content:
        # Add saveProgress after lesson completion
        content = re.sub(
            r'(completeLesson\([^)]+\);)',
            r'\1\n            saveProgress();',
            content
        )
    
    # For carousel answer selection
    if 'selectOption' in content and 'saveProgress()' not in content:
        # Find selectOption function and add saveProgress
        content = re.sub(
            r'(function selectOption\([^)]+\)\s*\{[^}]*showInsight\([^)]+\);)',
            r'\1\n            saveProgress();',
            content,
            flags=re.DOTALL
        )
    
    # Write updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ Added TAP OUT to {filepath}")
    return True

def main():
    """Main function to process all stripe files."""
    base_dir = Path(__file__).parent
    
    print("🚀 Adding TAP OUT functionality to all stripe files...\n")
    
    success_count = 0
    skip_count = 0
    
    for filename, config in STRIPE_CONFIG.items():
        filepath = base_dir / filename
        
        # Skip stripe1-carousel-NEW.html (already done)
        if 'stripe1-carousel-NEW' in filename:
            print(f"⏭️  Skipping {filename} (already has TAP OUT)")
            skip_count += 1
            continue
        
        if add_tap_out_to_file(filepath, config):
            success_count += 1
        else:
            skip_count += 1
    
    print(f"\n✅ Complete! Processed {success_count} files, skipped {skip_count} files.")

if __name__ == '__main__':
    main()


