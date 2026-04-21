from django.conf import settings


def site_settings(request):
    return {
        "company_name": "GyLo Softwares",
        "company_legal_name": "GyLo Softwares Company Limited",
        "company_email": "support@gylosoftwares.com",
        "company_phone": "+255614725009",
        "company_whatsapp": "+491745764722",
        "company_address": "19 Nzasa B, Dar es Salaam 15113",
        "instagram_url": "https://www.instagram.com/gylo_softwares/",
        "site_url": settings.SITE_URL,
        "phone_url": "tel:+255614725009",
        "whatsapp_url": "https://wa.me/491745764722",
    }
