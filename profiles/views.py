import logging
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_safe


from .models import Profile


@require_safe
def index(request):
    """Index of profiles, which lists the profiles in the database."""
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


@require_safe
def profile(request, username):
    """Detailed view of a profile.
    Parameters:
    username (str): username of a profile"""
    try:
        profile = get_object_or_404(Profile, user__username=username)
        context = {"profile": profile}
        return render(request, "profiles/profile.html", context)
    except Exception as e:
        logging.error(str(e))
        return render(request, "error.html", {"message": str(e)}, status=404)
