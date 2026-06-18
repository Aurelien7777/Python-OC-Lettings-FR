"""Views for the main site application."""

from django.shortcuts import render


def index(request):
    """Display the home page.

    Args:
        request: HTTP request sent by the user.

    Returns:
        HttpResponse: Rendered home page.
    """
    return render(request, "oc_lettings_site/index.html")


def page_not_found(request, exception):
    """Display custom 404 error page."""
    return render(request, "oc_lettings_site/404.html", status=404)


def server_error(request):
    """Display custom 500 error page."""
    return render(request, "oc_lettings_site/500.html", status=500)
