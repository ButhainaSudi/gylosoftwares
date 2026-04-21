from django.conf import settings
from django.urls import reverse


def absolute_url(path):
    if path.startswith("http://") or path.startswith("https://"):
        return path
    return f"{settings.SITE_URL}{path}"


def organization_schema():
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "GyLo Softwares Company Limited",
        "url": settings.SITE_URL,
        "email": "support@gylosoftwares.com",
        "telephone": "+255614725009",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "19 Nzasa B",
            "addressLocality": "Dar es Salaam",
            "postalCode": "15113",
            "addressCountry": "TZ",
        },
        "sameAs": ["https://www.instagram.com/gylo_softwares/"],
    }


def website_schema():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "GyLo Softwares",
        "url": settings.SITE_URL,
        "publisher": {"@type": "Organization", "name": "GyLo Softwares Company Limited"},
    }


def breadcrumb_schema(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": index,
                "name": label,
                "item": absolute_url(url),
            }
            for index, (label, url) in enumerate(items, start=1)
        ],
    }


def page_context(title, description, path=None, extra_schema=None, breadcrumbs=None):
    canonical_path = path or reverse("pages:home")
    structured_data = [organization_schema()]
    if extra_schema:
        structured_data.extend(extra_schema if isinstance(extra_schema, list) else [extra_schema])
    if breadcrumbs:
        structured_data.append(breadcrumb_schema(breadcrumbs))
    return {
        "meta_title": title,
        "meta_description": description,
        "canonical_url": absolute_url(canonical_path),
        "structured_data": structured_data,
    }
