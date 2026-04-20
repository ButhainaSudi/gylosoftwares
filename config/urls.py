from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from core.sitemaps import BlogPostSitemap, ProjectSitemap, ServiceSitemap, StaticViewSitemap
from core.views import robots_txt

sitemaps = {
    "static": StaticViewSitemap,
    "services": ServiceSitemap,
    "projects": ProjectSitemap,
    "blog": BlogPostSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("services/", include("services.urls")),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
    path("", include("leads.urls")),
    path("robots.txt", robots_txt, name="robots_txt"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("", include("pages.urls")),
]

handler404 = "pages.error_views.page_not_found"
handler500 = "pages.error_views.server_error"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
