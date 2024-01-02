from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
import pytest
import secrets

from lettings.models import Address, Letting


class TestLettingsViews:
    def setup_method(self):
        self.client = Client()
        """Create an Address instance"""
        self.address = Address.objects.create(
            number=secrets.randbelow(200),
            street=secrets.token_hex(20),
            city=secrets.token_hex(20),
            state=secrets.token_hex(2),
            zip_code=secrets.randbelow(4000),
            country_iso_code=secrets.token_hex(3),
        )

    @pytest.mark.django_db
    def test_index(self):
        letting = Letting.objects.create(
            title=secrets.token_hex(30), address=self.address
        )
        path = reverse("lettings:index")
        response = self.client.get(path)
        content = response.content.decode()
        expected_content = f"{letting.title}"

        """
        The first assert tests the content contains the title of the letting
        The second assert tests if the get request returns 200 (OK) status code
        The third assert making sure that the view returns the lettings/index.html template
        """
        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/index.html")

    @pytest.mark.django_db
    def test_index_without_letting(self):
        response = self.client.get(reverse("lettings:index"))
        content = response.content.decode()
        expected_content = "<p>No lettings are available.</p>"

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/index.html")

    @pytest.mark.django_db
    def test_letting(self):
        letting = Letting.objects.create(
            title=secrets.token_hex(30), address=self.address
        )
        response = self.client.get(
            reverse("lettings:letting", kwargs={"letting_id": letting.id})
        )
        content = response.content.decode()
        expected_content = f"<p>{self.address.number} {self.address.street}</p>"

        """
        The first assert tests the content contains the elements from address
        The second assert tests if the get request returns 200 (OK) status code
        The third assert making sure that the view returns the lettings/letting.html template
        """
        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/letting.html")

    @pytest.mark.django_db
    def test_letting_with_unknown_id(self):
        response = self.client.get(
            reverse("lettings:letting", kwargs={"letting_id": 25})
        )

        """
        The first assert tests if the get request returns 404 status code
        """
        assert response.status_code == 404
        assertTemplateUsed(response, "error.html")
