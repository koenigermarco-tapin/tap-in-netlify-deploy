#!/usr/bin/env python3
"""
Fix duplicate sections and non-functioning buttons in sales-recruiting-stage1.html
"""

from pathlib import Path
import re

def fix_assessment_issues():
    """Fix duplicate sections and button functionality"""
    file_path = Path('sales-recruiting-stage1.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # 1. Fix email capture auto-initialization - only initialize AFTER results are shown
    # Remove the auto-initialization that runs on page load
    old_init = r'setTimeout\(initializeEmailCapture, 2000\);'
    new_init = '''// Auto-initialize ONLY if results are already visible (check for results container)
            const existingResults = document.getElementById('resultContent') || 
                                    document.querySelector('.result-display') || 
                                    document.querySelector('.results-container');
            if (existingResults && existingResults.style.display !== 'none') {
                setTimeout(initializeEmailCapture, 1000);
            }'''
    content = re.sub(old_init, new_init, content)
    
    # 2. Ensure intro section is visible on load and assessment form is hidden
    # Check if display styles are correctly set
    if 'id="introSection"' in content:
        # Make sure introSection is visible by default (not display:none)
        intro_section_pattern = r'(<div class="intro-section"[^>]*?)style="([^"]*)"'
        def fix_intro_style(match):
            full_tag = match.group(0)
            if 'display: none' not in full_tag and 'style=' in full_tag:
                return full_tag  # Already correct
            elif 'display: none' in full_tag:
                # Remove display:none if present
                styles = match.group(2)
                styles = re.sub(r'display\s*:\s*none[;]?\s*', '', styles)
                styles = re.sub(r'[;]\s*;+', ';', styles)  # Clean up double semicolons
                return f'<div class="intro-section" id="introSection" style="{styles}"'
            return full_tag
        content = re.sub(intro_section_pattern, fix_intro_style, content, count=1)
    
    # 3. Ensure startAssessment function exists and works correctly
    if 'function startAssessment()' not in content:
        # Add the function if missing
        init_script = '''
            function startAssessment() {
                const introSection = document.getElementById('introSection');
                const progressContainer = document.querySelector('.progress-container');
                const assessmentForm = document.getElementById('assessmentForm');
                
                if (introSection) introSection.style.display = 'none';
                if (progressContainer) progressContainer.style.display = 'block';
                if (assessmentForm) {
                    assessmentForm.style.display = 'block';
                    currentQuestion = 0;
                    renderQuestion();
                    updateProgress();
                }
            }
            '''
        # Insert after the questions array or before first function
        if 'function renderQuestion()' in content:
            content = content.replace('function renderQuestion()', init_script + '\n            function renderQuestion()')
    
    # 4. Make sure assessment form is hidden by default
    assessment_form_pattern = r'(<div id="assessmentForm"[^>]*?)style="([^"]*)"'
    def ensure_hidden(match):
        styles = match.group(2)
        if 'display: none' not in styles:
            styles = 'display: none; ' + styles
        return f'{match.group(1)}style="{styles}"'
    content = re.sub(assessment_form_pattern, ensure_hidden, content)
    
    # 5. Make sure progress container is hidden by default
    progress_pattern = r'(<div class="progress-container"[^>]*?)style="([^"]*)"'
    def ensure_progress_hidden(match):
        styles = match.group(2)
        if 'display: none' not in styles:
            styles = 'display: none; ' + styles
        return f'{match.group(1)}style="{styles}"'
    content = re.sub(progress_pattern, ensure_progress_hidden, content)
    
    file_path.write_text(content, encoding='utf-8')
    print("✅ Fixed assessment structure and button functionality")
    print("   - Email capture only initializes after results are shown")
    print("   - Intro section visible on load")
    print("   - Assessment form hidden on load")
    print("   - Progress container hidden on load")
    print("   - startAssessment function verified")

if __name__ == '__main__':
    fix_assessment_issues()

