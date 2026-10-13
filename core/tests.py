import json
import re

from django.contrib.staticfiles import finders
from django.test import SimpleTestCase

from . import content, content_clutchly


class PageTests(SimpleTestCase):
    def get(self, path):
        return self.client.get(path, secure=True)

    def test_index_ok(self):
        response = self.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, content.SITE["name"])

    def test_index_renders_all_projects_and_businesses(self):
        response = self.get("/")
        for item in content.SITE["projects"] + content.SITE["businesses"]:
            self.assertContains(response, item["name"])

    def test_unknown_page_returns_404(self):
        response = self.get("/olmayan-sayfa/")
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "Ana sayfaya dön", status_code=404)
        self.assertContains(response, 'name="robots" content="noindex"', status_code=404)

    def test_external_links_open_safely(self):
        html = self.get("/").content.decode()
        self.assertEqual(html.count('target="_blank"'), html.count('rel="noopener"'))


class EnhancementTests(SimpleTestCase):
    """The page must stay complete without JS; enhancements only hook into it."""

    def html(self):
        return self.client.get("/", secure=True).content.decode()

    def test_nav_links_point_to_sections(self):
        html = self.html()
        for section_id in ("projeler", "isletmeler"):
            with self.subTest(section_id=section_id):
                self.assertIn(f'href="/#{section_id}"', html)
                self.assertIn(f'id="{section_id}"', html)

    def test_theme_toggle_is_hidden_until_js_runs(self):
        self.assertRegex(self.html(), r"<button[^>]*data-theme-toggle[^>]*\shidden>")

    def test_every_lightbox_link_has_a_dialog(self):
        html = self.html()
        targets = re.findall(r'data-lightbox="([^"]+)"', html)
        self.assertTrue(targets)
        for target in targets:
            with self.subTest(target=target):
                self.assertIn(f'<dialog class="lightbox" id="{target}"', html)

    def test_script_is_a_deferred_module(self):
        self.assertIn('<script type="module" src="/static/core/js/site.js"></script>', self.html())
        self.assertIsNotNone(finders.find("core/js/site.js"))


class SeoTests(SimpleTestCase):
    def get(self, path):
        return self.client.get(path, secure=True)

    def test_canonical_and_open_graph(self):
        response = self.get("/")
        self.assertContains(response, '<link rel="canonical" href="https://bayramcanerten.com/">')
        self.assertContains(response, 'property="og:image" content="https://bayramcanerten.com/static/core/img/og.jpg"')
        self.assertContains(response, 'name="twitter:card" content="summary_large_image"')

    def test_person_json_ld(self):
        html = self.get("/").content.decode()
        match = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
        self.assertIsNotNone(match)
        data = json.loads(match.group(1))
        self.assertEqual(data["@type"], "Person")
        self.assertEqual(data["name"], content.SITE["name"])
        self.assertEqual(data["alumniOf"]["name"], content.SITE["school"])
        self.assertIn("https://github.com/bayramcan17", data["sameAs"])

    def test_robots_txt(self):
        response = self.get("/robots.txt")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/plain")
        self.assertContains(response, "Sitemap: https://bayramcanerten.com/sitemap.xml")

    def test_sitemap_xml(self):
        response = self.get("/sitemap.xml")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/xml")
        self.assertContains(response, "<loc>https://bayramcanerten.com/</loc>")

    def test_favicon_ico_redirects_to_static(self):
        response = self.get("/favicon.ico")
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response["Location"], "/static/core/favicon/favicon.ico")


class ContentTests(SimpleTestCase):
    def test_referenced_static_files_exist(self):
        site = content.SITE
        paths = [site["og_image"]["src"]]
        for item in site["projects"] + site["businesses"]:
            if item.get("logo"):
                paths.append(item["logo"]["src"])
            for shot in item.get("screenshots", []):
                paths += [shot["src"], shot["thumb"]]
        for path in paths:
            with self.subTest(path=path):
                self.assertIsNotNone(finders.find(path))


class ClutchlyTests(SimpleTestCase):
    PATHS = ("/clutchly", "/clutchly/privacy", "/clutchly/support")

    def get(self, path, **headers):
        return self.client.get(path, secure=True, headers=headers)

    def test_pages_are_public_and_default_to_english(self):
        for path in self.PATHS:
            with self.subTest(path=path):
                response = self.get(path)
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, '<html lang="en">')
                self.assertIn("Accept-Language", response["Vary"])
                self.assertNotIn("Set-Cookie", response.headers)

    def test_turkish_browser_gets_turkish(self):
        response = self.get("/clutchly/privacy", accept_language="tr-TR,tr;q=0.9,en;q=0.8")
        self.assertContains(response, '<html lang="tr">')
        self.assertContains(response, "Clutchly Gizlilik Politikası")

    def test_accept_language_respects_quality(self):
        response = self.get("/clutchly", accept_language="de;q=1, en;q=0.4, tr;q=0.8")
        self.assertContains(response, '<html lang="tr">')

    def test_query_parameter_overrides_browser_language(self):
        response = self.get("/clutchly/support?lang=en", accept_language="tr")
        self.assertContains(response, '<html lang="en">')
        self.assertContains(response, "Clutchly Support")

    def test_language_switch_and_hreflang_are_present(self):
        html = self.get("/clutchly?lang=tr").content.decode()
        self.assertIn('href="/clutchly?lang=en" hreflang="en"', html)
        self.assertIn('hreflang="x-default" href="https://bayramcanerten.com/clutchly"', html)
        self.assertIn('<link rel="canonical" href="https://bayramcanerten.com/clutchly?lang=tr">', html)

    def test_bare_url_is_its_own_canonical(self):
        html = self.get("/clutchly/privacy").content.decode()
        self.assertIn('<link rel="canonical" href="https://bayramcanerten.com/clutchly/privacy">', html)

    def test_trailing_slash_redirects_keep_language(self):
        response = self.get("/clutchly/privacy/?lang=tr")
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response["Location"], "/clutchly/privacy?lang=tr")

    def test_support_shows_contact_email(self):
        for lang in content_clutchly.LANGUAGES:
            with self.subTest(lang=lang):
                response = self.get(f"/clutchly/support?lang={lang}")
                self.assertContains(response, 'href="mailto:bayrammcan17@gmail.com?subject=Clutchly"')

    def test_privacy_renders_every_section_cleanly(self):
        for lang in content_clutchly.LANGUAGES:
            html = self.get(f"/clutchly/privacy?lang={lang}").content.decode()
            for section in content_clutchly.TEXT[lang]["privacy"]["sections"]:
                with self.subTest(lang=lang, section=section["id"]):
                    self.assertIn(f'id="{section["id"]}"', html)
            self.assertIn('href="mailto:bayrammcan17@gmail.com"', html)
            self.assertNotIn("paragraphs", html)
            self.assertNotIn("{email}", html)

    def test_no_third_party_requests_or_trackers(self):
        for path in self.PATHS:
            html = self.get(path).content.decode()
            with self.subTest(path=path):
                self.assertNotIn("fonts.googleapis.com", html)
                for src in re.findall(r'<(?:script|link|img|iframe)[^>]+(?:src|href)="(https?://[^"]+)"', html):
                    self.assertTrue(src.startswith("https://bayramcanerten.com/"), src)

    def test_app_store_badge_waits_until_live(self):
        html = self.get("/clutchly?lang=en").content.decode()
        if content_clutchly.COMMON["app_store"]["live"]:
            self.assertIn(content_clutchly.COMMON["app_store"]["url"], html)
        else:
            self.assertIn("Coming soon", html)
            self.assertNotIn(content_clutchly.COMMON["app_store"]["url"], html)

    def test_screenshot_files_exist(self):
        for lang in content_clutchly.LANGUAGES:
            for screen in content_clutchly.COMMON["screens"]:
                for size in ("400", "800", "full"):
                    path = f"core/img/clutchly/{lang}/{screen['file']}-{size}.webp"
                    with self.subTest(path=path):
                        self.assertIsNotNone(finders.find(path))
        for lang in content_clutchly.LANGUAGES:
            self.assertIsNotNone(finders.find(f"core/img/clutchly/og-{lang}.jpg"))
        for name in ("icon-96.webp", "icon-192.webp", "icon-384.webp", "favicon-32.png", "apple-touch-icon.png"):
            self.assertIsNotNone(finders.find(f"core/img/clutchly/{name}"))

    def test_sitemap_lists_clutchly_pages(self):
        xml = self.get("/sitemap.xml").content.decode()
        for path in self.PATHS:
            with self.subTest(path=path):
                self.assertIn(f"<loc>https://bayramcanerten.com{path}</loc>", xml)
                self.assertIn(f"<loc>https://bayramcanerten.com{path}?lang=tr</loc>", xml)

    def test_home_links_to_product_page_in_same_tab(self):
        html = self.get("/").content.decode()
        self.assertIn('<a class="badge badge--web" href="/clutchly">', html)
