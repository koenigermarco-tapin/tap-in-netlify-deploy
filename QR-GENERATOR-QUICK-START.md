# 🎨 QR CARD GENERATOR - QUICK START GUIDE

## ✅ FILES CREATED

### 📱 Public Pages (QR Code Destinations)

1. **`contact-card-blackbelt.html`**
   - Landing page when someone scans your contact QR
   - Shows: Name, title, email, phone, website
   - Features: Click-to-call, click-to-email, vCard download
   - **URL:** `https://tap-in-platform.netlify.app/contact-card-blackbelt.html`

2. **`belt-assessment-card.html`**
   - Landing page for assessment invitation QR
   - Shows: Assessment invitation, benefits, CTA button
   - **URL:** `https://tap-in-platform.netlify.app/belt-assessment-card.html`

### 🔒 Private Generator (Password Protected)

3. **`admin-qr-generator.html`**
   - Your private card creation tool
   - Password: **`TAPIN2024`** (CHANGE THIS!)
   - **URL:** `https://tap-in-platform.netlify.app/admin-qr-generator.html`

---

## 🚀 QUICK START (3 Steps)

### Step 1: Access Generator
1. Go to: `admin-qr-generator.html`
2. Enter password: `TAPIN2024`
3. Generator opens

### Step 2: Customize & Generate
1. Edit any fields you want (name, title, company, etc.)
2. Click **"Generate Card"**
3. Preview updates automatically
4. QR code generates automatically

### Step 3: Download
1. Click **"Download PNG"**
2. Card downloads as image
3. Print or share!

---

## 🔐 CHANGE PASSWORD

**Important:** Change the default password!

1. Open `admin-qr-generator.html`
2. Find this line (around line 220):
   ```javascript
   const CORRECT_PASSWORD = "TAPIN2024";
   ```
3. Change to your password:
   ```javascript
   const CORRECT_PASSWORD = "YourSecurePassword123";
   ```
4. Save file

---

## 📝 CUSTOMIZE DEFAULT VALUES

Edit the defaults in `admin-qr-generator.html`:

1. Find the form fields (around line 200-250)
2. Update `value=""` attributes:
   ```html
   <input type="text" id="firstName" value="Marco">
   <input type="email" id="email" value="marco@tap-in.com">
   ```
3. Save file

---

## 🎯 USE CASES

### Personal Card
- Job Title: "Co-Founder - TAP-IN Leadership Academy"
- Company: "TAP-IN"

### Corporate Card
- Job Title: "Leadership Development"
- Company: "TAP-IN"

### Partnership Card
- Job Title: "Former Graz WC PM - TAP-IN Co-Founder"
- Company: "OneDay Partnership"
- Bio: "Skateboard expertise + Leadership development"

**Generate a new card for each context!**

---

## 🔗 QR CODE WORKFLOW

### Contact Card
1. Generate card in admin tool
2. Download PNG
3. Print business card
4. Someone scans QR
5. Lands on `contact-card-blackbelt.html`
6. Can save contact or take assessment

### Assessment Invitation
1. Generate QR pointing to `belt-assessment-card.html`
2. Print on materials
3. Someone scans
4. Lands on invitation page
5. Clicks "Start Assessment"
6. Takes assessment

---

## 📋 CHECKLIST

- [ ] Change password from default
- [ ] Customize default contact info
- [ ] Bookmark generator URL
- [ ] Generate first test card
- [ ] Test QR code scanning
- [ ] Generate cards for different contexts

---

## ⚠️ SECURITY NOTES

- ✅ Generator is password protected
- ✅ Not linked from any public pages
- ✅ No navigation to generator
- ✅ Bookmark URL for easy access
- ✅ Keep password secret!

---

**Ready to generate your first card?** 🎉

