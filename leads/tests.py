from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import ContactMessage, Lead


@override_settings(
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
    ADMIN_EMAILS=["support@gylosoftwares.com", "ops@gylosoftwares.com"],
    SITE_URL="https://gylosoftwares.com",
)
class LeadFormTests(TestCase):
    def test_contact_form_valid_submission_saves_data(self):
        with self.captureOnCommitCallbacks(execute=True):
            response = self.client.post(
                reverse("leads:contact"),
                {
                    "full_name": "Asha Mwinyi",
                    "company_name": "Asha Trading",
                    "email": "asha@example.com",
                    "phone": "+255614725009",
                    "service_interest": "AI Automation",
                    "message": "We need a customer support automation system.",
                },
            )
        self.assertRedirects(response, reverse("leads:contact_success"))
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 2)
        admin_email = mail.outbox[0]
        self.assertEqual(admin_email.to, ["support@gylosoftwares.com", "ops@gylosoftwares.com"])
        self.assertEqual(admin_email.reply_to, ["asha@example.com"])
        self.assertIn("New contact message: Asha Trading", admin_email.subject)
        self.assertIn("Message ID:", admin_email.body)
        self.assertIn("View in admin: https://gylosoftwares.com/admin/leads/contactmessage/", admin_email.body)

    def test_start_project_form_valid_submission_saves_data(self):
        with self.captureOnCommitCallbacks(execute=True):
            response = self.client.post(
                reverse("leads:start_project"),
                {
                    "full_name": "John Kileo",
                    "company_name": "Kileo Logistics",
                    "email": "john@example.com",
                    "phone": "+255700000000",
                    "industry": "Logistics and delivery",
                    "project_type": Lead.ProjectType.CUSTOM_BUSINESS_SYSTEM,
                    "budget_range": Lead.BudgetRange.TZS_3M_7M,
                    "timeline": "Within 3 months",
                    "message": "We need a delivery dashboard and rider assignment workflow.",
                    "has_existing_system": "on",
                    "has_existing_designs": "",
                },
            )
        self.assertRedirects(response, reverse("leads:start_project_success"))
        self.assertEqual(Lead.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 2)
        admin_email = mail.outbox[0]
        self.assertEqual(admin_email.to, ["support@gylosoftwares.com", "ops@gylosoftwares.com"])
        self.assertEqual(admin_email.reply_to, ["john@example.com"])
        self.assertIn("New project inquiry: Kileo Logistics - Custom Business System", admin_email.subject)
        self.assertIn("Lead ID:", admin_email.body)
        self.assertIn("Attachment uploaded: No", admin_email.body)
        self.assertIn("View in admin: https://gylosoftwares.com/admin/leads/lead/", admin_email.body)
