from django.urls import path

from . import views

""" To use lettings namespace """
app_name = "lettings"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]