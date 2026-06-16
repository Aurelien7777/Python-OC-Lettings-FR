"""Tests for main site URLs."""

from django.test import SimpleTestCase
from django.urls import resolve, reverse

from oc_lettings_site.views import index


class MainSiteUrlsTest(SimpleTestCase):
    """Test main site URL routing."""

    def test_index_url_resolves_to_index_view(self):
        """Test that the home URL resolves to the index view."""
        resolver = resolve(reverse("index"))

        self.assertEqual(resolver.func, index)
