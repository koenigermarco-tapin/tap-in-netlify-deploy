# 🚀 DEPLOY TO NETLIFY - QUICK GUIDE

## Option 1: Drag & Drop (Easiest)

1. **Go to Netlify**: https://app.netlify.com
2. **Log in** to your account
3. **Drag & Drop** the entire `/Users/marcok./tap-in-netlify-deploy/` folder onto Netlify
4. **Wait** for deployment (2-3 minutes)
5. **Get your URL** (e.g., `random-name-123.netlify.app`)

## Option 2: Netlify CLI (Recommended)

```bash
# Install Netlify CLI (if not installed)
npm install -g netlify-cli

# Login to Netlify
netlify login

# Deploy from current directory
cd /Users/marcok./tap-in-netlify-deploy
netlify deploy --prod

# Follow prompts:
# - Site name: tap-in-the-gym (or choose your own)
# - Publish directory: . (current directory)
```

## Option 3: Git Deployment (Best for Updates)

```bash
# Initialize Git (if not already done)
cd /Users/marcok./tap-in-netlify-deploy
git init
git add .
git commit -m "Initial deployment"

# Create GitHub repo and push
# Then connect to Netlify via GitHub
```

## ⚠️ IMPORTANT: Entry Point

Make sure `index.html` exists and is in the root directory. It should redirect to `index-DUAL-ENTRY.html` or serve the dual entry page directly.

## ✅ After Deployment

1. **Test the site**: Visit your Netlify URL
2. **Check console**: Open DevTools (F12) and check for errors
3. **Test navigation**: Click "The Gym" and "The Hub" links
4. **Test TAP OUT**: Start a stripe, tap out, resume from dashboard

## 🔧 If Site Shows 404

1. **Check Netlify dashboard**: Look for deployment errors
2. **Check `netlify.toml`**: Make sure `publish = "."` is correct
3. **Check `index.html`**: Make sure it exists in root
4. **Redeploy**: Try deploying again

## 📝 Current Configuration

- **Publish Directory**: `.` (root)
- **Build Command**: `echo 'No build needed - static site'`
- **Entry Point**: `index.html` → `index-DUAL-ENTRY.html`


