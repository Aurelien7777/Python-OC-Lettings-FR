"""Models for the profiles application."""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    """Store additional information about a Django user.

    Attributes:
        user: One-to-one relation with the Django authentication user.
        favorite_city: Optional favorite city of the user.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Return the username linked to the profile.

        Returns:
            str: Username of the related user.
        """

        return self.user.username
