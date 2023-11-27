from django.shortcuts import render


def home(request):
    """Renders home page"""
    return render(request, "home/home.html")
