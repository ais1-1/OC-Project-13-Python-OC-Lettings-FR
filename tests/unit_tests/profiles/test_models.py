from django.contrib.auth.models import User

from profiles.models import Profile

import secrets
import pytest


class TestProfilesModels:
    def setup_method(self):
        self.user = User.objects.create(
            username=secrets.token_hex(10), password=secrets.token_hex(10)
        )
        self.favorite_city = secrets.token_hex(10)
        self.profile = Profile.objects.create(
            user=self.user, favorite_city=self.favorite_city
        )

    @pytest.mark.django_db
    def test_profile(self):
        """
        Testing if Profile's __str__ method is properly implemented
        """

        assert str(self.profile) == self.user.username
