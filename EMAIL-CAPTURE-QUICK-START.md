# 📧 EMAIL CAPTURE SYSTEM - QUICK START

**Status:** ✅ **System Created - Ready for Configuration**

---

## ✅ WHAT'S DONE

### Components Created
- ✅ Email capture form component (`js/email-capture-component.js`)
- ✅ Styled CSS (`css/email-capture.css`)
- ✅ SendGrid email function (`netlify/functions/send-results-email.js`)
- ✅ Supabase lead storage (`netlify/functions/save-lead.js`)
- ✅ Database migration (`supabase/migrations/001_email_capture_leads.sql`)
- ✅ Email template (`email-templates/assessment-results.html`)

### Integration
- ✅ Integrated into 12 assessment result pages
- ✅ Shows 3 seconds after results display
- ✅ GDPR-compliant with consent checkbox
- ✅ Multiple delivery options (PDF, Action Plan, Benchmarks)

---

## 🚀 QUICK SETUP (30 Minutes)

### Step 1: SendGrid (15 min)

1. **Create Account**
   - Go to https://sendgrid.com
   - Sign up (free tier: 100 emails/day)

2. **Get API Key**
   - Settings → API Keys → Create API Key
   - Copy key (won't see again!)

3. **Verify Sender**
   - Settings → Sender Authentication
   - Verify `results@tap-in.com` (or your domain)

4. **Add to Netlify**
   - Netlify Dashboard → Site Settings → Environment Variables
   - Add:
     ```
     SENDGRID_API_KEY=SG.xxxxxxxxxxxxx
     SENDGRID_FROM_EMAIL=results@tap-in.com
     ```

### Step 2: Supabase (10 min)

1. **Run Migration**
   - Supabase Dashboard → SQL Editor
   - Paste contents of `supabase/migrations/001_email_capture_leads.sql`
   - Click Run

2. **Get Credentials**
   - Settings → API
   - Copy Project URL and Service Role Key

3. **Add to Netlify**
   ```
   SUPABASE_URL=https://xxxxx.supabase.co
   SUPABASE_SERVICE_KEY=eyJxxxxx (service role key!)
   ```

### Step 3: Test (5 min)

1. Complete an assessment
2. Email capture form appears after results
3. Enter your email and submit
4. Check your inbox!
5. Check Supabase `leads` table

---

## 📋 ENVIRONMENT VARIABLES CHECKLIST

Add these in Netlify Dashboard:

- [ ] `SENDGRID_API_KEY`
- [ ] `SENDGRID_FROM_EMAIL`
- [ ] `SUPABASE_URL`
- [ ] `SUPABASE_SERVICE_KEY`
- [ ] (Optional) `MAILCHIMP_API_KEY`
- [ ] (Optional) `MAILCHIMP_LIST_ID`

---

## 🎯 EXPECTED RESULTS

- **Conversion Rate:** 40-60% opt-in
- **Email Delivery:** Instant via SendGrid
- **Lead Storage:** Saved to Supabase
- **Tracking:** Analytics events fire

---

## 📖 FULL DOCUMENTATION

See `EMAIL-CAPTURE-SYSTEM-SETUP.md` for detailed setup instructions.

---

**Ready to go! Configure credentials and test!** 🚀

