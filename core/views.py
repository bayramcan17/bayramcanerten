from django.shortcuts import render

from . import clutchly, content, orbit_shift
from .jsonld import json_ld


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
    return json_ld(data)


def index(request):
    return render(
        request,
        "core/index.html",
        {"site": content.SITE, "json_ld": _person_json_ld()},
    )


def robots_txt(request):
    return render(request, "core/robots.txt", {"site": content.SITE}, content_type="text/plain")


def sitemap_xml(request):
    return render(
        request,
        "core/sitemap.xml",
        {
            "site": content.SITE,
            "clutchly_entries": clutchly.sitemap_entries(),
            "orbit_shift_entries": orbit_shift.sitemap_entries(),
        },
        content_type="application/xml",
    )


def page_not_found(request, exception):
    return render(request, "core/404.html", {"site": content.SITE}, status=404)
