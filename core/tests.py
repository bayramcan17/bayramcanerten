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
