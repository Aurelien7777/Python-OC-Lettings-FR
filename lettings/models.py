from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Store the address linked to a letting.

    Attributes:
        number: Street number of the address.
        street: Street name.
        city: City name.
        state: Two-letter state code.
        zip_code: Postal code.
        country_iso_code: Three-letter country ISO code.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        """Return a readable address representation.

        Returns:
            str: Street number and street name.
        """
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """Store a letting and its related address.

    Attributes:
        title: Title of the letting.
        address: One-to-one relation with the letting address.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Return the letting title.

        Returns:
            str: Title of the letting.
        """
        return self.title
