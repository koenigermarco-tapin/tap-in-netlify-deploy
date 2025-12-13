#!/usr/bin/env python3
"""
Fix assessment not starting - ensure renderQuestion actually displays content
"""

from pathlib import Path
import re

def fix_render_question():
    """Ensure renderQuestion properly displays the first question"""
    file_path = Path('sales-recruiting-stage1.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # Find renderQuestion function
    render_start = content.find('function renderQuestion()')
    if render_start == -1:
        print("⚠️  renderQuestion function not found")
        return
    
    render_end = content.find('\n        function ', render_start + 1)
    if render_end == -1:
        render_end = content.find('\n    function ', render_start + 1)
    if render_end == -1:
        render_end = render_start + 1000
    
    render_func = content[render_start:render_end]
    
    # Check if card.innerHTML is set
    if 'card.innerHTML = html;' in render_func:
        # Add error handling and ensure card is found
        new_render_func = render_func.replace(
            '            card.innerHTML = html;',
            '''            if (!card) {
                console.error('[Assessment] questionCard element not found!');
                return;
            }
            
            if (!q) {
                console.error('[Assessment] Question not found at index:', currentQuestion);
                return;
            }
            
            card.innerHTML = html;
            card.style.display = 'block';
            
            // Scroll to question
            setTimeout(() => {
                card.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }, 100);'''
        )
        content = content[:render_start] + new_render_func + content[render_end:]
        print("✅ Enhanced renderQuestion with error handling")
    
    # Also ensure startAssessment checks if questions exist
    start_assessment_pattern = r'(function startAssessment\(\) \{[\s\S]*?)renderQuestion\(\);'
    def enhance_start(match):
        func_body = match.group(1)
        enhancement = '''
                // Verify questions array exists
                if (!questions || questions.length === 0) {
                    console.error('[Assessment] Questions array is empty or undefined!');
                    alert('Error: Assessment questions not loaded. Please refresh the page.');
                    return;
                }
                
                // Verify questionCard element exists
                const questionCard = document.getElementById('questionCard');
                if (!questionCard) {
                    console.error('[Assessment] questionCard element not found!');
                    alert('Error: Assessment form not found. Please refresh the page.');
                    return;
                }
                
                '''
        return func_body + enhancement + 'renderQuestion();'
    
    content = re.sub(start_assessment_pattern, enhance_start, content, count=1)
    
    file_path.write_text(content, encoding='utf-8')
    print("✅ Added error handling to startAssessment")
    print("   - Verifies questions array exists")
    print("   - Verifies questionCard element exists")
    print("   - Enhanced renderQuestion with display and scroll")

if __name__ == '__main__':
    fix_render_question()

