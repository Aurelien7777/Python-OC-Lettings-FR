"""Tests for main site views."""

from django.test import TestCase
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
