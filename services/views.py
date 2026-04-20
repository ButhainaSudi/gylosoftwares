from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from core.seo import absolute_url, page_context

from .models import Service


def service_list(request):
    services = Service.objects.filter(is_active=True)
    context = page_context(
        "Software Development and AI Automation Services in Tanzania | GyLo Softwares",
        "Explore custom software development, web apps, mobile apps, AI automation, payment integrations, and analytics services from GyLo Softwares.",
        reverse("services:list"),
        breadcrumbs=[("Home", reverse("pages:home")), ("Services", reverse("services:list"))],
    )
    context["services"] = services
    return render(request, "services/service_list.html", context)


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)
    schema = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": service.title,
        "description": service.short_description,
        "provider": {
            "@type": "Organization",
            "name": "GyLo Softwares Company Limited",
            "url": absolute_url("/"),
        },
        "areaServed": "Tanzania",
        "url": absolute_url(service.get_absolute_url()),
    }
    context = page_context(
        service.seo_title,
        service.seo_description,
        service.get_absolute_url(),
        extra_schema=schema,
        breadcrumbs=[
            ("Home", reverse("pages:home")),
            ("Services", reverse("services:list")),
            (service.title, service.get_absolute_url()),
        ],
    )
    context["service"] = service
    return render(request, "services/service_detail.html", context)
