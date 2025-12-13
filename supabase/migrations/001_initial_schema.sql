-- TAP-IN Platform - Initial Database Schema
-- Complete schema for users, assessments, progress, teams, and sync management

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ============================================
-- TABLE 1: Users
-- ============================================
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    email_verified BOOLEAN DEFAULT FALSE,
    
    -- Profile
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    display_name VARCHAR(200),
    avatar_url TEXT,
    
    -- Progress defaults
    total_xp INTEGER DEFAULT 0,
    current_belt TEXT DEFAULT 'white',
    current_stripe INTEGER DEFAULT 1,
    current_level INTEGER DEFAULT 1,
    
    -- Stats
    streak_count INTEGER DEFAULT 0,
    longest_streak INTEGER DEFAULT 0,
    last_active TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Metadata
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    last_login TIMESTAMP WITH TIME ZONE,
    
    -- Constraints
    CONSTRAINT valid_belt CHECK (current_belt IN ('white', 'blue', 'purple', 'brown', 'black')),
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

-- ============================================
-- TABLE 2: Assessments
-- ============================================
CREATE TABLE IF NOT EXISTS assessments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    
    -- Assessment type
    assessment_type VARCHAR(50) NOT NULL,
    
    -- Results
    results_json JSONB DEFAULT '{}',
    scores_json JSONB DEFAULT '{}',
    
    -- Metadata
    completed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    time_taken_seconds INTEGER,
    device_type VARCHAR(50),
    language VARCHAR(2) DEFAULT 'en',
    
    -- Lead tracking
    lead_id UUID,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ============================================
-- TABLE 3: Progress
-- ============================================
CREATE TABLE IF NOT EXISTS progress (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE NOT NULL,
    
    -- Progress type
    progress_type VARCHAR(50) NOT NULL, -- 'stripe_completion', 'belt_completion', 'lesson_completion', 'xp_award'
    
    -- Details
    belt TEXT,
    stripe_number INTEGER,
    lesson_id VARCHAR(100),
    xp_amount INTEGER DEFAULT 0,
    
    -- Metadata
    completed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    progress_data JSONB DEFAULT '{}',
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Constraints
    CONSTRAINT valid_belt CHECK (belt IS NULL OR belt IN ('white', 'blue', 'purple', 'brown', 'black')),
    CONSTRAINT valid_stripe CHECK (stripe_number IS NULL OR stripe_number BETWEEN 1 AND 4)
);

-- ============================================
-- TABLE 4: Teams
-- ============================================
CREATE TABLE IF NOT EXISTS teams (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(200) NOT NULL,
    description TEXT,
    
    -- Team admin
    created_by UUID REFERENCES users(id),
    
    -- Invite system
    invite_code VARCHAR(20) UNIQUE,
    invite_code_expires_at TIMESTAMP WITH TIME ZONE,
    
    -- Metadata
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    is_active BOOLEAN DEFAULT TRUE
);

-- ============================================
-- TABLE 5: Team Members
-- ============================================
CREATE TABLE IF NOT EXISTS team_members (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    team_id UUID REFERENCES teams(id) ON DELETE CASCADE NOT NULL,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE NOT NULL,
    
    -- Role
    role VARCHAR(20) DEFAULT 'member' CHECK (role IN ('owner', 'admin', 'member')),
    
    -- Metadata
    joined_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    is_active BOOLEAN DEFAULT TRUE,
    
    -- Unique constraint
    UNIQUE(team_id, user_id)
);

-- ============================================
-- TABLE 6: Sync Log
-- ============================================
CREATE TABLE IF NOT EXISTS sync_log (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    
    -- Sync details
    sync_type VARCHAR(50) NOT NULL, -- 'progress', 'assessment', 'full_sync'
    entity_type VARCHAR(50), -- 'stripe', 'belt', 'xp', etc.
    entity_id UUID,
    
    -- Sync metadata
    device_id VARCHAR(100),
    sync_direction VARCHAR(20) CHECK (sync_direction IN ('upload', 'download', 'bidirectional')),
    sync_status VARCHAR(20) DEFAULT 'success' CHECK (sync_status IN ('success', 'failed', 'conflict')),
    
    -- Conflict resolution
    conflict_resolution VARCHAR(50), -- 'server_won', 'client_won', 'merged'
    resolved_data JSONB,
    
    -- Metadata
    synced_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    error_message TEXT,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ============================================
-- TABLE 7: User Sessions
-- ============================================
CREATE TABLE IF NOT EXISTS user_sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE NOT NULL,
    
    -- Session details
    device_id VARCHAR(100) NOT NULL,
    device_name VARCHAR(200),
    device_type VARCHAR(50), -- 'mobile', 'tablet', 'desktop'
    browser VARCHAR(100),
    
    -- Location
    ip_address INET,
    country VARCHAR(2),
    
    -- Session metadata
    last_activity TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    expires_at TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Unique constraint: one active session per user per device
    UNIQUE(user_id, device_id)
);

-- ============================================
-- INDEXES for Performance
-- ============================================
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_current_belt ON users(current_belt);
CREATE INDEX IF NOT EXISTS idx_assessments_user_id ON assessments(user_id);
CREATE INDEX IF NOT EXISTS idx_assessments_type ON assessments(assessment_type);
CREATE INDEX IF NOT EXISTS idx_assessments_completed_at ON assessments(completed_at DESC);
CREATE INDEX IF NOT EXISTS idx_progress_user_id ON progress(user_id);
CREATE INDEX IF NOT EXISTS idx_progress_type ON progress(progress_type);
CREATE INDEX IF NOT EXISTS idx_progress_belt_stripe ON progress(belt, stripe_number);
CREATE INDEX IF NOT EXISTS idx_progress_completed_at ON progress(completed_at DESC);
CREATE INDEX IF NOT EXISTS idx_team_members_team_id ON team_members(team_id);
CREATE INDEX IF NOT EXISTS idx_team_members_user_id ON team_members(user_id);
CREATE INDEX IF NOT EXISTS idx_sync_log_user_id ON sync_log(user_id);
CREATE INDEX IF NOT EXISTS idx_sync_log_synced_at ON sync_log(synced_at DESC);
CREATE INDEX IF NOT EXISTS idx_user_sessions_user_id ON user_sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_user_sessions_device_id ON user_sessions(device_id);
CREATE INDEX IF NOT EXISTS idx_user_sessions_last_activity ON user_sessions(last_activity DESC);
CREATE INDEX IF NOT EXISTS idx_teams_invite_code ON teams(invite_code);

-- ============================================
-- ROW LEVEL SECURITY (RLS)
-- ============================================

-- Enable RLS on all tables
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE assessments ENABLE ROW LEVEL SECURITY;
ALTER TABLE progress ENABLE ROW LEVEL SECURITY;
ALTER TABLE teams ENABLE ROW LEVEL SECURITY;
ALTER TABLE team_members ENABLE ROW LEVEL SECURITY;
ALTER TABLE sync_log ENABLE ROW LEVEL SECURITY;
ALTER TABLE user_sessions ENABLE ROW LEVEL SECURITY;

-- ============================================
-- RLS POLICIES
-- ============================================

-- Users: Can view own profile, update own profile
CREATE POLICY IF NOT EXISTS "Users can view own profile"
    ON users FOR SELECT
    USING (auth.uid() = id OR true); -- Allow anonymous for now

CREATE POLICY IF NOT EXISTS "Users can insert own profile"
    ON users FOR INSERT
    WITH CHECK (auth.uid() = id OR true);

CREATE POLICY IF NOT EXISTS "Users can update own profile"
    ON users FOR UPDATE
    USING (auth.uid() = id OR true);

-- Assessments: Can view/insert own assessments
CREATE POLICY IF NOT EXISTS "Users can view own assessments"
    ON assessments FOR SELECT
    USING (auth.uid() = user_id OR user_id IS NULL OR true);

CREATE POLICY IF NOT EXISTS "Users can insert own assessments"
    ON assessments FOR INSERT
    WITH CHECK (auth.uid() = user_id OR user_id IS NULL OR true);

-- Progress: Can view/insert own progress
CREATE POLICY IF NOT EXISTS "Users can view own progress"
    ON progress FOR SELECT
    USING (auth.uid() = user_id OR true);

CREATE POLICY IF NOT EXISTS "Users can insert own progress"
    ON progress FOR INSERT
    WITH CHECK (auth.uid() = user_id OR true);

CREATE POLICY IF NOT EXISTS "Users can update own progress"
    ON progress FOR UPDATE
    USING (auth.uid() = user_id OR true);

-- Teams: Open read, own write
CREATE POLICY IF NOT EXISTS "Anyone can view active teams"
    ON teams FOR SELECT
    USING (is_active = true);

CREATE POLICY IF NOT EXISTS "Users can create teams"
    ON teams FOR INSERT
    WITH CHECK (true);

CREATE POLICY IF NOT EXISTS "Users can update own teams"
    ON teams FOR UPDATE
    USING (created_by = auth.uid() OR true);

-- Team Members: View team members, join teams
CREATE POLICY IF NOT EXISTS "Users can view team members"
    ON team_members FOR SELECT
    USING (true);

CREATE POLICY IF NOT EXISTS "Users can join teams"
    ON team_members FOR INSERT
    WITH CHECK (true);

CREATE POLICY IF NOT EXISTS "Users can leave teams"
    ON team_members FOR DELETE
    USING (user_id = auth.uid() OR true);

-- Sync Log: View own logs
CREATE POLICY IF NOT EXISTS "Users can view own sync logs"
    ON sync_log FOR SELECT
    USING (auth.uid() = user_id OR user_id IS NULL OR true);

CREATE POLICY IF NOT EXISTS "Users can insert own sync logs"
    ON sync_log FOR INSERT
    WITH CHECK (auth.uid() = user_id OR user_id IS NULL OR true);

-- User Sessions: View own sessions
CREATE POLICY IF NOT EXISTS "Users can view own sessions"
    ON user_sessions FOR SELECT
    USING (auth.uid() = user_id OR true);

CREATE POLICY IF NOT EXISTS "Users can insert own sessions"
    ON user_sessions FOR INSERT
    WITH CHECK (auth.uid() = user_id OR true);

CREATE POLICY IF NOT EXISTS "Users can update own sessions"
    ON user_sessions FOR UPDATE
    USING (auth.uid() = user_id OR true);

-- ============================================
-- FUNCTIONS
-- ============================================

-- Function: Update last_active timestamp
CREATE OR REPLACE FUNCTION update_last_active()
RETURNS TRIGGER AS $$
BEGIN
    NEW.last_active = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger: Update last_active on user activity
DROP TRIGGER IF EXISTS trigger_update_last_active ON users;
CREATE TRIGGER trigger_update_last_active
    BEFORE UPDATE ON users
    FOR EACH ROW
    WHEN (OLD.total_xp IS DISTINCT FROM NEW.total_xp OR 
          OLD.current_belt IS DISTINCT FROM NEW.current_belt OR
          OLD.current_stripe IS DISTINCT FROM NEW.current_stripe)
    EXECUTE FUNCTION update_last_active();

-- Function: Handle new user creation
CREATE OR REPLACE FUNCTION handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
    -- Set default display name if not provided
    IF NEW.display_name IS NULL THEN
        NEW.display_name = COALESCE(NEW.first_name || ' ' || NEW.last_name, 
                                   split_part(NEW.email, '@', 1), 
                                   'User_' || substr(NEW.id::text, 1, 8));
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger: Handle new user
DROP TRIGGER IF EXISTS trigger_handle_new_user ON users;
CREATE TRIGGER trigger_handle_new_user
    BEFORE INSERT ON users
    FOR EACH ROW
    EXECUTE FUNCTION handle_new_user();

-- Function: Get team stats
CREATE OR REPLACE FUNCTION get_team_stats(team_uuid UUID)
RETURNS TABLE (
    total_members BIGINT,
    total_xp BIGINT,
    average_level NUMERIC,
    belts_earned JSONB
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        COUNT(DISTINCT tm.user_id) as total_members,
        COALESCE(SUM(u.total_xp), 0)::BIGINT as total_xp,
        COALESCE(AVG(u.current_level), 0) as average_level,
        jsonb_object_agg(
            u.current_belt, 
            COUNT(DISTINCT u.id)
        ) FILTER (WHERE u.current_belt IS NOT NULL) as belts_earned
    FROM team_members tm
    LEFT JOIN users u ON tm.user_id = u.id
    WHERE tm.team_id = team_uuid AND tm.is_active = true;
END;
$$ LANGUAGE plpgsql;

-- Function: Resolve sync conflict
CREATE OR REPLACE FUNCTION resolve_sync_conflict(
    server_data JSONB,
    client_data JSONB,
    conflict_field TEXT
)
RETURNS JSONB AS $$
DECLARE
    server_value NUMERIC;
    client_value NUMERIC;
    result JSONB;
BEGIN
    -- For numeric fields, take higher value
    IF conflict_field IN ('total_xp', 'current_level', 'streak_count') THEN
        server_value := COALESCE((server_data->>conflict_field)::NUMERIC, 0);
        client_value := COALESCE((client_data->>conflict_field)::NUMERIC, 0);
        
        result := server_data;
        result := jsonb_set(result, ARRAY[conflict_field], to_jsonb(GREATEST(server_value, client_value)));
        
        RETURN result;
    END IF;
    
    -- For arrays, union them
    IF jsonb_typeof(server_data->conflict_field) = 'array' AND 
       jsonb_typeof(client_data->conflict_field) = 'array' THEN
        result := server_data;
        result := jsonb_set(result, ARRAY[conflict_field], 
                           (server_data->conflict_field) || (client_data->conflict_field));
        RETURN result;
    END IF;
    
    -- Default: use server data
    RETURN server_data;
END;
$$ LANGUAGE plpgsql;

-- Function: Update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for updated_at
DROP TRIGGER IF EXISTS update_users_updated_at ON users;
CREATE TRIGGER update_users_updated_at
    BEFORE UPDATE ON users
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

DROP TRIGGER IF EXISTS update_teams_updated_at ON teams;
CREATE TRIGGER update_teams_updated_at
    BEFORE UPDATE ON teams
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- ============================================
-- VIEW: Leaderboard (Anonymized)
-- ============================================
CREATE OR REPLACE VIEW leaderboard AS
SELECT 
    ROW_NUMBER() OVER (ORDER BY total_xp DESC, last_active DESC) as rank,
    CASE 
        WHEN display_name IS NOT NULL AND display_name != '' THEN display_name
        WHEN first_name IS NOT NULL AND last_name IS NOT NULL THEN first_name || ' ' || LEFT(last_name, 1) || '.'
        WHEN first_name IS NOT NULL THEN first_name
        ELSE LEFT(email, 3) || '***'
    END as display_name,
    total_xp,
    current_belt,
    current_level,
    streak_count,
    last_active
FROM users
WHERE total_xp > 0
ORDER BY total_xp DESC, last_active DESC
LIMIT 100;

-- ============================================
-- COMMENTS
-- ============================================
COMMENT ON TABLE users IS 'User accounts and profiles';
COMMENT ON TABLE assessments IS 'Assessment submissions and results';
COMMENT ON TABLE progress IS 'User progress tracking (stripes, belts, XP)';
COMMENT ON TABLE teams IS 'Team/organization groups';
COMMENT ON TABLE team_members IS 'Team membership relationships';
COMMENT ON TABLE sync_log IS 'Sync operation audit log';
COMMENT ON TABLE user_sessions IS 'Active user sessions per device';

COMMENT ON FUNCTION get_team_stats IS 'Returns aggregated statistics for a team';
COMMENT ON FUNCTION resolve_sync_conflict IS 'Resolves conflicts between server and client data';
COMMENT ON VIEW leaderboard IS 'Public leaderboard with anonymized user data';

-- ============================================
-- GRANTS (Adjust based on your auth setup)
-- ============================================
-- For anonymous access (current setup):
-- GRANT SELECT, INSERT, UPDATE ON users TO anon;
-- GRANT SELECT, INSERT ON assessments TO anon;
-- GRANT SELECT, INSERT, UPDATE ON progress TO anon;
-- GRANT SELECT, INSERT ON teams TO anon;
-- GRANT SELECT, INSERT, DELETE ON team_members TO anon;
-- GRANT SELECT, INSERT ON sync_log TO anon;
-- GRANT SELECT, INSERT, UPDATE ON user_sessions TO anon;
-- GRANT SELECT ON leaderboard TO anon;

