"""Views for the profiles application."""

import logging

from django.shortcuts import render, get_object_or_404
from profiles.models import Profile

logger = logging.getLogger(__name__)


def profiles_index(request):
    """Display the list of all user profiles.

    Args:
        request: HTTP request sent by the user.

    Returns:
        HttpResponse: Rendered profiles index page.
    """
    profiles_list = Profile.objects.all()
    logger.info("Profiles index page accessed.")
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/profiles_index.html", context)


def profile(request, username):
    """Display the detail page for one user profile.

    Args:
        request: HTTP request sent by the user.
        username: Username linked to the profile to display.

    Returns:
        HttpResponse: Rendered profile detail page.
    """
    logger.info("Profile detail page requested.", extra={"username": username})
    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
