"""URL configuration for the lettings application."""

from lettings import views
from django.urls import path

app_name = "lettings"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]
