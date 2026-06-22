"""Views for the main site application."""

import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """Display the home page.

    Args:
        request: HTTP request sent by the user.

    Returns:
        HttpResponse: Rendered home page.
    """
    logger.info("Home page accessed.")
    return render(request, "oc_lettings_site/index.html")


def page_not_found(request, exception):
    """Display custom 404 error page."""
    logger.warning("404 page displayed.", extra={"path": request.path})
    return render(request, "oc_lettings_site/404.html", status=404)


def server_error(request):
    """Display custom 500 error page."""
    logger.error("500 error page displayed.", extra={"path": request.path})
    return render(request, "oc_lettings_site/500.html", status=500)
