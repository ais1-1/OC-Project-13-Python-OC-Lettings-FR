import logging
from django.shortcuts import render


def home(request):
    """Renders home page"""
    return render(request, "home/home.html")


def trigger_error(request):
    try:
        division_by_zero = 1 / 0
        return division_by_zero
    except ZeroDivisionError as e:
        logging.error(str(e))
        return render(request, "error.html", {"message": str(e)}, status=500)
