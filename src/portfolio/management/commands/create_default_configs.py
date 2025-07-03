from django.core.management.base import BaseCommand
from portfolio.models import Config


class Command(BaseCommand):
    help = "Make default configurations."

    def handle(self, *args, **options):
        defaults = {
            "primary_color": "#1a1a1a",
            "secondary_color": "#f0f0f0",
            "background_image_url": "",
            "font_family": "Arial, sans-serif",
            "favicon": "/favicon.ico",
            "nav_title": "My portfolio",
            "footer_markdown": "footer_markdown",
            "web_title": "My portfolio",
        }
        for name, data in defaults.items():
            Config.objects.get_or_create(
                name=name, defaults={"data": data, "enabled": True}
            )
        self.stdout.write(self.style.SUCCESS("Default configs creados/actualizados."))
