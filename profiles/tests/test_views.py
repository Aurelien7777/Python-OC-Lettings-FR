"""Tests for profiles views."""

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from profiles.models import Profile


class ProfilesViewsTest(TestCase):
    """Test profiles views."""

    def setUp(self):
        """Create test data for profiles views."""
        self.user = User.objects.create_user(username="testuser")
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city="Paris",
        )

    def test_profiles_index_returns_status_code_200(self):
        """Test that profiles index page is accessible."""
        response = self.client.get(reverse("profiles:index"))

        self.assertEqual(response.status_code, 200)

    def test_profiles_index_uses_expected_template(self):
        """Test that profiles index uses the expected template."""
        response = self.client.get(reverse("profiles:index"))

        self.assertTemplateUsed(response, "profiles/index.html")

    def test_profiles_index_contains_profiles_list(self):
        """Test that profiles index contains the profiles list."""
        response = self.client.get(reverse("profiles:index"))

        self.assertIn("profiles_list", response.context)
        self.assertEqual(list(response.context["profiles_list"]), [self.profile])

    def test_profile_detail_returns_status_code_200(self):
        """Test that profile detail page is accessible."""
        response = self.client.get(
            reverse("profiles:profile", kwargs={"username": self.user.username})
        )

        self.assertEqual(response.status_code, 200)

    def test_profile_detail_uses_expected_template(self):
        """Test that profile detail uses the expected template."""
        response = self.client.get(
            reverse("profiles:profile", kwargs={"username": self.user.username})
        )

        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_profile_detail_contains_expected_context(self):
        """Test that profile detail contains expected context data."""
        response = self.client.get(
            reverse("profiles:profile", kwargs={"username": self.user.username})
        )

        self.assertEqual(response.context["profile"], self.profile)

    def test_profile_detail_returns_404_when_not_found(self):
        response = self.client.get(
            reverse("profiles:profile", kwargs={"username": "unknown"})
        )

        self.assertEqual(response.status_code, 404)
