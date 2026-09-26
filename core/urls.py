from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("robots.txt", views.robots_txt, name="robots_txt"),
    path("sitemap.xml", views.sitemap_xml, name="sitemap_xml"),
    path(
        "favicon.ico",
        RedirectView.as_view(url=static("core/favicon/favicon.ico"), permanent=True),
    ),
]
