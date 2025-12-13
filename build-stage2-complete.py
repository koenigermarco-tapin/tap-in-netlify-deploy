#!/usr/bin/env python3
"""
Build complete Stage 2 Assessment with 25 questions in 4 sections
"""

from pathlib import Path
import re

def build_stage2_complete():
    """Build complete Stage 2 with all 25 questions"""
    base_file = Path('sales-recruiting-stage1.html')
    output_file = Path('sales-recruiting-stage2.html')
    
    content = base_file.read_text(encoding='utf-8', errors='ignore')
    
    # Update title and meta
    content = content.replace(
        '<title>Sales Profile Assessment - Stage 1 | TAP-IN Recruiting</title>',
        '<title>Sales Profile Assessment - Stage 2 | TAP-IN Recruiting</title>'
    )
    
    content = re.sub(
        r'property="og:title" content="[^"]*"',
        r'property="og:title" content="Sales Recruiting Assessment - Stage 2"',
        content
    )
    
    # Update header
    content = content.replace(
        '🎯 Sales Profile Assessment - Stage 1',
        '🎯 Sales Profile Assessment - Stage 2'
    )
    
    # Update subtitle
    content = content.replace(
        'Quick 3-minute screen to assess sales fit',
        'Detailed 10-minute profile for interview preparation'
    )
    
    # Update intro section
    new_intro = '''<div class="intro-section" id="introSection" style="background: #f8fafc; padding: 25px; border-radius: 12px; margin-bottom: 30px; border-left: 4px solid #1a365d;">
            <h3 style="color: #1e293b; margin-bottom: 15px; font-weight: 600;">📋 What to Expect</h3>
            <p style="color: #64748b; line-height: 1.7; margin-bottom: 15px;">
                This comprehensive assessment creates your complete sales profile 
                across 4 key dimensions. Results help us prepare customized interview 
                questions and predict your success in this role.
            </p>
            <ul style="color: #64748b; line-height: 1.8; margin-left: 20px; margin-bottom: 20px;">
                <li><strong>25 questions</strong> across 4 sections</li>
                <li><strong>~10 minutes</strong> to complete</li>
                <li><strong>Detailed profile</strong> with interview prep</li>
            </ul>
            
            <div style="text-align: center; margin-top: 25px;">
                <button class="btn btn-primary" onclick="startAssessment()" style="font-size: 1.2em; padding: 18px 40px;">
                    Start Assessment →
                </button>
            </div>
        </div>'''
    
    content = re.sub(
        r'<div class="intro-section"[^>]*>.*?</div>\s*</div>',
        new_intro,
        content,
        flags=re.DOTALL
    )
    
    # Update progress text
    content = content.replace('Question 1 of 10', 'Question 1 of 25')
    
    # Replace questions array with all 25 Stage 2 questions
    questions_array = '''const questions = [
            // SECTION 1: Work Style Deep Dive (8 questions)
            {
                id: 11,
                section: 1,
                text: "I manage my sales pipeline by:",
                type: "choice",
                options: [
                    { text: "Quick reviews, stay flexible", value: 6, key: "flexible" },
                    { text: "Systematic tracking, weekly reviews", value: 10, key: "systematic" },
                    { text: "Deep analysis, monthly strategy", value: 5, key: "analytical" }
                ]
            },
            {
                id: 12,
                section: 1,
                text: "My relationship with CRM systems:",
                type: "choice",
                options: [
                    { text: "Update when needed", value: 4, key: "casual" },
                    { text: "Religiously track every interaction", value: 10, key: "disciplined" },
                    { text: "Prefer personal notes", value: 2, key: "manual" }
                ]
            },
            {
                id: 13,
                section: 1,
                text: "After initial contact, I typically follow up:",
                type: "choice",
                options: [
                    { text: "Next day, stay top of mind", value: 7, key: "immediate" },
                    { text: "3-5 days, strategic timing", value: 10, key: "strategic" },
                    { text: "1-2 weeks, give them space", value: 5, key: "patient" }
                ]
            },
            {
                id: 14,
                section: 1,
                text: "When juggling multiple deals:",
                type: "choice",
                options: [
                    { text: "Switch rapidly between them", value: 6, key: "rapid" },
                    { text: "Time-block by deal stage", value: 10, key: "organized" },
                    { text: "Focus on one until resolved", value: 5, key: "focused" }
                ]
            },
            {
                id: 15,
                section: 1,
                text: "At start of quarter, I:",
                type: "choice",
                options: [
                    { text: "Hit the ground running", value: 7, key: "action" },
                    { text: "Map out pipeline strategy", value: 10, key: "planning" },
                    { text: "Set annual vision first", value: 5, key: "strategic" }
                ]
            },
            {
                id: 16,
                section: 1,
                text: "My sweet spot is closing:",
                type: "choice",
                options: [
                    { text: "5+ deals per month", value: 8, key: "high" },
                    { text: "2-4 deals per month", value: 10, key: "medium" },
                    { text: "1 major deal per quarter", value: 4, key: "low" }
                ]
            },
            {
                id: 17,
                section: 1,
                text: "I learn new sales techniques by:",
                type: "choice",
                options: [
                    { text: "Trying them immediately", value: 7, key: "experimental" },
                    { text: "Practicing systematically", value: 10, key: "methodical" },
                    { text: "Deep study first", value: 5, key: "academic" }
                ]
            },
            {
                id: 18,
                section: 1,
                text: "End-of-quarter pressure makes me:",
                type: "choice",
                options: [
                    { text: "Thrive with urgency", value: 8, key: "thrive" },
                    { text: "Execute my plan calmly", value: 10, key: "calm" },
                    { text: "Feel stressed by deadlines", value: 3, key: "stressed" }
                ]
            },
            // SECTION 2: Communication Mastery (8 questions)
            {
                id: 19,
                section: 2,
                text: "In first meetings, I focus on:",
                type: "choice",
                options: [
                    { text: "Establishing credibility quickly", value: 10, key: "credibility" },
                    { text: "Building personal connection", value: 7, key: "connection" },
                    { text: "Understanding their needs deeply", value: 6, key: "needs" }
                ]
            },
            {
                id: 20,
                section: 2,
                text: "When prospects raise concerns, I:",
                type: "choice",
                options: [
                    { text: "Address directly with confidence", value: 10, key: "direct" },
                    { text: "Empathize and explore deeper", value: 7, key: "empathetic" },
                    { text: "Provide detailed evidence", value: 5, key: "analytical" }
                ]
            },
            {
                id: 21,
                section: 2,
                text: "My presentations are:",
                type: "choice",
                options: [
                    { text: "Energetic and dynamic", value: 8, key: "energetic" },
                    { text: "Structured and clear", value: 10, key: "structured" },
                    { text: "Data-rich and thorough", value: 6, key: "analytical" }
                ]
            },
            {
                id: 22,
                section: 2,
                text: "On cold calls, I:",
                type: "choice",
                options: [
                    { text: "Jump in with high energy", value: 7, key: "energetic" },
                    { text: "Use proven scripts confidently", value: 10, key: "scripted" },
                    { text: "Research extensively first", value: 5, key: "prepared" }
                ]
            },
            {
                id: 23,
                section: 2,
                text: "I build trust by:",
                type: "choice",
                options: [
                    { text: "Delivering on promises consistently", value: 10, key: "reliable" },
                    { text: "Being genuinely interested in them", value: 8, key: "interested" },
                    { text: "Demonstrating expertise", value: 6, key: "expert" }
                ]
            },
            {
                id: 24,
                section: 2,
                text: "In negotiations, I:",
                type: "choice",
                options: [
                    { text: "Push for best terms assertively", value: 7, key: "assertive" },
                    { text: "Find win-win systematically", value: 10, key: "collaborative" },
                    { text: "Use market data strategically", value: 6, key: "analytical" }
                ]
            },
            {
                id: 25,
                section: 2,
                text: "With internal teams, I communicate:",
                type: "choice",
                options: [
                    { text: "Frequently, stay aligned", value: 7, key: "frequent" },
                    { text: "Structured updates, clear requests", value: 10, key: "structured" },
                    { text: "Strategic check-ins only", value: 5, key: "strategic" }
                ]
            },
            {
                id: 26,
                section: 2,
                text: "When receiving sales coaching, I:",
                type: "choice",
                options: [
                    { text: "Apply it immediately", value: 10, key: "immediate" },
                    { text: "Reflect and integrate thoughtfully", value: 7, key: "reflective" },
                    { text: "Prefer to find my own style", value: 3, key: "independent" }
                ]
            },
            // SECTION 3: Motivation & Values (5 questions)
            {
                id: 27,
                section: 3,
                text: "In my career, success means:",
                type: "choice",
                options: [
                    { text: "Recognition as top performer", value: 10, key: "recognition" },
                    { text: "Customer loyalty and referrals", value: 6, key: "loyalty" },
                    { text: "Work-life balance", value: 4, key: "balance" }
                ]
            },
            {
                id: 28,
                section: 3,
                text: "My ideal comp structure:",
                type: "choice",
                options: [
                    { text: "High variable, reward performance", value: 10, key: "variable" },
                    { text: "Balanced base and commission", value: 6, key: "balanced" },
                    { text: "Stable base, modest incentives", value: 3, key: "stable" }
                ]
            },
            {
                id: 29,
                section: 3,
                text: "In 3 years, I see myself:",
                type: "choice",
                options: [
                    { text: "Leading a team of sellers", value: 10, key: "leadership" },
                    { text: "Managing key accounts", value: 7, key: "account" },
                    { text: "Expanding to new markets", value: 6, key: "expansion" }
                ]
            },
            {
                id: 30,
                section: 3,
                text: "I feel most fulfilled when:",
                type: "choice",
                options: [
                    { text: "Closing a hard-fought deal", value: 10, key: "achievement" },
                    { text: "Solving a customer challenge", value: 6, key: "service" },
                    { text: "Building trusted relationships", value: 5, key: "relationships" }
                ]
            },
            {
                id: 31,
                section: 3,
                text: "I thrive in cultures that:",
                type: "choice",
                options: [
                    { text: "Celebrate wins and reward top performers", value: 10, key: "competitive" },
                    { text: "Emphasize collaboration and support", value: 6, key: "collaborative" },
                    { text: "Value autonomy and independence", value: 5, key: "autonomous" }
                ]
            },
            // SECTION 4: Resilience & Sustainability (4 questions)
            {
                id: 32,
                section: 4,
                text: "After a tough rejection, I'm back to 100% in:",
                type: "choice",
                options: [
                    { text: "Minutes - next call, next opportunity", value: 10, key: "instant" },
                    { text: "Hours - quick reflection, then move on", value: 6, key: "quick" },
                    { text: "Days - need to process and recharge", value: 2, key: "slow" }
                ]
            },
            {
                id: 33,
                section: 4,
                text: "During a 2-week dry spell with no wins:",
                type: "choice",
                options: [
                    { text: "Double down on proven activities", value: 10, key: "double" },
                    { text: "Try new approaches", value: 6, key: "experimental" },
                    { text: "Question if it's the right role", value: 2, key: "questioning" }
                ]
            },
            {
                id: 34,
                section: 4,
                text: "I maintain sales performance by:",
                type: "choice",
                options: [
                    { text: "Consistent daily routines", value: 10, key: "consistent" },
                    { text: "Riding waves of motivation", value: 5, key: "waves" },
                    { text: "Deep strategic planning", value: 6, key: "strategic" }
                ]
            },
            {
                id: 35,
                section: 4,
                text: "When quota pressure builds, I:",
                type: "choice",
                options: [
                    { text: "Focus on controllables - activity metrics", value: 10, key: "focus" },
                    { text: "Seek support from manager/team", value: 7, key: "support" },
                    { text: "Work longer hours until resolved", value: 5, key: "hustle" }
                ]
            }
        ];
        
        // Section headers
        const sections = [
            { id: 1, title: "Work Style Deep Dive", start: 0, end: 7 },
            { id: 2, title: "Communication Mastery", start: 8, end: 15 },
            { id: 3, title: "Motivation & Values", start: 16, end: 20 },
            { id: 4, title: "Resilience & Sustainability", start: 21, end: 24 }
        ];'''
    
    # Find and replace questions array
    q_start = content.find("const questions = [")
    q_end = content.find("];", q_start) + 2
    if q_start > 0 and q_end > q_start:
        content = content[:q_start] + questions_array + content[q_end:]
    
    # Update renderQuestion to show section headers
    render_question_pattern = r'function renderQuestion\(\) \{.*?updateButtons\(\);\s*\}'
    new_render_question = '''function renderQuestion() {
            const q = questions[currentQuestion];
            const card = document.getElementById('questionCard');
            
            const introSection = document.getElementById('introSection');
            if (introSection) {
                introSection.style.display = 'none';
            }
            
            // Find current section
            const currentSection = sections.find(s => currentQuestion >= s.start && currentQuestion <= s.end);
            const isSectionStart = currentSection && currentQuestion === currentSection.start;
            
            let html = '';
            
            // Show section header if at start of section
            if (isSectionStart && currentQuestion > 0) {
                html += `
                    <div class="section-header" style="background: linear-gradient(135deg, #1a365d 0%, #0f1f3d 100%); color: white; padding: 2rem; border-radius: 12px; margin-bottom: 2rem; text-align: center;">
                        <h2 style="color: white; margin: 0; font-size: 1.5em;">📊 ${currentSection.title}</h2>
                        <p style="color: rgba(255,255,255,0.9); margin-top: 0.5rem; font-size: 0.95em;">Section ${currentSection.id} of 4</p>
                    </div>
                `;
            }
            
            html += `
                <div class="question">
                    <div class="question-text">
                        <span class="question-number">${currentQuestion + 1}.</span>
                        ${q.text}
                    </div>
                    <div class="options">
            `;
            q.options.forEach((opt) => {
                const answer = answers[currentQuestion];
                const isSelected = answer && (answer.value === opt.value || answer === opt.value);
                const selected = isSelected ? 'selected' : '';
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
    
    # Replace scoring functions for Stage 2
    stage2_scoring = '''
        function calculateStage2Score() {
            const categoryScores = {
                workStyle: {
                    raw: sumCategoryScores([11,12,13,14,15,16,17,18]),
                    max: 80,
                    weight: 0.30
                },
                communication: {
                    raw: sumCategoryScores([19,20,21,22,23,24,25,26]),
                    max: 80,
                    weight: 0.30
                },
                motivation: {
                    raw: sumCategoryScores([27,28,29,30,31]),
                    max: 50,
                    weight: 0.25
                },
                resilience: {
                    raw: sumCategoryScores([32,33,34,35]),
                    max: 40,
                    weight: 0.15
                }
            };
            
            const finalScore = 
                (categoryScores.workStyle.raw / 80 * 30) +
                (categoryScores.communication.raw / 80 * 30) +
                (categoryScores.motivation.raw / 50 * 25) +
                (categoryScores.resilience.raw / 40 * 15);
            
            return { finalScore: Math.round(finalScore), categoryScores };
        }
        
        function sumCategoryScores(questionIds) {
            let sum = 0;
            questionIds.forEach(qId => {
                const qIndex = questions.findIndex(q => q.id === qId);
                if (qIndex >= 0) {
                    const answer = answers[qIndex];
                    if (answer && typeof answer === 'object' && answer.value) {
                        sum += answer.value;
                    } else if (answer && typeof answer === 'number') {
                        sum += answer;
                    }
                }
            });
            return sum;
        }
        
        function saveStage2Results(results) {
            const data = {
                assessmentType: 'sales-recruiting-stage2',
                completedDate: new Date().toISOString(),
                finalScore: results.finalScore,
                categoryScores: results.categoryScores,
                questionScores: Object.keys(answers).map(idx => {
                    const answer = answers[parseInt(idx)];
                    const q = questions[parseInt(idx)];
                    return {
                        questionId: q.id,
                        section: q.section,
                        value: typeof answer === 'object' ? answer.value : answer,
                        key: typeof answer === 'object' ? answer.key : null
                    };
                })
            };
            
            localStorage.setItem('salesRecruitingStage2', JSON.stringify(data));
        }
        
    '''
    
    # Replace Stage 1 functions with Stage 2
    content = re.sub(
        r'function calculateStage1Score\(\) \{.*?\}',
        stage2_scoring.replace('function calculateStage1Score', 'function calculateStage2Score').split('function saveStage2Results')[0],
        content,
        flags=re.DOTALL
    )
    
    # Add Stage 2 functions before showResults
    show_results_pos = content.find('function showResults()')
    if show_results_pos > 0:
        content = content[:show_results_pos] + stage2_scoring + content[show_results_pos:]
    
    # Replace showResults for Stage 2
    stage2_results = '''function showResults() {
                clearProgress();
                
                const results = calculateStage2Score();
                saveStage2Results(results);
                
                document.getElementById('assessmentForm').classList.add('hidden');
                document.getElementById('results').classList.add('active');
                
                const profileType = generateProfileType(results.categoryScores);
                const strengths = generateStrengths(results.categoryScores);
                const development = generateDevelopmentAreas(results.categoryScores);
                const interviewQuestions = generateInterviewQuestions(results.categoryScores);
                
                document.getElementById('resultContent').innerHTML = `
                    <div class="result-card" style="background: linear-gradient(135deg, #1a365d 0%, #0f1f3d 100%);">
                        <h2>🎯 Your Sales Profile</h2>
                        <div style="font-size: 1.3em; margin: 1rem 0; opacity: 0.95;">${profileType}</div>
                        <div style="margin: 2rem 0;">
                            <div style="font-size: 4em; font-weight: bold; margin-bottom: 0.5rem;">${results.finalScore}</div>
                            <div style="font-size: 1.2em; opacity: 0.9;">out of 100</div>
                        </div>
                    </div>
                    
                    <div class="assessment-card" style="margin-top: 2rem;">
                        <h3 style="color: #1a365d; margin-bottom: 1.5rem;">💪 Top Strengths</h3>
                        <div style="display: grid; gap: 1rem;">
                            ${strengths.map(s => `<div style="background: #f8fafc; padding: 1rem; border-radius: 8px; border-left: 4px solid #10b981;">${s}</div>`).join('')}
                        </div>
                    </div>
                    
                    <div class="assessment-card" style="margin-top: 2rem;">
                        <h3 style="color: #1a365d; margin-bottom: 1.5rem;">📈 Areas to Explore in Interview</h3>
                        <div style="display: grid; gap: 1rem;">
                            ${development.map(d => `<div style="background: #fff7ed; padding: 1rem; border-radius: 8px; border-left: 4px solid #f59e0b;">${d}</div>`).join('')}
                        </div>
                    </div>
                    
                    <div class="assessment-card" style="margin-top: 2rem;">
                        <h3 style="color: #1a365d; margin-bottom: 1.5rem;">🎯 Suggested Interview Questions</h3>
                        <div style="display: grid; gap: 1rem;">
                            ${interviewQuestions.map(q => `
                                <div style="background: #f8fafc; padding: 1.5rem; border-radius: 8px;">
                                    <div style="font-weight: 600; color: #1e293b; margin-bottom: 0.5rem;">${q.question}</div>
                                    <div style="font-size: 0.9em; color: #64748b; font-style: italic;">Look for: ${q.lookFor}</div>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                    
                    <div style="text-align: center; margin-top: 2rem;">
                        <a href="sales-recruiting-demo.html" class="btn btn-secondary" style="margin-right: 1rem;">View Sample Profiles</a>
                        <a href="business-portal.html" class="btn btn-secondary">← Back to Business Portal</a>
                    </div>
                `;
                
                window.scrollTo(0, 0);
            }
            
            function generateProfileType(categoryScores) {
                const workStyle = categoryScores.workStyle.raw >= 70 ? 'Systematic' : categoryScores.workStyle.raw >= 50 ? 'Balanced' : 'Flexible';
                const motivation = categoryScores.motivation.raw >= 40 ? 'Competitive Drive' : 'Service-Focused';
                return `${workStyle} Jogger with ${motivation}`;
            }
            
            function generateStrengths(categoryScores) {
                const strengths = [];
                if (categoryScores.workStyle.raw >= 70) strengths.push('Systematic pipeline management');
                if (categoryScores.communication.raw >= 70) strengths.push('Strong communication structure');
                if (categoryScores.motivation.raw >= 40) strengths.push('High achievement drive');
                if (categoryScores.resilience.raw >= 30) strengths.push('Strong bounce-back ability');
                return strengths.length > 0 ? strengths : ['Multiple strengths across all categories'];
            }
            
            function generateDevelopmentAreas(categoryScores) {
                const areas = [];
                if (categoryScores.workStyle.raw < 50) areas.push('Pipeline organization systems');
                if (categoryScores.communication.raw < 50) areas.push('Structured communication approach');
                if (categoryScores.motivation.raw < 30) areas.push('Competitive drive and recognition needs');
                if (categoryScores.resilience.raw < 25) areas.push('Rejection recovery strategies');
                return areas.length > 0 ? areas : ['Overall performance is strong across all areas'];
            }
            
            function generateInterviewQuestions(categoryScores) {
                const questions = [];
                if (categoryScores.workStyle.raw >= 70) {
                    questions.push({
                        question: "Walk me through how you manage your sales pipeline weekly.",
                        lookFor: "Systematic approach, specific tools, consistency"
                    });
                }
                if (categoryScores.communication.raw >= 70) {
                    questions.push({
                        question: "Tell me about a time you had to be direct with a prospect. What happened?",
                        lookFor: "Confidence, tact, outcome focus"
                    });
                }
                if (categoryScores.resilience.raw < 25) {
                    questions.push({
                        question: "Describe a time you lost a big deal. How did you recover?",
                        lookFor: "Recovery time, learning, next steps"
                    });
                }
                return questions.length > 0 ? questions : [{
                    question: "What excites you most about sales?",
                    lookFor: "Passion, motivation drivers, alignment with role"
                }];
            }'''
    
    # Replace showResults
    show_results_start = content.find('function showResults()')
    show_results_end = content.find('window.scrollTo(0, 0);', show_results_start)
    if show_results_end > 0:
        show_results_end = content.find('\n            }', show_results_end) + len('\n            }')
        content = content[:show_results_start] + stage2_results + content[show_results_end:]
    
    output_file.write_text(content, encoding='utf-8')
    print("✅ Created complete sales-recruiting-stage2.html with 25 questions")

if __name__ == '__main__':
    print("🔧 Building Stage 2 Assessment (Complete)...\n")
    build_stage2_complete()
    print("\n✅ Stage 2 complete!")

