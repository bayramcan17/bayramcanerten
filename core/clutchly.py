"""Views for the Clutchly pages.

The three URLs stay fixed (App Store links point at them). The language comes from
`?lang=tr|en`, otherwise from Accept-Language, otherwise English. No cookies are set.
"""

import json

from django.http import Http404
from django.shortcuts import render
from django.utils.cache import patch_vary_headers
from django.utils.safestring import mark_safe

from . import content, content_clutchly

PAGES = {
    "product": "/clutchly",
    "privacy": "/clutchly/privacy",
    "support": "/clutchly/support",
}

EMAIL = object()  # Marker for "{email}" inside a text, rendered as a mailto link.

# Escape characters that could close the <script> tag early.
_JSON_ESCAPES = {ord("<"): "\\u003C", ord(">"): "\\u003E", ord("&"): "\\u0026"}


def negotiate_language(request):
    """Return (language, chosen_explicitly)."""
    requested = request.GET.get("lang", "").lower()
    if requested in content_clutchly.LANGUAGES:
        return requested, True

    ranked = []
    for index, part in enumerate(request.headers.get("Accept-Language", "").split(",")):
        code, _, params = part.strip().partition(";")
        quality = 1.0
        if params.strip().startswith("q="):
            try:
                quality = float(params.strip()[2:])
            except ValueError:
                quality = 0.0
        ranked.append((-quality, index, code.split("-")[0].strip().lower()))
    for negative_quality, _index, code in sorted(ranked):
        if negative_quality < 0 and code in content_clutchly.LANGUAGES:
            return code, False
    return content_clutchly.DEFAULT_LANGUAGE, False


def split_email(text):
    """Split a text on "{email}" so templates can render the address as a link."""
    parts = []
    for index, chunk in enumerate(text.split("{email}")):
        if index:
            parts.append(EMAIL)
        if chunk:
            parts.append(chunk)
    return parts


def _page_urls(lang):
    return {key: f"{path}?lang={lang}" for key, path in PAGES.items()}


def _context(request, page, lang, explicit):
    site_url = content.SITE["url"].rstrip("/")
    text = content_clutchly.TEXT[lang]
    other = "en" if lang == "tr" else "tr"
    path = PAGES[page]
    return {
        "site": content.SITE,
        "app": content_clutchly.COMMON,
        "t": text,
        "ui": text["ui"],
        "lang": lang,
        "page": page,
        "page_text": text[page],
        "urls": _page_urls(lang),
        "email_marker": EMAIL,
        # Each URL is its own canonical: the bare one is the x-default (negotiated) page.
        "canonical": f"{site_url}{path}?lang={lang}" if explicit else f"{site_url}{path}",
        "alternates": [
            {"hreflang": code, "url": f"{site_url}{path}?lang={code}"}
            for code in content_clutchly.LANGUAGES
        ]
        + [{"hreflang": "x-default", "url": f"{site_url}{path}"}],
        "languages": [
            {
                "code": code,
                "name": content_clutchly.TEXT[code]["language_name"],
                "url": f"{path}?lang={code}",
                "current": code == lang,
            }
            for code in content_clutchly.LANGUAGES
        ],
        "other_locale": content_clutchly.TEXT[other]["locale"],
        "og_image": f"{site_url}/static/core/img/clutchly/og-{lang}.jpg",
    }


def clutchly_page(request, page):
    if page not in PAGES:
        raise Http404
    lang, explicit = negotiate_language(request)
    context = _context(request, page, lang, explicit)

    if page == "privacy":
        # Explicit keys: a dict's own `.items` would shadow a missing "items" key in templates.
        context["sections"] = [
            {
                "id": section["id"],
                "title": section["title"],
                "paragraphs": [split_email(p) for p in section.get("paragraphs", [])],
                "entries": section.get("items", []),
            }
            for section in context["page_text"]["sections"]
        ]
    elif page == "support":
        context["intro"] = split_email(context["page_text"]["intro"])
    else:
        base = f"core/img/clutchly/{lang}/"
        context["screens"] = [
            {
                "label": screen["label"][lang],
                "small": f"{base}{screen['file']}-400.webp",
                "medium": f"{base}{screen['file']}-800.webp",
                "full": f"{base}{screen['file']}-full.webp",
            }
            for screen in content_clutchly.COMMON["screens"]
        ]
        hero = content_clutchly.COMMON["hero_screen"]
        context["hero"] = {
            "small": f"{base}{hero}-400.webp",
            "medium": f"{base}{hero}-800.webp",
        }
        context["json_ld"] = _software_json_ld(lang, context["canonical"])

    response = render(request, f"core/clutchly/{page}.html", context)
    # The same URL can answer in either language, so caches must key on the header.
    patch_vary_headers(response, ["Accept-Language"])
    return response


def _software_json_ld(lang, url):
    text = content_clutchly.TEXT[lang]["product"]
    data = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": content_clutchly.COMMON["name"],
        "operatingSystem": "iOS",
        "applicationCategory": "SportsApplication",
        "description": text["description"],
        "inLanguage": ["tr", "en"],
        "url": url,
        "author": {"@type": "Person", "name": content.SITE["name"], "url": content.SITE["url"]},
    }
    return mark_safe(json.dumps(data, ensure_ascii=False).translate(_JSON_ESCAPES))


def sitemap_entries():
    site_url = content.SITE["url"].rstrip("/")
    entries = []
    for path in PAGES.values():
        alternates = [
            {"hreflang": code, "url": f"{site_url}{path}?lang={code}"}
            for code in content_clutchly.LANGUAGES
        ] + [{"hreflang": "x-default", "url": f"{site_url}{path}"}]
        for alternate in alternates:
            entries.append({"loc": alternate["url"], "alternates": alternates})
    return entries
