"""Tests for main site views."""

from django.test import TestCase, override_settings
from django.urls import reverse


class IndexViewTest(TestCase):
    """Test main site views."""

    def test_index_returns_status_code_200(self):
        """Test that home page is accessible."""
        response = self.client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)

    def test_index_uses_expected_template(self):
        """Test that home page uses the expected template."""
        response = self.client.get(reverse("index"))

        self.assertTemplateUsed(response, "oc_lettings_site/index.html")


class ErrorPagesTest(TestCase):
    """Test custom error pages."""

    @override_settings(DEBUG=False, ALLOWED_HOSTS=["testserver"])
    def test_custom_404_page_is_used(self):
        """Test that custom 404 page is displayed."""
        response = self.client.get("/unknown-page/")

        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "oc_lettings_site/404.html")

    def test_custom_500_view_returns_status_code_500(self):
        """Test that custom 500 view returns status code 500."""
        response = self.client.get("/")

        from oc_lettings_site.views import server_error

        response = server_error(response.wsgi_request)

        self.assertEqual(response.status_code, 500)
