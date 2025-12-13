#!/usr/bin/env python3
"""
Build Sales Recruiting Assessment System
Creates 3 files: Stage 1, Stage 2, and Demo
"""

from pathlib import Path
import re

def build_stage1():
    """Build sales-recruiting-stage1.html"""
    base_file = Path('worker-type-assessment.html')
    output_file = Path('sales-recruiting-stage1.html')
    
    content = base_file.read_text(encoding='utf-8', errors='ignore')
    
    # Update title and meta
    content = re.sub(
        r'<title>.*?</title>',
        r'<title>Sales Profile Assessment - Stage 1 | TAP-IN Recruiting</title>',
        content
    )
    
    content = re.sub(
        r'property="og:title" content="[^"]*"',
        r'property="og:title" content="Sales Recruiting Assessment - Stage 1"',
        content
    )
    
    # Update header
    content = re.sub(
        r'<h1[^>]*>🏃 Worker Type Assessment</h1>',
        r'<h1>🎯 Sales Profile Assessment - Stage 1</h1>',
        content
    )
    
    # Update intro section
    intro_pattern = r'<div class="intro-section"[^>]*>.*?</div>\s*</div>'
    new_intro = '''<div class="intro-section" id="introSection" style="background: #f8fafc; padding: 25px; border-radius: 12px; margin-bottom: 30px; border-left: 4px solid #1a365d;">
            <h3 style="color: #1e293b; margin-bottom: 15px; font-weight: 600;">📋 What to Expect</h3>
            <p style="color: #64748b; line-height: 1.7; margin-bottom: 15px;">
                This brief assessment helps us determine if there's a strong initial match 
                between your natural work style and our sales role. Takes 3 minutes.
            </p>
            <p style="color: #64748b; line-height: 1.7; margin-bottom: 20px;">
                <strong>Qualified candidates proceed to Stage 2</strong> (10-minute detailed profile).
            </p>
            
            <div style="text-align: center; margin-top: 25px;">
                <button class="btn btn-primary" onclick="startAssessment()" style="font-size: 1.2em; padding: 18px 40px;">
                    Start Assessment →
                </button>
            </div>
        </div>'''
    
    content = re.sub(intro_pattern, new_intro, content, flags=re.DOTALL)
    
    # Update progress text
    content = re.sub(
        r'Question 1 of 12',
        r'Question 1 of 10',
        content
    )
    
    # Replace questions array
    questions_array = '''const questions = [
            {
                id: 1,
                text: "In sales, I perform best with:",
                type: "choice",
                options: [
                    { text: "Fast-paced, quick wins (sprinter)", value: 7, key: "sprinter" },
                    { text: "Steady rhythm, consistent pipeline (jogger)", value: 10, key: "jogger" },
                    { text: "Long relationship building (ultra)", value: 3, key: "ultra" }
                ]
            },
            {
                id: 2,
                text: "My ideal sales cycle is:",
                type: "choice",
                options: [
                    { text: "1-2 weeks (short)", value: 7, key: "short" },
                    { text: "1-3 months (medium)", value: 10, key: "medium" },
                    { text: "6+ months (long)", value: 3, key: "long" }
                ]
            },
            {
                id: 3,
                text: "When presenting to potential clients, I naturally:",
                type: "choice",
                options: [
                    { text: "Confidently guide the conversation (assertive)", value: 10, key: "assertive" },
                    { text: "Listen carefully and adapt (empathetic)", value: 6, key: "empathetic" },
                    { text: "Present data and facts (analytical)", value: 4, key: "analytical" }
                ]
            },
            {
                id: 4,
                text: "After hearing 'no' from a prospect, I typically:",
                type: "choice",
                options: [
                    { text: "Move to the next opportunity immediately", value: 10, key: "quick" },
                    { text: "Review what went wrong briefly", value: 5, key: "reflect" },
                    { text: "Need time to recharge", value: 2, key: "slow" }
                ]
            },
            {
                id: 5,
                text: "What excites me most about sales is:",
                type: "choice",
                options: [
                    { text: "Hitting targets and winning", value: 10, key: "achievement" },
                    { text: "Helping customers solve problems", value: 7, key: "service" },
                    { text: "Building long-term relationships", value: 6, key: "relationships" }
                ]
            },
            {
                id: 6,
                text: "In a competitive sales environment, I:",
                type: "choice",
                options: [
                    { text: "Thrive and push to be #1", value: 10, key: "competitive" },
                    { text: "Perform well but prefer collaboration", value: 6, key: "collaborative" },
                    { text: "Feel stressed by competition", value: 2, key: "stressed" }
                ]
            },
            {
                id: 7,
                text: "When it's time to close, I:",
                type: "choice",
                options: [
                    { text: "Directly ask for the commitment", value: 10, key: "direct" },
                    { text: "Guide them to the decision gently", value: 6, key: "gentle" },
                    { text: "Present the logical next step", value: 4, key: "logical" }
                ]
            },
            {
                id: 8,
                text: "My ideal prospecting approach is:",
                type: "choice",
                options: [
                    { text: "High volume, many calls daily", value: 8, key: "volume" },
                    { text: "Targeted, consistent outreach", value: 10, key: "targeted" },
                    { text: "Deep research, few perfect calls", value: 4, key: "research" }
                ]
            },
            {
                id: 9,
                text: "My energy at work is typically:",
                type: "choice",
                options: [
                    { text: "High bursts, need variety", value: 7, key: "bursts" },
                    { text: "Steady and predictable", value: 10, key: "steady" },
                    { text: "Deep focus for long periods", value: 5, key: "deep" }
                ]
            },
            {
                id: 10,
                text: "When I lose a big deal to a competitor:",
                type: "choice",
                options: [
                    { text: "Analyze quickly and win the next one", value: 10, key: "resilient" },
                    { text: "Feel frustrated but recover", value: 5, key: "moderate" },
                    { text: "Question my approach", value: 2, key: "sensitive" }
                ]
            }
        ];'''
    
    # Find and replace questions array
    content = re.sub(
        r'const questions = \[.*?\];',
        questions_array,
        content,
        flags=re.DOTALL
    )
    
    # Update renderQuestion to handle new question structure
    # Need to update the rendering logic
    render_question_pattern = r'function renderQuestion\(\) \{.*?\}'
    new_render_question = '''function renderQuestion() {
            const q = questions[currentQuestion];
            const card = document.getElementById('questionCard');
            
            const introSection = document.getElementById('introSection');
            if (introSection) {
                introSection.style.display = 'none';
            }
            
            let html = '';
            html += `
                <div class="question">
                    <div class="question-text">
                        <span class="question-number">${currentQuestion + 1}.</span>
                        ${q.text}
                    </div>
                    <div class="options">
            `;
            q.options.forEach((opt) => {
                const selected = answers[currentQuestion] === opt.value ? 'selected' : '';
                html += `
                    <label class="option ${selected}" onclick="selectOption(this, ${opt.value}, '${opt.key}')">
                        <input type="radio" name="q${currentQuestion}" value="${opt.value}">
                        <div class="option-label">${opt.text}</div>
                    </label>
                `;
            });
            html += `
                    </div>
                </div>
            `;
            card.innerHTML = html;
            updateProgress();
            updateButtons();
        }'''
    
    content = re.sub(render_question_pattern, new_render_question, content, flags=re.DOTALL)
    
    # Update selectOption function
    select_option_pattern = r'function selectOption\([^)]*\) \{.*?\}'
    new_select_option = '''function selectOption(el, value, key) {
                answers[currentQuestion] = { value: value, key: key };
                saveProgress();
                document.querySelectorAll('.option').forEach(opt => opt.classList.remove('selected'));
                if (el && el.classList) el.classList.add('selected');
                const input = el.querySelector('input[type="radio"]');
                if (input) input.checked = true;
                document.getElementById('nextBtn').disabled = false;
            }'''
    
    content = re.sub(select_option_pattern, new_select_option, content, flags=re.DOTALL)
    
    # Replace showResults function with Stage 1 results
    results_pattern = r'function showResults\(\) \{.*?\n                window\.scrollTo\(0, 0\);'
    
    stage1_results = '''function showResults() {
                clearProgress();
                
                const results = calculateStage1Score();
                saveStage1Results(results);
                
                document.getElementById('assessmentForm').classList.add('hidden');
                document.getElementById('results').classList.add('active');
                
                const badgeClass = results.recommendation === 'EXCELLENT FIT' ? 'excellent' : 
                                  results.recommendation === 'GOOD FIT' ? 'good' :
                                  results.recommendation === 'MAYBE' ? 'maybe' : 'not-recommended';
                
                const badgeColor = results.color === 'green' ? '#10b981' :
                                  results.color === 'yellow' ? '#f59e0b' : '#ef4444';
                
                document.getElementById('resultContent').innerHTML = `
                    <div class="result-card" style="background: linear-gradient(135deg, ${badgeColor} 0%, ${badgeColor}dd 100%);">
                        <h2>🎯 Your Stage 1 Results</h2>
                        <div style="margin: 2rem 0;">
                            <div style="font-size: 4em; font-weight: bold; margin-bottom: 0.5rem;">${results.totalScore}</div>
                            <div style="font-size: 1.2em; opacity: 0.9;">out of 100</div>
                        </div>
                    </div>
                    
                    <div class="assessment-card" style="margin-top: 2rem;">
                        <div class="recommendation-badge" style="background: ${badgeColor}; color: white; padding: 1.5rem; border-radius: 12px; text-align: center; margin-bottom: 2rem;">
                            <h2 style="color: white; margin: 0; font-size: 1.8em;">${results.recommendation}</h2>
                        </div>
                        
                        <div class="next-steps-card" style="background: #f8fafc; padding: 2rem; border-radius: 12px; margin-bottom: 2rem;">
                            <h3 style="color: #1a365d; margin-bottom: 1rem;">📍 Next Steps</h3>
                            <p style="color: #64748b; line-height: 1.7; margin-bottom: 1.5rem;">${results.message}</p>
                            ${results.nextStep === 'stage2' ? `
                                <button class="btn btn-primary" onclick="window.location.href='sales-recruiting-stage2.html'" style="font-size: 1.1em; padding: 1rem 2rem;">
                                    Proceed to Stage 2 Assessment →
                                </button>
                            ` : ''}
                        </div>
                        
                        <div class="score-breakdown" style="margin-top: 2rem;">
                            <h3 style="color: #1a365d; margin-bottom: 1.5rem;">Score Breakdown</h3>
                            <div class="category-scores" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
                                <div class="category-score" style="background: #f8fafc; padding: 1.5rem; border-radius: 8px;">
                                    <div style="color: #64748b; font-size: 0.9em; margin-bottom: 0.5rem;">Work Style</div>
                                    <div style="font-size: 1.5em; font-weight: bold; color: #1a365d;" id="work-style-score">--/30</div>
                                </div>
                                <div class="category-score" style="background: #f8fafc; padding: 1.5rem; border-radius: 8px;">
                                    <div style="color: #64748b; font-size: 0.9em; margin-bottom: 0.5rem;">Communication</div>
                                    <div style="font-size: 1.5em; font-weight: bold; color: #1a365d;" id="communication-score">--/30</div>
                                </div>
                                <div class="category-score" style="background: #f8fafc; padding: 1.5rem; border-radius: 8px;">
                                    <div style="color: #64748b; font-size: 0.9em; margin-bottom: 0.5rem;">Motivation</div>
                                    <div style="font-size: 1.5em; font-weight: bold; color: #1a365d;" id="motivation-score">--/20</div>
                                </div>
                                <div class="category-score" style="background: #f8fafc; padding: 1.5rem; border-radius: 8px;">
                                    <div style="color: #64748b; font-size: 0.9em; margin-bottom: 0.5rem;">Resilience</div>
                                    <div style="font-size: 1.5em; font-weight: bold; color: #1a365d;" id="resilience-score">--/20</div>
                                </div>
                            </div>
                        </div>
                        
                        <div style="text-align: center; margin-top: 2rem;">
                            <a href="business-portal.html" class="btn btn-secondary">← Back to Business Portal</a>
                        </div>
                    </div>
                `;
                
                // Update category scores
                const categoryScores = calculateCategoryScores();
                document.getElementById('work-style-score').textContent = `${categoryScores.workStyle}/30`;
                document.getElementById('communication-score').textContent = `${categoryScores.communication}/30`;
                document.getElementById('motivation-score').textContent = `${categoryScores.motivation}/20`;
                document.getElementById('resilience-score').textContent = `${categoryScores.resilience}/20`;
                
                window.scrollTo(0, 0);
            }'''
    
    content = re.sub(results_pattern, stage1_results, content, flags=re.DOTALL)
    
    # Add Stage 1 specific functions before showResults
    stage1_functions = '''
        function calculateStage1Score() {
            let totalScore = 0;
            Object.values(answers).forEach(answer => {
                if (typeof answer === 'object' && answer.value) {
                    totalScore += answer.value;
                } else if (typeof answer === 'number') {
                    totalScore += answer;
                }
            });
            
            let recommendation, action, color, message, nextStep;
            
            if (totalScore >= 85) {
                recommendation = "EXCELLENT FIT";
                action = "SEND_STAGE_2";
                color = "green";
                message = "Strong potential match! Please proceed to Stage 2.";
                nextStep = "stage2";
            } else if (totalScore >= 70) {
                recommendation = "GOOD FIT";
                action = "REVIEW_CV";
                color = "yellow";
                message = "Promising profile. We'll review your CV and be in touch.";
                nextStep = "review";
            } else if (totalScore >= 55) {
                recommendation = "MAYBE";
                action = "REVIEW_CV";
                color = "yellow";
                message = "Some strengths shown. We'll review carefully.";
                nextStep = "review";
            } else {
                recommendation = "NOT RECOMMENDED";
                action = "POLITE_REJECT";
                color = "red";
                message = "Thank you for your interest. Your profile doesn't closely match this role.";
                nextStep = "reject";
            }
            
            return { totalScore, recommendation, action, color, message, nextStep };
        }
        
        function calculateCategoryScores() {
            const getAnswerValue = (qId) => {
                const answer = answers[qId - 1];
                return typeof answer === 'object' ? answer.value : (answer || 0);
            };
            
            return {
                workStyle: getAnswerValue(1) + getAnswerValue(2) + getAnswerValue(8) + getAnswerValue(9),
                communication: getAnswerValue(3) + getAnswerValue(7),
                motivation: getAnswerValue(5) + getAnswerValue(6),
                resilience: getAnswerValue(4) + getAnswerValue(10)
            };
        }
        
        function saveStage1Results(results) {
            const categoryScores = calculateCategoryScores();
            const data = {
                assessmentType: 'sales-recruiting-stage1',
                completedDate: new Date().toISOString(),
                totalScore: results.totalScore,
                recommendation: results.recommendation,
                action: results.action,
                questionScores: Object.keys(answers).map(idx => {
                    const answer = answers[idx];
                    const q = questions[idx];
                    return {
                        questionId: q.id,
                        value: typeof answer === 'object' ? answer.value : answer,
                        key: typeof answer === 'object' ? answer.key : null
                    };
                }),
                categoryScores: categoryScores
            };
            
            localStorage.setItem('salesRecruitingStage1', JSON.stringify(data));
        }
        
    '''
    
    # Insert functions before showResults
    content = re.sub(
        r'(function showResults)',
        stage1_functions + r'\1',
        content
    )
    
    # Initialize answers as object
    content = re.sub(
        r'let answers = \{\};',
        r'let answers = {};',
        content
    )
    
    # Update progress text calculation
    content = re.sub(
        r'Question \$\{currentQuestion \+ 1\} of \$\{questions\.length\}',
        r'Question ${currentQuestion + 1} of ${questions.length}',
        content
    )
    
    output_file.write_text(content, encoding='utf-8')
    print("✅ Created sales-recruiting-stage1.html")

def build_stage2():
    """Build sales-recruiting-stage2.html - will be simplified version"""
    print("⏳ Stage 2 will be created after Stage 1 is complete")

def build_demo():
    """Build sales-recruiting-demo.html"""
    print("⏳ Demo page will be created after Stage 2 is complete")

if __name__ == '__main__':
    print("🔧 Building Sales Recruiting Assessment System...\n")
    build_stage1()
    print("\n✅ Stage 1 complete!")
    print("📝 Next: Stage 2 and Demo")

