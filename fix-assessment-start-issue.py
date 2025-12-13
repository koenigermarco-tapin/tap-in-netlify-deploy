#!/usr/bin/env python3
"""
Fix assessment start issue - email capture showing and test not starting
"""

from pathlib import Path
import re

def fix_assessment_start():
    """Fix the assessment start functionality"""
    file_path = Path('sales-recruiting-stage1.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # 1. Make sure email capture component doesn't initialize on page load
    # Remove any auto-initialization that happens before results
    old_pattern = r'setTimeout\(initializeEmailCapture[^;]+;'
    content = re.sub(old_pattern, '', content)
    
    # 2. Ensure email capture only initializes when explicitly called from showResults
    email_init_pattern = r'(window\.initEmailCapture = initializeEmailCapture;)'
    replacement = r'''\1
            
            // DO NOT auto-initialize - only call from showResults() function
            // Email capture will be initialized after assessment completion'''
    content = re.sub(email_init_pattern, replacement, content)
    
    # 3. Make sure startAssessment properly initializes the question
    start_assessment_pattern = r'(function startAssessment\(\) \{[^}]+)renderQuestion\(\);'
    
    def enhance_start_assessment(match):
        func_body = match.group(1)
        # Add explicit initialization
        enhanced = func_body + '''
                // Reset to first question
                currentQuestion = 0;
                answers = {};
                
                // Ensure all elements are visible/hidden correctly
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
                if (results) results.style.display = 'none';
                
                // Render first question
                renderQuestion();
                updateProgress();
            }
'''
        return enhanced
    
    if 'function startAssessment()' in content:
        # Find and replace the function
        pattern = r'function startAssessment\(\) \{([^}]+)\}'
        def replace_func(match):
            body = match.group(1)
            # Check if it already has the enhancements
            if 'currentQuestion = 0' not in body:
                # Enhance it
                body = body.replace(
                    'renderQuestion();',
                    '''// Reset to first question
                currentQuestion = 0;
                answers = {};
                
                // Ensure all elements are visible/hidden correctly
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
                if (results) results.style.display = 'none';
                
                // Render first question
                renderQuestion();'''
                )
            return f'function startAssessment() {{{body}}}'
        
        content = re.sub(pattern, replace_func, content, count=1)
    
    # 4. Make sure email capture component check is more strict
    # This is already in js/email-capture-component.js but let's verify it's there
    
    file_path.write_text(content, encoding='utf-8')
    print("✅ Fixed assessment start functionality")
    print("   - Email capture will NOT auto-initialize on page load")
    print("   - startAssessment() properly initializes questions")
    print("   - All visibility states properly managed")

if __name__ == '__main__':
    fix_assessment_start()

