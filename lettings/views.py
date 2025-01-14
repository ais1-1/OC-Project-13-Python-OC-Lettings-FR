import logging
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_safe

from .models import Letting


@require_safe
def index(request):
    """Index of lettings, which lists lettings in the database."""
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


@require_safe
def letting(request, letting_id):
    """Detailed view of a letting.
    Parameters:
    letting_id (int): id of a letting"""
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        return render(request, "lettings/letting.html", context)
    except Exception as e:
        logging.error(str(e))
        return render(request, "error.html", {"message": str(e)}, status=404)
