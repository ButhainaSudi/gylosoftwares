from pathlib import Path

from django.core.exceptions import ValidationError


ALLOWED_ATTACHMENT_EXTENSIONS = {".pdf", ".doc", ".docx", ".png", ".jpg", ".jpeg", ".webp"}
MAX_ATTACHMENT_SIZE = 5 * 1024 * 1024


def validate_attachment(file):
    suffix = Path(file.name).suffix.lower()
    if suffix not in ALLOWED_ATTACHMENT_EXTENSIONS:
        allowed = ", ".join(sorted(ALLOWED_ATTACHMENT_EXTENSIONS))
        raise ValidationError(f"Unsupported file type. Allowed types: {allowed}.")
    if file.size > MAX_ATTACHMENT_SIZE:
        raise ValidationError("Attachment must be 5MB or smaller.")
