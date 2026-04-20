from django.core.management.base import BaseCommand
from django.utils import timezone

from blog.models import BlogCategory, BlogPost
from projects.models import Project
from services.models import Service


SERVICES = [
    {
        "title": "Custom Software Development",
        "slug": "custom-software-development",
        "icon": "CS",
        "short_description": "Business systems, internal portals, dashboards, workflow tools, booking systems, and marketplace platforms.",
        "full_description": "Growing companies often outgrow spreadsheets, disconnected tools, and manual approvals. Custom software creates a reliable system around the way your business actually works.",
        "seo_title": "Custom Software Development Tanzania | GyLo Softwares",
        "seo_description": "Build custom business systems, portals, dashboards, booking tools, and marketplace platforms with GyLo Softwares in Tanzania.",
    },
    {
        "title": "Web Application Development",
        "slug": "web-application-development",
        "icon": "WA",
        "short_description": "Modern Django-powered web applications, SaaS MVPs, business platforms, admin systems, and API-ready web products.",
        "full_description": "Web applications help teams centralize operations, serve customers online, and launch new digital products without the overhead of complex enterprise systems.",
        "seo_title": "Web Application Development Tanzania | GyLo Softwares",
        "seo_description": "Django-powered web application development for business platforms, SaaS MVPs, admin systems, and API-ready products in Tanzania.",
    },
    {
        "title": "Mobile App Development",
        "slug": "mobile-app-development",
        "icon": "MA",
        "short_description": "Flutter-based mobile applications for customer services, internal operations, field teams, and mobile-first businesses.",
        "full_description": "Mobile apps are useful when your customers, staff, riders, or field teams need fast access to services and workflows from their phones.",
        "seo_title": "Mobile App Development Tanzania | GyLo Softwares",
        "seo_description": "Flutter mobile app development for customer services, internal operations, field teams, and mobile-first businesses in Tanzania.",
    },
    {
        "title": "AI and Automation Solutions",
        "slug": "ai-and-automation-solutions",
        "icon": "AI",
        "short_description": "AI-powered assistants, WhatsApp automation, process automation, document Q&A systems, and internal knowledge tools.",
        "full_description": "Many business processes can be improved with automation, structured data capture, AI-assisted support, and tools that reduce repetitive manual work.",
        "seo_title": "AI Automation Tanzania | GyLo Softwares",
        "seo_description": "AI automation, WhatsApp automation, document Q&A systems, and internal knowledge tools for businesses in Tanzania.",
    },
    {
        "title": "API and Payment Integrations",
        "slug": "api-and-payment-integrations",
        "icon": "API",
        "short_description": "Integrations with Selcom, AzamPay, Flutterwave, M-Pesa workflows, WhatsApp Business API, email services, Google Workspace, and third-party APIs.",
        "full_description": "Connected systems reduce double entry, improve customer experience, and allow teams to manage payments, notifications, and operations from one workflow.",
        "seo_title": "Payment Integration Tanzania | GyLo Softwares",
        "seo_description": "API and payment integrations for Selcom, AzamPay, Flutterwave, M-Pesa workflows, WhatsApp Business API, and business tools.",
    },
    {
        "title": "Data Science and Analytics",
        "slug": "data-science-and-analytics",
        "icon": "DA",
        "short_description": "Business dashboards, forecasting, fraud detection, reporting systems, predictive analytics, and data-driven decision support.",
        "full_description": "Useful analytics turn business activity into clear dashboards, forecasts, reports, risk signals, and decisions that leaders can act on.",
        "seo_title": "Data Science and Analytics Tanzania | GyLo Softwares",
        "seo_description": "Business dashboards, forecasting, fraud detection, predictive analytics, and reporting systems from GyLo Softwares.",
    },
]


PROJECTS = [
    {
        "title": "Vuma",
        "slug": "vuma",
        "tagline": "Influencer marketplace for African brands and creators.",
        "summary": "Vuma is a digital marketplace concept built to help brands discover, evaluate, and collaborate with creators and influencers.",
        "problem": "Brands need a structured way to find suitable creators, manage campaign applications, check eligibility, and plan payments without relying only on scattered direct messages.",
        "solution": "Vuma organizes creator profiles, campaign posting, eligibility rules, applications, verification concepts, and payment planning into a focused marketplace workflow.",
        "key_features": "Brand campaign posting\nCreator/influencer profiles\nCampaign applications\nEligibility rules\nSocial account verification concept\nPayment/escrow planning\nMulti-language support",
        "tech_stack": "Django backend architecture\nMarketplace workflow design\nSocial account verification planning\nPayment and escrow workflow planning\nResponsive web interface",
        "industry": "Creator economy",
        "seo_title": "Vuma Influencer Marketplace | GyLo Softwares",
        "seo_description": "Vuma is an influencer marketplace concept for African brands and creators, designed by GyLo Softwares.",
    },
    {
        "title": "Kiosk",
        "slug": "kiosk",
        "tagline": "SME WhatsApp Automation Suite for Tanzanian businesses.",
        "summary": "Kiosk helps SMEs manage WhatsApp-driven customer communication, orders, payments, delivery coordination, and business operations from one digital system.",
        "problem": "Many SMEs receive orders and customer requests through WhatsApp but lack a reliable system for catalogs, payment confirmation, delivery assignment, and business visibility.",
        "solution": "Kiosk connects WhatsApp-driven ordering with catalog management, customer records, payment workflows, delivery coordination, and an owner dashboard.",
        "key_features": "WhatsApp order handling\nProduct/service catalog\nCustomer records\nPayment confirmation\nDelivery assignment\nBusiness owner dashboard\nFleet/rider management\nSelcom integration planning",
        "tech_stack": "Django business dashboard\nWhatsApp automation planning\nPayment integration planning\nOperations workflow design\nMobile-first responsive interface",
        "industry": "Retail and commerce",
        "seo_title": "Kiosk WhatsApp Automation Suite | GyLo Softwares",
        "seo_description": "Kiosk is a WhatsApp automation suite concept for Tanzanian SMEs managing orders, payments, delivery, and operations.",
    },
    {
        "title": "Instagram Fraud Detection",
        "slug": "instagram-fraud-detection",
        "tagline": "Machine learning-based trust and fraud detection system for Instagram sellers.",
        "summary": "Instagram Fraud Detection is a research-backed AI system concept for identifying suspicious seller profiles and improving trust in social commerce.",
        "problem": "Social commerce buyers can struggle to assess whether an Instagram seller is trustworthy, especially when account signals and customer evidence are hard to evaluate manually.",
        "solution": "The system analyzes seller profile signals, fraud indicators, text patterns, and Tanzania-specific social commerce context to support trustworthiness scoring.",
        "key_features": "Seller profile analysis\nFraud indicators\nTrustworthiness scoring\nNLP and machine learning methods\nTanzania-specific online shopping context\nEvidence-based fraud detection approach",
        "tech_stack": "Machine learning research workflow\nNLP feature extraction\nRisk scoring design\nEvidence-based model evaluation\nDjango-ready product architecture",
        "industry": "AI risk systems",
        "seo_title": "Instagram Fraud Detection Tanzania | GyLo Softwares",
        "seo_description": "Instagram Fraud Detection is an AI risk system concept for social commerce trust and suspicious seller profile analysis in Tanzania.",
    },
]


CATEGORIES = [
    "Software Development",
    "AI Automation",
    "Business Digitization",
    "WhatsApp Automation",
    "Payment Integrations",
    "Data Science",
    "Cybersecurity",
    "Startup MVPs",
]


POSTS = [
    ("How Tanzanian Businesses Can Use WhatsApp Automation to Manage Orders", "whatsapp-automation"),
    ("How Much Does It Cost to Build a Custom Business System in Tanzania?", "software-development"),
    ("Why SMEs Should Move From Excel to Business Dashboards", "business-digitization"),
    ("How AI Assistants Can Improve Customer Support", "ai-automation"),
    ("Web App vs Mobile App: Which One Should Your Business Build First?", "startup-mvps"),
]


class Command(BaseCommand):
    help = "Seed initial services, projects, blog categories, and draft blog posts."

    def handle(self, *args, **options):
        for index, service in enumerate(SERVICES, start=1):
            Service.objects.update_or_create(
                slug=service["slug"],
                defaults={**service, "order": index, "is_active": True},
            )

        for project in PROJECTS:
            Project.objects.update_or_create(
                slug=project["slug"],
                defaults={**project, "is_featured": True, "is_published": True},
            )

        categories = {}
        for name in CATEGORIES:
            slug = name.lower().replace(" ", "-")
            category, _ = BlogCategory.objects.update_or_create(slug=slug, defaults={"name": name})
            categories[slug] = category

        for title, category_slug in POSTS:
            slug = title.lower().replace(":", "").replace("?", "").replace(",", "").replace(" ", "-")
            BlogPost.objects.update_or_create(
                slug=slug,
                defaults={
                    "title": title,
                    "category": categories[category_slug],
                    "excerpt": "A practical draft article outline for business leaders evaluating software and automation decisions in Tanzania.",
                    "content": (
                        "This draft article is ready for review in Django Admin.\n\n"
                        "It should explain the business problem, practical options, implementation considerations, and how a company can decide the right next step.\n\n"
                        "Before publishing, update this draft with examples, pricing context where appropriate, and a clear call to action for GyLo Softwares."
                    ),
                    "status": BlogPost.Status.DRAFT,
                    "published_at": timezone.now(),
                    "seo_title": f"{title} | GyLo Softwares",
                    "seo_description": f"Learn about {title.lower()} with practical guidance from GyLo Softwares.",
                },
            )

        self.stdout.write(self.style.SUCCESS("Initial GyLo content seeded successfully."))
