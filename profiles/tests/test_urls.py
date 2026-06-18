"""Tests for profiles URLs."""

from django.test import SimpleTestCase
from django.urls import resolve, reverse

from profiles.views import profile, index


class ProfilesUrlsTest(SimpleTestCase):
    """Test profiles URL routing."""

    def test_profiles_index_url_resolves_to_profiles_index_view(self):
        """Test that profiles index URL resolves to the expected view."""
        resolver = resolve(reverse("profiles:index"))

        self.assertEqual(resolver.func, index)

    def test_profile_detail_url_resolves_to_profile_view(self):
        """Test that profile detail URL resolves to the expected view."""
        resolver = resolve(reverse("profiles:profile", kwargs={"username": "testuser"}))

        self.assertEqual(resolver.func, profile)
