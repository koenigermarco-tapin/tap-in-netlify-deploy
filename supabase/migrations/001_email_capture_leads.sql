-- Migration: Add email capture system for assessment leads
-- Creates 'leads' table if it doesn't exist and adds assessment-specific columns

-- Create leads table if it doesn't exist
CREATE TABLE IF NOT EXISTS leads (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Contact Information
    email VARCHAR(255) UNIQUE NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    
    -- Assessment Data
    assessment_type VARCHAR(50),
    scores_json JSONB DEFAULT '{}',
    results_json JSONB DEFAULT '{}',
    options JSONB DEFAULT '[]', -- Array of selected options: pdf_report, action_plan, industry_benchmarks
    
    -- GDPR & Consent
    gdpr_consent BOOLEAN DEFAULT FALSE,
    newsletter_subscribed BOOLEAN DEFAULT TRUE,
    newsletter_unsubscribed_at TIMESTAMP WITH TIME ZONE,
    
    -- Engagement Tracking
    assessments_completed INTEGER DEFAULT 1,
    last_assessment_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    email_verified BOOLEAN DEFAULT FALSE,
    
    -- Lead Scoring
    lead_score INTEGER DEFAULT 0, -- 0-100 based on engagement
    lead_status VARCHAR(20) DEFAULT 'new' CHECK (lead_status IN ('new', 'engaged', 'qualified', 'converted', 'lost')),
    
    -- Email Provider Integration
    sendgrid_contact_id VARCHAR(100),
    mailchimp_contact_id VARCHAR(100),
    
    -- Additional Metadata
    referrer TEXT,
    utm_source VARCHAR(100),
    utm_medium VARCHAR(100),
    utm_campaign VARCHAR(100),
    
    -- Notes
    notes TEXT,
    
    -- Indexes for common queries
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_leads_email ON leads(email);
CREATE INDEX IF NOT EXISTS idx_leads_assessment_type ON leads(assessment_type);
CREATE INDEX IF NOT EXISTS idx_leads_lead_status ON leads(lead_status);
CREATE INDEX IF NOT EXISTS idx_leads_created_at ON leads(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_leads_gdpr_consent ON leads(gdpr_consent);

-- Enable Row Level Security (RLS)
ALTER TABLE leads ENABLE ROW LEVEL SECURITY;

-- Create policy: Service role can do everything
CREATE POLICY IF NOT EXISTS "Service role full access" ON leads
    FOR ALL
    USING (auth.role() = 'service_role');

-- Create policy: Public can insert (for email capture forms)
CREATE POLICY IF NOT EXISTS "Public can insert leads" ON leads
    FOR INSERT
    WITH CHECK (true);

-- Create function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_leads_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create trigger for updated_at
DROP TRIGGER IF EXISTS update_leads_updated_at ON leads;
CREATE TRIGGER update_leads_updated_at
    BEFORE UPDATE ON leads
    FOR EACH ROW
    EXECUTE FUNCTION update_leads_updated_at();

-- Grant permissions (adjust based on your setup)
-- GRANT INSERT ON leads TO anon;
-- GRANT SELECT, UPDATE ON leads TO authenticated;

-- Add comments for documentation
COMMENT ON TABLE leads IS 'Stores email leads from assessment completion forms';
COMMENT ON COLUMN leads.scores_json IS 'JSON object containing assessment scores';
COMMENT ON COLUMN leads.results_json IS 'JSON object containing complete assessment results';
COMMENT ON COLUMN leads.options IS 'JSON array of selected options: pdf_report, action_plan, industry_benchmarks';
COMMENT ON COLUMN leads.lead_score IS 'Scoring system: 0-100 based on engagement level';

