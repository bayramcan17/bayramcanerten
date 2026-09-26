from django.test import SimpleTestCase

from . import content


class PageTests(SimpleTestCase):
    def test_index_ok(self):
        response = self.client.get("/", secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, content.SITE["name"])

    def test_index_renders_all_projects_and_businesses(self):
        response = self.client.get("/", secure=True)
        for item in content.SITE["projects"] + content.SITE["businesses"]:
            self.assertContains(response, item["name"])

    def test_unknown_page_returns_404(self):
        response = self.client.get("/olmayan-sayfa/", secure=True)
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "Ana sayfaya dön", status_code=404)

    def test_external_links_open_safely(self):
        response = self.client.get("/", secure=True)
        html = response.content.decode()
        self.assertEqual(html.count('target="_blank"'), html.count('rel="noopener"'))
