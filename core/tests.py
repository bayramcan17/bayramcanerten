import json
import re

from django.contrib.staticfiles import finders
from django.test import SimpleTestCase

from . import content, content_clutchly, content_orbit_shift


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

    def test_every_page_links_back_to_projects(self):
        for path in self.PATHS:
            for lang, label in (("tr", "Projeler"), ("en", "Projects")):
                with self.subTest(path=path, lang=lang):
                    html = self.get(f"{path}?lang={lang}").content.decode()
                    self.assertRegex(html, r'<a class="nav__back" href="/#projeler">[\s\S]*?' + label + "</span>")

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
        app_store = content_clutchly.COMMON["app_store"]
        if app_store["live"]:
            self.assertIn(f'<a class="store-badge" href="{app_store["urls"]["en"]}" target="_blank" rel="noopener">', html)
            self.assertIn(f'<meta name="apple-itunes-app" content="app-id={app_store["id"]}">', html)
            turkish = self.get("/clutchly?lang=tr").content.decode()
            self.assertIn(f'<a class="store-badge" href="{app_store["urls"]["tr"]}" target="_blank" rel="noopener">', turkish)
            self.assertIn("apps.apple.com/tr/app/id6821973888?l=tr", app_store["urls"]["tr"])
            home = self.get("/").content.decode()
            self.assertIn(f'href="{app_store["urls"]["tr"]}"', home)
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


class OrbitShiftTests(SimpleTestCase):
    PATHS = ("/orbit-shift", "/orbit-shift/privacy", "/orbit-shift/support")

    def get(self, path, **headers):
        return self.client.get(path, secure=True, headers=headers)

    def test_pages_are_public_english_and_cookie_free(self):
        for path in self.PATHS:
            with self.subTest(path=path):
                response = self.get(path, accept_language="tr")
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, '<html lang="en">')
                self.assertNotIn("Set-Cookie", response.headers)
                self.assertContains(response, f'<link rel="canonical" href="https://bayramcanerten.com{path}">')

    def test_trailing_slash_redirects(self):
        response = self.get("/orbit-shift/privacy/")
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response["Location"], "/orbit-shift/privacy")

    def test_every_page_links_back_to_projects(self):
        for path in self.PATHS:
            with self.subTest(path=path):
                self.assertRegex(
                    self.get(path).content.decode(),
                    r'<a class="nav__back" href="/#projeler">[\s\S]*?Projects</span>',
                )

    def test_product_page_meta_and_text(self):
        html = self.get("/orbit-shift").content.decode()
        self.assertIn(f"<title>{content_orbit_shift.PRODUCT['title']}</title>", html)
        self.assertIn('property="og:image" content="https://bayramcanerten.com/static/core/img/orbit-shift/og.jpg"', html)
        self.assertIn('property="og:description" content="Two orbits. One tap. How long can you last?"', html)
        self.assertIn(content_orbit_shift.PRODUCT["intro"], html)
        for feature in content_orbit_shift.PRODUCT["features"]:
            with self.subTest(feature=feature["title"]):
                self.assertIn(feature["text"], html)
        match = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
        data = json.loads(match.group(1))
        self.assertEqual(data["name"], "Orbit Shift: Neon Rush")
        self.assertEqual(data["applicationCategory"], "GameApplication")

    def test_store_badges_wait_until_live(self):
        html = self.get("/orbit-shift").content.decode()
        common = content_orbit_shift.COMMON
        if not common["app_store"]["live"]:
            self.assertNotIn("apple-itunes-app", html)
            self.assertNotIn("apps.apple.com", html)
        if not common["google_play"]["live"]:
            self.assertNotIn("play.google.com", html)
        if not (common["app_store"]["live"] or common["google_play"]["live"]):
            self.assertIn("Coming soon to the App Store and Google Play.", html)

    def test_privacy_renders_every_section_and_markup(self):
        html = self.get("/orbit-shift/privacy").content.decode()
        for section in content_orbit_shift.PRIVACY["sections"]:
            with self.subTest(section=section["id"]):
                self.assertIn(f'id="{section["id"]}"', html)
        self.assertIn("Effective date: November 16, 2026", html)
        self.assertIn('<a href="mailto:bayrammcan17@gmail.com">bayrammcan17@gmail.com</a>', html)
        self.assertIn('href="https://policies.google.com/privacy" target="_blank" rel="noopener"', html)
        self.assertIn("<strong>not collect</strong>", html)
        for leftover in ("**", "{email}", "](", "&lt;strong"):
            self.assertNotIn(leftover, html)

    def test_support_shows_contact_and_faq(self):
        html = self.get("/orbit-shift/support").content.decode()
        self.assertIn('href="mailto:bayrammcan17@gmail.com?subject=Orbit%20Shift"', html)
        self.assertIn('<a href="/orbit-shift/privacy">Privacy Policy</a>', html)
        for question, _answer in content_orbit_shift.SUPPORT["faq"]:
            with self.subTest(question=question):
                self.assertIn(f"<summary>{question}", html)
        self.assertNotIn("**", html)

    def test_no_third_party_requests(self):
        for path in self.PATHS:
            html = self.get(path).content.decode()
            with self.subTest(path=path):
                self.assertNotIn("fonts.googleapis.com", html)
                for src in re.findall(r'<(?:script|link|img|iframe)[^>]+(?:src|href)="(https?://[^"]+)"', html):
                    self.assertTrue(src.startswith("https://bayramcanerten.com/"), src)

    def test_static_files_exist(self):
        base = "core/img/orbit-shift/"
        names = ["og.jpg", "favicon-32.png", "apple-touch-icon.png"]
        names += [f"icon-{size}.webp" for size in (96, 192, 384)]
        for screen in content_orbit_shift.COMMON["screens"]:
            names += [f"screens/{screen['file']}-{size}.webp" for size in ("400", "full")]
        paths = [base + name for name in names]
        paths += ["core/fonts/space-grotesk-500.woff2", "core/fonts/space-grotesk-700.woff2", "core/css/orbit-shift.css"]
        for path in paths:
            with self.subTest(path=path):
                self.assertIsNotNone(finders.find(path))

    def test_sitemap_lists_pages(self):
        xml = self.get("/sitemap.xml").content.decode()
        for path in self.PATHS:
            with self.subTest(path=path):
                self.assertIn(f"<loc>https://bayramcanerten.com{path}</loc>", xml)

    def test_home_card_links_to_game_page(self):
        html = self.get("/").content.decode()
        self.assertIn('<a class="badge badge--web" href="/orbit-shift">', html)

    def test_app_ads_txt_only_with_publisher_id(self):
        publisher_id = content_orbit_shift.COMMON["admob_publisher_id"]
        response = self.get("/app-ads.txt")
        if publisher_id:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response["Content-Type"], "text/plain")
            self.assertEqual(response.content.decode(), f"google.com, {publisher_id}, DIRECT, f08c47fec0942fa0\n")
        else:
            self.assertEqual(response.status_code, 404)
