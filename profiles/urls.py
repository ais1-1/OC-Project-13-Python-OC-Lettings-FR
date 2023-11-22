from django.urls import path

from . import views

""" To use profiles namespace """
app_name = "profiles"

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]