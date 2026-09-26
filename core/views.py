import json

from django.shortcuts import render
from django.utils.safestring import mark_safe

from . import content

# Escape characters that could close the <script> tag early.
_JSON_ESCAPES = {ord("<"): "\\u003C", ord(">"): "\\u003E", ord("&"): "\\u0026"}


def _person_json_ld():
    site = content.SITE
    data = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": site["name"],
        "jobTitle": site["title"],
        "url": site["url"],
        "image": site["url"].rstrip("/") + "/static/" + site["og_image"]["src"],
        "alumniOf": {"@type": "CollegeOrUniversity", "name": site["school"]},
        "sameAs": [social["url"] for social in site["socials"]],
    }
    return mark_safe(json.dumps(data, ensure_ascii=False).translate(_JSON_ESCAPES))


def index(request):
    return render(
        request,
        "core/index.html",
        {"site": content.SITE, "json_ld": _person_json_ld()},
    )


def robots_txt(request):
    return render(request, "core/robots.txt", {"site": content.SITE}, content_type="text/plain")


def sitemap_xml(request):
    return render(request, "core/sitemap.xml", {"site": content.SITE}, content_type="application/xml")


def page_not_found(request, exception):
    return render(request, "core/404.html", {"site": content.SITE}, status=404)
