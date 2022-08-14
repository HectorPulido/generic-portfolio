import markdown
from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets

from portfolio.serializers import (
    PageNavSerializer,
    CompletePageSerializer,
    ConfigSerializer,
)

from portfolio.models import Page, Config


class PageViewSet(viewsets.ReadOnlyModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"

    queryset = Page.objects.filter(public=True).all()
    page_serializer = CompletePageSerializer
    page_nav_serializer = PageNavSerializer

    def config(self):
        config_data = Config.objects.filter(enabled=True)
        config_data = ConfigSerializer(config_data, many=True).data
        data_dict = {}
        
        for data in config_data:
            if 'markdown' in data['name']:
                data['data'] = markdown.markdown(data['data'])

            data_dict[data['name']] = data['data']
        
        return data_dict

    def list(self, request, *args, **kwargs):
        current_page = self.queryset.order_by("-priority").first()

        if not current_page:
            raise Http404()

        page_data = self.page_serializer(current_page).data

        # Nav
        nav_data = self.page_nav_serializer(
            self.queryset.order_by("-priority"), many=True
        ).data

        data = {"page_data": page_data, "nav_data": nav_data, "extra_data": self.config()}

        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        page_slug = kwargs.get("pk")
        if not page_slug:
            raise Http404()

        # Page
        current_page = get_object_or_404(Page, slug=page_slug)
        page_data = self.page_serializer(current_page).data

        # Nav
        nav_data = self.page_nav_serializer(
            self.queryset.order_by("-priority"), many=True
        ).data

        data = {"page_data": page_data, "nav_data": nav_data, "extra_data": self.config()}

        return Response(data)
