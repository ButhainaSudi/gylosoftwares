from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import BlogPost
from projects.models import Project
from services.models import Service


class StaticViewSitemap(Sitemap):
    protocol = "https"
    priority = 0.7
    changefreq = "monthly"

    names = [
        "pages:home",
        "pages:about",
        "services:list",
        "projects:list",
        "pages:industries",
        "blog:list",
        "leads:contact",
        "leads:start_project",
        "pages:privacy",
        "pages:terms",
    ]

    def items(self):
        return self.names

    def location(self, item):
        return reverse(item)


class ServiceSitemap(Sitemap):
    protocol = "https"
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Service.objects.filter(is_active=True).order_by("order", "title")

    def lastmod(self, obj):
        return obj.updated_at


class ProjectSitemap(Sitemap):
    protocol = "https"
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Project.objects.filter(is_published=True).order_by("title")

    def lastmod(self, obj):
        return obj.updated_at


class BlogPostSitemap(Sitemap):
    protocol = "https"
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return BlogPost.objects.published().order_by("-published_at")

    def lastmod(self, obj):
        return obj.updated_at
