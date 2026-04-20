from django.db import models
from django.urls import reverse

from core.models import UUIDTimestampedModel


class Service(UUIDTimestampedModel):
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True)
    short_description = models.CharField(max_length=260)
    full_description = models.TextField()
    icon = models.CharField(max_length=80, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    seo_title = models.CharField(max_length=180)
    seo_description = models.CharField(max_length=300)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("services:detail", kwargs={"slug": self.slug})
