import markdown
from rest_framework import serializers

from portfolio.models import Page, Section, Image, Config


class PageNavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ["title", "slug", "priority", "mode", "external_url"]


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ["title", "image", "description", "url", "display_style"]

    def get_image(self, obj):
        return obj.image.url


class SectionSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    html_data = serializers.SerializerMethodField()

    class Meta:
        model = Section
        fields = ["title", "html_data", "images", "image_position"]

    def get_images(self, obj):
        return ImageSerializer(obj.images.all(), many=True).data

    def get_html_data(self, obj):
        return markdown.markdown(obj.markdown)


class CompletePageSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ["title", "slug", "description", "sections"]

    def get_sections(self, obj):
        return SectionSerializer(obj.sections.all(), many=True).data


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = ["name", "data"]
