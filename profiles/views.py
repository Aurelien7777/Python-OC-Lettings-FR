"""Views for the profiles application."""

from django.shortcuts import render
from profiles.models import Profile


def profiles_index(request):
    """Display the list of all user profiles.

    Args:
        request: HTTP request sent by the user.

    Returns:
        HttpResponse: Rendered profiles index page.
    """
    profiles_list = Profile.objects.all()
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
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
