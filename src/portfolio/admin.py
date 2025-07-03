from django.contrib import admin
from nested_admin import NestedTabularInline, NestedModelAdmin
from portfolio.models import Image, Page, Section, Config, ArbitraryFile


# Register your models here.
class ImageInline(NestedTabularInline):
    model = Image
    extra = 1


class SectionAdmin(NestedTabularInline):
    fields = (
        "title",
        "markdown",
        "image_position",
    )
    inlines = (ImageInline,)
    model = Section
    extra = 1


class PageAdmin(NestedModelAdmin):
    inlines = (SectionAdmin,)


@admin.register(ArbitraryFile)
class ArbitraryFileAdmin(admin.ModelAdmin):
    list_display = ("slug", "filename")
    readonly_fields = ("filename",)


admin.site.register(Page, PageAdmin)
admin.site.register(Config)
admin.site.register(Image)
