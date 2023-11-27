from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
import pytest


class TestHomeViews:
    def setup_method(self):
        self.client = Client()

    @pytest.mark.django_db
    def test_home(self):
        response = self.client.get(reverse("home:home"))

        """
        The first assert tests if the get request returns 200 (OK) status code
        The second assert making sure that the view returns the home.html template
        """

        assert response.status_code == 200
        assertTemplateUsed(response, "home/home.html")
