from django.test import TestCase
from django.urls import reverse


class PublicPageTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse("pages:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Build software that runs your business smarter.")

    def test_industries_page_loads(self):
        response = self.client.get(reverse("pages:industries"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Retail and commerce")
