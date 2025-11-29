/**
 * TAP-IN Avatar System
 * CSS-based avatar with customizable items, belt sync, and XP integration
 */

const AvatarSystem = {
    // Default avatar state
    defaultState: {
        belt: 'white',
        beltStripes: 0,
        totalXP: 0,
        giColor: 'white',
        patchLeft: 'none',
        patchRight: 'none',
        background: 'garage',
        ownedItems: ['white-gi', 'garage-bg'],
        equippedItems: ['white-gi', 'garage-bg'],
        activeEffects: []
    },

    // Initialize avatar system
    init() {
        this.loadState();
        this.syncBeltWithProgress();
    },

    // Load state from localStorage or create default
    loadState() {
        const saved = localStorage.getItem('avatarState');
        if (saved) {
            try {
                this.state = JSON.parse(saved);
            } catch (e) {
                this.state = { ...this.defaultState };
            }
        } else {
            this.state = { ...this.defaultState };
            this.saveState();
        }
        return this.state;
    },

    // Save state to localStorage
    saveState() {
        // Sync with auth system if available
        if (window.tapInAuth && window.tapInAuth.saveAvatarState) {
            window.tapInAuth.saveAvatarState(this.state);
        }
        localStorage.setItem('avatarState', JSON.stringify(this.state));
    },

    // Get current state
    getState() {
        return this.state || this.loadState();
    },

    // Sync belt with user progress
    syncBeltWithProgress() {
        const currentBelt = localStorage.getItem('currentBelt') || 'white';
        const beltMap = {
            'White': 'white',
            'Blue': 'blue',
            'Purple': 'purple',
            'Brown': 'brown',
            'Black': 'black'
        };
        const beltColor = beltMap[currentBelt] || currentBelt.toLowerCase();
        
        // Count stripes completed
        let stripes = 0;
        for (let i = 1; i <= 4; i++) {
            const key = `${currentBelt.toLowerCase()}BeltStripe${i}Complete`;
            if (localStorage.getItem(key) === 'true') {
                stripes++;
            }
        }
        
        this.state = this.getState();
        this.state.belt = beltColor;
        this.state.beltStripes = stripes;
        this.state.totalXP = parseInt(localStorage.getItem('totalXP') || '0');
        this.saveState();
    },

    // Render avatar to container
    renderAvatar(containerId) {
        const container = document.getElementById(containerId);
        if (!container) return;

        const state = this.getState();
        this.syncBeltWithProgress();
        
        // Clear container
        container.innerHTML = '';

        // Create avatar layers
        const avatar = document.createElement('div');
        avatar.className = 'avatar-layers';
        
        // Background
        const bg = document.createElement('div');
        bg.className = `avatar-bg avatar-bg-${state.background}`;
        avatar.appendChild(bg);

        // Body (gi)
        const body = document.createElement('div');
        body.className = `avatar-body avatar-gi-${state.giColor}`;
        avatar.appendChild(body);

        // Patches
        if (state.patchLeft !== 'none') {
            const patchL = document.createElement('div');
            patchL.className = `avatar-patch avatar-patch-left avatar-patch-${state.patchLeft}`;
            avatar.appendChild(patchL);
        }
        if (state.patchRight !== 'none') {
            const patchR = document.createElement('div');
            patchR.className = `avatar-patch avatar-patch-right avatar-patch-${state.patchRight}`;
            avatar.appendChild(patchR);
        }

        // Belt
        const belt = document.createElement('div');
        belt.className = `avatar-belt avatar-belt-${state.belt}`;
        // Add stripes
        for (let i = 0; i < state.beltStripes; i++) {
            const stripe = document.createElement('div');
            stripe.className = 'avatar-stripe';
            belt.appendChild(stripe);
        }
        avatar.appendChild(belt);

        // Effects
        state.activeEffects.forEach(effect => {
            const effectEl = document.createElement('div');
            effectEl.className = `avatar-effect avatar-effect-${effect}`;
            avatar.appendChild(effectEl);
        });

        container.appendChild(avatar);
    },

    // Get owned items count
    getOwnedItems() {
        const state = this.getState();
        return state.ownedItems || [];
    },

    // Equip item
    equipItem(itemId) {
        const state = this.getState();
        if (!state.ownedItems.includes(itemId)) {
            return false; // Don't own it
        }
        
        // Handle different item types
        if (itemId.includes('-gi')) {
            state.giColor = itemId.replace('-gi', '');
        } else if (itemId.includes('-bg')) {
            state.background = itemId.replace('-bg', '');
        } else if (itemId.includes('-patch')) {
            const side = itemId.includes('-left') ? 'patchLeft' : 'patchRight';
            const patchType = itemId.replace('-patch-left', '').replace('-patch-right', '').replace('-patch', '');
            state[side] = patchType;
        }
        
        if (!state.equippedItems.includes(itemId)) {
            state.equippedItems.push(itemId);
        }
        
        this.saveState();
        return true;
    },

    // Unequip item
    unequipItem(itemId) {
        const state = this.getState();
        state.equippedItems = state.equippedItems.filter(id => id !== itemId);
        
        // Reset to defaults if unequipped
        if (itemId.includes('-gi')) {
            state.giColor = 'white';
        } else if (itemId.includes('-bg')) {
            state.background = 'garage';
        } else if (itemId.includes('-patch-left')) {
            state.patchLeft = 'none';
        } else if (itemId.includes('-patch-right')) {
            state.patchRight = 'none';
        }
        
        this.saveState();
        return true;
    },

    // Purchase item (check XP, add to owned)
    purchaseItem(itemId, cost) {
        const state = this.getState();
        const currentXP = parseInt(localStorage.getItem('totalXP') || '0');
        
        if (currentXP < cost) {
            return false; // Not enough XP
        }
        
        if (state.ownedItems.includes(itemId)) {
            return true; // Already owned
        }
        
        // Deduct XP
        const newXP = currentXP - cost;
        localStorage.setItem('totalXP', newXP.toString());
        state.totalXP = newXP;
        
        // Add to owned
        state.ownedItems.push(itemId);
        this.saveState();
        
        return true;
    }
};

// Auto-initialize on load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => AvatarSystem.init());
} else {
    AvatarSystem.init();
}

// Export for global access
window.AvatarSystem = AvatarSystem;


