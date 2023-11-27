from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
import pytest
from django.contrib.auth.models import User
import secrets

from profiles.models import Profile


class TestProfilesViews:
    def setup_method(self):
        self.client = Client()
        """Create a User and a connected Profile"""

        self.user = User.objects.create(
            username=secrets.token_hex(10), email="toto@example.com"
        )
        self.profile = Profile.objects.create(
            user=self.user, favorite_city=secrets.token_hex(20)
        )

    @pytest.mark.django_db
    def test_index(self):
        response = self.client.get(reverse("profiles:index"))
        content = response.content.decode()
        expected_content = f"{self.user.username}"

        """
        The first assert tests the content contains the username
        The seconed tests if the get request returns 200 (OK) status code
        The third assert making sure that the view returns the profiles/index.html template
        """
        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/index.html")

    @pytest.mark.django_db
    def test_profile(self):
        response = self.client.get(
            reverse("profiles:profile", kwargs={"username": self.user.username})
        )
        content = response.content.decode()
        expected_content = f"{self.user.email}"

        """
        The first assert tests if the content contains user email
        The second tests if the get request returns 200 (OK) status code
        The third assert making sure that the view returns the profiles/profile.html template
        """
        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/profile.html")
