/**
 * Supabase Configuration
 * Connect to existing Supabase backend
 * 
 * NOTE: Placeholder values are intentional - the system gracefully falls back to localStorage
 * when Supabase is not configured. This allows the platform to work without cloud sync.
 * 
 * To enable cloud sync (optional):
 * 1. Go to https://supabase.com → Your Project → Settings → API
 * 2. Copy Project URL and Anon Key
 * 3. Replace the values below
 */
const SUPABASE_URL = 'REPLACE_WITH_YOUR_URL';
const SUPABASE_ANON_KEY = 'REPLACE_WITH_YOUR_KEY';

// Initialize Supabase client
let supabase = null;
let supabaseReady = false;

try {
  // Check if Supabase library is loaded
  if (typeof window.supabase !== 'undefined') {
    
    // Check if credentials are configured
    if (SUPABASE_URL !== 'REPLACE_WITH_YOUR_URL' && 
        SUPABASE_ANON_KEY !== 'REPLACE_WITH_YOUR_KEY') {
      
      supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
      supabaseReady = true;
      console.log('✅ Supabase connected:', SUPABASE_URL);
      
    } else {
      console.warn('⚠️  Supabase credentials not configured - using localStorage only');
      console.log('ℹ️  To enable cloud sync:');
      console.log('   1. Go to https://supabase.com → Settings → API');
      console.log('   2. Copy Project URL and Anon Key');
      console.log('   3. Update js/supabase-config.js');
    }
    
  } else {
    console.warn('⚠️  Supabase library not loaded - add CDN script:');
    console.log('   <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>');
  }
  
} catch (error) {
  console.error('❌ Supabase initialization failed:', error);
}

// Export for use in other files
window.SupabaseClient = supabase;
window.supabaseReady = supabaseReady;

