import logging

from django.conf import settings
from django.core.mail import send_mail


logger = logging.getLogger(__name__)


def safe_send_mail(subject, message, recipient_list, fail_context):
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipient_list,
            fail_silently=False,
        )
    except Exception:
        logger.exception("Email delivery failed: %s", fail_context)


def notify_contact_message(message_obj):
    admin_message = (
        "New contact message submitted.\n\n"
        f"Name: {message_obj.full_name}\n"
        f"Company: {message_obj.company_name or 'Not provided'}\n"
        f"Email: {message_obj.email}\n"
        f"Phone: {message_obj.phone}\n"
        f"Service interest: {message_obj.service_interest or 'Not specified'}\n\n"
        f"Message:\n{message_obj.message}"
    )
    safe_send_mail(
        "New contact message - GyLo Softwares",
        admin_message,
        [settings.ADMIN_EMAIL],
        f"contact message {message_obj.id}",
    )
    safe_send_mail(
        "We received your message - GyLo Softwares",
        "Thank you for contacting GyLo Softwares. Our team has received your message and will respond as soon as possible.",
        [message_obj.email],
        f"contact confirmation {message_obj.id}",
    )


def notify_lead(lead):
    admin_message = (
        "New project inquiry submitted.\n\n"
        f"Name: {lead.full_name}\n"
        f"Company: {lead.company_name or 'Not provided'}\n"
        f"Email: {lead.email}\n"
        f"Phone: {lead.phone}\n"
        f"Industry: {lead.industry}\n"
        f"Project type: {lead.get_project_type_display()}\n"
        f"Budget: {lead.get_budget_range_display()}\n"
        f"Timeline: {lead.timeline}\n"
        f"Existing system: {'Yes' if lead.has_existing_system else 'No'}\n"
        f"Existing designs: {'Yes' if lead.has_existing_designs else 'No'}\n\n"
        f"Project description:\n{lead.message}"
    )
    safe_send_mail(
        "New project inquiry - GyLo Softwares",
        admin_message,
        [settings.ADMIN_EMAIL],
        f"lead {lead.id}",
    )
    safe_send_mail(
        "We received your project inquiry - GyLo Softwares",
        "Thank you for starting a project conversation with GyLo Softwares. We have received your inquiry and will review it carefully before getting back to you.",
        [lead.email],
        f"lead confirmation {lead.id}",
    )
