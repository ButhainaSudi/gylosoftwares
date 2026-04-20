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
        "short_description": "Custom business systems, internal portals, dashboards, workflow tools, booking systems, and marketplace platforms.",
        "full_description": "Many growing companies reach a point where spreadsheets, WhatsApp messages, manual approvals, and disconnected tools slow the business down. Custom software helps turn those repeated processes into one reliable system. GyLo designs and builds tools around the way your team actually works, including internal portals, customer portals, approval workflows, reporting dashboards, booking systems, and marketplace platforms. The goal is not to add complexity. The goal is to reduce manual work, improve visibility, and create a system your business can depend on as it grows.",
        "seo_title": "Custom Software Development Tanzania | GyLo Softwares",
        "seo_description": "Build custom business systems, portals, dashboards, booking tools, and marketplace platforms with GyLo Softwares in Tanzania.",
    },
    {
        "title": "Web Application Development",
        "slug": "web-application-development",
        "icon": "WA",
        "short_description": "Django-powered web applications, SaaS MVPs, business platforms, admin systems, and API-ready products.",
        "full_description": "A web application gives your company a secure, central platform that staff, customers, partners, or administrators can access from a browser. GyLo builds Django-powered web apps for operations, customer service, sales, reporting, inventory, bookings, marketplaces, and SaaS MVPs. We focus on clear user flows, strong backend foundations, admin visibility, clean interfaces, and integration-ready architecture so the product can launch lean and keep improving after real users start using it.",
        "seo_title": "Web Application Development Tanzania | GyLo Softwares",
        "seo_description": "Django-powered web application development for business platforms, SaaS MVPs, admin systems, and API-ready products in Tanzania.",
    },
    {
        "title": "Mobile App Development",
        "slug": "mobile-app-development",
        "icon": "MA",
        "short_description": "Flutter mobile apps for customer services, field teams, internal operations, and mobile-first businesses.",
        "full_description": "Mobile apps are most useful when your customers, staff, riders, field officers, or service teams need fast access from their phones. GyLo builds mobile-first products for order management, field reporting, customer self-service, delivery coordination, internal operations, and digital services. We use mobile development where it creates clear business value and advise honestly when a responsive web app would be the better first step.",
        "seo_title": "Mobile App Development Tanzania | GyLo Softwares",
        "seo_description": "Flutter mobile app development for customer services, internal operations, field teams, and mobile-first businesses in Tanzania.",
    },
    {
        "title": "AI and Automation Solutions",
        "slug": "ai-and-automation-solutions",
        "icon": "AI",
        "short_description": "AI assistants, WhatsApp automation, business process automation, document Q&A, and internal knowledge tools.",
        "full_description": "Companies lose time when teams repeat the same replies, search through documents manually, move data between systems, or depend on one person to know how everything works. GyLo builds practical AI and automation tools that support real operations: AI-assisted customer support, WhatsApp workflows, internal document search, process automation, lead qualification, and knowledge tools. We keep automation grounded in business rules, human review, and measurable value.",
        "seo_title": "AI Automation Tanzania | GyLo Softwares",
        "seo_description": "AI automation, WhatsApp automation, document Q&A systems, and internal knowledge tools for businesses in Tanzania.",
    },
    {
        "title": "API and Payment Integrations",
        "slug": "api-and-payment-integrations",
        "icon": "API",
        "short_description": "Integrations with Selcom, AzamPay, Flutterwave, M-Pesa workflows, WhatsApp Business API, Google Workspace, and third-party APIs.",
        "full_description": "When business systems do not communicate, teams waste time copying information, confirming payments manually, and reconciling records after the fact. GyLo integrates payment providers, WhatsApp workflows, email services, Google Workspace, analytics tools, and third-party APIs so your operations can move through one connected workflow. We design integrations with clear error handling, audit visibility, and practical admin tools.",
        "seo_title": "Payment Integration Tanzania | GyLo Softwares",
        "seo_description": "API and payment integrations for Selcom, AzamPay, Flutterwave, M-Pesa workflows, WhatsApp Business API, and business tools.",
    },
    {
        "title": "Data Science and Analytics",
        "slug": "data-science-and-analytics",
        "icon": "DA",
        "short_description": "Business dashboards, forecasting, fraud detection, reporting systems, predictive analytics, and decision support.",
        "full_description": "Business leaders need clear information without waiting for manual reports. GyLo builds dashboards, reporting systems, forecasting tools, fraud detection concepts, and analytics workflows that turn operational data into decisions. We help companies define the right metrics, clean the data flow, and create dashboards that management teams can actually use.",
        "seo_title": "Data Science and Analytics Tanzania | GyLo Softwares",
        "seo_description": "Business dashboards, forecasting, fraud detection, predictive analytics, and reporting systems from GyLo Softwares.",
    },
]


PROJECTS = [
    {
        "title": "Vuma",
        "slug": "vuma",
        "tagline": "Influencer marketplace for African brands and creators.",
        "summary": "Vuma is a digital marketplace concept built to help brands discover, evaluate, and collaborate with creators and influencers through a structured campaign workflow.",
        "problem": "Brands often manage influencer campaigns through scattered direct messages, manual spreadsheets, and uncertain creator verification. That makes it difficult to compare creators, manage applications, apply eligibility rules, and plan payments consistently.",
        "solution": "Vuma brings campaign posting, creator profiles, applications, verification concepts, eligibility rules, language support, and payment planning into a marketplace workflow designed for African brands and creators.",
        "key_features": "Brand campaign posting\nCreator/influencer profiles\nCampaign applications\nEligibility rules\nSocial account verification concept\nPayment/escrow planning\nMulti-language support",
        "tech_stack": "Django backend architecture\nMarketplace workflow design\nSocial account verification planning\nPayment and escrow workflow planning\nResponsive web interface\nAdmin-managed campaign operations",
        "industry": "Creator economy",
        "seo_title": "Vuma Influencer Marketplace | GyLo Softwares",
        "seo_description": "Vuma is an influencer marketplace concept for African brands and creators, designed by GyLo Softwares.",
    },
    {
        "title": "Kiosk",
        "slug": "kiosk",
        "tagline": "SME WhatsApp Automation Suite for Tanzanian businesses.",
        "summary": "Kiosk helps SMEs manage WhatsApp-driven customer communication, orders, payments, delivery coordination, and business operations from one digital system.",
        "problem": "Many SMEs receive customer orders through WhatsApp but lack a reliable backend system for catalogs, customer records, payment confirmation, rider assignment, and owner visibility.",
        "solution": "Kiosk connects WhatsApp order handling with product catalogs, customer records, payment workflows, delivery assignment, fleet management, and a business owner dashboard.",
        "key_features": "WhatsApp order handling\nProduct/service catalog\nCustomer records\nPayment confirmation\nDelivery assignment\nBusiness owner dashboard\nFleet/rider management\nSelcom integration planning",
        "tech_stack": "Django business dashboard\nWhatsApp automation planning\nPayment integration planning\nOperations workflow design\nMobile-first responsive interface\nRole-based admin tools",
        "industry": "Retail and commerce",
        "seo_title": "Kiosk WhatsApp Automation Suite | GyLo Softwares",
        "seo_description": "Kiosk is a WhatsApp automation suite concept for Tanzanian SMEs managing orders, payments, delivery, and operations.",
    },
    {
        "title": "Instagram Fraud Detection",
        "slug": "instagram-fraud-detection",
        "tagline": "Machine learning-based trust and fraud detection system for Instagram sellers.",
        "summary": "Instagram Fraud Detection is a research-backed AI system concept for identifying suspicious seller profiles and improving trust in social commerce.",
        "problem": "Social commerce buyers can struggle to assess whether an Instagram seller is trustworthy, especially when profile signals, text patterns, and customer evidence are hard to evaluate manually.",
        "solution": "The system analyzes seller profile signals, fraud indicators, language patterns, and Tanzania-specific social commerce context to support trustworthiness scoring and risk review.",
        "key_features": "Seller profile analysis\nFraud indicators\nTrustworthiness scoring\nNLP and machine learning methods\nTanzania-specific online shopping context\nEvidence-based fraud detection approach",
        "tech_stack": "Machine learning research workflow\nNLP feature extraction\nRisk scoring design\nEvidence-based model evaluation\nDjango-ready product architecture\nAdmin review workflow",
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


def article(*sections):
    return "\n\n".join(section.strip() for section in sections)


BLOG_POSTS = [
    {
        "title": "How Much Does It Cost to Build a Custom Business System in Tanzania?",
        "slug": "how-much-does-it-cost-to-build-a-custom-business-system-in-tanzania",
        "category": "software-development",
        "status": BlogPost.Status.PUBLISHED,
        "excerpt": "A practical guide to the factors that influence software project budgets in Tanzania, from scope and integrations to support and long-term maintenance.",
        "seo_title": "Cost to Build Custom Business Software in Tanzania | GyLo Softwares",
        "seo_description": "Understand the cost factors behind custom business systems in Tanzania, including scope, integrations, dashboards, mobile apps, support, and timelines.",
        "content": article(
            "One of the first questions business leaders ask is simple: how much will it cost to build a custom business system? The honest answer is that cost depends less on the word software and more on the business process being digitized. A small internal dashboard is very different from a customer portal with payments, WhatsApp automation, user roles, reports, and mobile access.",
            "For many Tanzanian businesses, a useful first system may start from a focused MVP: customer records, order tracking, staff roles, basic reports, and an admin dashboard. A larger platform may include mobile apps, payment integrations, advanced approvals, analytics, notifications, and audit trails. Each extra workflow adds value, but it also adds planning, development, testing, and support effort.",
            "The biggest cost drivers are scope, integrations, user roles, data migration, design complexity, reporting requirements, and launch support. Payment integrations such as Selcom, AzamPay, Flutterwave, or M-Pesa workflows need careful testing. WhatsApp automation needs clear conversation rules. Dashboards need reliable data. AI features need quality inputs and human review. These parts should be planned instead of rushed.",
            "A responsible software partner should help you separate must-have features from later improvements. The first version should solve the main operational problem, prove the workflow, and give your team something usable. After launch, the system can improve based on real feedback rather than assumptions.",
            "Before requesting a quotation, prepare the business problem, the users involved, the current manual process, the data you already have, required integrations, expected timeline, and budget range. A clear brief helps the developer estimate properly and avoid vague pricing.",
            "GyLo Softwares works with companies to clarify scope, define an MVP, and build systems that can grow. If your team is still using spreadsheets and manual WhatsApp follow-ups for important operations, a focused custom system may be the step that improves visibility and control.",
        ),
    },
    {
        "title": "How Tanzanian Businesses Can Use WhatsApp Automation to Manage Orders",
        "slug": "how-tanzanian-businesses-can-use-whatsapp-automation-to-manage-orders",
        "category": "whatsapp-automation",
        "status": BlogPost.Status.PUBLISHED,
        "excerpt": "WhatsApp is already where many customers buy and ask questions. Automation can help businesses turn those conversations into structured orders and better service.",
        "seo_title": "WhatsApp Automation for Tanzanian Business Orders | GyLo Softwares",
        "seo_description": "Learn how Tanzanian businesses can use WhatsApp automation to manage orders, customers, payments, delivery updates, and owner dashboards.",
        "content": article(
            "For many Tanzanian businesses, WhatsApp is not just a chat app. It is where customers ask for prices, send screenshots, confirm payments, request delivery, and follow up after purchase. The challenge is that WhatsApp conversations are often unstructured. Orders can be missed, payment confirmations can be buried, and business owners may not have a clear view of daily activity.",
            "WhatsApp automation helps by turning repeated conversations into a managed workflow. A customer can request a catalog, choose a product or service, share delivery details, receive payment instructions, and get order updates. Staff can see orders in a dashboard instead of scrolling through chats. Business owners can review order status, customers, delivery activity, and sales performance.",
            "Good automation does not mean removing people from the business. It means handling repetitive steps consistently and giving staff better tools. A human team can still step in when the request is complex, high-value, or sensitive. The system should make that handover clear.",
            "A practical WhatsApp order system may include a product catalog, customer records, order statuses, payment confirmation, delivery assignment, automated replies, staff roles, and reports. For businesses with riders or fleet operations, the system can include delivery tracking and assignment workflows. For businesses accepting digital payments, payment integration planning is important.",
            "The best approach is to start with the most common customer journey. What do customers ask first? What details must staff collect? Where do errors happen? Which updates are repeated every day? Once those answers are clear, automation can be designed around real business behavior.",
            "GyLo Softwares builds WhatsApp automation concepts and business dashboards for SMEs that want to improve customer service without losing the personal channel customers already trust.",
        ),
    },
    {
        "title": "Web App vs Mobile App: Which One Should Your Business Build First?",
        "slug": "web-app-vs-mobile-app-which-one-should-your-business-build-first",
        "category": "startup-mvps",
        "status": BlogPost.Status.PUBLISHED,
        "excerpt": "Choosing between a web app and a mobile app depends on users, workflows, budget, and how quickly the business needs to launch.",
        "seo_title": "Web App vs Mobile App for Business | GyLo Softwares",
        "seo_description": "Compare web apps and mobile apps for Tanzanian businesses deciding what to build first for customers, staff, operations, or digital products.",
        "content": article(
            "Many companies know they need software but are not sure whether to start with a web app or a mobile app. The right answer depends on who will use the system, where they will use it, and what the first version must prove.",
            "A web app is often the best first choice for admin dashboards, internal portals, booking systems, marketplaces, SaaS MVPs, reporting tools, and business platforms. It works from a browser, is easier to update, and can support desktop and mobile users with one responsive interface. For many corporate systems, this gives the fastest path to launch.",
            "A mobile app is stronger when users need frequent phone access, push notifications, offline behavior, device features, field data collection, delivery workflows, or a consumer experience that belongs on the home screen. Mobile apps can be powerful, but they also introduce app store processes, platform testing, and update management.",
            "Budget also matters. A polished mobile app usually requires more testing across devices and operating systems. If the business is still proving the workflow, a responsive web app may reduce risk. Once the product has real usage, a mobile app can be added for the users who need it most.",
            "The decision should not be emotional. Ask: who are the first users, what device do they use during the work, how often will they use the system, what features are essential, and what result must the first version deliver? These answers usually make the direction clear.",
            "GyLo Softwares helps businesses choose the right first platform. In many cases, the smartest path is a strong web application with mobile-friendly design, then a mobile app when the business case is proven.",
        ),
    },
    {
        "title": "Why SMEs Should Move From Excel to Business Dashboards",
        "slug": "why-smes-should-move-from-excel-to-business-dashboards",
        "category": "business-digitization",
        "status": BlogPost.Status.PUBLISHED,
        "excerpt": "Excel is useful, but growing businesses need dashboards when manual reports start delaying decisions and hiding operational problems.",
        "seo_title": "Move From Excel to Business Dashboards | GyLo Softwares",
        "seo_description": "Learn why Tanzanian SMEs should move from manual Excel reporting to business dashboards for operations, sales, finance, and management visibility.",
        "content": article(
            "Excel is one of the most useful tools in business. It helps teams start quickly, track records, calculate totals, and prepare reports. The problem begins when Excel becomes the main operating system of the company. Files multiply, formulas break, versions conflict, and management waits for someone to update reports manually.",
            "A business dashboard gives leaders a clearer view of what is happening now. Instead of asking for updated spreadsheets, managers can see sales, orders, customers, payments, delivery status, stock movement, team activity, and other key metrics from one place. The value is not just visual design. The value is faster decision-making.",
            "Moving from Excel to a dashboard does not mean throwing away every spreadsheet immediately. The first step is identifying which reports matter most and where the data should come from. Some data may come from forms, order systems, payment integrations, or staff workflows. Some may still be uploaded at first while the business transitions.",
            "A good dashboard should answer practical management questions. What is selling? Which orders are delayed? Which customers need follow-up? Which branches or teams are performing well? Where are payments pending? Which operational issues repeat every week?",
            "Dashboards also reduce dependence on one person who knows how the spreadsheet works. With proper user roles and clear data entry workflows, the business can create a more reliable reporting culture.",
            "GyLo Softwares builds dashboards and reporting systems for companies that want better visibility without overcomplicating operations. The best dashboard is not the one with the most charts. It is the one that helps management act.",
        ),
    },
    {
        "title": "How AI Assistants Can Improve Customer Support",
        "slug": "how-ai-assistants-can-improve-customer-support",
        "category": "ai-automation",
        "status": BlogPost.Status.PUBLISHED,
        "excerpt": "AI assistants can help companies respond faster, organize knowledge, and support staff when implemented with clear rules and human oversight.",
        "seo_title": "AI Assistants for Customer Support | GyLo Softwares",
        "seo_description": "See how AI assistants can improve customer support for businesses through faster replies, knowledge tools, escalation rules, and workflow automation.",
        "content": article(
            "Customer support teams answer many repeated questions: pricing, availability, delivery status, account details, opening hours, documents required, and service steps. As the business grows, these repeated questions can slow staff down and create inconsistent replies.",
            "AI assistants can improve support by helping customers get faster answers and helping staff find information quickly. The strongest use cases are not magic. They are practical: answering common questions from approved content, searching internal documents, drafting replies for staff review, routing inquiries, and summarizing customer conversations.",
            "A good AI support system needs boundaries. It should know which information it can answer, when to ask clarifying questions, and when to hand over to a human. It should not invent prices, make unsupported promises, or handle sensitive issues without approval. Human oversight is part of responsible automation.",
            "For many companies, the first step is organizing support knowledge. What questions do customers ask every day? Which documents contain correct answers? Which questions require staff approval? Which conversations should become sales leads? Once this knowledge is structured, an assistant can be useful.",
            "AI can also support internal teams. Staff can ask a document Q&A tool about policies, procedures, product information, or project notes. This reduces time wasted searching through folders and old messages.",
            "GyLo Softwares builds AI automation systems that support customer service while respecting business rules. The aim is faster response, better consistency, and less repetitive manual work, not uncontrolled automation.",
        ),
    },
    {
        "title": "Build vs Buy: Should Your Company Use Off-the-Shelf Software or Build Custom?",
        "slug": "build-vs-buy-should-your-company-use-off-the-shelf-software-or-build-custom",
        "category": "software-development",
        "status": BlogPost.Status.DRAFT,
        "excerpt": "A practical framework for deciding when ready-made software is enough and when a custom system becomes the better business investment.",
        "seo_title": "Build vs Buy Software for Businesses | GyLo Softwares",
        "seo_description": "Compare off-the-shelf software and custom software for growing companies evaluating cost, fit, workflow control, integrations, and long-term value.",
        "content": article(
            "Companies should not build custom software for every problem. In many cases, off-the-shelf software is faster, cheaper, and good enough. Accounting tools, basic email marketing platforms, document storage, and general collaboration tools often make sense to buy.",
            "Custom software becomes valuable when your process is specific, your team is forcing a tool to behave in unnatural ways, or your business model depends on a workflow that ready-made software cannot support well. It also matters when multiple tools create double entry, poor visibility, and manual reconciliation.",
            "The decision should consider fit, total cost, integrations, ownership, reporting, user roles, data control, and future growth. A cheap subscription can become expensive if staff spend hours every week working around it. A custom system can be wasteful if the business problem is not clear.",
            "A balanced approach is often best. Use proven tools where they fit, and build custom systems around the workflows that create your advantage. Integrations can connect both worlds.",
            "Before deciding, map the current process, pain points, data flow, approvals, reports, and customer experience. Then compare whether an existing product can handle the process without damaging the way your business works.",
            "GyLo Softwares helps companies evaluate build-versus-buy decisions honestly. The goal is not to build more software than necessary. The goal is to create the right system for the business outcome.",
        ),
    },
    {
        "title": "Why Payment Integration Matters for Digital Businesses in Tanzania",
        "slug": "why-payment-integration-matters-for-digital-businesses-in-tanzania",
        "category": "payment-integrations",
        "status": BlogPost.Status.DRAFT,
        "excerpt": "Payment integration can reduce manual confirmations, improve customer experience, and give business owners better visibility into transactions.",
        "seo_title": "Payment Integration Tanzania | GyLo Softwares",
        "seo_description": "Understand why payment integration matters for Tanzanian digital businesses using Selcom, AzamPay, Flutterwave, M-Pesa workflows, and dashboards.",
        "content": article(
            "Digital businesses need payment workflows that are clear for customers and manageable for staff. When payment confirmation is manual, teams spend time checking messages, screenshots, bank alerts, and order records. Mistakes can delay service and weaken customer trust.",
            "Payment integration helps connect transactions with the business system. Orders can be marked paid, receipts can be generated, staff can review transaction status, and management can see revenue activity in dashboards. This does not remove the need for finance controls. It improves the quality and speed of information.",
            "In Tanzania, businesses may need to consider providers and workflows such as Selcom, AzamPay, Flutterwave, mobile money, card payments, or M-Pesa-related processes. The right choice depends on customer behavior, provider availability, fees, settlement process, reconciliation needs, and technical support.",
            "A good payment integration should include clear success and failure states, webhook handling, transaction references, admin review, reconciliation support, and user-friendly customer instructions. It should also be tested carefully because payment bugs affect trust immediately.",
            "Payment integration is most valuable when connected to the wider business process: orders, subscriptions, delivery, invoices, customer records, and reporting.",
            "GyLo Softwares helps businesses plan and build payment-ready systems that fit the local market and reduce manual back-office work.",
        ),
    },
    {
        "title": "How API Integrations Help Companies Reduce Double Entry",
        "slug": "how-api-integrations-help-companies-reduce-double-entry",
        "category": "software-development",
        "status": BlogPost.Status.DRAFT,
        "excerpt": "API integrations connect systems so staff spend less time copying data and more time serving customers and managing operations.",
        "seo_title": "API Integrations for Business Systems | GyLo Softwares",
        "seo_description": "Learn how API integrations reduce double entry, improve workflows, connect tools, and support better business reporting.",
        "content": article(
            "Double entry happens when staff copy the same information from one system to another: orders into spreadsheets, payments into dashboards, customer details into CRMs, or delivery updates into WhatsApp messages. It seems small at first, but it becomes expensive as volume grows.",
            "API integrations allow systems to communicate. A website can create a lead in an internal dashboard. A payment provider can notify an order system. A WhatsApp workflow can create a customer record. A reporting tool can pull data from operations without waiting for manual updates.",
            "The business value is speed, accuracy, and visibility. Teams make fewer mistakes, customers get faster updates, and management sees cleaner data. Integrations also make it easier to scale because the process does not depend entirely on manual copying.",
            "Good integrations need careful planning. The system should handle errors, retries, missing data, authentication, rate limits, audit logs, and admin review. A fragile integration can create confusion, so reliability matters.",
            "Companies should start by identifying where staff repeat the same data entry every day. Those are often the best places to integrate first.",
            "GyLo Softwares builds API-ready systems and connects business tools in a practical way, focusing on workflows that save time and improve operational control.",
        ),
    },
    {
        "title": "How AI Fraud Detection Can Improve Trust in Online Commerce",
        "slug": "how-ai-fraud-detection-can-improve-trust-in-online-commerce",
        "category": "data-science",
        "status": BlogPost.Status.DRAFT,
        "excerpt": "AI fraud detection can help marketplaces, social commerce platforms, and digital businesses identify risk signals and improve customer trust.",
        "seo_title": "AI Fraud Detection for Online Commerce | GyLo Softwares",
        "seo_description": "Explore how AI fraud detection can support trust, risk scoring, profile analysis, and safer online commerce experiences.",
        "content": article(
            "Trust is one of the biggest challenges in online commerce. Buyers want to know whether a seller is real, whether a product will arrive, and whether previous customers had a good experience. Platforms and marketplaces need ways to identify suspicious behavior before it harms users.",
            "AI fraud detection can support this by analyzing patterns that humans may miss at scale. These patterns may include account behavior, text signals, profile completeness, transaction history, customer complaints, unusual activity, and other risk indicators. The output should usually be a risk score or review signal, not an automatic final judgment.",
            "For social commerce, fraud detection may involve seller profile analysis, language patterns, engagement signals, and evidence from previous interactions. The local context matters because buyer behavior, payment habits, and seller practices differ by market.",
            "Responsible AI fraud detection needs quality data, clear definitions of risk, human review, and ongoing evaluation. A system that flags too many honest users can damage trust. A system that misses obvious fraud also fails. Balance matters.",
            "AI is most useful when combined with operational workflows: review queues, admin notes, evidence storage, customer reporting, and escalation rules.",
            "GyLo Softwares explores AI risk systems that help businesses improve trust without making unsupported claims or removing human judgment from sensitive decisions.",
        ),
    },
    {
        "title": "What to Prepare Before Hiring a Software Development Company",
        "slug": "what-to-prepare-before-hiring-a-software-development-company",
        "category": "business-digitization",
        "status": BlogPost.Status.DRAFT,
        "excerpt": "A clear project brief helps software teams estimate properly, reduce risk, and build a system that matches the business problem.",
        "seo_title": "Prepare Before Hiring a Software Development Company | GyLo Softwares",
        "seo_description": "Learn what Tanzanian businesses should prepare before hiring a software development company for a web app, mobile app, dashboard, or automation system.",
        "content": article(
            "Hiring a software development company is easier when the business has prepared the right information. You do not need a technical specification before the first conversation, but you should understand the problem well enough to explain it clearly.",
            "Start with the business goal. Are you trying to reduce manual work, improve customer service, launch a marketplace, manage payments, track delivery, create dashboards, or automate support? A clear goal helps the development team recommend the right approach.",
            "Next, map the current process. Who does the work today? What tools are used? Where do mistakes happen? Which approvals are required? What reports does management need? Which customers or staff will use the system? This process map is often more valuable than a long feature wish list.",
            "Prepare any existing materials: spreadsheets, forms, sample reports, screenshots, brand assets, customer messages, and examples of tools you like. Also share constraints such as timeline, budget range, required integrations, and whether the first version must support mobile users.",
            "Good software teams will help refine the scope. They should ask questions, challenge unclear assumptions, and separate the first launch from future improvements. This protects your budget and improves the chance of a successful launch.",
            "GyLo Softwares starts projects with discovery because the right technical decision depends on the business workflow. A clear brief creates a better estimate, a better plan, and a better final system.",
        ),
    },
]


class Command(BaseCommand):
    help = "Seed or update GyLo services, projects, categories, and corporate blog content."

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

        published_at = timezone.now()
        for post in BLOG_POSTS:
            BlogPost.objects.update_or_create(
                slug=post["slug"],
                defaults={
                    "title": post["title"],
                    "category": categories[post["category"]],
                    "excerpt": post["excerpt"],
                    "content": post["content"],
                    "status": post["status"],
                    "published_at": published_at,
                    "seo_title": post["seo_title"],
                    "seo_description": post["seo_description"],
                },
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Seeded services, projects, blog categories, 5 published blog posts, and 5 draft blog posts."
            )
        )
