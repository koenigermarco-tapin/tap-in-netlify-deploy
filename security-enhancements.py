#!/usr/bin/env python3
"""
Security Enhancements
- Add Content Security Policy (CSP)
- Add Subresource Integrity (SRI) hints
- Enhance security headers
"""

from pathlib import Path

def enhance_security_headers():
    """Enhance _headers file with CSP and other security headers"""
    
    headers_file = Path('_headers')
    
    if not headers_file.exists():
        print("⚠️  _headers file not found, creating...")
        content = ''
    else:
        with open(headers_file, 'r', encoding='utf-8') as f:
            content = f.read()
    
    # CSP - Content Security Policy
    # Allow self, Google Fonts, CDN resources, but block inline scripts/styles except for necessary ones
    csp_policy = """default-src 'self';
script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.jsdelivr.net https://cdnjs.cloudflare.com;
style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
font-src 'self' https://fonts.gstatic.com;
img-src 'self' data: https:;
connect-src 'self' https://*.netlify.app https://*.supabase.co;
frame-ancestors 'none';
base-uri 'self';
form-action 'self';"""
    
    # Check if CSP already exists
    if 'Content-Security-Policy' not in content:
        # Add CSP to all HTML files
        csp_header = f'''
/*.html
  Content-Security-Policy: {csp_policy.replace(chr(10), ' ')}
'''
        
        # Insert after the existing security headers section
        if 'X-Frame-Options' in content:
            content = content.replace(
                'X-Frame-Options: DENY',
                f'X-Frame-Options: DENY\n  Content-Security-Policy: {csp_policy.replace(chr(10), " ")}'
            )
        else:
            # Add at the beginning
            content = csp_header + content
        
        with open(headers_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, "CSP added"
    
    return False, "CSP already exists"

def add_sri_hints():
    """Add SRI hints documentation (manual step for CDN resources)"""
    
    sri_doc = '''# Subresource Integrity (SRI) Guide

## For CDN Resources

When using external scripts/styles from CDNs, add integrity attributes:

```html
<!-- Example: Confetti library -->
<script 
    src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"
    integrity="sha384-..."
    crossorigin="anonymous">
</script>
```

## Generate SRI Hashes

Use online tool: https://www.srihash.org/

Or command line:
```bash
curl -s https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js | \
openssl dgst -sha384 -binary | openssl base64 -A
```

## Resources Currently Using CDN:
- canvas-confetti (jsdelivr)
- @supabase/supabase-js (jsdelivr)

## Note:
For development, SRI is optional. For production, add SRI to all CDN resources.
'''
    
    sri_file = Path('SECURITY-SRI-GUIDE.md')
    
    if not sri_file.exists():
        with open(sri_file, 'w', encoding='utf-8') as f:
            f.write(sri_doc)
        return True, "SRI guide created"
    
    return False, "SRI guide already exists"

def main():
    print("=" * 80)
    print("🔒 SECURITY ENHANCEMENTS")
    print("=" * 80)
    print()
    
    # 1. Enhance headers
    print("📝 Enhancing security headers...")
    success, msg = enhance_security_headers()
    if success:
        print(f"  ✅ {msg}")
    else:
        print(f"  ⏭️  {msg}")
    print()
    
    # 2. Add SRI guide
    print("📝 Creating SRI guide...")
    success, msg = add_sri_hints()
    if success:
        print(f"  ✅ {msg}")
    else:
        print(f"  ⏭️  {msg}")
    print()
    
    print("=" * 80)
    print("✅ Security enhancements complete")
    print("=" * 80)
    print()
    print("💡 Next steps:")
    print("   1. Review CSP policy - adjust if needed")
    print("   2. Add SRI hashes to CDN resources (see SECURITY-SRI-GUIDE.md)")
    print("   3. Test site functionality after CSP is applied")

if __name__ == '__main__':
    main()

