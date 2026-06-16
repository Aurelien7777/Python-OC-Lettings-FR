"""Admin configuration for the profiles application."""

from django.contrib import admin
from profiles.models import Profile

admin.site.register(Profile)
