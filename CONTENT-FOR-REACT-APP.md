# 🎯 TAP-IN Complete Content for React App

> **For Cursor Claude:** This file contains ALL questions, assessments, and content. Each section is ready to copy into React components.

---

## 📋 TABLE OF CONTENTS

1. [Combined Leadership Profile - 46 Questions](#combined-leadership-profile)
2. [Quick Assessments (3)](#quick-assessments)
3. [Extended Assessments (4)](#extended-assessments)
4. [Belt System Content](#belt-system-content)
5. [Gamification Data](#gamification-data)

---

# COMBINED LEADERSHIP PROFILE
## 46 Questions Total (Worker Type + Leadership + Team Dynamics)

### SECTION 1: WORKER TYPE (Questions 1-12)

```typescript
// Question 1
{
  id: 1,
  section: 'worker',
  text: 'How do you prefer to approach your work?',
  type: 'radio',
  insight: {
    icon: '⚡',
    title: 'Work Rhythm Matters',
    content: 'Some people are sprinters—intense bursts followed by recovery. Others are marathoners—steady, consistent output. Neither is better. But knowing your rhythm is everything.'
  },
  options: [
    { value: 'sprinter', text: 'Intense bursts of focus, then I need breaks' },
    { value: 'jogger', text: 'Steady, consistent pace throughout the day' },
    { value: 'ultrarunner', text: 'Deep, sustained focus for long periods' }
  ]
}

// Question 2
{
  id: 2,
  section: 'worker',
  text: 'When a deadline is approaching:',
  type: 'radio',
  insight: {
    icon: '⏰',
    title: 'Pressure Response Reveals Your Operating System',
    content: 'Deadlines are laboratories for self-discovery. Do you thrive? Collapse? Or stay steady? This is not about discipline—it\'s about design. You\'re wired a certain way.'
  },
  options: [
    { value: 'sprinter', text: 'I thrive—pressure activates my best work' },
    { value: 'jogger', text: 'I stay steady and execute my normal routine' },
    { value: 'ultrarunner', text: 'I\'m already done—I work ahead to avoid last-minute stress' }
  ]
}

// Question 3
{
  id: 3,
  section: 'worker',
  text: 'Your energy levels throughout the day are:',
  type: 'radio',
  insight: {
    icon: '🔋',
    title: 'Energy Pattern = Your Power Grid',
    content: 'Cal Newport (Deep Work): "The key to productivity is not managing time—it\'s managing energy." Know when you peak. Protect those hours ruthlessly.'
  },
  options: [
    { value: 'sprinter', text: 'Peaks and valleys—high energy, then crashes' },
    { value: 'jogger', text: 'Relatively stable with predictable rhythms' },
    { value: 'ultrarunner', text: 'Consistent and sustained throughout the day' }
  ]
}

// Question 4
{
  id: 4,
  section: 'worker',
  text: 'How many projects do you prefer to juggle simultaneously?',
  type: 'radio',
  insight: {
    icon: '🎯',
    title: 'Context Switching Has a Cost',
    content: 'Research shows: Every time you switch tasks, you lose 20+ minutes of deep work time. Sprinters excel at single-tasking. Joggers manage 2-3 well. Ultrarunners can sustain complexity.'
  },
  options: [
    { value: 'sprinter', text: 'One main thing at a time—deep focus' },
    { value: 'jogger', text: '2-3 projects I can rotate between' },
    { value: 'ultrarunner', text: 'Multiple long-term initiatives simultaneously' }
  ]
}

// Question 5
{
  id: 5,
  section: 'worker',
  text: 'Your ideal work block is:',
  type: 'radio',
  insight: {
    icon: '⏱️',
    title: 'Time Blocks Match Your Biology',
    content: 'There is no universal "best" work block. Sprinters need 60-90 min max. Joggers thrive in 2-4 hour blocks. Ultrarunners can go all day if uninterrupted. Honor your biology.'
  },
  options: [
    { value: 'sprinter', text: '60-90 minutes of intense focus, then break' },
    { value: 'jogger', text: '2-4 hours with short breaks mixed in' },
    { value: 'ultrarunner', text: 'All day if the work is engaging' }
  ]
}

// Question 6
{
  id: 6,
  section: 'worker',
  text: 'After completing a major project, you:',
  type: 'radio',
  insight: {
    icon: '🏁',
    title: 'Recovery Pattern = Sustainability',
    content: 'Elite athletes know: recovery is training. Sprinters need significant downtime. Joggers transition smoothly. Ultrarunners are already running. Know your pattern or burn out.'
  },
  options: [
    { value: 'sprinter', text: 'Need significant downtime before the next challenge' },
    { value: 'jogger', text: 'Transition smoothly to the next project' },
    { value: 'ultrarunner', text: 'Already well into the next long-term initiative' }
  ]
}

// Question 7
{
  id: 7,
  section: 'worker',
  text: 'When learning something new, you prefer to:',
  type: 'radio',
  insight: {
    icon: '📚',
    title: 'Learning Style Impacts Mastery Speed',
    content: 'Josh Waitzkin (The Art of Learning): "There are those who prefer depth to breadth." Sprinters learn fast but shallow. Ultrarunners go deep but slow. Both reach mastery—just different paths.'
  },
  options: [
    { value: 'sprinter', text: 'Dive in intensely and master it quickly' },
    { value: 'jogger', text: 'Learn consistently through regular practice' },
    { value: 'ultrarunner', text: 'Take time to deeply understand before moving forward' }
  ]
}

// Question 8
{
  id: 8,
  section: 'worker',
  text: 'Your productivity is highest when:',
  type: 'radio',
  insight: {
    icon: '🚀',
    title: 'Productivity Trigger = Performance Catalyst',
    content: 'Dan Pink (Drive): Autonomy, mastery, purpose. But also: TIMING. Some need urgency. Some need routine. Some need space. Design your environment to match your trigger.'
  },
  options: [
    { value: 'sprinter', text: 'There\'s a clear deadline creating urgency' },
    { value: 'jogger', text: 'You have a structured routine to follow' },
    { value: 'ultrarunner', text: 'You have ample time to do thorough work' }
  ]
}

// Question 9
{
  id: 9,
  section: 'worker',
  text: 'How do you recharge?',
  type: 'radio',
  insight: {
    icon: '🔌',
    title: 'Recovery = Performance Multiplier',
    content: 'Alex Soojung-Kim Pang (Rest): "Rest is not the absence of work. Rest is the presence of recovery." Match your rest pattern to your work pattern or crash.'
  },
  options: [
    { value: 'sprinter', text: 'Complete breaks from work - clear boundaries' },
    { value: 'jogger', text: 'Regular short breaks throughout the day' },
    { value: 'ultrarunner', text: 'Rarely feel drained - work is sustainable' }
  ]
}

// Question 10
{
  id: 10,
  section: 'worker',
  text: 'In a typical work week, you prefer:',
  type: 'radio',
  insight: {
    icon: '📅',
    title: 'Weekly Pattern Shapes Sustainability',
    content: 'Tony Schwartz (The Way We\'re Working Isn\'t Working): "Human beings are designed to pulse—to move between energy expenditure and recovery." Honor your pulse.'
  },
  options: [
    { value: 'sprinter', text: 'Variety and intensity - different challenges daily' },
    { value: 'jogger', text: 'Predictable structure with some variety' },
    { value: 'ultrarunner', text: 'Consistency - similar tasks and rhythms' }
  ]
}

// Question 11
{
  id: 11,
  section: 'worker',
  text: 'Your approach to meetings is:',
  type: 'radio',
  insight: {
    icon: '🗣️',
    title: 'Meeting Style Reveals Communication Pattern',
    content: 'Elon Musk: "Walk out of a meeting if you\'re not adding value." Sprinters hate long meetings. Joggers like structured agendas. Ultrarunners don\'t mind deep discussions.'
  },
  options: [
    { value: 'sprinter', text: 'Short and intense - get in, decide, get out' },
    { value: 'jogger', text: 'Scheduled regularly with clear agendas' },
    { value: 'ultrarunner', text: 'Thorough discussions - take time needed' }
  ]
}

// Question 12
{
  id: 12,
  section: 'worker',
  text: 'When stressed, you perform best by:',
  type: 'radio',
  insight: {
    icon: '🎯',
    title: 'Stress Response = Your Default Mode',
    content: 'Under pressure, you default to your archetype. Sprinters channel stress into action. Joggers maintain routine. Ultrarunners stay methodical. Know your pattern—don\'t fight it.'
  },
  options: [
    { value: 'sprinter', text: 'Channeling it into rapid, focused action' },
    { value: 'jogger', text: 'Maintaining your normal routine and pace' },
    { value: 'ultrarunner', text: 'Staying calm and methodical' }
  ]
}
```

### SECTION 2: LEADERSHIP STYLE (Questions 13-26)

```typescript
// Question 13
{
  id: 13,
  section: 'leadership',
  text: 'When starting a new project or initiative, your first instinct is to:',
  type: 'radio',
  insight: {
    icon: '🎬',
    title: 'First Move Reveals Your Leadership DNA',
    content: 'Simon Sinek: "People don\'t buy what you do—they buy why you do it." Visionaries start with why. Architects start with how. Facilitators start with who. Executors start with what. Commanders start with when. Coaches start with questions.'
  },
  options: [
    { value: 'visionary', text: 'Paint an inspiring vision of what success could look like' },
    { value: 'architect', text: 'Map out the strategy, structure, and dependencies' },
    { value: 'facilitator', text: 'Bring everyone together to build alignment and clarity' },
    { value: 'executor', text: 'Identify quick wins and start executing immediately' },
    { value: 'commander', text: 'Define clear objectives, roles, and chain of command' },
    { value: 'coach', text: 'Ask powerful questions to help the team discover the path forward' }
  ]
}

// Question 14
{
  id: 14,
  section: 'leadership',
  text: 'During team conflicts, you naturally:',
  type: 'radio',
  insight: {
    icon: '⚔️',
    title: 'Conflict Response = Leadership Style Under Fire',
    content: 'Patrick Lencioni: "If you could get all the people in an organization rowing in the same direction, you could dominate any industry." Conflict reveals who steers the boat—and how.'
  },
  options: [
    { value: 'visionary', text: 'Reframe the conflict around shared purpose and bigger goals' },
    { value: 'architect', text: 'Analyze root causes and design better processes' },
    { value: 'facilitator', text: 'Create space for everyone to be heard and find common ground' },
    { value: 'executor', text: 'Push for quick resolution so the team can move forward' },
    { value: 'commander', text: 'Make the final call and expect alignment' },
    { value: 'coach', text: 'Help people work through it themselves with guided questions' }
  ]
}

// Question 15
{
  id: 15,
  section: 'leadership',
  text: 'What energizes you most at work?',
  type: 'radio',
  insight: {
    icon: '⚡',
    title: 'Energy Source = Your Leadership Fuel',
    content: 'Marcus Buckingham (StandOut): "Your strengths are not what you\'re good at—they\'re what strengthens you." What energizes you reveals your archetype. Chase that feeling.'
  },
  options: [
    { value: 'visionary', text: 'Brainstorming big ideas and exploring new possibilities' },
    { value: 'architect', text: 'Solving complex problems and designing elegant solutions' },
    { value: 'facilitator', text: 'Helping people connect, grow, and work well together' },
    { value: 'executor', text: 'Checking off completed tasks and hitting milestones' },
    { value: 'commander', text: 'Making tough decisions and winning against competition' },
    { value: 'coach', text: 'Watching people have breakthroughs and level up' }
  ]
}

// Question 16
{
  id: 16,
  section: 'leadership',
  text: 'How do you prefer to communicate important information?',
  type: 'radio',
  insight: {
    icon: '💬',
    title: 'Communication Style = Leadership Signature',
    content: 'Aristotle: "Persuasion has three pillars: Ethos (credibility), Pathos (emotion), Logos (logic)." Visionaries lean pathos. Architects lean logos. Facilitators balance all three.'
  },
  options: [
    { value: 'visionary', text: 'Through storytelling and painting compelling pictures' },
    { value: 'architect', text: 'With data, frameworks, and logical reasoning' },
    { value: 'facilitator', text: 'In dialogue, ensuring everyone understands and feels heard' },
    { value: 'executor', text: 'Clearly and concisely with specific action items' },
    { value: 'commander', text: 'Directly and decisively with clear expectations' },
    { value: 'coach', text: 'Through questions that help others discover insights' }
  ]
}

// Question 17
{
  id: 17,
  section: 'leadership',
  text: 'When facing a major obstacle, your approach is to:',
  type: 'radio',
  insight: {
    icon: '🧗',
    title: 'Obstacle Response Separates Leaders',
    content: 'Ryan Holiday (The Obstacle Is The Way): "The impediment to action advances action. What stands in the way becomes the way." Your archetype determines HOW you turn obstacles into opportunities.'
  },
  options: [
    { value: 'visionary', text: 'Reframe it as an opportunity and inspire creative solutions' },
    { value: 'architect', text: 'Break it down systematically and engineer a solution' },
    { value: 'facilitator', text: 'Rally the team to tackle it together' },
    { value: 'executor', text: 'Find the fastest path around or through it' },
    { value: 'commander', text: 'Take charge, make the tough calls, and push through' },
    { value: 'coach', text: 'Challenge your team to find the solution themselves' }
  ]
}

// Question 18
{
  id: 18,
  section: 'leadership',
  text: 'In meetings, you are most likely to:',
  type: 'radio',
  insight: {
    icon: '🎤',
    title: 'Meeting Behavior Reveals Default Mode',
    content: 'Amazon\'s "two-pizza rule" and Jeff Bezos\' silent memo reading show structure matters. But your natural behavior in meetings? That\'s your archetype showing.'
  },
  options: [
    { value: 'visionary', text: 'Share bold ideas and challenge conventional thinking' },
    { value: 'architect', text: 'Present frameworks and analytical insights' },
    { value: 'facilitator', text: 'Ensure everyone has a voice and the discussion stays productive' },
    { value: 'executor', text: 'Drive toward decisions and action items' },
    { value: 'commander', text: 'Take control and keep things on track' },
    { value: 'coach', text: 'Ask questions that deepen thinking and clarity' }
  ]
}

// Question 19
{
  id: 19,
  section: 'leadership',
  text: 'Your team would describe you as someone who:',
  type: 'radio',
  insight: {
    icon: '🎭',
    title: 'External Perception = Your Leadership Brand',
    content: 'How others see you matters. Your perceived strengths become your opportunities—or your limitations. Self-aware leaders know their brand and actively shape it. You can\'t be all things to all people. Own your archetype.'
  },
  options: [
    { value: 'visionary', text: 'Sees possibilities others miss and makes them feel achievable' },
    { value: 'architect', text: 'Thinks deeply and designs smart solutions to complex problems' },
    { value: 'facilitator', text: 'Creates connection, trust, and brings out everyone\'s best' },
    { value: 'executor', text: 'Gets things done no matter what obstacles appear' },
    { value: 'commander', text: 'Provides clear direction and holds high standards' },
    { value: 'coach', text: 'Develops people through powerful questions and feedback' }
  ]
}

// Question 20
{
  id: 20,
  section: 'leadership',
  text: 'What frustrates you most in a team setting?',
  type: 'radio',
  insight: {
    icon: '😤',
    title: 'Frustrations Reveal Values',
    content: 'What frustrates you most reveals what you value most. Visionaries cannot stand small thinking. Architects hate sloppy execution. Facilitators resist silos. Executors despise inaction. Commanders reject indiscipline. Coaches resent passivity. Your frustration is not a flaw—it is your value system speaking.'
  },
  options: [
    { value: 'visionary', text: 'Playing too small and settling for incremental improvements' },
    { value: 'architect', text: 'Sloppy thinking and poorly designed processes' },
    { value: 'facilitator', text: 'People not listening to each other or working in silos' },
    { value: 'executor', text: 'Endless discussion without decisions or action' },
    { value: 'commander', text: 'Lack of discipline, accountability, and follow-through' },
    { value: 'coach', text: 'People not taking ownership of their own development' }
  ]
}

// Question 21
{
  id: 21,
  section: 'leadership',
  text: 'When delegating work, you focus on:',
  type: 'radio',
  insight: {
    icon: '📋',
    title: 'Delegation = Leadership Leverage',
    content: 'How you delegate reveals how you scale. Visionaries delegate execution, not vision. Architects delegate tasks within systems. Facilitators delegate through strengths. Executors delegate with checkpoints. Commanders delegate with authority. Coaches delegate through questions. Elite leaders delegate the work—not the accountability.'
  },
  options: [
    { value: 'visionary', text: 'The \'why\' and desired impact, trusting the team on the \'how\'' },
    { value: 'architect', text: 'Clear frameworks and decision rights so people can operate independently' },
    { value: 'facilitator', text: 'Matching tasks to people\'s strengths and development goals' },
    { value: 'executor', text: 'Specific deliverables, deadlines, and accountability checkpoints' },
    { value: 'commander', text: 'Clear orders with expected outcomes and reporting structure' },
    { value: 'coach', text: 'Challenging questions that help them figure out their own path' }
  ]
}

// Question 22
{
  id: 22,
  section: 'leadership',
  text: 'Under pressure, you tend to:',
  type: 'radio',
  insight: {
    icon: '🔥',
    title: 'Pressure Reveals Your Default Mode',
    content: 'Crisis does not build leaders—it exposes them. Under pressure, you default to your archetype. Visionaries inspire through chaos. Architects impose order. Facilitators steady the ship. Executors accelerate action. Commanders seize control. Coaches develop resilience. Awareness transforms your reflex into a choice.'
  },
  options: [
    { value: 'visionary', text: 'Double down on the vision and inspire urgency' },
    { value: 'architect', text: 'Step back to analyze and redesign the approach' },
    { value: 'facilitator', text: 'Rally the team and ensure everyone\'s aligned and supported' },
    { value: 'executor', text: 'Go into high gear and drive execution relentlessly' },
    { value: 'commander', text: 'Take control, make decisive calls, and eliminate distractions' },
    { value: 'coach', text: 'Stay calm and help the team navigate through it together' }
  ]
}

// Question 23
{
  id: 23,
  section: 'leadership',
  text: 'Your ideal work environment is one where:',
  type: 'radio',
  insight: {
    icon: '🏢',
    title: 'Culture Eats Strategy',
    content: 'Peter Drucker\'s famous line holds true. Your ideal environment reveals the culture you create. Visionaries build innovation labs. Architects optimize operations. Facilitators foster safety. Executors demand results. Commanders enforce standards. Coaches develop people. You don\'t join a culture—you radiate one.'
  },
  options: [
    { value: 'visionary', text: 'Innovation and bold ideas are encouraged and celebrated' },
    { value: 'architect', text: 'Systems are clean, processes are optimized, and logic prevails' },
    { value: 'facilitator', text: 'People feel safe, valued, and work together seamlessly' },
    { value: 'executor', text: 'Goals are clear, momentum is high, and results come fast' },
    { value: 'commander', text: 'Standards are high, roles are clear, and everyone executes' },
    { value: 'coach', text: 'People are challenged to grow and take ownership' }
  ]
}

// Question 24
{
  id: 24,
  section: 'leadership',
  text: 'When giving feedback, you emphasize:',
  type: 'radio',
  insight: {
    icon: '💭',
    title: 'Feedback Is Leadership in Real-Time',
    content: 'Kim Scott (Radical Candor): The best feedback is caring personally while challenging directly. Visionaries connect to mission. Architects explain logic. Facilitators build confidence. Executors specify actions. Commanders set standards. Coaches ask questions. All can be radically candid—just in different languages.'
  },
  options: [
    { value: 'visionary', text: 'Connecting their work to the bigger mission and potential' },
    { value: 'architect', text: 'The logic and framework behind what works and what doesn\'t' },
    { value: 'facilitator', text: 'Their growth journey and building their confidence' },
    { value: 'executor', text: 'Specific behaviors to change and results to achieve' },
    { value: 'commander', text: 'Clear standards and where they need to step up' },
    { value: 'coach', text: 'Questions that help them discover their own insights' }
  ]
}

// Question 25
{
  id: 25,
  section: 'leadership',
  text: 'Success for you is best measured by:',
  type: 'radio',
  insight: {
    icon: '📊',
    title: 'Success Metrics Define You',
    content: 'What you measure reveals what you value. Visionaries track transformation. Architects measure scalability. Facilitators count developed leaders. Executors monitor results. Commanders track wins. Coaches measure growth. Your scorecard isn\'t neutral—it shapes behavior. Choose metrics that align with your archetype.'
  },
  options: [
    { value: 'visionary', text: 'Creating lasting impact and transformation' },
    { value: 'architect', text: 'Building systems that scale and endure' },
    { value: 'facilitator', text: 'Developing people and strengthening team capability' },
    { value: 'executor', text: 'Hitting targets and delivering tangible results' },
    { value: 'commander', text: 'Winning decisively and outperforming competition' },
    { value: 'coach', text: 'How many people you\'ve helped reach their potential' }
  ]
}

// Question 26
{
  id: 26,
  section: 'leadership',
  text: 'Your leadership superpower is:',
  type: 'radio',
  insight: {
    icon: '🦸',
    title: 'Own Your Superpower',
    content: 'Every archetype has a superpower. Visionaries see the future. Architects design systems. Facilitators build teams. Executors drive results. Commanders make tough calls. Coaches develop talent. Your superpower is not what you TRY to do—it\'s what comes naturally when you\'re at your best.'
  },
  options: [
    { value: 'visionary', text: 'Painting a compelling future people want to follow' },
    { value: 'architect', text: 'Designing smart solutions to complex challenges' },
    { value: 'facilitator', text: 'Bringing out the best in people and building great teams' },
    { value: 'executor', text: 'Turning strategy into reality through flawless execution' },
    { value: 'commander', text: 'Making tough calls and leading decisively in chaos' },
    { value: 'coach', text: 'Developing people who go on to do great things' }
  ]
}
```

### SECTION 3: TEAM DYNAMICS (Questions 27-46)

```typescript
// Questions 27-46: Team Dynamics (Scale 1-5)
// Based on Patrick Lencioni's 5 Dysfunctions of a Team

// TRUST (Questions 27-31)
{
  id: 27,
  section: 'team',
  text: 'Team members openly admit their mistakes and weaknesses',
  type: 'scale',
  dysfunction: 'trust',
  insight: {
    icon: '🛡️',
    title: 'Vulnerability = Foundation of Trust',
    content: 'Brené Brown: "Vulnerability is not weakness. It\'s our greatest measure of courage." Teams that hide mistakes compound them. Teams that admit mistakes fix them fast.'
  }
}

{
  id: 28,
  section: 'team',
  text: 'People ask for help without hesitation',
  type: 'scale',
  dysfunction: 'trust',
  insight: {
    icon: '🤝',
    title: 'Asking for Help = Sign of Strength',
    content: 'In dysfunctional teams, asking for help is weakness. In high-performing teams, NOT asking for help is selfish. Which team are you on?'
  }
}

{
  id: 29,
  section: 'team',
  text: 'Team members give each other benefit of the doubt',
  type: 'scale',
  dysfunction: 'trust',
  insight: {
    icon: '💭',
    title: 'Assumptions Kill Teams',
    content: 'When trust is low, you assume the worst. When trust is high, you assume the best. This single shift changes everything.'
  }
}

{
  id: 30,
  section: 'team',
  text: 'People apologize quickly and genuinely when they mess up',
  type: 'scale',
  dysfunction: 'trust',
  insight: {
    icon: '🙏',
    title: 'Apology Culture = Accountability Culture',
    content: 'Teams that apologize quickly move faster. Teams that hide mistakes compound them. Fast apologies = fast learning = fast improvement.'
  }
}

{
  id: 31,
  section: 'team',
  text: 'Team meetings include passionate, unfiltered debate',
  type: 'scale',
  dysfunction: 'conflict',
  insight: {
    icon: '⚡',
    title: 'Conflict is Productive (When Done Right)',
    content: 'Artificial harmony is the enemy of truth. Great teams engage in fierce ideological debate—while maintaining personal respect. Conflict around ideas, not people.'
  }
}

// CONFLICT (Questions 32-35)
{
  id: 32,
  section: 'team',
  text: 'People voice disagreements during meetings (not after)',
  type: 'scale',
  dysfunction: 'conflict',
  insight: {
    icon: '🎤',
    title: 'Real-Time Dissent > Hallway Complaints',
    content: 'The most toxic phrase in business: "I didn\'t want to say anything in the meeting, but..." Great teams hash it out in the room, then commit.'
  }
}

{
  id: 33,
  section: 'team',
  text: 'Conflicts get resolved quickly and cleanly',
  type: 'scale',
  dysfunction: 'conflict',
  insight: {
    icon: '⚖️',
    title: 'Fast Resolution = High Performance',
    content: 'Unresolved conflict festers and spreads. Elite teams address tensions immediately—no passive-aggressive lingering. Clear the air, move forward.'
  }
}

{
  id: 34,
  section: 'team',
  text: 'Team members challenge each other\'s ideas respectfully',
  type: 'scale',
  dysfunction: 'conflict',
  insight: {
    icon: '🥊',
    title: 'Challenge Ideas, Not People',
    content: 'Ray Dalio (Bridgewater): "Thoughtful disagreement is the engine of excellence." Attack the idea with logic. Respect the person always. This distinction changes everything.'
  }
}

{
  id: 35,
  section: 'team',
  text: 'Decisions are made with clarity and buy-in from everyone',
  type: 'scale',
  dysfunction: 'commitment',
  insight: {
    icon: '✅',
    title: 'Commitment Requires Clarity',
    content: 'Ambiguous decisions create confusion and excuses. Great leaders ensure: (1) What was decided? (2) Who owns it? (3) By when? Clarity enables commitment.'
  }
}

// COMMITMENT (Questions 36-38)
{
  id: 36,
  section: 'team',
  text: 'Once a decision is made, everyone commits—even if they initially disagreed',
  type: 'scale',
  dysfunction: 'commitment',
  insight: {
    icon: '🤝',
    title: 'Disagree and Commit',
    content: 'Jeff Bezos: "Have backbone; disagree and commit." You can fight hard in the debate, but once the decision is made—you\'re all in. No sabotage, no passive resistance.'
  }
}

{
  id: 37,
  section: 'team',
  text: 'Team goals are more important than individual agendas',
  type: 'scale',
  dysfunction: 'commitment',
  insight: {
    icon: '🎯',
    title: 'Collective Goals > Individual Glory',
    content: 'The best teams subordinate ego to mission. Individual wins that hurt the team are celebrated in dysfunctional cultures, punished in elite ones.'
  }
}

{
  id: 38,
  section: 'team',
  text: 'People follow through on commitments without being reminded',
  type: 'scale',
  dysfunction: 'accountability',
  insight: {
    icon: '📋',
    title: 'Accountability = Keeping Commitments',
    content: 'Low-accountability teams need constant follow-up. High-accountability teams self-police. When you commit in front of peers, you deliver—or explain why not.'
  }
}

// ACCOUNTABILITY (Questions 39-42)
{
  id: 39,
  section: 'team',
  text: 'Team members hold each other accountable (not just the leader)',
  type: 'scale',
  dysfunction: 'accountability',
  insight: {
    icon: '👥',
    title: 'Peer Accountability > Top-Down Control',
    content: 'In great teams, peers hold each other to high standards—not just the boss. When the team owns the standard, performance skyrockets.'
  }
}

{
  id: 40,
  section: 'team',
  text: 'Poor performers are confronted directly and quickly',
  type: 'scale',
  dysfunction: 'accountability',
  insight: {
    icon: '🚨',
    title: 'Fast Feedback = Fast Improvement',
    content: 'Letting poor performance linger destroys team morale. Great teams address it immediately—with candor and support. Tolerating mediocrity is choosing it.'
  }
}

{
  id: 41,
  section: 'team',
  text: 'People are willing to make personal sacrifices for team success',
  type: 'scale',
  dysfunction: 'accountability',
  insight: {
    icon: '🏆',
    title: 'Sacrifice = Commitment Test',
    content: 'When the stakes are high, are people willing to stay late, take on extra work, or shift priorities? Great teams do this naturally because mission > comfort.'
  }
}

{
  id: 42,
  section: 'team',
  text: 'Team members celebrate each other\'s successes',
  type: 'scale',
  dysfunction: 'results',
  insight: {
    icon: '🎉',
    title: 'Celebrate Wins, Share Success',
    content: 'Toxic teams downplay others\' wins. Great teams amplify them. Recognition culture compounds success. What gets celebrated gets repeated.'
  }
}

// RESULTS (Questions 43-46)
{
  id: 43,
  section: 'team',
  text: 'Results and outcomes are prioritized over politics and process',
  type: 'scale',
  dysfunction: 'results',
  insight: {
    icon: '📈',
    title: 'Results > Politics',
    content: 'Dysfunctional teams optimize for looking good. High-performing teams optimize for being good. Process serves results—not the other way around.'
  }
}

{
  id: 44,
  section: 'team',
  text: 'The team regularly reviews performance and adjusts strategy',
  type: 'scale',
  dysfunction: 'results',
  insight: {
    icon: '🔄',
    title: 'Review, Reflect, Improve',
    content: 'Great teams treat performance reviews as learning sessions, not report cards. What worked? What didn\'t? What do we change? Continuous improvement is the standard.'
  }
}

{
  id: 45,
  section: 'team',
  text: 'Success is defined by achieving collective goals, not individual metrics',
  type: 'scale',
  dysfunction: 'results',
  insight: {
    icon: '🎖️',
    title: 'Team Wins > Individual Stats',
    content: 'Phil Jackson (11 NBA championships): "The strength of the team is each individual member. The strength of each member is the team." Collective success compounds individual growth.'
  }
}

{
  id: 46,
  section: 'team',
  text: 'The team has a shared sense of purpose that drives daily work',
  type: 'scale',
  dysfunction: 'results',
  insight: {
    icon: '🧭',
    title: 'Purpose = North Star',
    content: 'Simon Sinek: "People don\'t buy what you do—they buy WHY you do it." Teams without shared purpose drift. Teams with clear purpose dominate.'
  }
}
```

---

# QUICK ASSESSMENTS

## 1. Mental Wellness Baseline (8 questions)

```typescript
const mentalWellnessQuestions = [
  {
    id: 1,
    text: 'I feel energized and ready to tackle my day when I wake up',
    scale: '1-5' // Strongly Disagree to Strongly Agree
  },
  {
    id: 2,
    text: 'I\'m sleeping well and waking up refreshed most mornings'
  },
  {
    id: 3,
    text: 'My stress levels feel manageable right now'
  },
  {
    id: 4,
    text: 'I have consistent energy throughout the day without major crashes'
  },
  {
    id: 5,
    text: 'I feel mentally clear and focused during work'
  },
  {
    id: 6,
    text: 'I\'m able to disconnect from work stress in my personal time'
  },
  {
    id: 7,
    text: 'I feel emotionally balanced and resilient this week'
  },
  {
    id: 8,
    text: 'I\'m taking care of my physical health (movement, nutrition, rest)'
  }
];

// Scoring
const mentalWellnessResults = {
  high: {
    range: '32-40',
    title: 'High Wellness',
    description: 'You\'re in a strong mental wellness zone. Your energy, sleep, and stress management are working well. Keep up your current practices and use this as your baseline.',
    action: 'Focus on maintaining these habits and doubling down on what\'s working.'
  },
  medium: {
    range: '20-31',
    title: 'Medium Wellness',
    description: 'You\'re functioning but showing signs of strain. Some areas need attention before they become bigger issues.',
    action: 'Identify your lowest-scoring questions and create a 1-2 week action plan. Consider scheduling recovery time and reassessing boundaries.'
  },
  low: {
    range: '8-19',
    title: 'Low Wellness',
    description: 'You\'re running on fumes. Immediate action needed. This isn\'t sustainable.',
    action: 'Schedule a conversation with your manager about workload. Prioritize sleep, movement, and recovery this week. Consider professional support if this persists.'
  }
};
```

## 2. Work-Life Balance (8 questions)

```typescript
const workLifeBalanceQuestions = [
  {
    id: 1,
    text: 'I have clear boundaries between my work time and personal time'
  },
  {
    id: 2,
    text: 'I regularly take breaks during the workday to recharge'
  },
  {
    id: 3,
    text: 'I feel comfortable saying "no" to requests that would overextend me'
  },
  {
    id: 4,
    text: 'I have time each week for activities that energize me outside of work'
  },
  {
    id: 5,
    text: 'I\'m able to fully disconnect from work during evenings and weekends'
  },
  {
    id: 6,
    text: 'My personal relationships are getting the attention they deserve'
  },
  {
    id: 7,
    text: 'I make time for physical movement or exercise most weeks'
  },
  {
    id: 8,
    text: 'I prioritize recovery and rest without feeling guilty about it'
  }
];

const workLifeBalanceResults = {
  high: {
    range: '32-40',
    title: 'Strong Balance',
    description: 'You\'ve built sustainable boundaries and integration between work and life. You understand that balance isn\'t 50/50 every day—it\'s about intentional choices and recovery cycles.',
    action: 'Your challenge: help others on your team build this same foundation.'
  },
  medium: {
    range: '20-31',
    title: 'Moderate Balance',
    description: 'You\'re aware of balance but struggle to protect it consistently. Work often bleeds into personal time, or you feel guilty about disconnecting.',
    action: 'Focus on one boundary to strengthen this month. Start small: pick one evening to fully unplug, or block 30 minutes daily for non-work activities.'
  },
  low: {
    range: '8-19',
    title: 'Poor Balance',
    description: 'Work is consuming your life. You\'re in reactive mode with little control over your time. This pattern leads to burnout.',
    action: '(1) Audit your calendar—what can be delegated, declined, or shortened? (2) Block sacred personal time like a client meeting. (3) Have a direct conversation about workload sustainability.'
  }
};
```

## 3. Communication Style (10 questions)

```typescript
const communicationStyleQuestions = [
  {
    id: 1,
    text: 'I prefer to get straight to the point in conversations without much small talk',
    styles: { direct: +2, diplomatic: -1 }
  },
  {
    id: 2,
    text: 'I think out loud and often process ideas by talking them through with others',
    styles: { expressive: +2 }
  },
  {
    id: 3,
    text: 'I prefer written communication (email, Slack) over verbal conversations when possible',
    styles: { analytical: +2, expressive: -1 }
  },
  {
    id: 4,
    text: 'I focus heavily on data, logic, and evidence when making my case',
    styles: { analytical: +2 }
  },
  {
    id: 5,
    text: 'I\'m comfortable with direct, candid feedback even if it might create tension',
    styles: { direct: +2, diplomatic: -1 }
  },
  {
    id: 6,
    text: 'I prioritize maintaining harmony and positive relationships in conversations',
    styles: { diplomatic: +2, direct: -1 }
  },
  {
    id: 7,
    text: 'I take time to carefully choose my words before speaking in meetings',
    styles: { analytical: +1, diplomatic: +1 }
  },
  {
    id: 8,
    text: 'I express enthusiasm and emotion openly when communicating',
    styles: { expressive: +2, analytical: -1 }
  },
  {
    id: 9,
    text: 'I ask lots of questions to fully understand before forming opinions',
    styles: { analytical: +2 }
  },
  {
    id: 10,
    text: 'I adapt my communication style based on who I\'m talking to',
    styles: { diplomatic: +2, expressive: +1 }
  }
];

const communicationResults = {
  direct: {
    title: 'Direct Communicator',
    description: 'You value clarity, efficiency, and candor. You say what you mean and appreciate when others do the same.',
    strengths: 'Clear expectations, fast decisions, no confusion',
    watchOut: 'Coming across as blunt or insensitive',
    growthTip: 'Add context before delivering direct messages—explain the "why" to build buy-in.'
  },
  diplomatic: {
    title: 'Diplomatic Communicator',
    description: 'You prioritize relationships and harmony. You\'re skilled at reading the room and adapting your approach.',
    strengths: 'Build trust, navigate conflict smoothly, inclusive',
    watchOut: 'Avoiding necessary tough conversations, being too indirect',
    growthTip: 'Practice "caring candor"—you can be kind AND direct simultaneously.'
  },
  analytical: {
    title: 'Analytical Communicator',
    description: 'You lead with logic, data, and thorough analysis. You prepare carefully and value precision.',
    strengths: 'Well-reasoned arguments, credibility, minimizes errors',
    watchOut: 'Over-analyzing, slowing decisions, missing emotional dynamics',
    growthTip: 'Balance data with storytelling—numbers + narrative = influence.'
  },
  expressive: {
    title: 'Expressive Communicator',
    description: 'You\'re animated, enthusiastic, and process externally. You connect emotionally and inspire energy.',
    strengths: 'Engaging, builds momentum, makes ideas feel exciting',
    watchOut: 'Dominating conversations, not listening enough, overwhelming introverts',
    growthTip: 'Practice "think, pause, speak"—create space for others to contribute.'
  }
};
```

---

# EXTENDED ASSESSMENTS

## 4. Leadership Style Assessment (12 questions)

Full questions in REMAINING-ASSESSMENTS.md - 5 styles:
- Visionary (Phil Jackson example)
- Coach (Gregg Popovich example)
- Democratic (Pete Carroll example)
- Pacesetting (Bill Belichick example)
- Commanding (Nick Saban example)

## 5. Decision Making Style (10 questions)

Full questions in REMAINING-ASSESSMENTS.md - 4 styles:
- Gut-Instinct (Magic Johnson example)
- Analytical (Bill Belichick example)
- Collaborative (Phil Jackson example)
- Decisive (Kobe Bryant example)

## 6. Values Discovery (12 rating + ranking)

Full questions in REMAINING-ASSESSMENTS.md - 10 value types:
- Achievement-Driven (Kobe Bryant)
- Growth-Focused (LeBron James)
- Freedom-Seeker (Anthony Bourdain)
- Connection-Oriented (Brené Brown)
- Impact-Driven (Bill Gates)
- Excellence-Obsessed (Steve Jobs)
- Balance-Seeker (Tim Ferriss)
- Adventure-Lover (Richard Branson)
- Security-Focused (Warren Buffett)
- Creative Innovator (Lin-Manuel Miranda)

---

# BELT SYSTEM CONTENT

## White Belt: Trust & Self-Awareness

**Focus:** Foundation of vulnerability  
**Lencioni Dysfunction:** Absence of Trust  
**BJJ Philosophy:** Fundamentals win fights

### Stripe 1: Identity & Work Style
- Worker Type Assessment (12 questions above)
- Work-Life Balance Assessment (8 questions above)
- Discover natural rhythms and patterns

### Stripe 2: Communication & Impact
- Communication Style Assessment (10 questions above)
- Understand how you naturally express and connect
- Team impact awareness

### Stripe 3: Values & Purpose
- Values Discovery Assessment (12 questions + ranking)
- Identify top 3 core values
- Align work with what matters

### Stripe 4: Mental Health Baseline
- Mental Wellness Assessment (8 questions above)
- Establish stress/energy baseline
- Create wellness tracking foundation

---

## Blue Belt: Productive Conflict

**Focus:** Healthy disagreement  
**Lencioni Dysfunction:** Fear of Conflict  
**BJJ Philosophy:** Sparring is learning

### Stripe 1: Constructive Debate
- Learn to engage in ideological conflict
- Separate ideas from people
- Practice real-time dissent

### Stripe 2: Feedback Mastery
- Give and receive radical candor
- Balance care with directness
- Create feedback loops

### Stripe 3: Difficult Conversations
- Navigate tension with skill
- Address issues in real-time
- Clear the air fast

### Stripe 4: Conflict Resolution
- Resolve disagreements cleanly
- Turn conflict into clarity
- Build post-conflict commitment

---

## Purple Belt: Team Alignment

**Focus:** Commitment and buy-in  
**Lencioni Dysfunction:** Lack of Commitment  
**BJJ Philosophy:** Timing is everything

### Stripe 1: Decision-Making Frameworks
- Decision Making Assessment (10 questions)
- Learn frameworks for clear, fast decisions
- Build decision velocity

### Stripe 2: Cascading Communication
- Communicate decisions clearly
- Ensure understanding across team
- Create alignment through clarity

### Stripe 3: Meeting Mastery
- Lead productive meetings
- Drive to decisions, not just discussion
- Create action from conversation

### Stripe 4: Strategic Alignment
- Align team on long-term vision
- Connect daily work to big picture
- Build shared purpose

---

## Brown Belt: Accountability & Standards

**Focus:** Peer accountability  
**Lencioni Dysfunction:** Avoidance of Accountability  
**BJJ Philosophy:** Teams without accountability are nice, but not effective

### Stripe 1: Peer-to-Peer Accountability
- Hold teammates accountable (not just boss)
- Create culture of follow-through
- Build self-policing teams

### Stripe 2: Performance Standards
- Define clear standards
- Address poor performance fast
- Raise the bar consistently

### Stripe 3: Commitment Tracking
- Track and review commitments
- Create accountability systems
- Measure what matters

### Stripe 4: Coaching for Performance
- Develop others through accountability
- Balance support with challenge
- Create ownership culture

---

## Black Belt: Results Over Ego

**Focus:** Collective results  
**Lencioni Dysfunction:** Inattention to Results  
**BJJ Philosophy:** The final level—mastery in service of the team

### Stripe 1: Results-Oriented Culture
- Prioritize outcomes over politics
- Focus on collective wins
- Measure team success

### Stripe 2: Strategic Execution
- Turn strategy into results
- Drive flawless execution
- Create momentum

### Stripe 3: Team Performance Review
- Regular retrospectives
- Adjust strategy based on results
- Continuous improvement mindset

### Stripe 4: Leadership Legacy
- Develop future leaders
- Build self-sustaining teams
- Create lasting impact

---

# GAMIFICATION DATA

## XP Rewards
- Quick Assessment (3 min): 100 XP
- Medium Assessment (5-7 min): 150 XP
- Long Assessment (10-15 min): 200 XP
- Stripe Completion: 250 XP
- Belt Assessment: 500 XP

## Levels (every 1000 XP)
- Level 1-5: Beginner
- Level 6-10: Intermediate
- Level 11-15: Advanced
- Level 16-20: Expert
- Level 21+: Master

## Achievements
- First Assessment: "Starting the Journey" (100 XP bonus)
- Complete White Belt: "Foundation Built" (500 XP bonus)
- 7-Day Streak: "Consistency Matters" (200 XP bonus)
- 30-Day Streak: "Discipline Over Motivation" (1000 XP bonus)
- All 46 Questions: "Complete Profile" (500 XP bonus)
- First Black Belt Stripe: "Advanced Practitioner" (1000 XP bonus)

## Open Mat Tools (Optional Practice)
- Box Breathing (5 min): 25 XP
- Morning Routine (5 min): 25 XP
- Energy Audit (10 min): 50 XP
- Weekly Review (15 min): 75 XP
- Decision Framework (20 min): 100 XP

---

# BELT ASSESSMENTS (75 SCENARIO QUESTIONS)
## 5 Dysfunctions of a Functional Team - Complete Question Bank

---

## ⚪ WHITE BELT ASSESSMENT: Vulnerability-Based Trust
**15 Scenario Questions | 80% Passing Score (12/15) | 500 XP Reward**

```typescript
const whiteBeltScenarios = [
  {
    id: 1,
    question: "A team member consistently avoids speaking up in meetings, even when they clearly have expertise on the topic being discussed.",
    options: [
      "Ignore it—some people are just quiet",
      "Call them out publicly to encourage participation",
      "Have a private conversation to understand their hesitation and create safety",
      "Assign them to present at the next meeting to force engagement"
    ],
    correct: 2, // Index of correct answer (0-based)
    correctLetter: 'C',
    explanation: "Building trust with avoiders requires private conversation and creating safety, not public pressure or forcing."
  },
  {
    id: 2,
    question: "In a meeting, two team members have a minor disagreement. Everyone else goes silent and the energy in the room shifts uncomfortably.",
    options: [
      "Change the subject to reduce tension",
      "Say: 'This is healthy—disagreement helps us make better decisions. Let's hear both perspectives.'",
      "Take the discussion offline to avoid discomfort",
      "Ask everyone to vote to resolve quickly"
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Normalizing productive disagreement in the moment builds trust. Avoiding it signals that conflict is dangerous."
  },
  {
    id: 3,
    question: "You made a significant mistake that affected your team's project timeline. The mistake hasn't been discovered yet.",
    options: [
      "Fix it quietly and hope no one notices",
      "Wait until someone asks about it, then explain",
      "Proactively share the mistake with your team, explain what happened, and outline your plan to address it",
      "Blame external factors to minimize personal impact"
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "Vulnerability-based trust requires proactive admission of mistakes. It's the 'vulnerability first move.'"
  },
  {
    id: 4,
    question: "During a Personal History exercise, one team member shares something deeply personal. Another team member tries to offer advice and 'fix' the situation.",
    options: [
      "Let it happen—they're trying to help",
      "Intervene gently: 'Thank you for sharing. Let's just listen without fixing right now.'",
      "Move quickly to the next person to avoid awkwardness",
      "Ask the group if anyone else has advice to give"
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Personal History requires listening only, no fixing. The facilitator must protect the space for vulnerability."
  },
  {
    id: 5,
    question: "Your team completed the 360° Trust Grid and discovered that two people have asymmetric trust—Person A trusts Person B (5/5), but Person B doesn't trust Person A (2/5).",
    options: [
      "Share the results publicly to create accountability",
      "Ignore it—trust will build naturally over time",
      "Facilitate a private conversation between them to surface and address the gap",
      "Remove Person B from the team for not being a team player"
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "Trust asymmetries require facilitated private conversation to understand and repair the gap."
  },
  {
    id: 6,
    question: "A new team member joins and immediately admits in their first meeting: 'I don't understand the technical details here—can someone explain?'",
    options: [
      "Quickly explain so they don't feel embarrassed",
      "Suggest they review documentation offline",
      "Thank them publicly for asking and provide a clear explanation, reinforcing that questions are welcome",
      "Ask if anyone else has questions to move on faster"
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "Publicly thanking vulnerability reinforces that admitting gaps is safe and valued."
  },
  {
    id: 7,
    question: "During a Trust Vulnerability Stack exercise, one team member says 'I'll pass' on sharing their struggle in Round 3.",
    options: [
      "Pressure them gently: 'Come on, everyone else shared'",
      "Respect the pass and move to the next person without comment or pressure",
      "Ask them privately after the meeting why they didn't share",
      "Make a note to address their lack of engagement later"
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Honoring passes without pressure is essential. Forced vulnerability destroys trust faster than silence."
  },
  {
    id: 8,
    question: "You notice that after team meetings, people have different 'side conversations' in Slack where they share opinions they didn't voice in the meeting.",
    options: [
      "Ban side conversations to force everything into meetings",
      "Join the side conversations to stay informed",
      "Address it directly: 'I'm noticing important conversations happening after meetings. Let's create space to have them during meetings.'",
      "Ignore it—people need to vent sometimes"
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "Side conversations signal lack of safety in meetings. Address the pattern directly to build trust."
  },
  {
    id: 9,
    question: "A team member violates confidentiality by sharing something personal that another team member disclosed during a trust exercise.",
    options: [
      "Address it privately with the violator only",
      "Ignore it to avoid further damage",
      "Have a direct conversation with the violator about impact, and potentially address it with the team to rebuild safety",
      "Remove the violator from future trust exercises"
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "Confidentiality breaches are trust ruptures that require direct addressing and potential public repair."
  },
  {
    id: 10,
    question: "Your leader asks in a meeting: 'What's one thing I could do better?' No one responds.",
    options: [
      "Break the silence by sharing your own feedback first as a peer",
      "Say 'You're doing great!' to fill the awkward silence",
      "Suggest people send feedback privately instead",
      "Wait silently until someone speaks"
    ],
    correct: 0,
    correctLetter: 'A',
    explanation: "The vulnerability first move—modeling by going first—creates safety for others to follow."
  },
  {
    id: 11,
    question: "During a Grip-Switch drill, one person is being overly aggressive and competitive rather than collaborative.",
    options: [
      "Let them work it out themselves",
      "Pause the exercise and remind everyone: 'This is about flow and trust, not winning. Let's reset.'",
      "Match their intensity to show them how it feels",
      "Exclude them from future physical exercises"
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Physical trust exercises require facilitation to maintain the collaborative intent, not competitive energy."
  },
  {
    id: 12,
    question: "Your team has built strong trust, but you're about to bring in three new team members. How do you maintain trust culture?",
    options: [
      "Expect new members to adapt to existing norms naturally",
      "Run Personal History and vulnerability exercises with the full team including new members within their first two weeks",
      "Have existing members explain the trust norms to new members",
      "Wait six months for new members to integrate before doing trust work"
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Onboarding new members requires intentional trust-building exercises, not assumption they'll adapt naturally."
  },
  {
    id: 13,
    question: "A team member approaches you privately with a concern about another team member's performance but asks you not to tell anyone.",
    options: [
      "Keep their confidence and address the performance issue yourself",
      "Say: 'I appreciate you sharing this. For us to address it, we need to involve the person directly. Can we do that together?'",
      "Share it with the other person but don't reveal the source",
      "Ignore it since it was shared in confidence"
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Triangulation destroys trust. Encourage direct communication while offering support."
  },
  {
    id: 14,
    question: "After implementing trust rituals (like weekly check-ins) for a month, some team members complain they feel 'forced' and 'performative.'",
    options: [
      "Stop the rituals—they're not working",
      "Make them optional to reduce pressure",
      "Acknowledge the feedback and ask: 'What would make this feel more genuine? Should we adjust the format?'",
      "Push through—resistance means it's working"
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "Rituals should be collaboratively designed and adjusted. Rigidity kills authenticity."
  },
  {
    id: 15,
    question: "You're facilitating a trust repair conversation between two people. Person A says 'I'm sorry if you felt hurt.' How do you respond?",
    options: [
      "Accept it and move on",
      "Say: 'Can you try that again without the 'if'? Take responsibility for impact, not just intent.'",
      "Let it go—at least they apologized",
      "Ask Person B if they accept the apology"
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "'Sorry if you felt' deflects responsibility. Real repair requires owning impact without conditions."
  }
];
```

---

## 🔵 BLUE BELT ASSESSMENT: Fear of Conflict
**15 Scenario Questions | 80% Passing Score (12/15) | 750 XP Reward**

```typescript
const blueBeltScenarios = [
  {
    id: 1,
    question: "Your team just wrapped a sprint planning meeting where everyone quickly agreed on an aggressive timeline. As you're leaving, you notice several engineers looking uncomfortable and whispering to each other. What should you do?",
    options: [
      "Nothing—they agreed in the meeting, so move forward with the timeline.",
      "Send a follow-up Slack asking if anyone has concerns about the timeline.",
      "Pull the team back and say 'I noticed some discomfort. Let's surface all concerns before we commit.'",
      "Talk to the uncomfortable engineers 1-on-1 to understand concerns, then bring the team back together if needed."
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "Mining for conflict in the moment prevents artificial harmony. Address the discomfort directly."
  },
  {
    id: 2,
    question: "Your team debated two product approaches for an hour. The majority wants Option A, but you strongly believe Option B is better. The CEO is making the final call and chooses Option A. What's the best response?",
    options: [
      "Tell the CEO you disagree and will need to be convinced before you can support it.",
      "Say 'I disagree but I'll commit. Here's how I'll support Option A moving forward.'",
      "Stay quiet publicly but tell your team privately that you think it's the wrong call.",
      "Ask to revisit the decision in two weeks after you gather more data to support Option B."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Disagree and commit is essential after healthy debate. Express disagreement, then full commitment."
  },
  {
    id: 3,
    question: "During a heated design review, you notice your heart racing, your face getting hot, and a strong urge to interrupt and prove someone wrong. What's the best first step?",
    options: [
      "Take three deep breaths, acknowledge internally that you're activated, then choose your response consciously.",
      "Interrupt immediately to make your point before you forget it.",
      "Excuse yourself from the meeting to cool down completely.",
      "Push through the discomfort and stay in the debate—conflict requires staying engaged."
    ],
    correct: 0,
    correctLetter: 'A',
    explanation: "Managing conflict physiology is critical. Breathe, acknowledge activation, then choose your response."
  },
  {
    id: 4,
    question: "You're facilitating a product roadmap discussion. Three people have spoken strongly in favor of Feature X. Four people haven't said anything yet. What's the best mining technique?",
    options: [
      "Move forward—silence usually means agreement.",
      "Say 'Let's hear from people who haven't spoken yet. Jordan, what do you think?'",
      "Assign someone to play devil's advocate and argue against Feature X.",
      "Pause and say 'This consensus came quickly. What concerns might we be missing about Feature X?'"
    ],
    correct: 3,
    correctLetter: 'D',
    explanation: "Mining requires surfacing unspoken concerns. Fast agreement is often artificial harmony."
  },
  {
    id: 5,
    question: "Two team members are in a heated debate about technical architecture. One person keeps interrupting the other, and the conversation is becoming personal ('You never listen to engineers!'). How do you intervene?",
    options: [
      "Let them work it out—they're both adults and can manage conflict themselves.",
      "Say 'Let's pause. We're debating ideas, not people. What's the core technical tradeoff we're trying to solve?'",
      "End the meeting immediately and send them both an email about professional conduct.",
      "Take sides with whoever has the better technical argument to resolve the conflict quickly."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Real-time facilitation redirects personal attacks back to ideas. Focus on the tradeoff, not the people."
  },
  {
    id: 6,
    question: "Product and Engineering are locked in disagreement about whether to prioritize new features or pay down tech debt. As the facilitator, what should you do first in the 7-step resolution process?",
    options: [
      "Ask both sides to surface their positions and debate until consensus emerges.",
      "Generate multiple options that blend both features and tech debt work.",
      "Define the decision method (who decides) and set time boundaries for the discussion.",
      "Explore the underlying interests driving each position (speed to market vs. system stability)."
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "The 7-step process starts with defining HOW you'll decide, not diving into content immediately."
  },
  {
    id: 7,
    question: "A team member comes to you: 'I can't work with Sarah anymore. She's blocking all my PRs with nitpicky comments.' What's the best coaching response?",
    options: [
      "Say 'Let me talk to Sarah and tell her to ease up on the reviews.'",
      "Ask 'What do you think Sarah cares about in those reviews? What do you care about? How could you talk to her about finding a balance?'",
      "Tell them to write cleaner code so Sarah won't have as many comments.",
      "Reassign them to different projects so they don't have to work together."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Coach them to handle conflict directly. Don't rescue or solve for them."
  },
  {
    id: 8,
    question: "The exec team must decide on layoffs (20% of staff). The CFO says it's necessary for survival. The CTO says it will kill critical projects. As CEO facilitating this, what principle matters most?",
    options: [
      "Move fast—in high-stakes conflicts, speed is essential to reduce uncertainty.",
      "Slow down to speed up—align on process (how we'll decide) before diving into content (what to decide).",
      "Take a vote so everyone feels their voice was heard equally.",
      "Bring in a neutral third-party consultant to make the decision for you."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "High-stakes conflict requires slowing down first. Process alignment prevents decisions from blowing up."
  },
  {
    id: 9,
    question: "Two engineers have different coding style preferences. One prefers functional programming, the other object-oriented. They're debating which to use. Where does this fall on the conflict continuum?",
    options: [
      "Destructive conflict—personal preferences shouldn't create disagreement.",
      "Productive conflict—they're debating technical tradeoffs that matter for code quality and maintainability.",
      "Artificial harmony—they should avoid this debate and just pick one standard.",
      "Mean-spirited conflict—they're attacking each other's competence."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Technical tradeoff debates are productive conflict—they should have this discussion."
  },
  {
    id: 10,
    question: "You avoided giving critical feedback to an underperforming team member because you didn't want to hurt their feelings. Three months later, their work quality has declined further and they're surprised when you bring it up. What happened?",
    options: [
      "The team member should have known they were underperforming without being told.",
      "Avoidance cascade—avoiding conflict created a bigger problem (performance gap + trust damage).",
      "You gave them enough time to self-correct, which was the right approach.",
      "The team member is at fault for not asking for feedback proactively."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Avoiding conflict creates avoidance cascades. Small issues become big problems plus damaged trust."
  }
];
```

## 🔵 BLUE BELT ASSESSMENT (continued - Questions 11-15)

```typescript
const blueBeltScenariospart2 = [
  {
    id: 11,
    question: "You're using Spar-&-Solve to debate two product directions with a colleague. You've both shared your positions and debated for 10 minutes. What comes next in the technique?",
    options: [
      "Keep debating until one person convinces the other they're right.",
      "Switch perspectives—you argue for their position, they argue for yours.",
      "Take a vote to decide which direction to pursue.",
      "End the debate and defer to whoever has more seniority."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Spar-&-Solve requires perspective switching to build empathy and find better solutions."
  },
  {
    id: 12,
    question: "Your team created a Conflict Norms Canvas three months ago, but no one references it anymore and people have fallen back into old patterns. What's the best fix?",
    options: [
      "The canvas didn't work—abandon it and try a different approach.",
      "Make the canvas visible in meetings and reference it when conflict happens: 'Remember we agreed to...'",
      "Remind the team about the canvas via email once a month.",
      "Blame the team for not following the norms they agreed to."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Norms must be actively reinforced. Make them visible and reference them in real-time."
  },
  {
    id: 13,
    question: "You're facilitating a conflict between a U.S. team member (direct communication culture) and a Japanese team member (indirect communication culture). The U.S. person says 'Why didn't you just say you disagreed in the meeting?' What should you do?",
    options: [
      "Tell the Japanese team member they need to adapt to U.S. norms since that's the company culture.",
      "Explain cultural differences to both, then create a hybrid process (open debate + 1-on-1 follow-ups).",
      "Tell the U.S. team member to be more sensitive and read between the lines better.",
      "Avoid addressing the cultural difference and focus only on the technical disagreement."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Cross-cultural conflict requires acknowledging differences and creating hybrid processes."
  },
  {
    id: 14,
    question: "You strongly disagree with your manager's decision to cut QA resources. Which is the most skillful way to express disagreement?",
    options: [
      "'I disagree with cutting QA. Here's my concern: we'll ship more bugs and damage customer trust. Can we discuss alternatives?'",
      "'That's a terrible idea. Every good engineering team knows QA is essential.'",
      "Say nothing in the meeting, then complain to your team about the bad decision.",
      "'I'm not sure that will work, but you're the manager so whatever you think is best.'"
    ],
    correct: 0,
    correctLetter: 'A',
    explanation: "Express disagreement with reasoning, impact, and openness to dialogue."
  },
  {
    id: 15,
    question: "Two teammates are debating whether to refactor legacy code. One says 'You always want to over-engineer everything because you can't ship fast.' The other responds 'You always cut corners because you don't care about quality.' What type of conflict is this?",
    options: [
      "Productive conflict—they're passionately debating an important technical tradeoff.",
      "Destructive conflict—they've shifted from debating the decision to attacking character and motives.",
      "Artificial harmony—they're avoiding the real disagreement about code quality standards.",
      "Healthy debate—strong language shows they care about getting the right answer."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Once conflict becomes about character ('you always...'), it's destructive. Redirect to ideas."
  }
];
```

---

## 🟣 PURPLE BELT ASSESSMENT: Lack of Commitment
**15 Scenario Questions | 80% Passing Score (12/15) | 1000 XP Reward**

```typescript
const purpleBeltScenarios = [
  {
    id: 1,
    question: "At the end of a planning meeting, your product manager says 'I'll try to get the designs done soon.' Two weeks later, nothing has happened. What's the core problem?",
    options: [
      "The PM is overwhelmed and needs capacity support.",
      "The commitment was too vague—'try,' 'soon,' and no specific deliverable creates no accountability.",
      "The PM doesn't care about the project enough to prioritize it.",
      "Two weeks isn't long enough to follow up—give them more time."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Vague commitments create no accountability. Needs: what, when, who, specific deliverable."
  },
  {
    id: 2,
    question: "Your team is behind on a major deliverable. Your best engineer says 'I can work this weekend to catch up.' What's the best response as their leader?",
    options: [
      "Thank them for the offer and let them work the weekend—shows commitment to the team.",
      "Say 'I appreciate the offer, but weekends are sacred. Let's look at what we can descope or push back instead.'",
      "Accept the offer only if everyone else on the team also works the weekend to be fair.",
      "Tell them to work the weekend but promise them comp time next month."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Protect sacred time. Descope or renegotiate instead of sacrificing sustainability."
  },
  {
    id: 3,
    question: "Which of these is the BEST example of a clear, actionable commitment?",
    options: [
      "'I'll work on the API integration this week.'",
      "'I'll ship the user authentication endpoints by Friday 5pm, with Swagger docs and unit tests at 80% coverage.'",
      "'I'll do my best to get the authentication stuff done soon.'",
      "'I'll make progress on authentication by end of week.'"
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Clear commitments: specific deliverable, deadline, definition of done."
  },
  {
    id: 4,
    question: "You've asked a team member three times to update the documentation. Each time they say 'sure' but nothing happens. What's the best next step?",
    options: [
      "Escalate to their manager—this is a performance issue.",
      "Do it yourself—it's faster than continuing to ask.",
      "Have a direct conversation: 'I've asked three times with no follow-through. What's blocking you? Do you have capacity? Is this unclear?'",
      "Stop asking—clearly documentation isn't a priority for them."
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "Address the pattern directly. Understand the blocker before escalating or doing it yourself."
  },
  {
    id: 5,
    question: "You committed to delivering a feature by Monday. On Thursday, you realize a critical dependency is blocked and you won't make the deadline. What should you do?",
    options: [
      "Work over the weekend to hit the Monday deadline—never break commitments.",
      "Wait until Monday to tell stakeholders you missed the deadline.",
      "Ship an incomplete version on Monday to technically meet the commitment.",
      "Renegotiate immediately on Thursday: 'The dependency is blocked. Here are three options with new timelines.'"
    ],
    correct: 3,
    correctLetter: 'D',
    explanation: "Renegotiate early when context changes. Communicate proactively, offer options."
  },
  {
    id: 6,
    question: "In your team's planning meeting, everyone commits to aggressive goals. Privately, several people tell you 'there's no way we'll hit those numbers.' What's the systemic problem?",
    options: [
      "People are lazy and don't want to work hard.",
      "Lack of psychological safety—people can't speak truth about capacity in public settings.",
      "The goals aren't aggressive enough—teams always sandbag estimates.",
      "People need better project management training to estimate accurately."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Public commitment without safety creates fake buy-in. Need psychological safety to speak truth."
  },
  {
    id: 7,
    question: "You want to build a culture where commitments are taken seriously. What's the most effective practice to implement?",
    options: [
      "Punish anyone who misses a deadline to create accountability.",
      "Make all commitments public in a shared tracker with specific 'What by When by Whom' details.",
      "Stop making any commitments—work is too unpredictable.",
      "Only allow leaders to make commitments—individual contributors can't be trusted."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Public commitments with clarity (what/when/who) create accountability without punishment."
  },
  {
    id: 8,
    question: "You're running at 110% capacity. Your manager asks if you can take on 'one more small thing.' You know it's not actually small. What's the best response?",
    options: [
      "Say yes—saying no makes you look uncommitted or lazy.",
      "Say 'I'm at capacity. Here's my current load. If this is priority, what should I drop or delay?'",
      "Say yes, then work nights and weekends to fit it in.",
      "Say yes, but do a mediocre job since you don't have time to do it well."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Capacity honesty requires transparency and trade-off discussion, not heroics or poor quality."
  },
  {
    id: 9,
    question: "You've told yourself for three weeks that you'll start exercising before work. Every morning you hit snooze and skip it. What's the integrity issue?",
    options: [
      "Personal commitments don't matter as much as professional ones—this isn't a real problem.",
      "You're lazy and just need more willpower.",
      "You're eroding self-trust by repeatedly breaking commitments to yourself, which affects all areas of leadership.",
      "Morning isn't the right time—just exercise whenever you feel like it."
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "Self-commitments matter. Breaking them erodes self-trust, which undermines all leadership."
  },
  {
    id: 10,
    question: "Your team constantly misses commitments because 'things come up.' What structural change would help most?",
    options: [
      "Fire the people who miss deadlines most often.",
      "Implement a weekly 'commitment review' where all promises are tracked and blockers are surfaced publicly.",
      "Stop making any commitments—work is too unpredictable.",
      "Hire a project manager to track everything for the team."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Commitment reviews create visibility and accountability systems. Make promises visible."
  },
  {
    id: 11,
    question: "A sales rep promises a client a custom feature by next week without consulting engineering. The client is excited. Engineering says it'll take six weeks minimum. What's your move as the engineering leader?",
    options: [
      "Crunch mode for a week—the client is counting on us now.",
      "Call the client immediately: 'Sales made a mistake. It'll be six weeks.' Then fix the internal process.",
      "Let sales deal with it—they made the promise, they can handle the consequences.",
      "Ship a half-finished version in a week, then iterate based on client feedback."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Renegotiate immediately with transparency. Fix the broken process to prevent future issues."
  },
  {
    id: 12,
    question: "A junior team member has missed three small commitments in a row (updating docs, responding to PRs, attending standups). How do you coach them?",
    options: [
      "Ignore it—they're junior and still learning.",
      "Put them on a performance improvement plan immediately.",
      "Say 'I've noticed a pattern. These seem small, but commitments are commitments. What's getting in the way? How can we set you up to follow through?'",
      "Stop giving them commitments to make—just do the work yourself."
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "Address patterns early. Commitments are commitments. Coach with curiosity and support."
  },
  {
    id: 13,
    question: "Your CEO asks you in a board meeting 'Can we launch this quarter?' You know it's technically possible but would require the team to work 70-hour weeks. What do you say?",
    options: [
      "'Yes, we can do it!' Don't make the CEO look bad in front of the board.",
      "'We can launch this quarter if the team works unsustainable hours. That's not a commitment I'll make. Here are sustainable alternatives.'",
      "'I'll check with the team and let you know after the meeting.'",
      "'We can launch a reduced-scope version this quarter. Full feature set will take one more quarter.'"
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Integrity under pressure means saying hard truths. Offer sustainable alternatives."
  },
  {
    id: 14,
    question: "As a leader, which behavior MOST powerfully signals that commitments matter in your culture?",
    options: [
      "Sending emails at 2am to show you work harder than everyone.",
      "Publicly calling out people who miss deadlines in team meetings.",
      "When you miss a commitment, immediately owning it publicly, explaining what happened, and renegotiating.",
      "Never missing any commitment, no matter the personal cost."
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "Model accountability by owning your misses publicly. Vulnerability + responsibility = culture."
  },
  {
    id: 15,
    question: "What's the paradox at the heart of high-commitment cultures?",
    options: [
      "The harder you push for commitments, the less people actually deliver.",
      "You build commitment culture by making it safe to say no and renegotiate, not by punishing broken promises.",
      "Commitments kill innovation because they reduce flexibility.",
      "Individual commitments matter less than team commitments."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "The commitment paradox: safety to say no creates MORE commitment, not less."
  }
];
```

---

## 🟤 BROWN BELT ASSESSMENT: Avoidance of Accountability
**15 Scenario Questions | 80% Passing Score (12/15) | 1500 XP Reward**

```typescript
const brownBeltScenarios = [
  {
    id: 1,
    question: "A team member missed a client deadline. It's been 48 hours. What's the accountability standard?",
    options: [
      "Wait a week to see if they bring it up themselves.",
      "Address it directly within 48 hours: 'You missed the Friday deadline. What happened?'",
      "Mention it casually in the next team meeting as a general reminder.",
      "Let it go this time—everyone misses deadlines occasionally."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Accountability requires speed. Address missed commitments within 48 hours, directly and specifically."
  },
  {
    id: 2,
    question: "You want your team to hold each other accountable, not just wait for you to do it. What's the most effective enabler?",
    options: [
      "Tell them they should feel empowered to call each other out.",
      "Publicly give permission and model it yourself: 'I want you to hold ME accountable too.'",
      "Create a 'feedback form' they can submit anonymously about each other.",
      "Reward people who call out accountability gaps."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Permission + modeling = peer accountability. Leaders must invite it and demonstrate vulnerability."
  },
  {
    id: 3,
    question: "You've coached a team member twice on the same performance issue. No improvement. What's the next accountability move?",
    options: [
      "Coach them a third time with more detail.",
      "Move to formal performance management with documented expectations and timeline.",
      "Let them go—they've had enough chances.",
      "Assign them different work that plays to their strengths."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "After coaching fails, move to performance management. Document, set timelines, escalate."
  },
  {
    id: 4,
    question: "A peer on another team isn't delivering their part of a cross-functional project. Your team is blocked. What do you do?",
    options: [
      "Complain to your manager and let them handle it.",
      "Go directly to the peer: 'We're blocked on X. What's the issue? How can I help?'",
      "Work around them and deliver what you can without their input.",
      "Escalate to their manager immediately."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Peer accountability starts with direct conversation. Escalate only after direct attempt fails."
  },
  {
    id: 5,
    question: "Your boss publicly committed to a strategy you don't think the team can execute. What's the accountable move?",
    options: [
      "Complain to your teammates that the boss is out of touch.",
      "Talk to your boss privately: 'You committed to X. I don't think we can deliver. Here's why.'",
      "Just try your best and let the strategy fail to prove your point.",
      "Go along publicly but slow-roll execution."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Hold your boss accountable through private, direct conversation. Managing up requires courage."
  },
  {
    id: 6,
    question: "Under pressure, you're about to compromise quality standards to hit a deadline. What's the accountable response?",
    options: [
      "Ship it and fix it later—deadlines matter more than perfection.",
      "Name the trade-off publicly: 'We can hit the date OR maintain quality. Which matters more?'",
      "Work extra hours to hit both the deadline and quality standards.",
      "Miss the deadline silently and hope no one notices."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Accountability means naming trade-offs explicitly, not hiding them or heroic overwork."
  },
  {
    id: 7,
    question: "You notice your team's public commitment board hasn't been updated in 2 weeks. People are making vague commitments like 'I'll work on the redesign.' What does this signal?",
    options: [
      "The board tool is bad, switch to a different tool.",
      "Early culture erosion—systems are decaying and specificity is disappearing.",
      "People are too busy for the board right now.",
      "You're micromanaging, let them work how they want."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Commitment boards decay quickly. Vague language + abandonment = culture erosion in progress."
  },
  {
    id: 8,
    question: "A project involving Engineering, Product, and Design fails to launch on time. Each team says they did their part but the other teams dropped the ball. What's the root accountability issue?",
    options: [
      "No single person was accountable for the whole outcome.",
      "The teams don't like each other.",
      "The deadline was unrealistic.",
      "Someone is lying about doing their part."
    ],
    correct: 0,
    correctLetter: 'A',
    explanation: "Diffused accountability = no accountability. Complex projects need one owner for the whole outcome."
  },
  {
    id: 9,
    question: "You committed to delivering a report by Friday. On Wednesday you realize it's going to take until Monday to do it well. What's the accountable response?",
    options: [
      "Work all weekend to hit Friday even if quality suffers.",
      "Message Wednesday: 'I committed to Friday, but I need until Monday to do this right. Does that work, or should I deliver partial version Friday?'",
      "Deliver Friday with a disclaimer: 'This is rushed, sorry.'",
      "Don't say anything Wednesday, deliver Monday, apologize then."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Renegotiate early with transparency and options. Don't surprise people or sacrifice quality silently."
  },
  {
    id: 10,
    question: "You want your team to make explicit public commitments. What's the most effective way to build this habit?",
    options: [
      "Send an email explaining why public commitments matter.",
      "Start every team meeting by stating your own crisp commitments first, then ask them for theirs.",
      "Require everyone to submit written commitments every Monday.",
      "Call out people who make vague commitments."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Model first. Go first with your own commitments, then invite theirs. Modeling beats mandating."
  },
  {
    id: 11,
    question: "A team member worked 50 hours this week and shipped on time, but the quality is poor and full of bugs. How do you address this?",
    options: [
      "Praise the effort: 'Thanks for working so hard!'",
      "Focus only on the outcome: 'The quality isn't acceptable.'",
      "Acknowledge effort AND address outcome: 'I see how hard you worked, and the quality still isn't where it needs to be. Let's figure out what went wrong.'",
      "Don't say anything—they're already stressed."
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "Acknowledge effort while holding outcome standard. Both matter. Don't choose between them."
  },
  {
    id: 12,
    question: "Three different people have missed the same type of deadline over the last 2 months. What does this pattern suggest?",
    options: [
      "You hired the wrong people.",
      "There's a systemic issue—unclear process, unrealistic timeline, or missing dependencies.",
      "People aren't trying hard enough.",
      "The team doesn't respect deadlines."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Patterns = system problems, not people problems. Fix the system before blaming individuals."
  },
  {
    id: 13,
    question: "Your boss committed to making a budget decision 3 weeks ago. You've followed up twice via email with no response. Your team is blocked. What's your best next step?",
    options: [
      "Send another follow-up email.",
      "Request a 15-minute meeting: 'My team is blocked on the budget decision. What's preventing it? Can I help move it forward?'",
      "Complain to your boss's boss.",
      "Make the decision yourself since they're not responding."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Managing up requires direct escalation with support offer. Email isn't working—switch channels."
  },
  {
    id: 14,
    question: "A team member proactively updated you that his Friday commitment would slip to Monday due to unexpected technical debt. How should you respond?",
    options: [
      "Express frustration about the delay.",
      "Say nothing—this should be normal behavior.",
      "Thank them for the early heads-up and adjust plans together—model that renegotiation is valued.",
      "Ask why they didn't plan better."
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "Celebrate early renegotiation. Reinforce the behavior you want—proactive communication."
  },
  {
    id: 15,
    question: "You need to address a pattern of missed commitments with a team member. What's the most important element of that conversation?",
    options: [
      "Making them feel bad so they change.",
      "Stating the facts, naming the impact, asking for their perspective, and agreeing on specific next actions.",
      "Giving them one more chance without specific expectations.",
      "Comparing them to better performers on the team."
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Accountability conversation structure: facts + impact + perspective + agreement on actions."
  }
];
```

---

## ⬛ BLACK BELT ASSESSMENT: Inattention to Results (Integration Test)
**15 Scenario Questions | 80% Passing Score (12/15) | 2500 XP Reward**

```typescript
const blackBeltScenarios = [
  {
    id: 1,
    question: "Your leadership team has been working together for 18 months. Meetings are polite and professional. People share updates but rarely ask each other for help. When you ask team members privately what they think of each other, you get carefully diplomatic answers. Last week, two leaders had a project conflict—instead of talking to each other, they both came to you separately. What is the ROOT dysfunction here?",
    options: [
      "Fear of Conflict - They need conflict training to address issues directly",
      "Absence of Trust - Without vulnerability-based trust, they can't have productive conflict",
      "Avoidance of Accountability - They should be holding each other accountable for direct communication",
      "Lack of Commitment - They need clearer decision-making processes"
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Polite = artificial. Coming to you instead of each other = no trust. Trust is the foundation."
  },
  {
    id: 2,
    question: "Your team has strong trust—people are vulnerable, admit mistakes, and ask for help freely. But in strategy meetings, when you present a major decision, everyone nods along. You explicitly ask 'What concerns do you have?' and get surface-level questions. The meeting ends with apparent agreement. Then, over the next week, you hear through the grapevine that several leaders have serious reservations they never voiced. What's the core issue?",
    options: [
      "Lack of Commitment - They're not truly bought in, so they're not speaking up",
      "Absence of Trust - Despite appearances, they still don't feel safe being honest",
      "Fear of Conflict - They trust you but haven't learned to engage in productive ideological debate",
      "Avoidance of Accountability - They should hold each other accountable for voicing concerns in the moment"
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "They have trust but can't engage in conflict. This is fear of conflict, not lack of trust."
  },
  {
    id: 3,
    question: "Your team has excellent trust and healthy conflict. Meetings are passionate—people challenge ideas freely and debate vigorously. The problem: debates go in circles. You discuss the same strategic questions meeting after meeting. Even when you think you've reached a decision, someone reopens the discussion two weeks later. Leaders leave meetings energized by the debate but unclear about what was actually decided. What dysfunction is present?",
    options: [
      "Fear of Conflict - They're actually avoiding making hard choices by staying in debate mode",
      "Avoidance of Accountability - No one is holding the team accountable to decisions",
      "Lack of Commitment - Without clarity and closure, they can't commit even after healthy debate",
      "Inattention to Results - They enjoy the debate more than they care about actual outcomes"
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "Good debate without closure = lack of commitment. Need decision methods and clarity."
  },
  {
    id: 4,
    question: "Your team commits clearly to decisions. Everyone leaves meetings knowing exactly what they own and when it's due. But when someone misses a deadline or delivers subpar work, their peers say nothing. Instead, they come to you privately: 'I don't want to throw them under the bus, but...' You end up being the only one who addresses performance issues, while team members watch from the sidelines. What's the primary dysfunction?",
    options: [
      "Absence of Trust - They don't trust each other enough to have hard conversations",
      "Lack of Commitment - They weren't truly committed to the standards, so they won't enforce them",
      "Avoidance of Accountability - They avoid peer-to-peer accountability, defaulting to leader-driven enforcement",
      "Inattention to Results - They care more about being liked than achieving team outcomes"
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "Clear commitments but no peer accountability = avoidance of accountability dysfunction."
  },
  {
    id: 5,
    question: "Your leadership team has all five elements working: high trust, healthy conflict, clear commitments, peer accountability, and results focus. You're crushing your primary metric. But in your weekly meetings, most of the time is spent on status updates about departmental activities. Each leader shares what their team accomplished, plans for next week, and current projects. The team's collective goal—growing annual recurring revenue by 25%—is mentioned briefly at the end. When you check mid-quarter, you're only at 8% growth, but everyone has been 'busy.' What dysfunction has emerged?",
    options: [
      "Lack of Commitment - They're not truly committed to the 25% goal",
      "Avoidance of Accountability - No one is being held accountable for the revenue target",
      "Inattention to Results - They're focused on individual/departmental activity instead of collective outcomes",
      "Fear of Conflict - They're avoiding the difficult conversation about being off track"
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "Activity ≠ Results. Busy ≠ Progress. This is classic inattention to results."
  },
  {
    id: 6,
    question: "During a strategy offsite, you run a trust-building exercise where leaders share personal histories and challenges. The energy in the room shifts—people open up, laugh, and connect. You feel optimistic. But the next day, when you discuss whether to sunset an underperforming product line, the debate lasts 15 minutes before someone suggests 'we should probably study this more' and everyone agrees to table it. This is the third time you've tabled this exact discussion. What's happening?",
    options: [
      "The trust exercise worked, but they need more time to develop conflict skills",
      "One exercise doesn't build real trust—they shared stories but not vulnerability about current weaknesses",
      "This is lack of commitment—they can't decide, so they keep delaying",
      "Inattention to results—they care more about keeping the product team happy than the business outcome"
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Surface trust ≠ real trust. One exercise doesn't overcome fear of conflict. Need ongoing work."
  },
  {
    id: 7,
    question: "After healthy debate, your team makes a clear decision: shift 30% of engineering resources from feature development to technical debt for Q2. Everyone verbally agrees. You document it. Two weeks later, the VP of Engineering is still allocating resources the old way. When you ask why, they say 'I support the decision in principle, but the timing isn't right—we have customer commitments.' Other leaders nod sympathetically. No one challenges this. What dysfunctions are at play?",
    options: [
      "Only lack of commitment—the VP never truly bought in to the decision",
      "Only avoidance of accountability—peers should call out the VP for not following through",
      "Both—the VP lacked true commitment, AND peers are avoiding accountability by staying silent",
      "Inattention to results—they're prioritizing short-term feature delivery over long-term system health"
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "Multiple dysfunctions cascade together. Lack of commitment + avoidance of accountability."
  },
  {
    id: 8,
    question: "Your VP of Sales consistently hits targets, runs tight meetings, and gives polished presentations. But in leadership team meetings, they never ask for help, never admit uncertainty, and deflect any suggestion that something in their area needs improvement. When their team has a major customer churn issue, they present it as 'handled' before anyone even knew it happened. Other leaders are starting to do the same—everyone projects competence and control. What's the core issue?",
    options: [
      "Avoidance of accountability—no one is holding them accountable for transparency",
      "Absence of trust—they're protecting their image instead of being vulnerable about weaknesses",
      "This is actually good—high performers should solve problems independently",
      "Fear of conflict—they're avoiding difficult conversations about the churn issue"
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Invulnerability = no trust. Leaders protecting image prevents real team function."
  },
  {
    id: 9,
    question: "You're presenting a major pivot in product strategy. The room is quiet as you lay out the plan. You ask 'What are your concerns?' Silence. You ask again, 'Does anyone disagree with this direction?' More silence. You move forward. Three weeks later, the CFO mentions in a 1-on-1 that they think the financial assumptions are flawed. When you ask why they didn't say this in the meeting, they respond: 'I wasn't sure. I didn't want to derail things if I was wrong.' What's the root problem?",
    options: [
      "Absence of trust—the CFO doesn't feel safe being wrong in front of peers",
      "Fear of conflict—you haven't created permission and expectation for real-time debate",
      "Lack of commitment—the CFO isn't committed to the strategy so they're staying quiet",
      "This is normal—not everyone has concerns to share in every meeting"
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Silence after asking for concerns = fear of conflict. Need to mine and create permission."
  },
  {
    id: 10,
    question: "After a vigorous 90-minute debate about entering a new market, the team is split. You have strong proponents on both sides who've made compelling cases. As CEO, you make the final call: 'We're going in. I know not everyone agrees, but this is the decision.' Leaders nod. You ask each person to verbally commit. They all say 'yes.' But over the next month, you notice the leaders who disagreed aren't allocating resources, aren't talking about the new market in their team meetings, and aren't adjusting their plans. What's missing?",
    options: [
      "Avoidance of accountability—you need to hold them accountable for follow-through",
      "Lack of commitment—they said yes but never truly bought in to disagree and commit",
      "Fear of conflict—they're afraid to say they won't support the decision",
      "Your decision-making process was flawed—you should have built more consensus"
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Verbal 'yes' ≠ real commitment. Disagree and commit requires genuine buy-in, not compliance."
  },
  {
    id: 11,
    question: "Your leadership team has made real progress: they share vulnerabilities in meetings, debate decisions vigorously, make clear commitments, and call each other out when someone misses a deadline. But you've noticed something troubling—in quarterly business reviews, no one asks about the company's strategic objectives. Instead, each leader presents their function's achievements: 'We shipped 12 features,' 'We hired 8 people,' 'We cut costs by 15%.' These are all good things, but no one connects them to revenue growth, customer retention, or market position. What's the dysfunction?",
    options: [
      "This isn't a dysfunction—functional excellence is what drives company results",
      "Avoidance of accountability—they're not holding each other accountable for strategic outcomes",
      "Inattention to results—they're focused on their own functional wins rather than collective business outcomes",
      "Lack of commitment—they haven't truly committed to the company's strategic goals"
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "Functional wins ≠ company results. Top of the pyramid: collective outcomes over individual status."
  },
  {
    id: 12,
    question: "You're leading a team through intense pressure—a major product deadline, a key customer threatening to leave, and two executives on medical leave. In this crisis, you notice behavior regressing: people who used to debate now stay quiet and agree quickly. Leaders who used to ask for help now solve everything alone. Commitments that used to be specific are now vague ('we'll figure it out'). Team members who used to call each other out now let things slide. What's the right diagnosis?",
    options: [
      "Under pressure, teams naturally fall back to old dysfunction patterns—need to reinforce all five behaviors",
      "This is normal crisis behavior—focus on results first, culture later",
      "Only fear of conflict is showing up—people are avoiding debate to save time",
      "This is poor leadership—you should have prepared them better for pressure"
    ],
    correct: 0,
    correctLetter: 'A',
    explanation: "Pressure reveals foundation. Dysfunctions resurface under stress. Need deliberate reinforcement."
  },
  {
    id: 13,
    question: "As a new leader joining a company, you observe the following in your first 30 days: (1) Team meetings are polite and efficient—no one interrupts or disagrees. (2) After meetings, people huddle in hallways to discuss what they 'really think.' (3) Decisions take weeks because consensus is required. (4) When projects fail, blame is diffused ('market conditions,' 'bad timing'). (5) People celebrate activity metrics (emails sent, meetings held) rather than outcomes. If you could only fix ONE dysfunction first, which creates the fastest cascade of improvement?",
    options: [
      "Start with accountability—if people face consequences, behavior will change quickly",
      "Start with results orientation—if you focus everyone on outcomes, the rest will follow",
      "Start with trust—vulnerability is the foundation that enables all other behaviors",
      "Start with conflict—teach people to debate in meetings so they stop hallway conversations"
    ],
    correct: 2,
    correctLetter: 'C',
    explanation: "Pyramid builds from bottom. Trust enables conflict enables commitment enables accountability enables results."
  },
  {
    id: 14,
    question: "Your leadership team has been working together for two years. You've done trust exercises, conflict training, commitment protocols, accountability frameworks, and results tracking. The team functions well—until you promote a new VP from within. Within weeks, you notice: the team reverts to politeness in meetings, avoids giving the new VP direct feedback, and discusses concerns about them privately rather than openly. The new VP, sensing something is off, becomes defensive and overly formal. What's the issue?",
    options: [
      "The new VP lacks trust-building skills—they need coaching",
      "Trust isn't transferable—the team needs to rebuild the foundation with the new member",
      "This is normal adjustment—give it time and things will settle",
      "The team is avoiding accountability—they should address the new VP's performance directly"
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Trust is relational, not transferable. New member = restart trust-building. Can't skip the foundation."
  },
  {
    id: 15,
    question: "You're coaching a CEO who says: 'My team is high-performing. We have healthy debate, clear decisions, strong accountability, and we hit our numbers. But I feel like something is missing. People are professional and competent, but there's no real... connection. No one admits when they're struggling. No one asks for help. It all feels a bit sterile.' They ask: 'Is this just the reality of executive teams, or can we do better?' What's your answer?",
    options: [
      "This is normal for executive teams—professional distance maintains authority and respect",
      "They're missing the foundation—without vulnerability-based trust, high performance has a ceiling",
      "This is inattention to results—they're prioritizing individual image over collective outcomes",
      "This is good enough—competence and results matter more than emotional connection"
    ],
    correct: 1,
    correctLetter: 'B',
    explanation: "Competent ≠ cohesive. High-functioning ≠ high-performing. Without trust foundation, the ceiling is lower than you think."
  }
];
```

---

## 🎯 FOR CURSOR CLAUDE:

**Copy each section as needed:**
1. Use the 46 questions exactly as formatted
2. All insights are included—don't create new ones
3. Assessment scoring rubrics are defined
4. Belt structure is complete
5. XP/gamification values are set

**Need more detail on a specific section? Ask!**
