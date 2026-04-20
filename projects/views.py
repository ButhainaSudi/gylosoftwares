from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from core.seo import absolute_url, page_context

from .models import Project


def project_list(request):
    projects = Project.objects.filter(is_published=True).order_by("-is_featured", "title")
    context = page_context(
        "Software Projects and Product Concepts | GyLo Softwares",
        "Explore GyLo Softwares project showcases including Vuma, Kiosk, and Instagram Fraud Detection.",
        reverse("projects:list"),
        breadcrumbs=[("Home", reverse("pages:home")), ("Projects", reverse("projects:list"))],
    )
    context["projects"] = projects
    return render(request, "projects/project_list.html", context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, is_published=True)
    schema = {
        "@context": "https://schema.org",
        "@type": "CreativeWork",
        "name": project.title,
        "description": project.summary,
        "creator": {
            "@type": "Organization",
            "name": "GyLo Softwares Company Limited",
            "url": absolute_url("/"),
        },
        "url": absolute_url(project.get_absolute_url()),
    }
    context = page_context(
        project.seo_title,
        project.seo_description,
        project.get_absolute_url(),
        extra_schema=schema,
        breadcrumbs=[
            ("Home", reverse("pages:home")),
            ("Projects", reverse("projects:list")),
            (project.title, project.get_absolute_url()),
        ],
    )
    context["project"] = project
    return render(request, "projects/project_detail.html", context)
