-- Migration: Backend Sync for User Progress
-- Creates tables for syncing belt progress, XP, and stats across devices

-- Enable UUID extension if not exists
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table 1: User Progress (Main progress tracking)
CREATE TABLE IF NOT EXISTS user_progress (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID UNIQUE NOT NULL,
    total_xp INTEGER DEFAULT 0,
    current_belt TEXT DEFAULT 'white',
    current_stripe INTEGER DEFAULT 1,
    streak_count INTEGER DEFAULT 0,
    longest_streak INTEGER DEFAULT 0,
    last_activity TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Additional stats
    total_lessons_completed INTEGER DEFAULT 0,
    total_stripes_earned INTEGER DEFAULT 0,
    total_belts_earned INTEGER DEFAULT 0,
    
    -- Constraints
    CONSTRAINT valid_belt CHECK (current_belt IN ('white', 'blue', 'purple', 'brown', 'black')),
    CONSTRAINT valid_stripe CHECK (current_stripe BETWEEN 1 AND 4)
);

-- Table 2: Stripe Completions (Track which stripes user has completed)
CREATE TABLE IF NOT EXISTS stripe_completions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL,
    belt TEXT NOT NULL,
    stripe_number INTEGER NOT NULL,
    completed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    xp_earned INTEGER DEFAULT 0,
    
    -- Additional metadata
    time_taken_minutes INTEGER,
    score_percentage INTEGER,
    
    -- Unique constraint: one completion per user per stripe
    UNIQUE(user_id, belt, stripe_number),
    
    -- Constraints
    CONSTRAINT valid_belt CHECK (belt IN ('white', 'blue', 'purple', 'brown', 'black')),
    CONSTRAINT valid_stripe CHECK (stripe_number BETWEEN 1 AND 4)
);

-- Table 3: Belt Completions (Track full belt achievements)
CREATE TABLE IF NOT EXISTS belt_completions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL,
    belt TEXT NOT NULL,
    completed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    assessment_score INTEGER,
    xp_earned INTEGER DEFAULT 0,
    
    -- Assessment metadata
    assessment_date TIMESTAMP WITH TIME ZONE,
    assessment_type TEXT,
    
    -- Unique constraint: one completion per user per belt
    UNIQUE(user_id, belt),
    
    -- Constraints
    CONSTRAINT valid_belt CHECK (belt IN ('white', 'blue', 'purple', 'brown', 'black'))
);

-- Table 4: Game Sessions (For multiplayer games)
CREATE TABLE IF NOT EXISTS game_sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    game_type TEXT NOT NULL,
    game_data JSONB DEFAULT '{}',
    created_by UUID,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Session metadata
    status TEXT DEFAULT 'active' CHECK (status IN ('active', 'completed', 'cancelled')),
    player_count INTEGER DEFAULT 0,
    max_players INTEGER DEFAULT 10
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_user_progress_user_id ON user_progress(user_id);
CREATE INDEX IF NOT EXISTS idx_user_progress_current_belt ON user_progress(current_belt);
CREATE INDEX IF NOT EXISTS idx_stripe_completions_user_id ON stripe_completions(user_id);
CREATE INDEX IF NOT EXISTS idx_stripe_completions_belt_stripe ON stripe_completions(belt, stripe_number);
CREATE INDEX IF NOT EXISTS idx_belt_completions_user_id ON belt_completions(user_id);
CREATE INDEX IF NOT EXISTS idx_game_sessions_game_type ON game_sessions(game_type);
CREATE INDEX IF NOT EXISTS idx_game_sessions_status ON game_sessions(status);

-- Enable Row Level Security (RLS)
ALTER TABLE user_progress ENABLE ROW LEVEL SECURITY;
ALTER TABLE stripe_completions ENABLE ROW LEVEL SECURITY;
ALTER TABLE belt_completions ENABLE ROW LEVEL SECURITY;
ALTER TABLE game_sessions ENABLE ROW LEVEL SECURITY;

-- RLS Policies

-- User Progress Policies
CREATE POLICY IF NOT EXISTS "Users can view own progress"
    ON user_progress FOR SELECT
    USING (true); -- Allow anonymous users for now (can restrict later)

CREATE POLICY IF NOT EXISTS "Users can insert own progress"
    ON user_progress FOR INSERT
    WITH CHECK (true);

CREATE POLICY IF NOT EXISTS "Users can update own progress"
    ON user_progress FOR UPDATE
    USING (true);

-- Stripe Completions Policies
CREATE POLICY IF NOT EXISTS "Users can view own stripe completions"
    ON stripe_completions FOR SELECT
    USING (true);

CREATE POLICY IF NOT EXISTS "Users can insert own stripe completions"
    ON stripe_completions FOR INSERT
    WITH CHECK (true);

-- Belt Completions Policies
CREATE POLICY IF NOT EXISTS "Users can view own belt completions"
    ON belt_completions FOR SELECT
    USING (true);

CREATE POLICY IF NOT EXISTS "Users can insert own belt completions"
    ON belt_completions FOR INSERT
    WITH CHECK (true);

-- Game Sessions Policies (more open for multiplayer)
CREATE POLICY IF NOT EXISTS "Anyone can view active game sessions"
    ON game_sessions FOR SELECT
    USING (status = 'active');

CREATE POLICY IF NOT EXISTS "Anyone can create game sessions"
    ON game_sessions FOR INSERT
    WITH CHECK (true);

CREATE POLICY IF NOT EXISTS "Users can update own game sessions"
    ON game_sessions FOR UPDATE
    USING (true);

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for updated_at
DROP TRIGGER IF EXISTS update_user_progress_updated_at ON user_progress;
CREATE TRIGGER update_user_progress_updated_at
    BEFORE UPDATE ON user_progress
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

DROP TRIGGER IF EXISTS update_game_sessions_updated_at ON game_sessions;
CREATE TRIGGER update_game_sessions_updated_at
    BEFORE UPDATE ON game_sessions
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- Grant permissions (adjust based on your auth setup)
-- For anonymous access (current setup):
-- GRANT SELECT, INSERT, UPDATE ON user_progress TO anon;
-- GRANT SELECT, INSERT ON stripe_completions TO anon;
-- GRANT SELECT, INSERT ON belt_completions TO anon;
-- GRANT SELECT, INSERT, UPDATE ON game_sessions TO anon;

-- Add comments for documentation
COMMENT ON TABLE user_progress IS 'Main user progress tracking - syncs across devices';
COMMENT ON TABLE stripe_completions IS 'Individual stripe completions per user';
COMMENT ON TABLE belt_completions IS 'Full belt completions per user';
COMMENT ON TABLE game_sessions IS 'Multiplayer game sessions';

COMMENT ON COLUMN user_progress.user_id IS 'Anonymous user ID from localStorage or authenticated user ID';
COMMENT ON COLUMN stripe_completions.xp_earned IS 'XP earned for completing this stripe';
COMMENT ON COLUMN belt_completions.assessment_score IS 'Score from belt assessment (0-100)';

