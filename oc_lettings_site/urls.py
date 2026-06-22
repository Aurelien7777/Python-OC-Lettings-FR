"""URL configuration for the main OC Lettings site."""

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("profiles/", include("profiles.urls")),
    path("lettings/", include("lettings.urls")),
]

handler404 = "oc_lettings_site.views.page_not_found"
handler500 = "oc_lettings_site.views.server_error"
