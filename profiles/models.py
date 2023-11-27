""" Define profiles models """
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile model
    Attributes:
    user (User): User model instance
    favorite_city (string): favorite city of the user"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        """The name of the database table to use for the model"""

        db_table = "oc_lettings_site_profile"

    def __str__(self):
        """Used in print"""
        return self.user.username
