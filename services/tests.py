from django.test import TestCase
from django.urls import reverse


class ServicePageTests(TestCase):
    def test_services_page_loads(self):
        response = self.client.get(reverse("services:list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Custom software")
