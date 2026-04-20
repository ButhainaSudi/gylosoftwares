from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from core.seo import absolute_url, page_context

from .models import BlogCategory, BlogPost


def blog_list(request):
    posts = BlogPost.objects.published().select_related("category")
    categories = BlogCategory.objects.all()
    context = page_context(
        "Software, AI Automation and Business Digitization Insights | GyLo Softwares",
        "Read GyLo Softwares insights on software development, AI automation, WhatsApp automation, payment integrations, and business digitization in Tanzania.",
        reverse("blog:list"),
        breadcrumbs=[("Home", reverse("pages:home")), ("Blog", reverse("blog:list"))],
    )
    context.update({"posts": posts, "categories": categories})
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost.objects.published().select_related("category"), slug=slug)
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": post.title,
        "description": post.excerpt,
        "datePublished": post.published_at.isoformat(),
        "dateModified": post.updated_at.isoformat(),
        "author": {"@type": "Organization", "name": "GyLo Softwares Company Limited"},
        "publisher": {
            "@type": "Organization",
            "name": "GyLo Softwares Company Limited",
            "url": absolute_url("/"),
        },
        "mainEntityOfPage": absolute_url(post.get_absolute_url()),
    }
    context = page_context(
        post.seo_title,
        post.seo_description,
        post.get_absolute_url(),
        extra_schema=schema,
        breadcrumbs=[
            ("Home", reverse("pages:home")),
            ("Blog", reverse("blog:list")),
            (post.title, post.get_absolute_url()),
        ],
    )
    context["post"] = post
    return render(request, "blog/blog_detail.html", context)
