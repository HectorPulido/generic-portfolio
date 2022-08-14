from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets

from portfolio.serializers import PageNavSerializer, CompletePageSerializer

from portfolio.models import Page


class PageViewSet(viewsets.ReadOnlyModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"

    queryset = Page.objects.filter(public=True).all()
    page_serializer = CompletePageSerializer
    page_nav_serializer = PageNavSerializer

    def list(self, request, *args, **kwargs):
        current_page = self.queryset.order_by("priority").first()
        page_data = self.page_serializer(current_page).data

        # Nav
        nav_data = self.page_nav_serializer(
            self.queryset.order_by("priority"), many=True
        ).data

        data = {"page_data": page_data, "nav_data": nav_data}

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
            self.queryset.order_by("priority"), many=True
        ).data

        data = {"page_data": page_data, "nav_data": nav_data}

        return Response(data)
