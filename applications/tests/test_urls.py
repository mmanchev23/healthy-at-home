from applications.views import *
from django.test import SimpleTestCase
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse("index")
        self.assertEqual(resolve(url).func, index)

    def test_register_url(self):
        url = reverse("register")
        self.assertEqual(resolve(url).func, sign_up)

    def test_login_url(self):
        url = reverse("login")
        self.assertEqual(resolve(url).func, sign_in)

    def test_logout_url(self):
        url = reverse("logout")
        self.assertEqual(resolve(url).func, sign_out)
