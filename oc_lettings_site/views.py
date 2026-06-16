"""Views for the main site application."""

from django.shortcuts import render


def index(request):
    """Display the home page.

    Args:
        request: HTTP request sent by the user.

    Returns:
        HttpResponse: Rendered home page.
    """
    return render(request, "index.html")
