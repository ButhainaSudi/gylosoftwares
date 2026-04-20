from django.db import models
from django.urls import reverse

from core.models import UUIDTimestampedModel


class Project(UUIDTimestampedModel):
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True)
    tagline = models.CharField(max_length=220)
    summary = models.TextField()
    problem = models.TextField()
    solution = models.TextField()
    key_features = models.TextField(help_text="One feature per line.")
    tech_stack = models.TextField(help_text="One technology or approach per line.")
    industry = models.CharField(max_length=160)
    featured_image = models.ImageField(upload_to="projects/", blank=True)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    seo_title = models.CharField(max_length=180)
    seo_description = models.CharField(max_length=300)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"slug": self.slug})

    def feature_list(self):
        return [item.strip() for item in self.key_features.splitlines() if item.strip()]

    def tech_list(self):
        return [item.strip() for item in self.tech_stack.splitlines() if item.strip()]
