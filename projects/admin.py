from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "industry", "is_featured", "is_published", "updated_at")
    list_filter = ("is_featured", "is_published", "industry", "created_at")
    search_fields = ("title", "tagline", "summary", "industry")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("id", "created_at", "updated_at")
    ordering = ("title",)
