#!/usr/bin/env python3
"""
Fix English assessment structure to match working German version
"""

from pathlib import Path
import re

def fix_english_structure():
    """Fix English version to match German structure"""
    file_path = Path('sales-recruiting-stage1.html')
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # Find where the script tag starts for questions
    # In German version, it's at line 276: <script>
    # Check if questions are inside a script tag
    
    questions_pos = content.find('const questions = [')
    script_before = content.rfind('<script>', 0, questions_pos)
    script_after = content.find('</script>', questions_pos)
    
    print(f"Questions found at position: {questions_pos}")
    print(f"Script tag before questions: {script_before}")
    print(f"Script tag after questions: {script_after}")
    
    # Check if questions is in global scope or inside a function
    # In German version, questions is in global scope right after <script>
    
    # Find the startAssessment function and check its structure
    start_assessment_pos = content.find('function startAssessment()')
    
    # Check if there are any scope issues
    # The problem might be that questions array is defined inside a function scope
    
    # Let's check what's between the results section and questions array
    results_end = content.find('</div>', content.find('id="results"'))
    
    # The issue might be that questions is not in global scope
    # Let's ensure questions array is accessible globally
    
    # Check if there's a script tag wrapping that might cause issues
    # German version has clean structure: <script> then const questions = [
    
    # Find if questions is inside any function or block
    function_before_questions = content.rfind('function', 0, questions_pos)
    brace_before = content.rfind('{', 0, questions_pos)
    
    # If questions is inside a function, that's the problem
    if function_before_questions > 0 and brace_before > function_before_questions:
        print("⚠️  Questions array might be inside a function scope!")
        # We need to move it to global scope
    
    # Another issue: check if currentQuestion and answers are defined
    current_question_pos = content.find('let currentQuestion')
    answers_pos = content.find('let answers')
    
    print(f"currentQuestion defined: {current_question_pos > -1}")
    print(f"answers defined: {answers_pos > -1}")
    
    # The German version works, so let's check its exact structure
    de_file = Path('sales-recruiting-stage1-de.html')
    de_content = de_file.read_text(encoding='utf-8', errors='ignore')
    
    # Find script start in German
    de_script_start = de_content.find('<script>', de_content.find('id="results"'))
    de_questions_start = de_content.find('const questions = [', de_script_start)
    
    # Check what's between script and questions in German
    de_between = de_content[de_script_start:de_questions_start]
    print(f"\nGerman structure between script and questions:\n{de_between[:200]}")
    
    # Check English structure
    en_between = content[script_before if script_before > 0 else 0:questions_pos]
    print(f"\nEnglish structure before questions:\n{en_between[-200:]}")
    
    # The key difference: German has simpler structure
    # Let's simplify English to match

if __name__ == '__main__':
    fix_english_structure()

