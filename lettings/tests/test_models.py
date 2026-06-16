"""Tests for lettings models."""

from django.test import TestCase

from lettings.models import Address, Letting


class AddressModelTest(TestCase):
    """Test Address model."""

    def test_address_str_returns_number_and_street(self):
        """Test that Address string representation is correct."""
        address = Address.objects.create(
            number=10,
            street="Main Street",
            city="Paris",
            state="FR",
            zip_code=75000,
            country_iso_code="FRA",
        )

        self.assertEqual(str(address), "10 Main Street")


class LettingModelTest(TestCase):
    """Test Letting model."""

    def test_letting_str_returns_title(self):
        """Test that Letting string representation is correct."""
        address = Address.objects.create(
            number=10,
            street="Main Street",
            city="Paris",
            state="FR",
            zip_code=75000,
            country_iso_code="FRA",
        )
        letting = Letting.objects.create(
            title="Beautiful apartment",
            address=address,
        )

        self.assertEqual(str(letting), "Beautiful apartment")
