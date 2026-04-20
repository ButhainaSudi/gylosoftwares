from django import forms

from .models import ContactMessage, Lead


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["full_name", "company_name", "email", "phone", "service_interest", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 5}),
        }


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            "full_name",
            "company_name",
            "email",
            "phone",
            "industry",
            "project_type",
            "budget_range",
            "timeline",
            "message",
            "has_existing_system",
            "has_existing_designs",
            "attachment",
        ]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 6}),
            "has_existing_system": forms.CheckboxInput(),
            "has_existing_designs": forms.CheckboxInput(),
        }
