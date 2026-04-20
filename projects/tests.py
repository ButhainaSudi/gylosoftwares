from django.test import TestCase
from django.urls import reverse


class ProjectPageTests(TestCase):
    def test_projects_page_loads(self):
        response = self.client.get(reverse("projects:list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Selected project showcases")
