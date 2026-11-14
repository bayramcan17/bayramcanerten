"""Views for the Orbit Shift: Neon Rush pages.

The three URLs stay fixed: the game (Settings > Privacy policy) and the store listings link
to them. English only, like the game. /app-ads.txt lives here too because AdMob reads it
for this game.
"""

import json
import re

from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.utils.html import escape
from django.utils.safestring import mark_safe

from . import content
from . import content_orbit_shift as text

PAGES = {
    "product": "/orbit-shift",
    "privacy": "/orbit-shift/privacy",
    "support": "/orbit-shift/support",
}

# Escape characters that could close the <script> tag early.
_JSON_ESCAPES = {ord("<"): "\\u003C", ord(">"): "\\u003E", ord("&"): "\\u0026"}

_BOLD = re.compile(r"\*\*(.+?)\*\*")
_LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")


def inline(value):
    """Render the small markup used in content_orbit_shift: **bold**, [label](url), {email}."""
    email = text.COMMON["email"]
    html = escape(value)
    html = _LINK.sub(
        lambda m: (
            f'<a href="{m.group(2)}">{m.group(1)}</a>'
            if m.group(2).startswith("/")
            else f'<a href="{m.group(2)}" target="_blank" rel="noopener">{m.group(1)}</a>'
        ),
        html,
    )
    html = _BOLD.sub(r"<strong>\1</strong>", html)
    html = html.replace("{email}", f'<a href="mailto:{email}">{email}</a>')
    return mark_safe(html)


def _store_urls():
    common = text.COMMON
    return {
        "app_store": common["app_store"]["url"] if common["app_store"]["live"] else None,
        "google_play": common["google_play"]["url"] if common["google_play"]["live"] else None,
    }


def _context(page):
    site_url = content.SITE["url"].rstrip("/")
    return {
        "site": content.SITE,
        "app": text.COMMON,
        "ui": text.UI,
        "nav": text.NAV,
        "lang": "en",
        "page": page,
        "urls": PAGES,
        "canonical": f"{site_url}{PAGES[page]}",
        "og_image": f"{site_url}/static/core/img/orbit-shift/og.jpg",
        "stores": _store_urls(),
    }


def orbit_shift_page(request, page):
    if page not in PAGES:
        raise Http404
    context = _context(page)

    if page == "privacy":
        page_text = text.PRIVACY
        context["intro"] = inline(page_text["intro"])
        context["sections"] = [
            {
                "id": section["id"],
                "title": section["title"],
                "paragraphs": [inline(p) for p in section.get("paragraphs", [])],
                "entries": [inline(item) for item in section.get("items", [])],
                "after": [inline(p) for p in section.get("after", [])],
            }
            for section in page_text["sections"]
        ]
    elif page == "support":
        page_text = text.SUPPORT
        context["intro"] = inline(page_text["intro"])
        context["faq"] = [(question, inline(answer)) for question, answer in page_text["faq"]]
    else:
        page_text = text.PRODUCT
        base = "core/img/orbit-shift/screens/"
        context["screens"] = [
            {
                "label": screen["label"],
                "small": f"{base}{screen['file']}-400.webp",
                "full": f"{base}{screen['file']}-full.webp",
            }
            for screen in text.COMMON["screens"]
        ]
        hero = text.COMMON["hero_screen"]
        context["hero"] = {"small": f"{base}{hero}-400.webp", "full": f"{base}{hero}-full.webp"}
        context["json_ld"] = _game_json_ld(context["canonical"])

    context["page_text"] = page_text
    return render(request, f"core/orbit_shift/{page}.html", context)


def _game_json_ld(url):
    data = {
        "@context": "https://schema.org",
        "@type": ["VideoGame", "SoftwareApplication"],
        "name": text.COMMON["name"],
        "description": text.PRODUCT["description"],
        "applicationCategory": "GameApplication",
        "genre": "Arcade",
        "operatingSystem": "iOS 15+, Android 7.1+",
        "gamePlatform": ["iPhone", "iPad", "Android"],
        "inLanguage": "en",
        "contentRating": "13+",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "url": url,
        "image": f"{content.SITE['url'].rstrip('/')}/static/core/img/orbit-shift/og.jpg",
        "author": {"@type": "Person", "name": content.SITE["name"], "url": content.SITE["url"]},
    }
    installs = [link for link in _store_urls().values() if link]
    if installs:
        data["installUrl"] = installs[0] if len(installs) == 1 else installs
    return mark_safe(json.dumps(data, ensure_ascii=False).translate(_JSON_ESCAPES))


def app_ads_txt(request):
    """AdMob's authorized-sellers file (domain root). 404 until the publisher ID is known."""
    publisher_id = text.COMMON["admob_publisher_id"]
    if not publisher_id:
        raise Http404
    # f08c47fec0942fa0 is Google's fixed certification authority ID.
    body = f"google.com, {publisher_id}, DIRECT, f08c47fec0942fa0\n"
    return HttpResponse(body, content_type="text/plain")


def sitemap_entries():
    site_url = content.SITE["url"].rstrip("/")
    return [f"{site_url}{path}" for path in PAGES.values()]
