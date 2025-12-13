# ⚡ Quick Deployment Instructions

## 🎯 **Fastest Way: Manual Deploy via Netlify Dashboard**

1. **Extract the ZIP file**
   - Extract `TAP-IN-FULL-REPO-20251201-192517.zip`
   - You'll get a folder with all files

2. **Go to Netlify Dashboard**
   - Visit: https://app.netlify.com
   - Click on your TAP-IN site

3. **Deploy Manually**
   - Click **"Deploys"** tab
   - Click **"Deploy site"** → **"Deploy manually"**
   - Drag and drop the **entire folder** into the deployment area
   - OR click **"Browse to upload"** and select the folder

4. **Wait for Deployment**
   - Netlify will process the files
   - Deployment usually takes 1-2 minutes

5. **Verify**
   - Visit your Netlify site URL
   - Hard refresh: `Cmd+Shift+R` (Mac) / `Ctrl+Shift+R` (Windows)
   - Check that error messages are gone

---

## 🔧 **Alternative: Use Deployment Script**

If you have Netlify CLI installed:

```bash
./deploy-to-netlify.sh
```

Or manually:
```bash
netlify deploy --prod --dir=.
```

---

## 🚨 **Force Cache Clear (If Needed)**

After deployment, if users still see old content:

1. **In Browser DevTools:**
   - Open DevTools (F12)
   - Go to **Application** tab
   - Click **Service Workers**
   - Click **"Unregister"** for old workers
   - Reload page

2. **Or clear browser cache:**
   - Hard refresh: `Cmd+Shift+R` / `Ctrl+Shift+R`
   - Or clear browsing data in browser settings

---

## ✅ **That's It!**

The service worker cache version has been updated, so new visitors will automatically get the fresh version. Existing users may need to hard refresh once.

**Your site should now work without cache issues!** 🎉

