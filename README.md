# GyLo Softwares Website

Corporate lead-generation website for **GyLo Softwares Company Limited**, a software engineering, AI automation, and business systems company serving Tanzania and beyond.

## Tech Stack

- Python 3.12+
- Django 5.2 LTS
- Django templates and Django Admin
- PostgreSQL via `DATABASE_URL`, with SQLite fallback for local development
- WhiteNoise for static files
- Gunicorn for production serving
- Plain CSS and minimal JavaScript

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Update `.env` with local values. Never commit real secrets.

## Environment Variables

- `DEBUG`
- `SECRET_KEY`
- `ALLOWED_HOSTS`
- `CSRF_TRUSTED_ORIGINS`
- `DATABASE_URL`
- `EMAIL_HOST`
- `EMAIL_PORT`
- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`
- `EMAIL_USE_TLS`
- `POSTMARK_SERVER_TOKEN`
- `POSTMARK_API_URL`
- `POSTMARK_MESSAGE_STREAM`
- `DEFAULT_FROM_EMAIL`
- `ADMIN_EMAIL`
- `ADMIN_EMAILS`
- `SITE_URL`
- `SECURE_SSL_REDIRECT`
- `SESSION_COOKIE_SECURE`
- `CSRF_COOKIE_SECURE`

If `POSTMARK_SERVER_TOKEN` is set, production emails are sent through the Postmark HTTPS API. If it is not set, Django falls back to SMTP when `EMAIL_HOST` is configured, or console email locally when email variables are missing.

## Run Locally

```bash
python manage.py migrate
python manage.py seed_initial_content
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`.

## Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Seed Initial Content

```bash
python manage.py seed_initial_content
```

This creates or updates matching slugs for:

- 6 services
- 3 projects: Vuma, Kiosk, Instagram Fraud Detection
- Blog categories
- 10 corporate blog posts: 5 published and 5 draft

## Tests

```bash
python3 manage.py test
```

## Railway Deployment Notes

The project includes:

- `requirements.txt`
- `Procfile`
- `railway.json`
- `runtime.txt`
- WhiteNoise static configuration
- Gunicorn start command
- PostgreSQL-ready `DATABASE_URL` support

Recommended Railway variables:

```text
DEBUG=False
SECRET_KEY=<secure-generated-secret>
ALLOWED_HOSTS=gylosoftwares.com,www.gylosoftwares.com,healthcheck.railway.app,.railway.app,.up.railway.app
CSRF_TRUSTED_ORIGINS=https://gylosoftwares.com,https://www.gylosoftwares.com,https://*.railway.app,https://*.up.railway.app
SITE_URL=https://gylosoftwares.com
DATABASE_URL=<Railway Postgres URL>
POSTMARK_SERVER_TOKEN=<Postmark server API token>
POSTMARK_MESSAGE_STREAM=outbound
DEFAULT_FROM_EMAIL=GyLo Softwares <support@gylosoftwares.com>
ADMIN_EMAIL=support@gylosoftwares.com
ADMIN_EMAILS=support@gylosoftwares.com
```

Railway blocks outbound SMTP on non-Pro plans, so production website emails should use Postmark over HTTPS. Google Workspace remains the real inbox for `support@gylosoftwares.com`; Postmark only sends transactional website emails.

### Postmark Setup

1. Create or log in to a Postmark account.
2. Create a Postmark server for this website.
3. Verify the sending domain `gylosoftwares.com` in Postmark, or at minimum verify the sender signature for `support@gylosoftwares.com`.
4. Add the DKIM TXT record Postmark shows for the domain in your DNS provider.
5. Add the custom Return-Path CNAME record Postmark shows. Postmark commonly uses `pm_bounces` pointing to `pm.mtasv.net`, but use the exact values shown in your Postmark account.
6. Add a DMARC TXT record if the domain does not already have one. A monitoring policy such as `p=none` is a safe starting point.
7. Wait for Postmark to show DKIM and Return-Path as verified. DNS verification can take up to 48 hours, though it is often faster.
8. Copy the server API token from the Postmark server's API Tokens tab.
9. Set `POSTMARK_SERVER_TOKEN` in Railway to that token and keep `POSTMARK_MESSAGE_STREAM=outbound`.
10. Ensure `DEFAULT_FROM_EMAIL` uses the verified sender or verified domain, for example `GyLo Softwares <support@gylosoftwares.com>`.
11. Deploy, then submit a contact form or start-project form and confirm the message appears in Postmark Activity and reaches `ADMIN_EMAILS`.

The included `railway.json` sets the Railpack build command to collect static files, starts Gunicorn on Railway's `PORT`, and runs migrations before deploy.

After the first deploy, run:

```bash
python manage.py seed_initial_content
python manage.py createsuperuser
```

To connect Namecheap, add the custom domain in Railway, then create the CNAME record Railway gives you in Namecheap DNS.

## Admin

Django Admin is available at `/admin/`. For a later hardening pass, consider moving the admin URL to an environment-configured path and enabling stronger operational controls.

## SEO Checklist

- Unique page titles and meta descriptions
- Canonical URLs
- Open Graph tags
- Twitter/X card tags
- JSON-LD structured data
- Organization schema
- Website schema on homepage
- Service schema on service pages
- Article schema on blog detail pages
- Breadcrumb schema where useful
- Sitemap at `/sitemap.xml`
- Robots file at `/robots.txt`
- Custom 404 and 500 templates
- Mobile-first responsive layout
- Natural Tanzania software and automation keyword targeting

Connect Google Search Console after deployment and submit `https://gylosoftwares.com/sitemap.xml`.

## MVP Feature Checklist

- [x] Home page
- [x] About page
- [x] Services listing
- [x] Service detail pages
- [x] Projects listing
- [x] Vuma project page
- [x] Kiosk project page
- [x] Instagram Fraud Detection project page
- [x] Industries page
- [x] Blog listing
- [x] Blog detail
- [x] Contact form
- [x] Start Project form
- [x] Django Admin content management
- [x] Email notifications
- [x] Sitemap.xml
- [x] Robots.txt
- [x] SEO meta tags
- [x] Structured data
- [x] Responsive design
- [x] Custom 404 page
- [x] Custom 500 page
- [x] Tests

## Manual Steps Before Launch

- Add real Postmark credentials and verify sending from `support@gylosoftwares.com`.
- Confirm final logo/favicon assets.
- Review Privacy Policy and Terms of Service with legal counsel.
- Create a production superuser.
- Connect Railway PostgreSQL.
- Connect the Namecheap domain.
- Verify Google Search Console and submit the sitemap.
