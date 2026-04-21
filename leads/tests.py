from unittest.mock import patch

from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import ContactMessage, Lead


@override_settings(
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
    ADMIN_EMAILS=["support@gylosoftwares.com", "ops@gylosoftwares.com"],
    POSTMARK_SERVER_TOKEN="",
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


@override_settings(
    POSTMARK_SERVER_TOKEN="pm_test_token",
    POSTMARK_API_URL="https://api.postmark.test/email",
    POSTMARK_MESSAGE_STREAM="outbound",
    DEFAULT_FROM_EMAIL="GyLo Softwares <support@gylosoftwares.com>",
    EMAIL_TIMEOUT=10,
)
class PostmarkEmailTests(TestCase):
    @patch("leads.email.urllib.request.urlopen")
    def test_postmark_payload_includes_plain_text_and_reply_to(self, mock_urlopen):
        from leads.email import safe_send_mail

        mock_urlopen.return_value.__enter__.return_value.status = 200

        safe_send_mail(
            "New contact message: Asha Trading",
            "Body text",
            ["support@gylosoftwares.com"],
            "contact message test",
            reply_to=["asha@example.com"],
        )

        request = mock_urlopen.call_args.args[0]
        self.assertEqual(request.full_url, "https://api.postmark.test/email")
        self.assertEqual(request.get_header("X-postmark-server-token"), "pm_test_token")
        self.assertIn(b'"From": "GyLo Softwares <support@gylosoftwares.com>"', request.data)
        self.assertIn(b'"To": "support@gylosoftwares.com"', request.data)
        self.assertIn(b'"TextBody": "Body text"', request.data)
        self.assertIn(b'"ReplyTo": "asha@example.com"', request.data)
        self.assertIn(b'"MessageStream": "outbound"', request.data)
