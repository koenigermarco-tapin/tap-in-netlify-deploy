# 🚀 DEPLOYMENT GUIDE - Black Belt Leadership Assessments

## ✅ YOUR PACKAGE IS READY!

All files are assembled and ready to deploy. Here's what you have:

### 📦 Core Deployment Files (What You Need):
```
✅ index.html (13K) - Landing page
✅ black-belt-stripe1.html (51K) - Strategic Thinking
✅ black-belt-stripe2.html (60K) - Organizational Impact
✅ black-belt-stripe3.html (72K) - Visionary Leadership
✅ black-belt-stripe4.html (52K) - Leadership Integration
✅ _redirects (493 bytes) - Netlify routing
✅ netlify.toml (905 bytes) - Netlify config
✅ README.md (6.5K) - Documentation
```

**Total Size:** ~250KB (very lightweight!)

---

## 🚀 FASTEST DEPLOYMENT: NETLIFY DROP (2 MINUTES)

### Step 1: Download Files
Download these 8 files to a folder called `black-belt-deploy`:
- index.html
- black-belt-stripe1.html
- black-belt-stripe2.html
- black-belt-stripe3.html
- black-belt-stripe4.html
- _redirects
- netlify.toml
- README.md

### Step 2: Deploy
1. Go to: **https://app.netlify.com/drop**
2. **Drag the `black-belt-deploy` folder** onto the page
3. Wait 10 seconds for upload
4. **Done!** You get a live URL like: `https://zealous-curie-123abc.netlify.app`

### Step 3: (Optional) Custom Domain
1. In Netlify dashboard, click "Domain Settings"
2. Click "Add custom domain"
3. Enter your domain (e.g., `blackbelt.tap-in-academy.com`)
4. Follow DNS instructions
5. Wait for DNS propagation (5 mins - 48 hours)

### Step 4: Test Your Site
Visit your URL and verify:
- ✅ Landing page loads
- ✅ Can click into each stripe
- ✅ Assessments work
- ✅ Progress saves (localStorage)

**YOU'RE LIVE! 🎉**

---

## 🐙 ALTERNATIVE: GITHUB PAGES (With Version Control)

### Step 1: Create Local Repository
```bash
# Create folder and move in your files
mkdir black-belt-deploy
cd black-belt-deploy

# Copy your 8 files here, then:
git init
git add .
git commit -m "Initial deployment: Black Belt assessments"
```

### Step 2: Create GitHub Repository
**Option A - GitHub CLI:**
```bash
gh repo create tap-in-black-belt --public --source=. --remote=origin
git push -u origin main
```

**Option B - Manual:**
1. Go to https://github.com/new
2. Create repo named `tap-in-black-belt`
3. Don't initialize with README
4. Copy the commands shown, run them:
```bash
git remote add origin https://github.com/YOUR-USERNAME/tap-in-black-belt.git
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages
1. Go to your repo on GitHub
2. Click **Settings** → **Pages** (left sidebar)
3. Under "Source", select **Deploy from a branch**
4. Branch: **main**, Folder: **/ (root)**
5. Click **Save**
6. Wait 1-2 minutes

### Step 4: Get Your URL
After deployment completes, you'll see:
```
Your site is live at https://YOUR-USERNAME.github.io/tap-in-black-belt/
```

**YOU'RE LIVE! 🎉**

---

## 📋 PRE-DEPLOYMENT CHECKLIST

Before deploying, verify locally:

```bash
# Open index.html in browser
open index.html  # Mac
start index.html  # Windows
xdg-open index.html  # Linux
```

Check:
- [ ] Landing page displays correctly
- [ ] All 4 stripe links work
- [ ] Can complete a question in each stripe
- [ ] Progress saves (close and reopen browser)
- [ ] Mobile view looks good (resize browser)
- [ ] No console errors (F12 → Console)

---

## 🎨 CUSTOMIZATION (Optional)

### Add Your Logo
Edit `index.html`, find the header section and add:
```html
<div class="header">
    <img src="your-logo.png" alt="Logo" style="max-width: 200px; margin-bottom: 1rem;">
    <div class="badge">⚫🔴 Black Belt Leadership</div>
    ...
</div>
```

### Add Google Analytics
Add to `<head>` section of each HTML file:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Change Colors
The RED accent system is defined in CSS variables. Find and edit in each file:
```css
:root {
    --accent-red: #dc2626;  /* Change to your color */
    --accent-red-bright: #ef4444;  /* Change to your color */
}
```

---

## 🔧 TROUBLESHOOTING

### "Drag and drop didn't work"
- Try using Chrome or Firefox
- Make sure you're dragging the FOLDER, not individual files
- Check folder contains all 8 files

### "Pages not linking correctly"
- Ensure all HTML files are in same directory
- Check file names are exact (case-sensitive)
- Open browser console (F12) for errors

### "Progress not saving"
- Check localStorage isn't disabled in browser
- Try incognito mode to test
- Some browsers block localStorage on local files (must be on server)

### "Mobile looks broken"
- Clear browser cache
- Try different mobile browser
- Check viewport meta tag exists in <head>

---

## 📊 WHAT HAPPENS AFTER DEPLOYMENT

### User Experience:
1. User lands on index.html (landing page)
2. Clicks a stripe → Goes to assessment
3. Completes assessment → Score & recommendations
4. localStorage saves completion status
5. Returns to landing page → Sees progress

### No Backend Needed:
- All data in browser localStorage
- No server processing
- No database
- No user accounts
- Privacy-friendly

### For Production Use:
Consider adding:
- Backend API for data persistence
- User authentication
- Admin dashboard
- Email reports
- Certificate generation
- LMS integration

---

## 🎯 SUCCESS METRICS TO TRACK

Once deployed, monitor:
- Page views (each stripe)
- Completion rates
- Time on page
- Drop-off points
- Device types (mobile vs desktop)
- Scores distribution

**Use Google Analytics or Plausible for tracking.**

---

## 🆘 NEED HELP?

### Common Questions:

**Q: Can I password-protect the site?**
A: Yes! In Netlify: Site Settings → Access Control → Enable password protection

**Q: Can I collect user responses?**
A: Not with this version (localStorage only). Need backend for that.

**Q: Can I customize questions?**
A: Yes! Edit the questions array in each HTML file.

**Q: How do I see user scores?**
A: Currently no admin dashboard. Would need backend implementation.

**Q: Can I integrate with our LMS?**
A: Possible with custom development (SCORM package or API integration).

---

## 🎉 YOU'RE READY TO GO LIVE!

**Deployment is literally 2 minutes away:**

1. Download files ✅
2. Go to Netlify Drop ✅  
3. Drag folder ✅
4. Get live URL ✅
5. Share with users! 🚀

**Your Black Belt Leadership Platform is ready for the world!**

---

*From the mat to the boardroom - let's transform leadership development.*

**TAP-IN Leadership Development Platform**  
*Black Belt: Strategic Leadership Excellence*
