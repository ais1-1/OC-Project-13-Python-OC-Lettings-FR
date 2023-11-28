from lettings.models import Address, Letting

import secrets
import pytest


class TestLettingsModels:
    def setup_method(self):
        """Create an Address instance and a Letting instance"""
        self.address = Address.objects.create(
            number=secrets.randbelow(200),
            street=secrets.token_hex(20),
            city=secrets.token_hex(20),
            state=secrets.token_hex(2),
            zip_code=secrets.randbelow(4000),
            country_iso_code=secrets.token_hex(3),
        )
        self.letting = Letting.objects.create(
            title=secrets.token_hex(30), address=self.address
        )

    @pytest.mark.django_db
    def test_address(self):
        """
        Testing if Address's __str__ method is properly implemented
        """

        assert str(self.address) == f"{self.address.number} {self.address.street}"

    @pytest.mark.django_db
    def test_letting(self):
        """
        Testing if Letting's __str__ method is properly implemented
        """

        assert str(self.letting) == self.letting.title
