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
- `DEFAULT_FROM_EMAIL`
- `ADMIN_EMAIL`
- `ADMIN_EMAILS`
- `SITE_URL`
- `SECURE_SSL_REDIRECT`
- `SESSION_COOKIE_SECURE`
- `CSRF_COOKIE_SECURE`

If email variables are missing locally, Django uses the console email backend so forms still save and the user flow does not crash.

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
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=support@gylosoftwares.com
EMAIL_HOST_PASSWORD=<Google Workspace app password>
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=GyLo Softwares <support@gylosoftwares.com>
ADMIN_EMAIL=support@gylosoftwares.com
ADMIN_EMAILS=support@gylosoftwares.com
```

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

- Add real SMTP credentials.
- Confirm final logo/favicon assets.
- Review Privacy Policy and Terms of Service with legal counsel.
- Create a production superuser.
- Connect Railway PostgreSQL.
- Connect the Namecheap domain.
- Verify Google Search Console and submit the sitemap.
