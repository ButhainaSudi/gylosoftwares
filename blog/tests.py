from django.test import TestCase
from django.urls import reverse


class BlogPageTests(TestCase):
    def test_blog_listing_loads(self):
        response = self.client.get(reverse("blog:list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Software and automation thinking")
