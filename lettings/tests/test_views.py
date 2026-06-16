"""Tests for lettings views."""

from django.test import TestCase
from django.urls import reverse

from lettings.models import Address, Letting


class LettingsViewsTest(TestCase):
    """Test lettings views."""

    def setUp(self):
        """Create test data for lettings views."""
        self.address = Address.objects.create(
            number=10,
            street="Main Street",
            city="Paris",
            state="FR",
            zip_code=75000,
            country_iso_code="FRA",
        )
        self.letting = Letting.objects.create(
            title="Beautiful apartment",
            address=self.address,
        )

    def test_lettings_index_returns_status_code_200(self):
        """Test that lettings index page is accessible."""
        response = self.client.get(reverse("lettings_index"))

        self.assertEqual(response.status_code, 200)

    def test_lettings_index_uses_expected_template(self):
        """Test that lettings index uses the expected template."""
        response = self.client.get(reverse("lettings_index"))

        self.assertTemplateUsed(response, "lettings/lettings_index.html")

    def test_lettings_index_contains_lettings_list(self):
        """Test that lettings index contains the lettings list."""
        response = self.client.get(reverse("lettings_index"))

        self.assertIn("lettings_list", response.context)
        self.assertEqual(list(response.context["lettings_list"]), [self.letting])

    def test_letting_detail_returns_status_code_200(self):
        """Test that letting detail page is accessible."""
        response = self.client.get(
            reverse("letting", kwargs={"letting_id": self.letting.id})
        )

        self.assertEqual(response.status_code, 200)

    def test_letting_detail_uses_expected_template(self):
        """Test that letting detail uses the expected template."""
        response = self.client.get(
            reverse("letting", kwargs={"letting_id": self.letting.id})
        )

        self.assertTemplateUsed(response, "lettings/letting.html")

    def test_letting_detail_contains_expected_context(self):
        """Test that letting detail contains expected context data."""
        response = self.client.get(
            reverse("letting", kwargs={"letting_id": self.letting.id})
        )

        self.assertEqual(response.context["title"], "Beautiful apartment")
        self.assertEqual(response.context["address"], self.address)
