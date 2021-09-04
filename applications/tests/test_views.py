from django.urls import reverse
from django.test import TestCase, Client


class TestViews(TestCase):
    def SetUp(self):
        self.client = Client()

    def test_index_POST(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "apps/index.html")

    def test_register_POST(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "apps/register.html")

    def test_login_POST(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "apps/login.html")

    def test_logout_POST(self):
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, "apps/logout.html")
