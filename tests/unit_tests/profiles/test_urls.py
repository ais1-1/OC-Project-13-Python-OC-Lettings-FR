from django.urls import reverse, resolve
from profiles.views import index, profile


class TestProfilesUrls:
    def test_index_url(self):
        """Testing if the 'profiles/' route maps to profiles 'index' view"""

        url = reverse("profiles:index")
        assert resolve(url).view_name == "profiles:index"
        assert resolve(url).func, index

    def test_profile_url(self):
        """Testing if the 'profile' route maps to 'profile' view"""

        url = reverse("profiles:profile", args=["toto"])
        assert resolve(url).view_name == "profiles:profile"
        assert resolve(url).func, profile
