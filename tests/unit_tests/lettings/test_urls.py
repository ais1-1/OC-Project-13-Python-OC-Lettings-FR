from django.urls import reverse, resolve
from lettings.views import index, letting


class TestLettingsUrls:
    def test_index_url(self):
        """Testing if the 'lettings/' route maps to profiles 'index' view"""

        url = reverse("lettings:index")
        assert resolve(url).view_name == "lettings:index"
        assert resolve(url).func, index

    def test_letting_url(self):
        """Testing if the 'letting' route maps to 'letting' view"""

        url = reverse("lettings:letting", args=[1])
        assert resolve(url).view_name == "lettings:letting"
        assert resolve(url).func, letting
