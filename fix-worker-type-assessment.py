#!/usr/bin/env python3
"""
Fix worker type assessment start issue - match working pattern
"""

from pathlib import Path
import re

def fix_worker_type_assessment():
    """Fix worker type assessment to match working pattern"""
    file_path = Path('worker-type-assessment.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # Find startAssessment function
    start_pattern = r'function startAssessment\(\) \{([^}]+)\}'
    
    def replace_start(match):
        func_body = match.group(1)
        
        # Ensure variables are reset and form is properly shown
        new_func = '''
            // Reset to first question
            currentQuestion = 0;
            answers = {};
            
            // Hide intro, show assessment form
            const introSection = document.getElementById('introSection');
            const progressContainer = document.querySelector('.progress-container');
            const assessmentForm = document.getElementById('assessmentForm');
            const results = document.getElementById('results');
            
            if (introSection) introSection.style.display = 'none';
            if (progressContainer) progressContainer.style.display = 'block';
            if (assessmentForm) {
                assessmentForm.style.display = 'block';
                assessmentForm.classList.remove('hidden');
            }
            if (results) {
                results.style.display = 'none';
                results.classList.remove('active');
            }
            
            // Render first question
            renderQuestion();
            updateProgress();
        }
'''
        return new_func
    
    if 'function startAssessment()' in content:
        content = re.sub(start_pattern, replace_start, content, count=1)
        print("✅ Fixed startAssessment function")
    
    # Also ensure renderQuestion has proper error handling
    render_pattern = r'(function renderQuestion\(\) \{[\s\S]*?card\.innerHTML = html;)'
    
    def enhance_render(match):
        render_func = match.group(0)
        if 'if (!card)' not in render_func:
            # Add error checking before innerHTML
            render_func = render_func.replace(
                'card.innerHTML = html;',
                '''if (!card) {
                console.error('[Worker Type Assessment] questionCard element not found!');
                return;
            }
            
            if (!q) {
                console.error('[Worker Type Assessment] Question not found at index:', currentQuestion);
                return;
            }
            
            card.innerHTML = html;
            card.style.display = 'block';'''
            )
        return render_func
    
    content = re.sub(render_pattern, enhance_render, content, count=1)
    
    file_path.write_text(content, encoding='utf-8')
    print("✅ Enhanced renderQuestion with error handling")
    print("✅ Fixed worker type assessment start functionality")

if __name__ == '__main__':
    fix_worker_type_assessment()

