# ✅ Supabase Setup Complete - Quick Reference

## Your Supabase Credentials

**Project URL:**
```
https://huollcibglqghqwzufjn.supabase.co
```

**Anon Key (Public - Safe for Client):**
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh1b2xsY2liZ2xxZ2hxd3p1ZmpuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjM2ODUwNjMsImV4cCI6MjA3OTI2MTA2M30.SWx1g10YeNRxkiVXNmoHOD-blcZh_2axMSW2x52aAU0
```

**Service Role Key:**
```
You need to get this from Supabase Dashboard:
Settings → API → Project API keys → service_role (secret)
```

---

## 🚀 Next Steps

### 1. Add Environment Variables to Netlify

Go to: https://app.netlify.com/sites/YOUR_SITE/settings/env

Add these 3 variables:

| Key | Value |
|-----|-------|
| `SUPABASE_URL` | `https://huollcibglqghqwzufjn.supabase.co` |
| `SUPABASE_ANON_KEY` | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` (from above) |
| `SUPABASE_SERVICE_KEY` | Get from Supabase Settings → API → service_role |

### 2. Run the Database Schema

1. Go to Supabase SQL Editor: https://supabase.com/dashboard/project/huollcibglqghqwzufjn/sql
2. Copy contents of `supabase-setup.sql` from this repo
3. Paste and click "RUN"
4. Verify tables created: `leads`, `assessments`

### 3. Test the Integration

1. Complete any assessment on your site
2. Enter email and submit
3. Check Supabase Table Editor to see data: https://supabase.com/dashboard/project/huollcibglqghqwzufjn/editor
4. Try submitting same email again - should get "already used" error

---

## 📊 Quick Links

- **Supabase Dashboard:** https://supabase.com/dashboard/project/huollcibglqghqwzufjn
- **Table Editor:** https://supabase.com/dashboard/project/huollcibglqghqwzufjn/editor
- **SQL Editor:** https://supabase.com/dashboard/project/huollcibglqghqwzufjn/sql
- **API Settings:** https://supabase.com/dashboard/project/huollcibglqghqwzufjn/settings/api

---

## ✅ Verification Checklist

- [ ] Supabase project created
- [ ] Database schema (`supabase-setup.sql`) executed successfully
- [ ] `SUPABASE_URL` added to Netlify env vars
- [ ] `SUPABASE_ANON_KEY` added to Netlify env vars
- [ ] `SUPABASE_SERVICE_KEY` added to Netlify env vars
- [ ] Netlify site redeployed (automatic after env var changes)
- [ ] Test submission works (check Supabase tables)
- [ ] Duplicate email detection works (try same email twice)

---

## 🔧 Troubleshooting

**"Cannot find module '@supabase/supabase-js'"**
- Run: `npm install` in project root
- Netlify should auto-install from package.json

**"Invalid API key"**
- Double-check keys copied correctly (no extra spaces)
- Make sure using service_role key for SUPABASE_SERVICE_KEY

**"Table 'leads' does not exist"**
- Run the SQL schema in Supabase SQL Editor
- Check Table Editor to verify tables exist

**Data not appearing in Supabase**
- Check Netlify Function logs for errors
- Verify env vars are set in Netlify dashboard
- Redeploy site after adding env vars
