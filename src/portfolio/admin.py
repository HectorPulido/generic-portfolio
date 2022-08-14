from django.contrib import admin
from nested_admin import NestedTabularInline, NestedModelAdmin
from portfolio.models import Image, Page, Section

# Register your models here.
class ImageInline(NestedTabularInline):
    model = Image
    extra = 1


class SectionAdmin(NestedTabularInline):
    fields = (
        "title",
        "markdown",
    )
    inlines = (ImageInline,)
    model = Section
    extra = 1


class PageAdmin(NestedModelAdmin):
    inlines = (SectionAdmin,)


admin.site.register(Page, PageAdmin)
