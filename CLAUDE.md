# softdevcan - Django Portfolio & Blog Application

## Project Overview
- **URL:** softdevcan.com
- **Stack:** Django 5.2, Python 3.12, PostgreSQL 16, Redis 7, Gunicorn, Nginx
- **Deployment:** Docker Compose on VDS, Cloudflare for SSL/CDN
- **Admin Theme:** django-unfold (modern admin UI)

## Apps & Architecture

### 3 Django Apps
| App | Purpose | Key Models |
|-----|---------|------------|
| `core` | Portfolio, skills, site settings | GeneralSetting, ImageSetting, Skill, Experience, Education, SocialMedia, Document, Project, ProjectCategory |
| `blog` | Blog posts with Markdown | Post, Category, Tag |
| `contact` | Contact form + email | Message |

### Critical Architecture Pattern: Context Processor
`core/views.py:layout()` is a **context processor** (registered in `resume/settings.py` TEMPLATES). It provides site-wide data (GeneralSetting, ImageSetting, SocialMedia, Documents) to ALL templates via Redis cache (1-hour TTL).

### Signal-Based Cache Invalidation
All 3 apps have `signals.py` that clear Redis cache on model save/delete:
- `core/signals.py` → clears cache on GeneralSetting, ImageSetting, Document, SocialMedia, Skill, Experience, Education, Project, ProjectCategory changes
- `blog/signals.py` → clears cache on Post, Category, Tag changes
- `contact/signals.py` → clears layout_context on Message creation

## Project Structure
```
softdevcan/
├── resume/              # Django project config
│   ├── settings.py      # Main settings (env-driven)
│   ├── urls.py          # Root URL config
│   ├── wsgi.py          # WSGI for Gunicorn
│   ├── sitemaps.py      # XML sitemaps (static, blog, projects)
│   ├── custom_storage.py # FileSystemStorage classes (migration compat)
│   ├── .env.txt         # Environment template (safe, tracked)
│   └── docker.env       # Real credentials (git-ignored via *.env)
├── core/                # Portfolio app
├── blog/                # Blog app (with templatetags/markdown_extras.py)
├── contact/             # Contact form app
├── templates/           # All HTML templates
│   ├── layout.html      # Base template (navbar, footer, blocks)
│   └── includes/        # head.html, navbar.html, footer.html, scripts.html
├── static/              # Source static files (css/, js/, fonts/, vendors/)
├── staticfiles/         # Collected output (ManifestStaticFilesStorage, git-ignored)
├── media/               # User uploads (git-ignored)
├── nginx/               # Nginx config + Dockerfile
├── scripts/backup.sh    # PostgreSQL + media backup (30-day retention)
├── logs/                # Application logs (git-ignored)
├── docs/                # Development documentation (git-ignored)
├── Dockerfile           # Python 3.12-slim app container
├── docker-compose.yml   # Production: postgres, redis, app, nginx
├── docker-compose.dev.yml # Dev override: exposed ports, runserver
├── entrypoint.sh        # Runs migrate + collectstatic on container start
├── requirements.txt     # Python dependencies
├── pyproject.toml       # Ruff linting config
└── .pre-commit-config.yaml # ruff, trailing-whitespace, EOF, yaml check
```

## Development Environment
- **OS:** Windows 11, shell runs via Git Bash
- **No local venv** — all Django commands must run through Docker:
  ```bash
  docker compose up -d                    # Start all services
  docker compose run --rm app python manage.py test  # Run tests
  docker compose run --rm app python manage.py migrate  # Migrations
  ```
- **Dev mode:** `docker compose -f docker-compose.yml -f docker-compose.dev.yml up`
- **Lint:** `ruff check .` (locally or via pre-commit)

## Environment Variables (resume/.env.txt template)
```
DEBUG=off
SECRET_KEY=<random-string>
ALLOWED_HOSTS=127.0.0.1,localhost,softdevcan.com,softdevcan.com,www.softdevcan.com
CSRF_TRUSTED_ORIGINS=https://softdevcan.com,https://softdevcan.com,https://www.softdevcan.com
ADMIN_URL=admin/              # Change to random string in production
EMAIL=<gmail>
EMAIL_PASSWORD=<app-password>
DATABASE_URL=postgres://resume_user:<password>@postgres:5432/resume_db
POSTGRES_USER=resume_user
POSTGRES_PASSWORD=<strong-password>
POSTGRES_DB=resume_db
REDIS_URL=redis://redis:6379/0
```

## Caching Rules (Important!)
- `layout()` context processor: 1-hour Redis cache
- `index()` view: 15-min `@cache_page`
- `portfolio()` view: 15-min `@cache_page`
- `blog_home()`: **NO cache when search query is present**
- `blog_detail()`: **NEVER cache** (view_count increment would break)

## Testing
- ~27 tests using Django's built-in TestCase (no pytest)
- `core/tests.py` (9), `blog/tests.py` (9), `contact/tests.py` (6)
- CI: GitHub Actions runs `ruff check .` + `python manage.py test --verbosity=2`

## Known Gotchas
1. `bare except` was fixed to `except Exception` in get_general_setting/get_image_setting
2. `blog_detail` view CANNOT be cached (view_count increment would break)
3. `blog_home` view shouldn't use `@cache_page` when search query is present
4. `resume/custom_storage.py` exists only for migration 0010 compatibility — models no longer use it
5. `*.md` and `docs/` are in `.gitignore` — only `CLAUDE.md` has an exception
6. `staticfiles/` is git-ignored (generated by collectstatic with ManifestStaticFilesStorage)

## Security Configuration
- Cloudflare handles SSL termination (SECURE_SSL_REDIRECT=False)
- HSTS enabled (1 year, subdomains, preload) for defense-in-depth
- All cookies: Secure, HttpOnly, SameSite=Lax
- Nginx rate limiting: 10 req/s general, 5 req/min login
- Password minimum length: 12 characters
- Admin URL configurable via ADMIN_URL env var

## Deployment Infrastructure
- **Docker Compose:** postgres:16-alpine, redis:7-alpine, python:3.12-slim app, nginx:1.27-alpine
- **Entrypoint:** auto-runs `migrate --noinput` + `collectstatic --noinput`
- **Nginx:** Cloudflare IP whitelisting, gzip, static cache (1yr immutable), media cache (30d)
- **Backup:** `scripts/backup.sh` via cron (`0 3 * * *`), 30-day retention
- **CI/CD:** GitHub Actions (lint + test on push/PR to main)

## Modernization Status
- Phases 0-7 complete (cleanup, infra, security, DB, frontend, features, performance, DevOps)
- Phase 8 (API Layer) is optional/future
- Bootstrap 5.3 migration: 100% complete
