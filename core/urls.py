from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView

from . import clutchly, views

urlpatterns = [
    path("", views.index, name="index"),
    path("robots.txt", views.robots_txt, name="robots_txt"),
    path("sitemap.xml", views.sitemap_xml, name="sitemap_xml"),
    path(
        "favicon.ico",
        RedirectView.as_view(url=static("core/favicon/favicon.ico"), permanent=True),
    ),
    # Clutchly: the URLs without a trailing slash are the public ones (App Store links).
    path("clutchly", clutchly.clutchly_page, {"page": "product"}, name="clutchly"),
    path("clutchly/privacy", clutchly.clutchly_page, {"page": "privacy"}, name="clutchly_privacy"),
    path("clutchly/support", clutchly.clutchly_page, {"page": "support"}, name="clutchly_support"),
    path("clutchly/", RedirectView.as_view(url="/clutchly", query_string=True, permanent=True)),
    path("clutchly/privacy/", RedirectView.as_view(url="/clutchly/privacy", query_string=True, permanent=True)),
    path("clutchly/support/", RedirectView.as_view(url="/clutchly/support", query_string=True, permanent=True)),
]
