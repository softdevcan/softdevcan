# 🔒 Security Configuration Guide

## Overview

This document outlines the security measures implemented in the portfolio application.

---

## 🛡️ Security Layers

### 1. Cloudflare (Edge Layer)
- **SSL/TLS Encryption**: Cloudflare provides SSL/TLS certificates
- **DDoS Protection**: Automatic mitigation
- **WAF (Web Application Firewall)**: Additional protection layer
- **CDN**: Content delivery with security features

**Setup:**
1. Point your domain DNS to Cloudflare nameservers
2. Enable "Full (strict)" SSL/TLS mode in Cloudflare dashboard
3. Enable "Always Use HTTPS"
4. Optional: Enable Bot Fight Mode

---

### 2. Nginx (Proxy Layer)

**Implemented Features:**
- ✅ Rate limiting (10 req/s general, 5 req/m for admin login)
- ✅ Cloudflare real IP detection
- ✅ Security headers (X-Frame-Options, X-Content-Type-Options, etc.)
- ✅ Gzip compression
- ✅ Static/Media file caching
- ✅ Server tokens hidden
- ✅ Request timeouts (60s)
- ✅ Client body size limit (15MB)

**Rate Limiting Zones:**
```nginx
general: 10 requests/second (burst: 20)
login: 5 requests/minute (burst: 3)
```

---

### 3. Django (Application Layer)

**Security Settings (Production):**
- ✅ `SECURE_PROXY_SSL_HEADER`: Respect X-Forwarded-Proto from Cloudflare
- ✅ `SESSION_COOKIE_SECURE`: HTTPS-only session cookies
- ✅ `CSRF_COOKIE_SECURE`: HTTPS-only CSRF cookies
- ✅ `SECURE_HSTS_SECONDS`: HTTP Strict Transport Security (1 year)
- ✅ `SECURE_CONTENT_TYPE_NOSNIFF`: Prevent MIME type sniffing
- ✅ `X_FRAME_OPTIONS`: Prevent clickjacking
- ✅ Password minimum length: 12 characters
- ✅ Common password validation
- ✅ User attribute similarity validation

---

## 🔑 Secret Management

### Environment Variables (.env file)

**Required secrets:**
```bash
SECRET_KEY=<50-char random string>
POSTGRES_PASSWORD=<strong random password>
AWS_SECRET_ACCESS_KEY=<AWS secret>
EMAIL_PASSWORD=<Gmail app-specific password>
```

### Generating Secure Secrets

**Django SECRET_KEY:**
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

**Random Password:**
```bash
openssl rand -base64 32
```

---

## 📋 Security Checklist

### Before Production Deployment

- [ ] Change `DEBUG=off` in .env
- [ ] Generate new `SECRET_KEY`
- [ ] Set strong `POSTGRES_PASSWORD`
- [ ] Configure Cloudflare SSL/TLS (Full strict mode)
- [ ] Add domain to `ALLOWED_HOSTS`
- [ ] Add https URLs to `CSRF_TRUSTED_ORIGINS`
- [ ] Optional: Change `ADMIN_URL` to random string (e.g., `secret-admin-panel-xyz/`)
- [ ] Enable Gmail 2FA and generate app-specific password
- [ ] Review AWS IAM permissions (S3 bucket access only)
- [ ] Test rate limiting (try rapid requests)
- [ ] Verify HTTPS redirect works
- [ ] Check security headers (use securityheaders.com)

---

## 🚨 Admin Panel Security

### Custom Admin URL (Optional but Recommended)

**Default:** `/admin/`
**Recommended:** Change to random URL

1. Set in `.env`:
   ```bash
   ADMIN_URL=secret-panel-xyz123/
   ```

2. Update `resume/urls.py` to use `settings.ADMIN_URL`

### Admin Login Protection

- Rate limited to 5 attempts per minute
- Strong password required (12+ characters)
- Session expires after 2 weeks of inactivity

---

## 🔍 Security Headers

**Current headers sent by Nginx:**
```
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Referrer-Policy: strict-origin-when-cross-origin
```

**Additional headers from Cloudflare:**
```
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

---

## 🔐 Database Security

**PostgreSQL Configuration:**
- Container-isolated (not exposed to public internet)
- Strong password authentication
- Port 5432 only accessible within Docker network
- Data persistence with encrypted volume

---

## 📊 Monitoring & Logging

**Recommended additions (Future):**
- [ ] Django admin action logging
- [ ] Failed login attempt monitoring
- [ ] Sentry for error tracking
- [ ] Cloudflare Analytics for traffic analysis

---

## 🆘 Incident Response

**If breach suspected:**
1. Immediately rotate all secrets (SECRET_KEY, database passwords, AWS keys)
2. Check Cloudflare logs for suspicious activity
3. Review Django admin logs
4. Check database for unauthorized changes
5. Force logout all users (clear sessions)

---

## 📚 References

- [Django Security Documentation](https://docs.djangoproject.com/en/5.2/topics/security/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Cloudflare SSL/TLS Documentation](https://developers.cloudflare.com/ssl/)
- [Nginx Security](https://nginx.org/en/docs/http/ngx_http_ssl_module.html)

---

**Last Updated:** 2026-02-02
**Security Version:** 1.0
