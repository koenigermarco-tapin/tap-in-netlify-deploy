# 🔐 Netlify Access Denied - Fix Guide

**Issue:** Netlify says "access denied" when trying to deploy

---

## 🔍 COMMON CAUSES

### 1. Not Logged In to Netlify CLI
**Solution:**
```bash
# Check if logged in
netlify status

# If not logged in, login:
netlify login
```

### 2. Wrong Site ID or Not Linked
**Solution:**
```bash
# Link to your Netlify site
netlify link

# Or manually set site ID
netlify link --id YOUR_SITE_ID
```

### 3. Git Repository Not Connected
**Solution:**
```bash
# Check if git remote is set
git remote -v

# If not connected to GitHub/GitLab:
# Option A: Connect via Netlify UI
# 1. Go to https://app.netlify.com
# 2. Add new site → Import from Git
# 3. Authorize and select repository

# Option B: Deploy manually
netlify deploy --prod
```

### 4. Insufficient Permissions
**Solution:**
- Check Netlify dashboard → Site settings → Access control
- Ensure your account has deploy permissions
- If team site, ask admin to grant access

---

## 🚀 QUICK FIXES

### Fix 1: Re-authenticate
```bash
# Logout and login again
netlify logout
netlify login
```

### Fix 2: Manual Deploy (No Git Required)
```bash
# Deploy directly without Git
netlify deploy --prod --dir .
```

### Fix 3: Use Netlify Drop (Easiest)
1. Go to: https://app.netlify.com/drop
2. Drag your project folder
3. Wait for upload
4. Get your site URL

### Fix 4: Deploy via Git Push
```bash
# If you have Git connected:
git add .
git commit -m "fix: language switcher and syntax errors"
git push origin main

# Netlify will auto-deploy if connected
```

---

## 🔧 CHECK CURRENT STATUS

Run these commands to diagnose:

```bash
# Check Netlify CLI status
netlify status

# Check Git remote
git remote -v

# Check if site is linked
cat .netlify/state.json
```

---

## 📋 STEP-BY-STEP FIX

### Step 1: Login to Netlify
```bash
netlify login
# This will open browser for authentication
```

### Step 2: Link Your Site
```bash
# If you know your site ID:
netlify link --id YOUR_SITE_ID

# Or let Netlify find it:
netlify link
```

### Step 3: Deploy
```bash
# Deploy to production
netlify deploy --prod

# Or deploy to draft first:
netlify deploy
```

---

## 🆘 IF STILL NOT WORKING

### Option A: Use Netlify Web UI
1. Go to https://app.netlify.com
2. Click "Add new site"
3. Choose "Deploy manually" or "Import from Git"
4. Upload files or connect repository

### Option B: Check Site Settings
1. Go to Netlify dashboard
2. Site settings → General
3. Check "Site name" and "Site ID"
4. Verify you're the owner or have deploy access

### Option C: Create New Site
If access is completely blocked:
1. Create new Netlify site
2. Deploy fresh copy
3. Update domain if needed

---

## ✅ VERIFICATION

After fixing, verify:
```bash
# Check deployment status
netlify status

# List sites
netlify sites:list

# Check current site
netlify open
```

---

**Most common fix:** Run `netlify login` and `netlify link` to authenticate and connect your site.

