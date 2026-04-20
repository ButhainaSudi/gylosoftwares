from django.contrib import admin

from .models import ContactMessage, Lead


@admin.action(description="Mark selected leads as contacted")
def mark_as_contacted(modeladmin, request, queryset):
    queryset.update(status=Lead.Status.CONTACTED)


@admin.action(description="Mark selected leads as qualified")
def mark_as_qualified(modeladmin, request, queryset):
    queryset.update(status=Lead.Status.QUALIFIED)


@admin.action(description="Mark selected leads as won")
def mark_as_won(modeladmin, request, queryset):
    queryset.update(status=Lead.Status.WON)


@admin.action(description="Mark selected leads as lost")
def mark_as_lost(modeladmin, request, queryset):
    queryset.update(status=Lead.Status.LOST)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("full_name", "company_name", "project_type", "budget_range", "status", "created_at")
    list_filter = ("status", "project_type", "budget_range", "created_at")
    search_fields = ("full_name", "company_name", "email", "phone", "message")
    readonly_fields = ("id", "created_at", "updated_at")
    ordering = ("-created_at",)
    actions = [mark_as_contacted, mark_as_qualified, mark_as_won, mark_as_lost]


@admin.action(description="Mark selected messages as read")
def mark_as_read(modeladmin, request, queryset):
    queryset.update(is_read=True)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("full_name", "company_name", "email", "service_interest", "is_read", "created_at")
    list_filter = ("is_read", "service_interest", "created_at")
    search_fields = ("full_name", "company_name", "email", "phone", "message")
    readonly_fields = ("id", "created_at", "updated_at")
    ordering = ("-created_at",)
    actions = [mark_as_read]
