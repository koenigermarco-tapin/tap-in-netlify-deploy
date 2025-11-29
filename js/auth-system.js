// ============================================
// TAP-IN ANONYMOUS AUTH WITH BACKEND SYNC
// Supabase Anonymous Authentication
// GDPR Compliant - No Email Required
// ============================================

class TapInAuth {
    constructor() {
        this.supabase = null;
        this.currentUser = null;
        this.backupCode = null;
        this.init();
    }

    // ============================================
    // INITIALIZATION
    // ============================================
    async init() {
        // Initialize Supabase client
        // TODO: Replace with your Supabase credentials
        this.supabase = supabase.createClient(
            'YOUR_SUPABASE_URL',      // ← Replace with your Supabase project URL
            'YOUR_SUPABASE_ANON_KEY'  // ← Replace with your Supabase anon key
        );

        // Check for existing session
        const { data: { session } } = await this.supabase.auth.getSession();
        
        if (session) {
            // User has existing anonymous session
            this.currentUser = session.user;
            await this.loadBackupCode();
        } else {
            // Check for backup code in localStorage
            const savedCode = localStorage.getItem('tap_in_backup_code');
            if (savedCode) {
                // Try to restore from backup code
                await this.restoreFromBackupCode(savedCode);
            } else {
                // Create new anonymous user
                await this.createAnonymousUser();
            }
        }

        // Setup auth state listener
        this.supabase.auth.onAuthStateChange((event, session) => {
            if (event === 'SIGNED_IN') {
                this.currentUser = session.user;
            } else if (event === 'SIGNED_OUT') {
                this.currentUser = null;
            }
        });
    }

    // ============================================
    // ANONYMOUS USER CREATION
    // ============================================
    async createAnonymousUser() {
        try {
            // Sign in anonymously (Supabase creates user automatically)
            const { data, error } = await this.supabase.auth.signInAnonymously();
            
            if (error) throw error;
            
            this.currentUser = data.user;
            
            // Generate backup code
            this.backupCode = this.generateBackupCode();
            
            // Save backup code to Supabase AND localStorage
            await this.saveBackupCode(this.backupCode);
            localStorage.setItem('tap_in_backup_code', this.backupCode);
            
            // Show backup code to user (IMPORTANT!)
            this.showBackupCodeModal();
            
            return {
                success: true,
                userId: data.user.id,
                backupCode: this.backupCode
            };
        } catch (error) {
            console.error('Error creating anonymous user:', error);
            return { success: false, error };
        }
    }

    // ============================================
    // BACKUP CODE GENERATION
    // ============================================
    generateBackupCode() {
        const words = [
            'alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot',
            'golf', 'hotel', 'india', 'juliet', 'kilo', 'lima',
            'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo',
            'sierra', 'tango', 'uniform', 'victor', 'whiskey', 'xray',
            'yankee', 'zulu'
        ];
        
        const word1 = words[Math.floor(Math.random() * words.length)];
        const word2 = words[Math.floor(Math.random() * words.length)];
        const word3 = words[Math.floor(Math.random() * words.length)];
        const num = Math.floor(1000 + Math.random() * 8999);
        
        return `${word1}-${word2}-${word3}-${num}`;
    }

    // ============================================
    // BACKUP CODE STORAGE
    // ============================================
    async saveBackupCode(code) {
        try {
            // Store backup code in Supabase
            const { error } = await this.supabase
                .from('user_backup_codes')
                .insert({
                    user_id: this.currentUser.id,
                    backup_code: code,
                    created_at: new Date().toISOString()
                });
            
            if (error) throw error;
            
            return true;
        } catch (error) {
            console.error('Error saving backup code:', error);
            return false;
        }
    }

    async loadBackupCode() {
        try {
            const { data, error } = await this.supabase
                .from('user_backup_codes')
                .select('backup_code')
                .eq('user_id', this.currentUser.id)
                .single();
            
            if (error) throw error;
            
            this.backupCode = data.backup_code;
            localStorage.setItem('tap_in_backup_code', this.backupCode);
            
            return this.backupCode;
        } catch (error) {
            console.error('Error loading backup code:', error);
            return null;
        }
    }

    // ============================================
    // RESTORE FROM BACKUP CODE
    // ============================================
    async restoreFromBackupCode(code) {
        try {
            // Find user by backup code
            const { data, error } = await this.supabase
                .from('user_backup_codes')
                .select('user_id')
                .eq('backup_code', code)
                .single();
            
            if (error || !data) {
                throw new Error('Invalid backup code');
            }
            
            // Create new anonymous session for this user
            // (Supabase doesn't allow direct login with user_id, 
            //  so we need to handle this differently)
            
            // Store the user_id we want to restore
            localStorage.setItem('restoring_user_id', data.user_id);
            
            // Sign in anonymously (creates new session)
            const { data: authData, error: authError } = 
                await this.supabase.auth.signInAnonymously();
            
            if (authError) throw authError;
            
            // Migrate old user's data to new session
            await this.migrateUserData(data.user_id, authData.user.id);
            
            // Update backup code to new user
            await this.supabase
                .from('user_backup_codes')
                .update({ user_id: authData.user.id })
                .eq('backup_code', code);
            
            this.currentUser = authData.user;
            this.backupCode = code;
            
            localStorage.removeItem('restoring_user_id');
            localStorage.setItem('tap_in_backup_code', code);
            
            return {
                success: true,
                userId: authData.user.id
            };
        } catch (error) {
            console.error('Error restoring from backup code:', error);
            return {
                success: false,
                error: error.message
            };
        }
    }

    // ============================================
    // DATA MIGRATION
    // ============================================
    async migrateUserData(oldUserId, newUserId) {
        try {
            // Migrate avatar state
            const { data: avatarData } = await this.supabase
                .from('avatar_state')
                .select('*')
                .eq('user_id', oldUserId)
                .single();
            
            if (avatarData) {
                await this.supabase
                    .from('avatar_state')
                    .insert({
                        ...avatarData,
                        user_id: newUserId,
                        id: undefined // Let Supabase generate new ID
                    });
            }
            
            // Migrate progress
            const { data: progressData } = await this.supabase
                .from('user_progress')
                .select('*')
                .eq('user_id', oldUserId);
            
            if (progressData && progressData.length > 0) {
                const migratedProgress = progressData.map(p => ({
                    ...p,
                    user_id: newUserId,
                    id: undefined
                }));
                
                await this.supabase
                    .from('user_progress')
                    .insert(migratedProgress);
            }
            
            // Delete old user's data
            await this.supabase
                .from('avatar_state')
                .delete()
                .eq('user_id', oldUserId);
            
            await this.supabase
                .from('user_progress')
                .delete()
                .eq('user_id', oldUserId);
            
            return true;
        } catch (error) {
            console.error('Error migrating user data:', error);
            return false;
        }
    }

    // ============================================
    // DATA SYNC METHODS
    // ============================================
    async saveProgress(progressData) {
        if (!this.currentUser) {
            console.error('No authenticated user');
            return false;
        }
        
        try {
            const { error } = await this.supabase
                .from('user_progress')
                .upsert({
                    user_id: this.currentUser.id,
                    current_belt: progressData.currentBelt,
                    stripes_completed: progressData.stripesCompleted,
                    total_xp: progressData.totalXP,
                    completed_lessons: progressData.completedLessons,
                    last_active: new Date().toISOString(),
                    updated_at: new Date().toISOString()
                }, {
                    onConflict: 'user_id'
                });
            
            if (error) throw error;
            
            return true;
        } catch (error) {
            console.error('Error saving progress:', error);
            return false;
        }
    }

    async loadProgress() {
        if (!this.currentUser) {
            console.error('No authenticated user');
            return null;
        }
        
        try {
            const { data, error } = await this.supabase
                .from('user_progress')
                .select('*')
                .eq('user_id', this.currentUser.id)
                .single();
            
            if (error && error.code !== 'PGRST116') throw error; // PGRST116 = not found
            
            return data || null;
        } catch (error) {
            console.error('Error loading progress:', error);
            return null;
        }
    }

    async saveAvatarState(avatarData) {
        if (!this.currentUser) {
            console.error('No authenticated user');
            return false;
        }
        
        try {
            const { error } = await this.supabase
                .from('avatar_state')
                .upsert({
                    user_id: this.currentUser.id,
                    belt: avatarData.belt,
                    belt_stripes: avatarData.beltStripes,
                    gi_color: avatarData.giColor,
                    patch_left: avatarData.patchLeft,
                    patch_right: avatarData.patchRight,
                    background: avatarData.background,
                    owned_items: avatarData.ownedItems,
                    equipped_items: avatarData.equippedItems,
                    active_effects: avatarData.activeEffects,
                    updated_at: new Date().toISOString()
                }, {
                    onConflict: 'user_id'
                });
            
            if (error) throw error;
            
            return true;
        } catch (error) {
            console.error('Error saving avatar state:', error);
            return false;
        }
    }

    async loadAvatarState() {
        if (!this.currentUser) {
            console.error('No authenticated user');
            return null;
        }
        
        try {
            const { data, error } = await this.supabase
                .from('avatar_state')
                .select('*')
                .eq('user_id', this.currentUser.id)
                .single();
            
            if (error && error.code !== 'PGRST116') throw error;
            
            return data ? {
                belt: data.belt,
                beltStripes: data.belt_stripes,
                giColor: data.gi_color,
                patchLeft: data.patch_left,
                patchRight: data.patch_right,
                background: data.background,
                ownedItems: data.owned_items,
                equippedItems: data.equipped_items,
                activeEffects: data.active_effects
            } : null;
        } catch (error) {
            console.error('Error loading avatar state:', error);
            return null;
        }
    }

    // ============================================
    // LEADERBOARD
    // ============================================
    async getLeaderboard(limit = 100) {
        try {
            const { data, error } = await this.supabase
                .from('user_progress')
                .select('user_id, total_xp, current_belt, last_active')
                .order('total_xp', { ascending: false })
                .limit(limit);
            
            if (error) throw error;
            
            // Load avatar states for top users
            const userIds = data.map(u => u.user_id);
            const { data: avatars } = await this.supabase
                .from('avatar_state')
                .select('user_id, gi_color, belt, background')
                .in('user_id', userIds);
            
            // Combine data
            const leaderboard = data.map((user, index) => {
                const avatar = avatars?.find(a => a.user_id === user.user_id);
                return {
                    rank: index + 1,
                    userId: user.user_id,
                    xp: user.total_xp,
                    belt: user.current_belt,
                    avatar: avatar || null,
                    isCurrentUser: user.user_id === this.currentUser?.id
                };
            });
            
            return leaderboard;
        } catch (error) {
            console.error('Error fetching leaderboard:', error);
            return [];
        }
    }

    async getCurrentUserRank() {
        if (!this.currentUser) return null;
        
        try {
            // Count users with more XP
            const { data: currentUserData } = await this.supabase
                .from('user_progress')
                .select('total_xp')
                .eq('user_id', this.currentUser.id)
                .single();
            
            if (!currentUserData) return null;
            
            const { count } = await this.supabase
                .from('user_progress')
                .select('*', { count: 'exact', head: true })
                .gt('total_xp', currentUserData.total_xp);
            
            return (count || 0) + 1; // Rank = number of users ahead + 1
        } catch (error) {
            console.error('Error getting user rank:', error);
            return null;
        }
    }

    // ============================================
    // UI HELPERS
    // ============================================
    showBackupCodeModal() {
        const modal = document.createElement('div');
        modal.id = 'backupCodeModal';
        modal.innerHTML = `
            <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
                        background: rgba(0,0,0,0.8); display: flex; align-items: center; 
                        justify-content: center; z-index: 10000;">
                <div style="background: white; padding: 3rem; border-radius: 20px; 
                            max-width: 500px; text-align: center;">
                    <h2 style="margin-bottom: 1rem; color: #1e293b;">
                        🔐 Save Your Backup Code
                    </h2>
                    <p style="color: #64748b; margin-bottom: 2rem;">
                        This code lets you restore your progress on any device. 
                        Save it somewhere safe!
                    </p>
                    
                    <div style="background: #f8fafc; padding: 1.5rem; border-radius: 12px; 
                                margin-bottom: 2rem; font-family: monospace; font-size: 1.5rem; 
                                font-weight: 700; color: #1e293b; word-break: break-all;">
                        ${this.backupCode}
                    </div>
                    
                    <div style="display: flex; gap: 1rem; justify-content: center; margin-bottom: 1rem;">
                        <button onclick="TapInAuth.copyBackupCode()" 
                                style="padding: 1rem 2rem; background: #3b82f6; color: white; 
                                       border: none; border-radius: 12px; font-weight: 700; 
                                       cursor: pointer;">
                            📋 Copy Code
                        </button>
                        
                        <button onclick="TapInAuth.downloadBackupCode()" 
                                style="padding: 1rem 2rem; background: #10b981; color: white; 
                                       border: none; border-radius: 12px; font-weight: 700; 
                                       cursor: pointer;">
                            💾 Download
                        </button>
                    </div>
                    
                    <button onclick="TapInAuth.closeBackupModal()" 
                            style="padding: 1rem 2rem; background: #64748b; color: white; 
                                   border: none; border-radius: 12px; font-weight: 700; 
                                   cursor: pointer; width: 100%;">
                        I've Saved It
                    </button>
                    
                    <p style="color: #dc2626; font-size: 0.85rem; margin-top: 1rem;">
                        ⚠️ Without this code, you cannot restore your progress!
                    </p>
                </div>
            </div>
        `;
        
        document.body.appendChild(modal);
    }

    static copyBackupCode() {
        const code = window.tapInAuth.backupCode;
        navigator.clipboard.writeText(code);
        alert('✅ Backup code copied to clipboard!');
    }

    static downloadBackupCode() {
        const code = window.tapInAuth.backupCode;
        const blob = new Blob([`TAP-IN Backup Code\n\n${code}\n\nKeep this code safe!`], 
                              { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'tap-in-backup-code.txt';
        a.click();
        URL.revokeObjectURL(url);
    }

    static closeBackupModal() {
        const modal = document.getElementById('backupCodeModal');
        if (modal) modal.remove();
    }

    // ============================================
    // PUBLIC API
    // ============================================
    getUserId() {
        return this.currentUser?.id || null;
    }

    getBackupCode() {
        return this.backupCode;
    }

    isAuthenticated() {
        return !!this.currentUser;
    }
}

// ============================================
// GLOBAL INSTANCE
// ============================================
window.tapInAuth = new TapInAuth();

// Export for modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = TapInAuth;
}
