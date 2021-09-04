from django.test import TestCase
from applications.models import *


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
