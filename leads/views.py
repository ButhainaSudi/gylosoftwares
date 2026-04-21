from django.db import transaction
from django.shortcuts import redirect, render
from django.urls import reverse

from core.seo import page_context

from .email import notify_contact_message, notify_lead
from .forms import ContactMessageForm, LeadForm


def contact(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            transaction.on_commit(lambda: notify_contact_message(message))
            return redirect("leads:contact_success")
    else:
        form = ContactMessageForm()

    context = page_context(
        "Contact GyLo Softwares | Software Development Company in Tanzania",
        "Contact GyLo Softwares for custom software development, AI automation, WhatsApp automation, and business system inquiries in Tanzania.",
        reverse("leads:contact"),
        breadcrumbs=[("Home", reverse("pages:home")), ("Contact", reverse("leads:contact"))],
    )
    context["form"] = form
    return render(request, "leads/contact.html", context)


def contact_success(request):
    context = page_context(
        "Message Received | GyLo Softwares",
        "Thank you for contacting GyLo Softwares. Our team will respond soon.",
        reverse("leads:contact_success"),
    )
    return render(request, "leads/success.html", context)


def start_project(request):
    if request.method == "POST":
        form = LeadForm(request.POST, request.FILES)
        if form.is_valid():
            lead = form.save()
            transaction.on_commit(lambda: notify_lead(lead))
            return redirect("leads:start_project_success")
    else:
        form = LeadForm()

    context = page_context(
        "Start a Software Project | GyLo Softwares",
        "Start your custom software, AI automation, web app, mobile app, dashboard, or business system project with GyLo Softwares.",
        reverse("leads:start_project"),
        breadcrumbs=[("Home", reverse("pages:home")), ("Start a Project", reverse("leads:start_project"))],
    )
    context["form"] = form
    return render(request, "leads/start_project.html", context)


def start_project_success(request):
    context = page_context(
        "Project Inquiry Received | GyLo Softwares",
        "Thank you for submitting your project inquiry to GyLo Softwares.",
        reverse("leads:start_project_success"),
    )
    return render(request, "leads/success.html", context)
