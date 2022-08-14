from django.db import models
from cloudinary.models import CloudinaryField


class Page(models.Model):
    priority = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    public = models.BooleanField(default=True)
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
        Section, related_name="images", on_delete=models.DO_NOTHING
    )

    def __str__(self) -> str:
        return f"{self.section.title} # {self.title}"
