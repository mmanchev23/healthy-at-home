from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.test import TestCase, Client
from apps.models import *
from apps.views import index_view, register_view, login_view, logout_view


class TestUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse("index")
        self.assertEqual(resolve(url).func, index_view)

    def test_register_url(self):
        url = reverse("register")
        self.assertEqual(resolve(url).func, register_view)

    def test_login_url(self):
        url = reverse("login")
        self.assertEqual(resolve(url).func, login_view)

    def test_logout_url(self):
        url = reverse("logout")
        self.assertEqual(resolve(url).func, logout_view)


class TestModels(TestCase):
    def test_model_user_username(self):
        user = User.objects.create_user("User 1")
        self.assertEqual(str(user), "User 1")

    def test_model_user_email(self):
        user = User.objects.create_user("user1@example.com")
        self.assertEqual(str(user), "user1@example.com")

    def test_model_user_password(self):
        user = User.objects.create_user("12345")
        self.assertEqual(str(user), "12345")

    def test_model_workout_name(self):
        workout = Workout(name="Workout 1")
        self.assertEqual(workout.name, "Workout 1")

    def test_model_workout_image_url(self):
        workout = Workout(image="someurl/url")
        self.assertEqual(workout.image, "someurl/url")

    def test_model_workout_video_url(self):
        workout = Workout(video="someurl/url")
        self.assertEqual(workout.video, "someurl/url")

    def test_model_workout_content(self):
        workout = Workout(content="some content")
        self.assertEqual(workout.content, "some content")

    def test_model_workout_exercises(self):
        workout = Workout(exercises="some exercises")
        self.assertEqual(workout.exercises, "some exercises")


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
        