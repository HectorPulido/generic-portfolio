from django.urls import path, include

from portfolio.views import PageViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"", PageViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path('', IndexView.as_view(), name='index'),
    # path('<slug:page_slug>/', PagesView.as_view(), name='page'),
]
