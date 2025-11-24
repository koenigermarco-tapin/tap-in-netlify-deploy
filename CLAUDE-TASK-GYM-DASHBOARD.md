# TASK: Build The GYM Dashboard System

## 🎯 Mission Overview

You're building **THE GYM** - the central hub where users train daily in TAP-IN. This is where everything comes together: belt progress, daily practices, training modules, open mat content, tools, and assessments.

**Current state:** We have a beautiful frontend mockup (`gym-dashboard.html`)  
**Your job:** Make it functional, dynamic, and connected to real data

---

## 📋 What You're Building

### 1. **Dashboard Hub** (Frontend Enhancement)
Transform the static mockup into a dynamic, personalized dashboard

### 2. **Backend Data Layer** (Supabase Integration)
Build the database schema and API functions to power everything

### 3. **Content Library** (Educational Resources)
Create the actual training modules, articles, exercises, and tools

### 4. **Gamification Engine** (XP, Streaks, Challenges)
Implement the progression and reward systems

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────┐
│         gym-dashboard.html              │
│  (User's personalized training hub)     │
└─────────────────┬───────────────────────┘
                  │
                  ├── User State (localStorage + Supabase)
                  ├── Belt Progress Data
                  ├── Daily Practice Queue
                  ├── Training Modules
                  ├── Open Mat Content
                  ├── Tools & Assessments
                  └── Gamification (XP, Streaks, Challenges)
```

---

## 📊 DATABASE SCHEMA

### Core Tables You Need to Create

#### 1. `user_profiles`
```sql
CREATE TABLE user_profiles (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES auth.users NOT NULL,
  display_name TEXT,
  current_belt TEXT DEFAULT 'white', -- white, blue, purple, brown, black
  belt_xp INTEGER DEFAULT 0,
  total_xp INTEGER DEFAULT 0,
  current_streak INTEGER DEFAULT 0,
  longest_streak INTEGER DEFAULT 0,
  last_active_date DATE,
  worker_type TEXT, -- sprinter, jogger, ultrarunner
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

#### 2. `belt_progress`
```sql
CREATE TABLE belt_progress (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES auth.users NOT NULL,
  belt_level TEXT NOT NULL,
  stripe_1_complete BOOLEAN DEFAULT FALSE,
  stripe_2_complete BOOLEAN DEFAULT FALSE,
  stripe_3_complete BOOLEAN DEFAULT FALSE,
  stripe_4_complete BOOLEAN DEFAULT FALSE,
  belt_complete BOOLEAN DEFAULT FALSE,
  started_at TIMESTAMP DEFAULT NOW(),
  completed_at TIMESTAMP,
  UNIQUE(user_id, belt_level)
);
```

#### 3. `training_modules`
```sql
CREATE TABLE training_modules (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  belt_level TEXT NOT NULL,
  stripe_number INTEGER, -- 1-4, or NULL for open mat
  module_key TEXT UNIQUE NOT NULL, -- 'white-self-awareness', etc.
  title TEXT NOT NULL,
  description TEXT,
  icon TEXT, -- emoji
  lesson_count INTEGER DEFAULT 0,
  estimated_minutes INTEGER,
  xp_reward INTEGER DEFAULT 25,
  unlock_condition TEXT, -- JSON: {"requires_stripe": 1, "requires_module": "xxx"}
  sort_order INTEGER,
  is_open_mat BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT NOW()
);
```

#### 4. `user_module_progress`
```sql
CREATE TABLE user_module_progress (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES auth.users NOT NULL,
  module_id UUID REFERENCES training_modules NOT NULL,
  lessons_completed INTEGER DEFAULT 0,
  is_complete BOOLEAN DEFAULT FALSE,
  started_at TIMESTAMP DEFAULT NOW(),
  completed_at TIMESTAMP,
  UNIQUE(user_id, module_id)
);
```

#### 5. `daily_practices`
```sql
CREATE TABLE daily_practices (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES auth.users NOT NULL,
  practice_date DATE NOT NULL,
  morning_intention_done BOOLEAN DEFAULT FALSE,
  daily_module_done BOOLEAN DEFAULT FALSE,
  evening_reflection_done BOOLEAN DEFAULT FALSE,
  morning_intention_xp INTEGER DEFAULT 10,
  daily_module_xp INTEGER DEFAULT 25,
  evening_reflection_xp INTEGER DEFAULT 10,
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(user_id, practice_date)
);
```

#### 6. `open_mat_content`
```sql
CREATE TABLE open_mat_content (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  content_key TEXT UNIQUE NOT NULL,
  title TEXT NOT NULL,
  description TEXT,
  content_type TEXT NOT NULL, -- article, video, exercise, worksheet, audio, experiment
  icon TEXT,
  estimated_minutes INTEGER,
  xp_reward INTEGER,
  badge TEXT, -- 'new', 'popular', 'quick'
  content_html TEXT, -- Full HTML content
  research_citations TEXT[], -- Array of research sources
  is_featured BOOLEAN DEFAULT FALSE,
  view_count INTEGER DEFAULT 0,
  created_at TIMESTAMP DEFAULT NOW()
);
```

#### 7. `user_open_mat_progress`
```sql
CREATE TABLE user_open_mat_progress (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES auth.users NOT NULL,
  content_id UUID REFERENCES open_mat_content NOT NULL,
  completed BOOLEAN DEFAULT FALSE,
  xp_earned INTEGER DEFAULT 0,
  completed_at TIMESTAMP,
  UNIQUE(user_id, content_id)
);
```

#### 8. `tools`
```sql
CREATE TABLE tools (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  tool_key TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  description TEXT,
  icon TEXT,
  url TEXT NOT NULL, -- Link to tool page
  category TEXT, -- reflection, planning, breathing, tracking
  is_active BOOLEAN DEFAULT TRUE,
  sort_order INTEGER
);
```

#### 9. `weekly_challenges`
```sql
CREATE TABLE weekly_challenges (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  challenge_key TEXT UNIQUE NOT NULL,
  title TEXT NOT NULL,
  description TEXT,
  days_required INTEGER DEFAULT 7,
  xp_reward INTEGER DEFAULT 100,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  is_active BOOLEAN DEFAULT TRUE
);
```

#### 10. `user_challenge_progress`
```sql
CREATE TABLE user_challenge_progress (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES auth.users NOT NULL,
  challenge_id UUID REFERENCES weekly_challenges NOT NULL,
  days_completed INTEGER DEFAULT 0,
  is_complete BOOLEAN DEFAULT FALSE,
  completed_at TIMESTAMP,
  UNIQUE(user_id, challenge_id)
);
```

#### 11. `user_activity_log`
```sql
CREATE TABLE user_activity_log (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES auth.users NOT NULL,
  activity_type TEXT NOT NULL, -- 'module_complete', 'practice_complete', 'assessment_complete', etc.
  activity_title TEXT NOT NULL,
  xp_earned INTEGER DEFAULT 0,
  created_at TIMESTAMP DEFAULT NOW()
);
```

#### 12. `assessments`
```sql
CREATE TABLE assessments (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  assessment_key TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  icon TEXT,
  url TEXT NOT NULL,
  required_for_belt TEXT, -- Which belt requires this
  xp_reward INTEGER DEFAULT 50,
  is_active BOOLEAN DEFAULT TRUE
);
```

#### 13. `user_assessment_results`
```sql
CREATE TABLE user_assessment_results (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES auth.users NOT NULL,
  assessment_id UUID REFERENCES assessments NOT NULL,
  results_json JSONB, -- Store full assessment results
  completed_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(user_id, assessment_id)
);
```

---

## 🔧 BACKEND FUNCTIONS TO BUILD

### Supabase Edge Functions / Database Functions

#### 1. `get_user_dashboard_data(user_id)`
Returns everything needed for dashboard:
- User profile (name, belt, XP, streak)
- Belt progress for current belt
- Today's practice status
- Current training modules with progress
- Recent activity (last 5)
- Active weekly challenge
- Available assessments

#### 2. `complete_daily_practice(user_id, practice_type)`
- Marks practice as done
- Awards XP
- Updates streak if all 3 practices done
- Logs activity

#### 3. `complete_module_lesson(user_id, module_id)`
- Increments lesson count
- Awards XP if module complete
- Unlocks next module if applicable
- Logs activity

#### 4. `complete_open_mat_content(user_id, content_id)`
- Marks content as viewed
- Awards XP
- Logs activity
- Increments view count

#### 5. `update_weekly_challenge(user_id, challenge_id)`
- Increments days completed
- Awards XP if challenge complete
- Logs activity

#### 6. `award_xp(user_id, amount, reason)`
- Adds to total_xp and belt_xp
- Checks if belt promotion earned
- Logs activity

#### 7. `check_and_update_streak(user_id)`
- Checks if user completed all 3 daily practices
- Updates current_streak
- Resets if day was missed
- Awards streak milestone bonuses (7, 14, 30, 100 days)

#### 8. `get_open_mat_library(user_id, filter)`
- Returns open mat content
- Marks which ones user has completed
- Can filter by type, badge, etc.

---

## 📚 CONTENT TO CREATE

### White Belt Training Modules

#### Module 1: Self-Awareness (5 lessons)
**Lessons:**
1. **What is Self-Awareness?** (5 min)
   - Definition and research (Tasha Eurich)
   - Why it's the foundation
   - XP: 15

2. **The Two Types of Self-Awareness** (6 min)
   - Internal vs External
   - Common blind spots
   - XP: 20

3. **Self-Awareness Assessment** (8 min)
   - Interactive reflection
   - Identify your patterns
   - XP: 25

4. **Building Your Awareness Practice** (7 min)
   - Daily check-in framework
   - Questions to ask yourself
   - XP: 20

5. **Awareness in Action** (10 min)
   - Real scenarios
   - Practice exercises
   - XP: 30

**Total XP for completion:** 110

#### Module 2: Vulnerability as Strength (5 lessons)
**Lessons:**
1. **The Vulnerability Paradox** (6 min)
   - Brené Brown research
   - Why it feels dangerous
   - XP: 15

2. **Armor vs Authenticity** (7 min)
   - Defense mechanisms
   - Cost of invulnerability
   - XP: 20

3. **Vulnerability ≠ Weakness** (8 min)
   - Reframing the narrative
   - Examples from leadership
   - XP: 25

4. **Practicing Small Vulnerabilities** (10 min)
   - Safe experiments
   - Start where you are
   - XP: 25

5. **Vulnerability and Trust** (9 min)
   - How they connect
   - Building deeper relationships
   - XP: 30

**Total XP for completion:** 115

#### Module 3: Building Self-Trust (7 lessons)
**Lessons:**
1. **What is Self-Trust?** (5 min)
2. **Keeping Promises to Yourself** (8 min)
3. **Your Personal Integrity Gap** (10 min)
4. **The Self-Trust Audit** (12 min)
5. **Small Commitments, Big Impact** (8 min)
6. **When You Break a Promise to Yourself** (9 min)
7. **Self-Trust as Foundation** (10 min)

**Total XP for completion:** 180

#### Module 4: Journaling Practice (5 lessons)
1. **Why Journaling Works** (Science-backed benefits)
2. **Types of Journaling** (Free-write, structured, gratitude, etc.)
3. **Morning Pages Practice** (Julia Cameron method)
4. **Evening Reflection Framework**
5. **Your Personal Journaling System**

**Total XP for completion:** 110

### Open Mat Content Library (20+ pieces)

#### Articles (Research-Based)
1. **The Inner Game of Leadership** (Timothy Gallwey)
   - Self-talk and performance
   - Internal obstacles
   - 8 min read, 25 XP

2. **Google's Project Aristotle: What Makes Teams Work**
   - Psychological safety findings
   - Implementation insights
   - 10 min read, 30 XP

3. **The Five Dysfunctions Explained**
   - Patrick Lencioni framework
   - How to identify in your team
   - 12 min read, 35 XP

4. **Growth Mindset Research** (Carol Dweck)
   - Fixed vs growth mindset
   - How to develop it
   - 9 min read, 25 XP

5. **Energy Management Over Time Management**
   - HBR research
   - Practical applications
   - 11 min read, 30 XP

#### Exercises (Practical)
1. **Box Breathing for Pressure**
   - Navy SEAL technique
   - Interactive timer
   - 5 min, 15 XP

2. **Reframe in 60 Seconds**
   - Cognitive reframing micro-practice
   - 1 min, 10 XP

3. **Energy Mapping Exercise**
   - Track energy for a week
   - Discover patterns
   - 15 min setup, 40 XP

4. **Values Clarification Workout**
   - Identify top 5 values
   - Alignment check
   - 20 min, 50 XP

5. **Morning Intention Setting**
   - Daily practice
   - Focused start
   - 2 min, 10 XP

#### Videos (Educational)
1. **Jiu-Jitsu Philosophy for Life**
   - Gentle art principles
   - Leadership without force
   - 12 min, 30 XP

2. **The Power of Vulnerability** (Brené Brown style)
   - Why it matters
   - How to practice
   - 15 min, 35 XP

3. **Stoic Morning Routine**
   - Marcus Aurelius practices
   - Modern application
   - 10 min, 25 XP

#### Worksheets
1. **Energy Audit Template**
2. **Weekly Reflection Worksheet**
3. **Personal Values Worksheet**
4. **Goal Alignment Matrix**
5. **Difficult Conversation Prep Sheet**

#### Weekly Experiments
1. **Say "I Don't Know" (7 days)**
   - Practice intellectual humility
   - Track reactions
   - 100 XP

2. **7 Days of Vulnerability**
   - Share one honest thing daily
   - Build trust muscles
   - 100 XP

3. **Morning Gratitude Week**
   - Write 3 things every AM
   - Shift perspective
   - 100 XP

---

## 🎮 GAMIFICATION SYSTEM

### XP Awards Structure

**Daily Practices:**
- Morning Intention: 10 XP
- Daily Module Lesson: 25 XP
- Evening Reflection: 10 XP
- **Daily Total:** 45 XP

**Training Modules:**
- Short lesson (5 min): 15-20 XP
- Medium lesson (8-10 min): 25-30 XP
- Long lesson (12+ min): 35-40 XP
- Module completion bonus: 50 XP

**Open Mat Content:**
- Quick win (1-5 min): 10-15 XP
- Article (8-12 min): 25-35 XP
- Video (10-15 min): 30-40 XP
- Worksheet (15-20 min): 40-50 XP
- Weekly experiment (7 days): 100 XP

**Assessments:**
- Quick assessment: 30 XP
- Full assessment: 50 XP
- Belt assessment: 100 XP

**Streaks:**
- 7 days: 50 XP bonus
- 14 days: 100 XP bonus
- 30 days: 250 XP bonus
- 100 days: 1000 XP bonus

### Belt XP Requirements
- **White Belt:** 0-1000 XP
- **Blue Belt:** 1000-3000 XP
- **Purple Belt:** 3000-6000 XP
- **Brown Belt:** 6000-10000 XP
- **Black Belt:** 10000+ XP

### Stripe Requirements (per belt)
Each stripe requires:
- Completing the stripe's training module(s)
- Earning 200-250 XP within that stripe's focus area
- Maintaining a 7+ day streak

---

## 🛠️ TOOLS TO BUILD

### 1. Journal Tool
**File:** `tool-journal.html`
- Free-write interface
- Auto-save to localStorage/Supabase
- Search previous entries
- Prompts library
- Export functionality

### 2. Goal Tracker
**File:** `tool-goals.html`
- SMART goal framework
- Progress visualization
- Weekly check-ins
- Accountability features

### 3. Mood Log (21-Day Tracker)
**File:** `tool-mood-tracker.html`
- Daily mood rating
- Energy levels
- Stress levels
- Pattern recognition
- Insights based on data

### 4. Breathing Exercises
**File:** `tool-breathing.html`
- Box breathing (4-4-4-4)
- 4-7-8 breathing
- Wim Hof method
- Visual/audio guides
- Timer functionality

### 5. Focus Timer (Pomodoro)
**File:** `tool-focus-timer.html`
- 25/5 min intervals
- Customizable durations
- Break reminders
- Session tracking
- XP for completed sessions

### 6. Random Reflection Prompt
**File:** `tool-random-prompt.html`
- Library of 100+ prompts
- Categorized (leadership, values, conflict, etc.)
- Journal integration
- Daily surprise prompt

### 7. Progress Report
**File:** `tool-progress-report.html`
- Weekly summary
- XP gained
- Modules completed
- Streak status
- Areas of growth
- Downloadable PDF

### 8. AI Coach (Future)
**File:** `tool-ai-coach.html`
- Chat interface
- Context-aware responses
- Training recommendations
- Reflection questions

---

## 📱 DYNAMIC DASHBOARD FEATURES

### Features to Implement

#### 1. Personalized Welcome
- Use actual user name from profile
- Real-time date
- Current belt status
- Motivational message based on progress

#### 2. Smart Daily Practice Queue
- Morning Intention (available 5 AM - 12 PM)
- Daily Module (available all day, suggests next incomplete lesson)
- Evening Reflection (available 5 PM - 11 PM)
- Mark practices as complete
- Award XP
- Update streak

#### 3. Belt Progress Visualization
- Real-time calculation of % complete
- XP toward next belt
- Stripe completion status
- Path visualization (completed, current, locked)
- "Ready to test" notification when requirements met

#### 4. Training Modules Grid
- Pull from database
- Show progress per module
- Lock modules based on unlock conditions
- Visual indicators (completed, in-progress, locked)
- Click to open module

#### 5. Open Mat Dynamic Content
- Featured content rotation
- Badges (new, popular, quick win)
- Filter by type
- Track completed content
- Award XP on completion

#### 6. Recent Activity Feed
- Last 5 activities
- Real-time updates
- XP display
- Timestamp formatting

#### 7. Weekly Challenge Tracker
- Show active challenge
- Progress bar
- Days remaining
- Update progress
- Completion celebration

#### 8. Assessments Status
- Show completed vs available
- Link to assessment pages
- Track results
- Suggest next assessment

#### 9. Streak Management
- Visual flame icon
- Highlight milestones (7, 14, 30, 100 days)
- Warning if streak at risk
- Streak recovery grace period (1 day)

#### 10. Toolbox Quick Access
- Dynamic tool loading
- Usage tracking
- Favorites system
- Most-used highlighted

---

## 🎨 CONTENT WRITING GUIDELINES

### Tone & Voice
- **Direct:** No fluff, get to the point (Jocko style)
- **Honest:** Don't sugarcoat difficulty
- **Educational:** Cite research, explain why
- **Motivating:** Inspire through clarity, not cheerleading
- **Respectful:** Assume intelligence, give context

### Structure for Articles
1. **Hook** (Why this matters)
2. **Research** (What science says)
3. **Application** (How to use it)
4. **Practice** (What to do today)
5. **Deeper Dive** (Optional reading)

### Structure for Exercises
1. **Purpose** (Why you're doing this)
2. **Instructions** (Step-by-step)
3. **Tips** (Common mistakes to avoid)
4. **Reflection** (Processing questions)

### Structure for Videos (Scripts)
1. **Opening** (0-30 sec: The problem/question)
2. **Core Content** (2-10 min: Teaching)
3. **Action Step** (30-60 sec: What to do next)
4. **Closing** (15 sec: Reminder/encouragement)

---

## 🚀 IMPLEMENTATION PHASES

### Phase 1: Backend Foundation (Week 1)
- [ ] Create all Supabase tables
- [ ] Build database functions
- [ ] Set up authentication
- [ ] Test data insertion/retrieval

### Phase 2: Dashboard Dynamics (Week 2)
- [ ] Connect dashboard to real data
- [ ] Implement daily practice system
- [ ] Build XP and streak logic
- [ ] Activity logging

### Phase 3: Training Modules (Week 3)
- [ ] Write White Belt module content (20 lessons)
- [ ] Build module navigation system
- [ ] Progress tracking
- [ ] Completion logic

### Phase 4: Open Mat Library (Week 4)
- [ ] Write 10 articles
- [ ] Create 10 exercises
- [ ] Build content viewer
- [ ] Completion tracking

### Phase 5: Tools (Week 5)
- [ ] Build Journal tool
- [ ] Build Mood Tracker
- [ ] Build Breathing tool
- [ ] Build Focus Timer

### Phase 6: Gamification (Week 6)
- [ ] Weekly challenges system
- [ ] Achievement badges
- [ ] Leaderboards (optional)
- [ ] Progress reports

### Phase 7: Polish & Testing (Week 7)
- [ ] Mobile optimization
- [ ] Performance optimization
- [ ] User testing
- [ ] Bug fixes

---

## 📝 CONTENT TEMPLATE EXAMPLES

### Article Template
```html
<article class="open-mat-article">
    <header>
        <span class="badge">Article • 10 min read</span>
        <h1>The Inner Game of Leadership</h1>
        <p class="byline">Why your self-talk determines your ceiling</p>
    </header>
    
    <section class="intro">
        <p>Hook: Every leader has two conversations happening simultaneously...</p>
    </section>
    
    <section class="research">
        <h2>What the Research Shows</h2>
        <p>Timothy Gallwey's work in "The Inner Game of Tennis" revealed...</p>
        <div class="citation">
            Source: Gallwey, T. (1974). The Inner Game of Tennis.
        </div>
    </section>
    
    <section class="application">
        <h2>How to Apply This</h2>
        <ol>
            <li>Step one...</li>
            <li>Step two...</li>
        </ol>
    </section>
    
    <section class="practice">
        <h2>Practice This Today</h2>
        <div class="exercise-box">
            [Specific action to take]
        </div>
    </section>
    
    <footer>
        <button onclick="markComplete()">Mark Complete (+25 XP)</button>
    </footer>
</article>
```

### Exercise Template
```html
<article class="open-mat-exercise">
    <header>
        <span class="badge">Exercise • 5 min</span>
        <h1>Box Breathing for Pressure</h1>
        <p class="byline">The Navy SEAL technique for staying calm</p>
    </header>
    
    <section class="purpose">
        <h2>Why This Works</h2>
        <p>Box breathing activates your parasympathetic nervous system...</p>
    </section>
    
    <section class="instructions">
        <h2>How to Do It</h2>
        <ol>
            <li>Breathe in for 4 counts</li>
            <li>Hold for 4 counts</li>
            <li>Breathe out for 4 counts</li>
            <li>Hold for 4 counts</li>
            <li>Repeat 4 times</li>
        </ol>
    </section>
    
    <section class="interactive">
        <div class="breathing-timer">
            [Visual breathing guide with timer]
        </div>
        <button onclick="startExercise()">Start Exercise</button>
    </section>
    
    <section class="reflection">
        <h2>After You Complete</h2>
        <p>How do you feel? What changed?</p>
    </section>
    
    <footer>
        <button onclick="markComplete()">Complete (+15 XP)</button>
    </footer>
</article>
```

---

## 🎯 SUCCESS METRICS

Dashboard is successful when:
- [ ] Users log in daily (streak system working)
- [ ] 80%+ complete daily practices
- [ ] Average session time: 15-30 min
- [ ] Module completion rate: 70%+
- [ ] Open mat engagement: 3+ pieces per week
- [ ] XP system feels rewarding, not grindy
- [ ] Users report "I learned something valuable"

---

## 🔑 KEY PRINCIPLES

1. **Education over decoration** - Pretty is good, valuable is essential
2. **Research-backed content** - Every claim needs a source
3. **Actionable immediately** - Always clear next steps
4. **Respect user time** - No fluff, no filler
5. **Honest about difficulty** - Growth is hard, say so
6. **Gamification serves learning** - XP rewards real progress, not busy work

---

## 📚 RESEARCH LIBRARY TO INTEGRATE

**White Belt Focus:**
- Tasha Eurich: Self-awareness research
- Brené Brown: Vulnerability research
- Carol Dweck: Growth mindset
- Timothy Gallwey: Inner game concepts
- Patrick Lencioni: Trust foundations

**Blue Belt Focus:**
- VitalSmarts: Crucial conversations
- Kim Scott: Radical candor
- Harvard: Active listening research
- Google: Project Aristotle (psychological safety)

**Purple Belt Focus:**
- Roger Martin: Strategic thinking
- Peter Senge: Systems thinking
- Marshall Goldsmith: Coaching

**Brown Belt Focus:**
- Simon Sinek: Leadership
- Ed Schein: Organizational culture
- John Kotter: Change management

**Black Belt Focus:**
- Ray Dalio: Principles
- Jocko Willink: Extreme ownership
- BJJ philosophy: Belt journey

---

## 🚀 DELIVERABLES

When you're done, we should have:

1. **Functional Database** (Supabase)
   - All tables created
   - Functions working
   - Sample data loaded

2. **Dynamic Dashboard** (gym-dashboard.html enhanced)
   - Connected to real data
   - All features working
   - Mobile responsive

3. **Content Library**
   - 20 White Belt lessons written
   - 20 Open Mat pieces created
   - All properly formatted

4. **Tools Built**
   - At minimum: Journal, Mood Tracker, Breathing, Focus Timer
   - Fully functional
   - Data persistence

5. **Documentation**
   - API documentation
   - Content creation guidelines
   - User guide

---

**Remember:** The dashboard is the daily habit. If it's not engaging, educational, and rewarding, users won't come back. Make it impossible NOT to want to train daily.

🥋 Let's build THE GYM.
