from django.db import models
from cloudinary.models import CloudinaryField


class Config(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    data = models.TextField()
    enabled = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.name


class Page(models.Model):
    priority = models.IntegerField(default=0, db_index=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    public = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.slug


class Section(models.Model):
    title = models.CharField(max_length=200)
    markdown = models.TextField(null=True, blank=True)
    page = models.ForeignKey(Page, related_name="sections", on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.page.slug} # {self.title}"


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = CloudinaryField("image")
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    section = models.ForeignKey(
        Section,
        related_name="images",
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self) -> str:
        return f"{self.section.title} # {self.title}"
