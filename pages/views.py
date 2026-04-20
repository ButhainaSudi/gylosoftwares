from django.shortcuts import render
from django.urls import reverse

from core.seo import page_context, website_schema
from projects.models import Project
from services.models import Service


INDUSTRIES = [
    {
        "name": "Retail and commerce",
        "problem": "Manual stock tracking, fragmented customer orders, and limited sales visibility.",
        "help": "We build commerce systems, dashboards, payment workflows, and WhatsApp ordering tools.",
        "example": "An order management dashboard connected to payments and delivery updates.",
    },
    {
        "name": "Logistics and delivery",
        "problem": "Dispatch teams struggle with rider assignment, tracking, and customer updates.",
        "help": "We create fleet tools, delivery coordination systems, and automated notifications.",
        "example": "A delivery operations portal with rider assignment and customer communication.",
    },
    {
        "name": "Financial services",
        "problem": "Financial teams need secure workflows, reporting, risk checks, and integrations.",
        "help": "We build secure portals, reporting tools, payment integrations, and analytics systems.",
        "example": "A compliance-ready dashboard for transactions, reporting, or customer operations.",
    },
    {
        "name": "Real estate",
        "problem": "Property leads, site visits, documents, and client follow-up are often scattered.",
        "help": "We design listing platforms, client portals, lead management workflows, and dashboards.",
        "example": "A property inquiry platform with admin tools and automated follow-up.",
    },
    {
        "name": "Education",
        "problem": "Schools and training teams need simpler tools for learners, records, and communication.",
        "help": "We build student portals, learning tools, reporting systems, and communication automation.",
        "example": "A student management portal with dashboards and notifications.",
    },
    {
        "name": "Healthcare",
        "problem": "Clinics need better appointment, records, billing, and patient communication systems.",
        "help": "We develop secure operational tools that improve service flow and reporting.",
        "example": "An appointment and patient communication system for clinic teams.",
    },
    {
        "name": "NGOs and development projects",
        "problem": "Project teams need field data, beneficiary records, reporting, and transparency.",
        "help": "We build data collection, monitoring, dashboards, and stakeholder communication systems.",
        "example": "A monitoring dashboard for field activity and donor reporting.",
    },
    {
        "name": "Creator economy",
        "problem": "Brands and creators need better discovery, campaign management, and trust workflows.",
        "help": "We build marketplaces, creator profiles, campaign tools, and verification concepts.",
        "example": "An influencer campaign marketplace for brand and creator collaboration.",
    },
    {
        "name": "Transport and fleet businesses",
        "problem": "Fleet owners need visibility into vehicles, drivers, trips, revenue, and maintenance.",
        "help": "We create fleet dashboards, assignment workflows, and operational reporting systems.",
        "example": "A fleet management dashboard for trips, assignments, and business performance.",
    },
    {
        "name": "Professional services",
        "problem": "Service firms need better client intake, project tracking, documents, and reporting.",
        "help": "We build client portals, internal workflow tools, and business dashboards.",
        "example": "A client intake and project management portal for service delivery.",
    },
]


def home(request):
    services = Service.objects.filter(is_active=True)[:6]
    projects = Project.objects.filter(is_published=True, is_featured=True)[:3]
    context = page_context(
        "GyLo Softwares | Software Development and AI Automation in Tanzania",
        "GyLo Softwares builds custom software, AI automation systems, web apps, mobile apps, dashboards, and business systems for growing companies in Tanzania and beyond.",
        reverse("pages:home"),
        extra_schema=website_schema(),
    )
    context.update({"services": services, "projects": projects, "industries": INDUSTRIES})
    return render(request, "pages/home.html", context)


def about(request):
    context = page_context(
        "About GyLo Softwares | Software Engineering Company in Tanzania",
        "Learn about GyLo Softwares, a Tanzania-based software engineering company building custom software, AI automation, and business systems.",
        reverse("pages:about"),
        breadcrumbs=[("Home", reverse("pages:home")), ("About", reverse("pages:about"))],
    )
    return render(request, "pages/about.html", context)


def industries(request):
    context = page_context(
        "Industries Served | GyLo Softwares",
        "GyLo Softwares builds software, automation, dashboards, and digital platforms for retail, logistics, finance, real estate, education, healthcare, NGOs, and professional services.",
        reverse("pages:industries"),
        breadcrumbs=[("Home", reverse("pages:home")), ("Industries", reverse("pages:industries"))],
    )
    context["industries"] = INDUSTRIES
    return render(request, "pages/industries.html", context)


def privacy(request):
    context = page_context(
        "Privacy Policy | GyLo Softwares Company Limited",
        "Read the GyLo Softwares Company Limited privacy policy for website visitors, clients, and project inquiries.",
        reverse("pages:privacy"),
    )
    return render(request, "pages/privacy_policy.html", context)


def terms(request):
    context = page_context(
        "Terms of Service | GyLo Softwares Company Limited",
        "Read the GyLo Softwares Company Limited terms of service for website visitors and prospective clients.",
        reverse("pages:terms"),
    )
    return render(request, "pages/terms_of_service.html", context)
