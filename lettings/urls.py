"""URL configuration for the lettings application."""

from lettings import views
from django.urls import path

urlpatterns = [
    path("", views.lettings_index, name="lettings_index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]
