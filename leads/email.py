import json
import logging
import urllib.error
import urllib.request

from django.conf import settings
from django.core.mail import EmailMessage
from django.urls import reverse


logger = logging.getLogger(__name__)


def admin_change_url(obj):
    url_name = f"admin:{obj._meta.app_label}_{obj._meta.model_name}_change"
    return f"{settings.SITE_URL}{reverse(url_name, args=[obj.pk])}"


def admin_recipients():
    return getattr(settings, "ADMIN_EMAILS", None) or [settings.ADMIN_EMAIL]


def comma_join(addresses):
    return ", ".join(addresses)


def _from_domain():
    addr = settings.DEFAULT_FROM_EMAIL
    email_part = addr[addr.rfind("<") + 1:].rstrip(">") if "<" in addr else addr
    return email_part.split("@")[-1].lower()


def send_postmark_email(subject, message, recipient_list, reply_to=None):
    if getattr(settings, "POSTMARK_SANDBOX_MODE", False):
        domain = _from_domain()
        filtered = [r for r in recipient_list if r.lower().endswith(f"@{domain}")]
        if not filtered:
            logger.info("Sandbox mode: skipping email to external recipients %s", recipient_list)
            return
        if len(filtered) < len(recipient_list):
            logger.info("Sandbox mode: dropped external recipients, sending only to %s", filtered)
        recipient_list = filtered

    payload = {
        "From": settings.DEFAULT_FROM_EMAIL,
        "To": comma_join(recipient_list),
        "Subject": subject,
        "TextBody": message,
        "MessageStream": settings.POSTMARK_MESSAGE_STREAM,
    }
    if reply_to:
        payload["ReplyTo"] = comma_join(reply_to)

    request = urllib.request.Request(
        settings.POSTMARK_API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Postmark-Server-Token": settings.POSTMARK_SERVER_TOKEN,
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=settings.EMAIL_TIMEOUT) as response:
        if response.status >= 400:
            body = response.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Postmark API returned HTTP {response.status}: {body}")


def send_django_email(subject, message, recipient_list, reply_to=None):
    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipient_list,
        reply_to=reply_to or None,
    )
    email.send(fail_silently=False)


def safe_send_mail(subject, message, recipient_list, fail_context, reply_to=None):
    try:
        if settings.POSTMARK_SERVER_TOKEN:
            send_postmark_email(subject, message, recipient_list, reply_to=reply_to)
        else:
            send_django_email(subject, message, recipient_list, reply_to=reply_to)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        logger.exception("Email delivery failed: %s. Postmark response: %s", fail_context, body)
    except Exception:
        logger.exception("Email delivery failed: %s", fail_context)


def notify_contact_message(message_obj):
    admin_message = (
        "New contact message submitted.\n\n"
        f"Message ID: {message_obj.id}\n"
        f"Name: {message_obj.full_name}\n"
        f"Company: {message_obj.company_name or 'Not provided'}\n"
        f"Email: {message_obj.email}\n"
        f"Phone: {message_obj.phone}\n"
        f"Service interest: {message_obj.service_interest or 'Not specified'}\n\n"
        f"Message:\n{message_obj.message}\n\n"
        f"View in admin: {admin_change_url(message_obj)}"
    )
    subject_company = message_obj.company_name or message_obj.full_name
    safe_send_mail(
        f"New contact message: {subject_company}",
        admin_message,
        admin_recipients(),
        f"contact message {message_obj.id}",
        reply_to=[message_obj.email],
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
        f"Lead ID: {lead.id}\n"
        f"Name: {lead.full_name}\n"
        f"Company: {lead.company_name or 'Not provided'}\n"
        f"Email: {lead.email}\n"
        f"Phone: {lead.phone}\n"
        f"Industry: {lead.industry}\n"
        f"Project type: {lead.get_project_type_display()}\n"
        f"Budget: {lead.get_budget_range_display()}\n"
        f"Timeline: {lead.timeline}\n"
        f"Existing system: {'Yes' if lead.has_existing_system else 'No'}\n"
        f"Existing designs: {'Yes' if lead.has_existing_designs else 'No'}\n"
        f"Attachment uploaded: {'Yes' if lead.attachment else 'No'}\n\n"
        f"Project description:\n{lead.message}\n\n"
        f"View in admin: {admin_change_url(lead)}"
    )
    subject_company = lead.company_name or lead.full_name
    safe_send_mail(
        f"New project inquiry: {subject_company} - {lead.get_project_type_display()}",
        admin_message,
        admin_recipients(),
        f"lead {lead.id}",
        reply_to=[lead.email],
    )
    safe_send_mail(
        "We received your project inquiry - GyLo Softwares",
        "Thank you for starting a project conversation with GyLo Softwares. We have received your inquiry and will review it carefully before getting back to you.",
        [lead.email],
        f"lead confirmation {lead.id}",
    )
