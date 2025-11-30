#!/usr/bin/env python3
"""
Add empty states for new users and achievements
"""

from pathlib import Path
import re

def add_empty_states(content):
    """Add empty state components"""
    
    empty_state_css = '''
/* Empty States */
.empty-state {
    text-align: center;
    padding: 3rem 2rem;
    color: rgba(255, 255, 255, 0.6);
}

.empty-state-icon {
    font-size: 4rem;
    margin-bottom: 1rem;
    opacity: 0.5;
}

.empty-state-title {
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: rgba(255, 255, 255, 0.8);
}

.empty-state-description {
    font-size: 1rem;
    margin-bottom: 1.5rem;
    max-width: 500px;
    margin-left: auto;
    margin-right: auto;
}

.empty-state-action {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    background: #6366f1;
    color: white;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    transition: background 0.2s;
}

.empty-state-action:hover {
    background: #4f46e5;
}
'''
    
    empty_state_html = '''
<!-- Empty State Template (for achievements) -->
<div id="empty-achievements" class="empty-state" style="display: none;">
    <div class="empty-state-icon">🏆</div>
    <div class="empty-state-title">No Achievements Yet</div>
    <div class="empty-state-description">
        Start your leadership journey to unlock achievements and track your progress!
    </div>
    <a href="/gym-dashboard.html" class="empty-state-action">Start Training</a>
</div>

<!-- Empty State Template (for progress) -->
<div id="empty-progress" class="empty-state" style="display: none;">
    <div class="empty-state-icon">📊</div>
    <div class="empty-state-title">Welcome to TAP-IN!</div>
    <div class="empty-state-description">
        Begin your leadership development journey. Complete your first assessment or start a belt stripe to see your progress here.
    </div>
    <a href="/belt-assessment-v2.html" class="empty-state-action">Take Assessment</a>
</div>
'''
    
    changes = []
    
    # Add CSS if not present
    if '.empty-state' not in content:
        style_pattern = r'(</style>)'
        if re.search(style_pattern, content):
            content = re.sub(style_pattern, empty_state_css + r'\1', content, count=1)
            changes.append("empty state CSS")
        elif '</head>' in content:
            style_tag = f'<style>{empty_state_css}</style>'
            content = re.sub(r'(</head>)', style_tag + r'\1', content, count=1)
            changes.append("empty state CSS")
    
    # Add HTML templates if not present
    if 'empty-achievements' not in content and 'empty-progress' not in content:
        body_pattern = r'(<main[^>]*>|<div[^>]*class="[^"]*main[^"]*"[^>]*>)'
        if re.search(body_pattern, content):
            content = re.sub(body_pattern, r'\1\n    ' + empty_state_html, content, count=1)
            changes.append("empty state HTML")
        elif '</body>' in content:
            content = re.sub(r'(</body>)', empty_state_html + '\n\1', content, count=1)
            changes.append("empty state HTML")
    
    return content, len(changes) > 0

def main():
    print("=" * 80)
    print("📭 ADDING EMPTY STATES")
    print("=" * 80)
    print()
    
    files_to_update = [
        'gym-dashboard.html',
        'achievements.html',
    ]
    
    updated = 0
    
    for filename in files_to_update:
        filepath = Path(filename)
        if not filepath.exists():
            print(f"⚠️  {filename} - File not found, skipping")
            continue
        
        print(f"📝 {filename}...")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            content, changed = add_empty_states(content)
            
            if changed:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated += 1
                print(f"  ✅ Added empty states")
            else:
                print(f"  ⏭️  Already has empty states")
        except Exception as e:
            print(f"  ❌ Error: {e}")
        print()
    
    print("=" * 80)
    print(f"✅ Updated: {updated}/{len(files_to_update)}")
    print("=" * 80)

if __name__ == '__main__':
    main()

