"""Tests for profiles models."""

from django.contrib.auth.models import User
from django.test import TestCase

from profiles.models import Profile


class ProfileModelTest(TestCase):
    """Test Profile model."""

    def test_profile_str_returns_username(self):
        """Test that Profile string representation is correct."""
        user = User.objects.create_user(username="testuser")
        profile = Profile.objects.create(
            user=user,
            favorite_city="Paris",
        )

        self.assertEqual(str(profile), "testuser")
