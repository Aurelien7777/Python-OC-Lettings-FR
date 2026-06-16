"""Views for the lettings application."""

from django.shortcuts import render
from lettings.models import Letting


def lettings_index(request):
    """Display the list of all lettings.

    Args:
        request: HTTP request sent by the user.

    Returns:
        HttpResponse: Rendered lettings index page.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/lettings_index.html", context)


def letting(request, letting_id):
    """Display the detail page for one letting.

    Args:
        request: HTTP request sent by the user.
        letting_id: Identifier of the letting to display.

    Returns:
        HttpResponse: Rendered letting detail page.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
