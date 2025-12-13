#!/usr/bin/env python3
"""
Fix worker type assessment start function
"""

from pathlib import Path

def fix_start_assessment():
    file_path = Path('worker-type-assessment.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # Find the exact function
    old_func = '''            function startAssessment() {
                document.getElementById('introSection').style.display = 'none';
                document.querySelector('.progress-container').style.display = 'block';
                document.getElementById('assessmentForm').style.display = 'block';
                renderQuestion();
                updateProgress();
            }'''
    
    new_func = '''            function startAssessment() {
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
            }'''
    
    if old_func in content:
        content = content.replace(old_func, new_func)
        file_path.write_text(content, encoding='utf-8')
        print("✅ Fixed worker type assessment start function")
    else:
        print("⚠️  Function not found in expected format, checking...")
        # Try to find it with more flexible matching
        if 'function startAssessment()' in content:
            print("✅ startAssessment function exists, may need manual fix")

if __name__ == '__main__':
    fix_start_assessment()

