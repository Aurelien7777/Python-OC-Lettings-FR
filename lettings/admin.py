"""Admin configuration for the lettings application."""

from django.contrib import admin
from lettings.models import Address, Letting

admin.site.register(Address)
admin.site.register(Letting)
