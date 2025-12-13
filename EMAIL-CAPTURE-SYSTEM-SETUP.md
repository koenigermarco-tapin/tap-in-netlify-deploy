# 📧 EMAIL CAPTURE SYSTEM - COMPLETE SETUP GUIDE

**Status:** ✅ **System Created, Ready for Configuration**

---

## 📁 FILES CREATED

### Frontend Components
- ✅ `js/email-capture-component.js` - Reusable email capture form
- ✅ `css/email-capture.css` - Styles for email capture form

### Backend Functions
- ✅ `netlify/functions/send-results-email.js` - SendGrid email sending
- ✅ `netlify/functions/save-lead.js` - Supabase lead storage

### Database
- ✅ `supabase/migrations/001_email_capture_leads.sql` - Leads table migration

### Email Template
- ✅ `email-templates/assessment-results.html` - Email template

### Integration
- ✅ Integrated into **12 assessment result pages**

---

## 🚀 SETUP STEPS

### Step 1: Configure SendGrid (30 min)

1. **Create SendGrid Account**
   - Go to https://sendgrid.com
   - Sign up for free tier (100 emails/day)
   - Verify your email

2. **Create API Key**
   - Go to Settings → API Keys
   - Click "Create API Key"
   - Name: "TAP-IN Assessment Results"
   - Permissions: Full Access (or Mail Send only)
   - Copy the API key (you won't see it again!)

3. **Set Up Sender Identity**
   - Go to Settings → Sender Authentication
   - Verify a Single Sender or Domain
   - Use: `results@tap-in.com` (or your domain)

4. **Add to Netlify Environment Variables**
   - Go to Netlify Dashboard → Site Settings → Environment Variables
   - Add:
     ```
     SENDGRID_API_KEY=SG.xxxxxxxxxxxxx (your API key)
     SENDGRID_FROM_EMAIL=results@tap-in.com
     ```

---

### Step 2: Configure Supabase (30 min)

1. **Run Database Migration**
   - Go to Supabase Dashboard → SQL Editor
   - Open `supabase/migrations/001_email_capture_leads.sql`
   - Copy and paste into SQL Editor
   - Click "Run"

2. **Get Supabase Credentials**
   - Go to Settings → API
   - Copy:
     - Project URL
     - Service Role Key (service_role, not anon key!)

3. **Add to Netlify Environment Variables**
   - Go to Netlify Dashboard → Environment Variables
   - Add:
     ```
     SUPABASE_URL=https://xxxxx.supabase.co
     SUPABASE_SERVICE_KEY=eyJxxxxx (service role key)
     ```

4. **Verify Table Created**
   - Go to Supabase Dashboard → Table Editor
   - You should see `leads` table
   - Verify columns are correct

---

### Step 3: Install Netlify Functions Dependencies (5 min)

Create `netlify/functions/package.json`:

```json
{
  "name": "netlify-functions",
  "version": "1.0.0",
  "dependencies": {
    "node-fetch": "^2.6.7"
  }
}
```

Then install:

```bash
cd netlify/functions
npm install
```

Or add to root `package.json`:

```json
{
  "dependencies": {
    "node-fetch": "^2.6.7"
  }
}
```

---

### Step 4: Test Email Capture (15 min)

1. **Deploy to Netlify**
   - Commit and push changes
   - Netlify will auto-deploy

2. **Test on Assessment Page**
   - Go to any assessment: `belt-assessment-v2.html`
   - Complete the assessment
   - When results show, email capture form should appear after 3 seconds
   - Enter your email
   - Submit form

3. **Check Results**
   - Check your email inbox
   - Check Supabase `leads` table for new entry
   - Check Netlify Functions logs for errors

---

### Step 5: Optional - Mailchimp Integration (15 min)

1. **Get Mailchimp API Key**
   - Go to Mailchimp → Account → Extras → API Keys
   - Create new API key

2. **Get List ID**
   - Go to Audience → Settings → Audience name and defaults
   - Copy List ID

3. **Add to Netlify Environment Variables**
   ```
   MAILCHIMP_API_KEY=xxxxx
   MAILCHIMP_LIST_ID=xxxxx
   ```

   Leads will automatically be added to Mailchimp with tags!

---

## 📋 ENVIRONMENT VARIABLES CHECKLIST

Add these to Netlify Dashboard → Site Settings → Environment Variables:

### Required:
- [ ] `SENDGRID_API_KEY` - Your SendGrid API key
- [ ] `SENDGRID_FROM_EMAIL` - Verified sender email (e.g., results@tap-in.com)
- [ ] `SUPABASE_URL` - Your Supabase project URL
- [ ] `SUPABASE_SERVICE_KEY` - Supabase service role key

### Optional:
- [ ] `MAILCHIMP_API_KEY` - For Mailchimp auto-tagging
- [ ] `MAILCHIMP_LIST_ID` - Your Mailchimp list ID

---

## 🎯 FEATURES

### Email Capture Form
- ✅ GDPR-compliant consent checkbox
- ✅ Multiple delivery options (PDF, Action Plan, Benchmarks)
- ✅ Real-time email validation
- ✅ Accessible (ARIA labels, keyboard navigation)
- ✅ Responsive design
- ✅ Smooth animations

### Email Delivery
- ✅ Personalized subject line
- ✅ HTML email template
- ✅ Results summary
- ✅ 3 personalized action items
- ✅ CTA button: "Book Free Strategy Session"
- ✅ Tracking enabled (opens, clicks)

### Lead Storage
- ✅ Stores in Supabase `leads` table
- ✅ Includes assessment type, scores, results
- ✅ GDPR consent tracking
- ✅ Automatic Mailchimp sync (optional)

---

## 📊 EXPECTED METRICS

### Conversion Rate
- **Target:** 40-60% of users opt-in
- **Tracking:** Analytics event `email_capture_submitted`

### Email Metrics
- **Open Rate:** Track via SendGrid dashboard
- **Click Rate:** Track CTA button clicks
- **PDF Downloads:** Track attachment downloads (when implemented)

---

## 🔧 TROUBLESHOOTING

### Email Not Sending

1. **Check SendGrid API Key**
   - Verify in Netlify environment variables
   - Check key has Mail Send permissions

2. **Check Sender Identity**
   - Verify sender email is verified in SendGrid
   - Check `SENDGRID_FROM_EMAIL` matches verified email

3. **Check Netlify Function Logs**
   - Go to Netlify Dashboard → Functions → Logs
   - Look for errors

### Lead Not Saving

1. **Check Supabase Credentials**
   - Verify `SUPABASE_URL` and `SUPABASE_SERVICE_KEY`
   - Check service key has write permissions

2. **Check Database Migration**
   - Verify `leads` table exists
   - Check table structure matches migration

3. **Check RLS Policies**
   - Service role should bypass RLS
   - Verify policies allow inserts

### Form Not Showing

1. **Check JavaScript Loading**
   - Verify `js/email-capture-component.js` loads
   - Check browser console for errors

2. **Check Timing**
   - Form appears 3 seconds after results
   - Check if results container exists

3. **Check CSS**
   - Verify `css/email-capture.css` loads
   - Check for CSS conflicts

---

## 📈 TRACKING & ANALYTICS

### Events Tracked

1. **`email_capture_shown`**
   - When form appears
   - Data: `assessment_type`

2. **`email_capture_submitted`**
   - When user submits form
   - Data: `assessment_type`, `options`

3. **`email_capture_success`**
   - When email sent successfully
   - Data: `email`

### SendGrid Analytics

- Open rates
- Click rates
- Bounce rates
- Unsubscribe rates

Access in SendGrid Dashboard → Activity

---

## 🔄 NEXT STEPS

1. **Test with Real Users**
   - Deploy to production
   - Monitor conversion rates
   - Collect feedback

2. **Optimize Email Template**
   - A/B test subject lines
   - Test different CTAs
   - Optimize for mobile

3. **Add PDF Generation**
   - Implement PDF report generation
   - Attach to emails
   - Track downloads

4. **Set Up Email Sequences**
   - Welcome email
   - Follow-up sequences
   - Nurture campaigns

---

## ✅ TESTING CHECKLIST

Before going live:

- [ ] SendGrid API key configured
- [ ] Supabase credentials configured
- [ ] Database migration run successfully
- [ ] Email capture form appears on results page
- [ ] Form validation works
- [ ] Email sends successfully
- [ ] Lead saved to Supabase
- [ ] Email opens correctly
- [ ] CTA button works
- [ ] Privacy policy link works
- [ ] GDPR consent tracked
- [ ] Analytics events fire
- [ ] Mobile responsive
- [ ] Accessible (keyboard navigation)

---

**🎉 System Ready! Follow setup steps above to activate.**

