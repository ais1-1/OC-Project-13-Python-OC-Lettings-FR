from django.shortcuts import render, get_object_or_404

from .models import Profile


def index(request):
    """Index of profiles, which lists the profiles in the database."""
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """Detailed view of a profile.
    Parameters:
    username (str): username of a profile"""
    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
