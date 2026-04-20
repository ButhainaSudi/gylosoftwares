from django.db import models

from core.models import UUIDTimestampedModel

from .validators import validate_attachment


class Lead(UUIDTimestampedModel):
    class Status(models.TextChoices):
        NEW = "new", "New"
        CONTACTED = "contacted", "Contacted"
        QUALIFIED = "qualified", "Qualified"
        WON = "won", "Won"
        LOST = "lost", "Lost"

    class ProjectType(models.TextChoices):
        COMPANY_WEBSITE = "company_website", "Company Website"
        WEB_APPLICATION = "web_application", "Web Application"
        MOBILE_APPLICATION = "mobile_application", "Mobile Application"
        AI_AUTOMATION = "ai_automation", "AI Automation"
        WHATSAPP_AUTOMATION = "whatsapp_automation", "WhatsApp Automation"
        PAYMENT_INTEGRATION = "payment_integration", "Payment Integration"
        DASHBOARD_ANALYTICS = "dashboard_analytics", "Dashboard / Analytics"
        CUSTOM_BUSINESS_SYSTEM = "custom_business_system", "Custom Business System"
        OTHER = "other", "Other"

    class BudgetRange(models.TextChoices):
        BELOW_1M = "below_1m", "Below TZS 1M"
        TZS_1M_3M = "tzs_1m_3m", "TZS 1M - 3M"
        TZS_3M_7M = "tzs_3m_7m", "TZS 3M - 7M"
        TZS_7M_15M = "tzs_7m_15m", "TZS 7M - 15M"
        TZS_15M_PLUS = "tzs_15m_plus", "TZS 15M+"
        NOT_SURE = "not_sure", "Not sure yet"

    full_name = models.CharField(max_length=160)
    company_name = models.CharField(max_length=180, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=60)
    industry = models.CharField(max_length=140)
    project_type = models.CharField(max_length=60, choices=ProjectType.choices)
    budget_range = models.CharField(max_length=40, choices=BudgetRange.choices)
    timeline = models.CharField(max_length=140)
    message = models.TextField(verbose_name="Project description")
    has_existing_system = models.BooleanField(default=False)
    has_existing_designs = models.BooleanField(default=False)
    attachment = models.FileField(
        upload_to="lead-attachments/",
        validators=[validate_attachment],
        blank=True,
    )
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.NEW)
    admin_notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.get_project_type_display()}"


class ContactMessage(UUIDTimestampedModel):
    full_name = models.CharField(max_length=160)
    company_name = models.CharField(max_length=180, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=60)
    service_interest = models.CharField(max_length=180, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.email}"
