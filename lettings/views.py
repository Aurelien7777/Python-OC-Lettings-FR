"""Views for the lettings application."""

import logging

from django.shortcuts import render, get_object_or_404
from lettings.models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """Display the list of all lettings.

    Args:
        request: HTTP request sent by the user.

    Returns:
        HttpResponse: Rendered lettings index page.
    """
    lettings_list = Letting.objects.all()
    logger.info("Lettings index page accessed.")
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """Display the detail page for one letting.

    Args:
        request: HTTP request sent by the user.
        letting_id: Identifier of the letting to display.

    Returns:
        HttpResponse: Rendered letting detail page.
    """
    logger.info("Letting detail page requested.", extra={"letting_id": letting_id})
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
