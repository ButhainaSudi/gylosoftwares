from django.test import TestCase
from django.urls import reverse


class SeoEndpointTests(TestCase):
    def test_sitemap_loads(self):
        response = self.client.get(reverse("django.contrib.sitemaps.views.sitemap"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "/services/")

    def test_robots_loads(self):
        response = self.client.get(reverse("robots_txt"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sitemap:")
