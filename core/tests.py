import json
import re

from django.contrib.staticfiles import finders
from django.test import SimpleTestCase

from . import content


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
