from django.test import TestCase
from api.models import *


class TestCustomerModel(TestCase):
    def setUp(self):
        self.username = "Test Username"
        self.first_name = "Test"
        self.last_name = "Username"
        self.email = "test@test.com"
        self.password = "Test Password"
        self.is_superuser = False
        self.is_staff = False
        self.is_active = True
        self.profile_picture = "default_profile_picture.png"
        self.public = True
        self.total_calories = 50.00
        self.total_fat = 23.89
        self.total_protein = 15.96
        self.total_carbs = 67.00

        self.customer = Customer.objects.create_user(
            username=self.username,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            is_superuser=self.is_superuser,
            is_staff=self.is_staff,
            is_active=self.is_active,
            profile_picture=self.profile_picture,
            public=self.public,
            password=self.password,
            total_calories=self.total_calories,
            total_fat=self.total_fat,
            total_protein=self.total_protein,
            total_carbs=self.total_carbs
        )

    def test_customer_username(self):
        self.assertEqual(self.customer.username, str("Test Username"))

    def test_customer_firstname(self):
        self.assertEqual(self.customer.first_name, str("Test"))

    def test_customer_lastname(self):
        self.assertEqual(self.customer.last_name, str("Username"))

    def test_customer_email(self):
        self.assertEqual(self.customer.email, str("test@test.com"))

    def test_customer_is_superuser(self):
        self.assertEqual(self.customer.is_superuser, False)

    def test_customer_is_staff(self):
        self.assertEqual(self.customer.is_staff, False)

    def test_customer_is_active(self):
        self.assertEqual(self.customer.is_active, True)

    def test_customer_profile_picture(self):
        self.assertEqual(self.customer.profile_picture, 'default_profile_picture.png')

    def test_customer_public(self):
        self.assertEqual(self.customer.public, True)

    def test_customer_total_calories(self):
        self.assertEqual(self.customer.total_calories, 50.00)

    def test_customer_total_fat(self):
        self.assertEqual(self.customer.total_fat, 23.89)

    def test_customer_total_protein(self):
        self.assertEqual(self.customer.total_protein, 15.96)

    def test_customer_total_carbs(self):
        self.assertEqual(self.customer.total_carbs, 67.00)


class TestWorkoutModel(TestCase):
    def setUp(self):
        customer = Customer.objects.create(username="Test", password="12345")
        self.customer = customer
        self.title = "Test Workout"
        self.workout_image = "default_workout_image.png"
        self.description = "Test Description"
        self.exercises = "Test Exercises"
        self.public = True

        self.workout = Workout.objects.create(
            customer=self.customer,
            title=self.title,
            workout_image=self.workout_image,
            description=self.description,
            exercises=self.exercises,
            public=self.public
        )

    def test_workout_customer(self):
        self.assertEqual(self.workout.customer, self.customer)

    def test_workout_title(self):
        self.assertEqual(self.workout.title, "Test Workout")

    def test_workout_workout_image(self):
        self.assertEqual(self.workout.workout_image, "default_workout_image.png")

    def test_workout_description(self):
        self.assertEqual(self.workout.description, "Test Description")

    def test_workout_exercises(self):
        self.assertEqual(self.workout.exercises, "Test Exercises")

    def test_workout_public(self):
        self.assertEqual(self.workout.public, True)


class TestBMICalculatorModel(TestCase):
    def setUp(self):
        customer = Customer.objects.create(username="Test", password="12345")
        self.customer = customer
        self.height = 1.00
        self.weight = 2.00
        self.result = (1.00 / (2.00 / 100) ** 2)

        self.bmi = BMICalculator.objects.create(
            customer=self.customer,
            height=self.height,
            weight=self.weight,
            result=self.result
        )

    def test_workout_customer(self):
        self.assertEqual(self.bmi.customer, self.customer)

    def test_workout_height(self):
        self.assertEqual(self.bmi.height, 1.00)

    def test_workout_weight(self):
        self.assertEqual(self.bmi.weight, 2.00)

    def test_workout_result(self):
        self.assertEqual(self.bmi.result, 20000.0)


class TestFoodModel(TestCase):
    def setUp(self):
        customer = Customer.objects.create(username="Test", password="12345")
        self.customer = customer
        self.calories = 13.98
        self.fat = 2.00
        self.protein = 15.86
        self.carbs = 14.76

        self.food = Food.objects.create(
            customer=self.customer,
            calories=self.calories,
            fat=self.fat,
            protein=self.protein,
            carbs=self.carbs
        )

    def test_workout_customer(self):
        self.assertEqual(self.food.customer, self.customer)

    def test_workout_calories(self):
        self.assertEqual(self.food.calories, 13.98)

    def test_workout_fat(self):
        self.assertEqual(self.food.fat, 2.00)

    def test_workout_protein(self):
        self.assertEqual(self.food.protein, 15.86)

    def test_workout_carbs(self):
        self.assertEqual(self.food.carbs, 14.76)
