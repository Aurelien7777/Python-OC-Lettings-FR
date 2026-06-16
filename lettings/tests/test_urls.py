"""Tests for lettings URLs."""

from django.test import SimpleTestCase
from django.urls import resolve, reverse

from lettings.views import letting, lettings_index


class LettingsUrlsTest(SimpleTestCase):
    """Test lettings URL routing."""

    def test_lettings_index_url_resolves_to_lettings_index_view(self):
        """Test that lettings index URL resolves to the expected view."""
        resolver = resolve(reverse("lettings_index"))

        self.assertEqual(resolver.func, lettings_index)

    def test_letting_detail_url_resolves_to_letting_view(self):
        """Test that letting detail URL resolves to the expected view."""
        resolver = resolve(reverse("letting", kwargs={"letting_id": 1}))

        self.assertEqual(resolver.func, letting)
