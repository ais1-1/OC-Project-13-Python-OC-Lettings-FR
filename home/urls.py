from django.urls import path

from . import views

""" To use lettings namespace """
app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
]
