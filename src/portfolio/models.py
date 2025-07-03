import os
from django.db import models


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
    external_url = models.TextField(
        null=True, blank=True, help_text="This is only useful if mode is external"
    )

    MODE_CHOICES = [
        ("page", "Internal page"),
        ("external", "External page"),
    ]
    mode = models.CharField(
        max_length=20,
        choices=MODE_CHOICES,
        default="page",
        help_text="Select if the page is internal, redirect or external link",
    )
    show_in_nav = models.BooleanField(
        default=True,
        db_index=True,
        help_text="If false, the page will not show in the nav",
    )

    def __str__(self) -> str:
        return self.slug


class Section(models.Model):
    title = models.CharField(max_length=200)
    markdown = models.TextField(null=True, blank=True)
    page = models.ForeignKey(Page, related_name="sections", on_delete=models.DO_NOTHING)
    POS_CHOICES = [("top", "Top"), ("bottom", "Bottom"), ("none", "None")]
    image_position = models.CharField(
        max_length=10,
        choices=POS_CHOICES,
        default="none",
        help_text="Set the images on top or on bottom .",
    )

    def __str__(self) -> str:
        return f"{self.page.slug} # {self.title}"


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    section = models.ForeignKey(
        Section,
        related_name="images",
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
    )
    STYLE_CHOICES = [("rect", "Rect"), ("round", "Circular")]
    display_style = models.CharField(
        max_length=10,
        choices=STYLE_CHOICES,
        default="rect",
        help_text="Defines if the image is circular or rectangular.",
    )

    def __str__(self) -> str:
        return f"{self.section.title} # {self.title}"


class ArbitraryFile(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    file = models.FileField(upload_to="arbitrary/")

    def __str__(self):
        return self.slug

    @property
    def filename(self):
        return os.path.basename(self.file.name)
