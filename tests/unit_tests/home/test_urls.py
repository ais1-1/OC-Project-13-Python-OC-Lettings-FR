from django.urls import reverse, resolve
from home.views import home


class TestHomeUrls:
    def test_home_url(self):
        """Testing if the '' route maps to 'home' view"""

        url = reverse("home:home")
        assert resolve(url).view_name == "home:home"
        assert resolve(url).func, home
