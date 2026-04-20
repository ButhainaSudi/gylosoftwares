from django.db import models
from django.urls import reverse
from django.utils import timezone

from core.models import UUIDTimestampedModel


class BlogCategory(UUIDTimestampedModel):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "blog categories"

    def __str__(self):
        return self.name


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=BlogPost.Status.PUBLISHED, published_at__lte=timezone.now())


class BlogPost(UUIDTimestampedModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.PROTECT, related_name="posts")
    excerpt = models.TextField()
    content = models.TextField()
    featured_image = models.ImageField(upload_to="blog/", blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    published_at = models.DateTimeField(default=timezone.now)
    seo_title = models.CharField(max_length=180)
    seo_description = models.CharField(max_length=300)

    objects = BlogPostQuerySet.as_manager()

    class Meta:
        ordering = ["-published_at", "title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
