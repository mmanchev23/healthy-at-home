from rest_framework.test import APITestCase
from decimal import Decimal
from api.models import *
from api.serializers import *


class TestCustomerSerializer(APITestCase):
    def setUp(self):

        self.customer_attributes = {
            'username': str("Test Username"),
            'first_name': str("Test"),
            'last_name': str("Username"),
            'email': str("test@test.com"),
            'password': str("Test Password"),
            'is_superuser': False,
            'is_staff': False,
            'is_active': True,
            'profile_picture': str('default_profile_picture.png'),
            'public': True,
            'total_calories': Decimal(50.00),
            'total_fat': Decimal(23.89),
            'total_protein': Decimal(15.96),
            'total_carbs': Decimal(67.00),
        }

        self.serializer_data = {
            'username': "Test Username",
            'first_name': "Test",
            'last_name': "Username",
            'email': "test@test.com",
            'password': "Test Password",
            'is_superuser': False,
            'is_staff': False,
            'is_active': True,
            'profile_picture': 'default_profile_picture.png',
            'public': True,
            'total_calories': 50.00,
            'total_fat': 23.89,
            'total_protein': 15.96,
            'total_carbs': 67.00,
        }

        self.customer = Customer.objects.create(**self.customer_attributes)
        self.serialized = CustomerSerializer(instance=self.customer)


    # Check Fields
    def test_customer_expected_fields(self):
        data = self.serializer_data

        self.assertEqual(set(data.keys()), set([
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password',
            'is_superuser',
            'is_staff',
            'is_active',
            'profile_picture',
            'public',
            'total_calories',
            'total_fat',
            'total_protein',
            'total_carbs',
        ]))


    # Check Content
    def test_username_field_content(self):
        data = self.serializer_data

        self.assertEqual(data['username'], self.customer_attributes['username'])

    def test_first_name_field_content(self):
        data = self.serializer_data
        
        self.assertEqual(data['first_name'], self.customer_attributes['first_name'])

    def test_last_name_field_content(self):
        data = self.serializer_data
        
        self.assertEqual(data['last_name'], self.customer_attributes['last_name'])

    def test_email_field_content(self):
        data = self.serializer_data
        
        self.assertEqual(data['email'], self.customer_attributes['email'])

    def test_password_field_content(self):
        data = self.serializer_data
        
        self.assertEqual(data['password'], self.customer_attributes['password'])

    def test_is_superuser_field_content(self):
        data = self.serializer_data
        
        self.assertEqual(data['is_superuser'], self.customer_attributes['is_superuser'])

    def test_is_staff_field_content(self):
        data = self.serializer_data
        
        self.assertEqual(data['is_staff'], self.customer_attributes['is_staff'])

    def test_is_active_field_content(self):
        data = self.serializer_data
        
        self.assertEqual(data['is_active'], self.customer_attributes['is_active'])

    def test_profile_picture_field_content(self):
        data = self.serializer_data
        
        self.assertEqual(data['profile_picture'], self.customer_attributes['profile_picture'])

    def test_public_field_content(self):
        data = self.serializer_data
        
        self.assertEqual(data['public'], self.customer_attributes['public'])

    def test_total_calories_field_content(self):
        data = self.serializer_data
        
        self.assertEqual(data['total_calories'], self.customer_attributes['total_calories'])

    def test_total_fat_field_content(self):
        data = self.serializer_data
        
        self.assertEqual(data['total_fat'], self.customer_attributes['total_fat'])

    def test_total_protein_content(self):
        data = self.serializer_data
        
        self.assertEqual(data['total_protein'], self.customer_attributes['total_protein'])

    def test_total_carbs_field_content(self):
        data = self.serializer_data
        
        self.assertEqual(data['total_carbs'], self.customer_attributes['total_carbs'])


    # Check Type
    def test_username_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['username'], str(self.customer_attributes['username']))

    def test_first_name_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['first_name'], str(self.customer_attributes['first_name']))

    def test_last_name_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['last_name'], str(self.customer_attributes['last_name']))

    def test_email_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['email'], str(self.customer_attributes['email']))

    def test_password_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['password'], str(self.customer_attributes['password']))

    def test_is_staff_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['is_staff'], bool(self.customer_attributes['is_staff']))

    def test_is_active_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['is_active'], bool(self.customer_attributes['is_active']))

    def test_profile_picture_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['profile_picture'], str(self.customer_attributes['profile_picture']))

    def test_public_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['public'], bool(self.customer_attributes['public']))

    def test_total_calories_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['total_calories'], Decimal(self.customer_attributes['total_calories']))

    def test_total_fat_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['total_fat'], Decimal(self.customer_attributes['total_fat']))

    def test_total_protein_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['total_protein'], Decimal(self.customer_attributes['total_protein']))

    def test_total_carbs_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['total_carbs'], Decimal(self.customer_attributes['total_carbs']))


class TestWorkoutSerializer(APITestCase):
    def setUp(self):

        self.customer = Customer.objects.create_user(
            username='Test Username',
            password='12345'
        )

        self.workout_attributes = {
            'customer': self.customer,
            'title': str("Test Workout"),
            'workout_image': str("default_workout_image.png"),
            'description': str("Test Description"),
            'exercises': str("Test Exercises"),
            'public': True,
        }

        self.serializer_data = {
            'customer': self.customer,
            'title': "Test Workout",
            'workout_image': "default_workout_image.png",
            'description': "Test Description",
            'exercises': "Test Exercises",
            'public': True,
        }

        self.workout = Workout.objects.create(**self.workout_attributes)
        self.serialized = WorkoutSerializer(instance=self.workout)

    
    # Check Fields
    def test_customer_expected_fields(self):
        data = self.serializer_data

        self.assertEqual(set(data.keys()), set([
            'customer', 
            'title', 
            'workout_image', 
            'description', 
            'exercises',
            'public',
        ]))


    # Check Content
    # Not testing the foreign key field, e.g. customer/username field because it's slug and readonly field
    def test_title_field_content(self):
        data = self.serializer_data

        self.assertEqual(data['title'], self.workout_attributes['title'])

    def test_workout_image_field_content(self):
        data = self.serializer_data

        self.assertEqual(data['workout_image'], self.workout_attributes['workout_image'])

    def test_description_field_content(self):
        data = self.serializer_data

        self.assertEqual(data['description'], self.workout_attributes['description'])

    def test_exercises_field_content(self):
        data = self.serializer_data

        self.assertEqual(data['exercises'], self.workout_attributes['exercises'])

    def test_public_field_content(self):
        data = self.serializer_data

        self.assertEqual(data['public'], self.workout_attributes['public'])


    # Check Type
    # Not testing the foreign key field, e.g. customer/username field because it's slug and readonly field
    def test_title_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['title'], str(self.workout_attributes['title']))

    def test_workout_image_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['workout_image'], str(self.workout_attributes['workout_image']))

    def test_description_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['description'], str(self.workout_attributes['description']))

    def test_exercises_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['exercises'], str(self.workout_attributes['exercises']))
    
    def test_public_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['public'], bool(self.workout_attributes['public']))


class TestToDoListSerializer(APITestCase):
    def setUp(self):

        self.customer = Customer.objects.create_user(
            username='Test Username',
            password='12345'
        )

        self.todo_attributes = {
            'customer': self.customer,
            'title': str("Test To Do List"),
            'description': str("Test Description"),
            'completed': False,
        }

        self.serializer_data = {
            'customer': self.customer,
            'title': "Test To Do List",
            'description': "Test Description",
            'completed': False,
        }

        self.todo = ToDoList.objects.create(**self.todo_attributes)
        self.serialized = ToDoListSerializer(instance=self.todo)

    
    # Check Fields
    def test_customer_expected_fields(self):
        data = self.serializer_data

        self.assertEqual(set(data.keys()), set([
            'customer', 
            'title', 
            'description',
            'completed',
        ]))

    # Check Content
    # Not testing the foreign key field, e.g. customer/username field because it's slug and readonly field
    def test_title_field_content(self):
        data = self.serializer_data

        self.assertEqual(data['title'], self.todo_attributes['title'])

    def test_description_field_content(self):
        data = self.serializer_data

        self.assertEqual(data['description'], self.todo_attributes['description'])

    def test_completed_field_content(self):
        data = self.serializer_data

        self.assertEqual(data['completed'], self.todo_attributes['completed'])


    # Check Type
    # Not testing the foreign key field, e.g. customer/username field because it's slug and readonly field
    def test_title_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['title'], str(self.todo_attributes['title']))

    def test_description_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['description'], str(self.todo_attributes['description']))

    def test_completed_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['completed'], bool(self.todo_attributes['completed']))


class TestBMICalculatorSerializer(APITestCase):
    def setUp(self):

        self.customer = Customer.objects.create_user(
            username='Test Username',
            password='12345'
        )

        self.bmi_attributes = {
            'customer': self.customer,
            'height': Decimal(186.5),
            'weight': Decimal(84.4),
            'result': Decimal(24.6),
        }

        self.serializer_data = {
            'customer': self.customer,
            'height': 186.5,
            'weight': 84.4,
            'result': 24.6,
        }

        self.bmi = BMICalculator.objects.create(**self.bmi_attributes)
        self.serialized = BMICalculatorSerializer(instance=self.bmi)


    # Check Fields
    def test_customer_expected_fields(self):
        data = self.serializer_data

        self.assertEqual(set(data.keys()), set([
            'customer', 
            'height', 
            'weight',
            'result',
        ]))


    # Check Content
    # Not testing the foreign key field, e.g. customer/username field because it's slug and readonly field
    def test_height_field_content(self):
        data = self.serializer_data

        self.assertEqual(data['height'], self.bmi_attributes['height'])

    def test_weight_field_content(self):
        data = self.serializer_data

        self.assertEqual(data['weight'], self.bmi_attributes['weight'])

    def test_result_field_content(self):
        data = self.serializer_data

        self.assertEqual(data['result'], self.bmi_attributes['result'])


    # Check Type
    # Not testing the foreign key field, e.g. customer/username field because it's slug and readonly field
    def test_height_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['height'], Decimal(self.bmi_attributes['height']))

    def test_weight_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['weight'], Decimal(self.bmi_attributes['weight']))

    def test_result_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['result'], Decimal(self.bmi_attributes['result']))


class TestFoodSerializer(APITestCase):
    def setUp(self):

        self.customer = Customer.objects.create_user(
            username='Test Username',
            password='12345'
        )

        self.food_attributes = {
            'customer': self.customer,
            'name': str("Test Food"),
            'calories': Decimal(84.4),
            'fat': Decimal(24.6),
            'protein': Decimal(35.4),
            'carbs': Decimal(85.6),
        }

        self.serializer_data = {
            'customer': self.customer,
            'name': "Test Food",
            'calories': 84.4,
            'fat': 24.6,
            'protein': 35.4,
            'carbs': 85.6,
        }

        self.food = Food.objects.create(**self.food_attributes)
        self.serialized = FoodSerializer(instance=self.food)


    # Check Fields
    def test_food_expected_fields(self):
        data = self.serializer_data

        self.assertEqual(set(data.keys()), set([
            'customer',
            'name',
            'calories',
            'fat',
            'protein',
            'carbs',
        ]))

    
    # Check Content
    # Not testing the foreign key field, e.g. customer/username field because it's slug and readonly field
    def test_name_field_content(self):
        data = self.serializer_data

        self.assertEqual(data['name'], self.food_attributes['name'])

    def test_calories_field_content(self):
        data = self.serializer_data

        self.assertEqual(data['calories'], self.food_attributes['calories'])

    def test_fat_field_content(self):
        data = self.serializer_data

        self.assertEqual(data['fat'], self.food_attributes['fat'])

    def test_protein_field_content(self):
        data = self.serializer_data

        self.assertEqual(data['protein'], self.food_attributes['protein'])

    def test_carbs_field_content(self):
        data = self.serializer_data

        self.assertEqual(data['carbs'], self.food_attributes['carbs'])


    # Check Type
    # Not testing the foreign key field, e.g. customer/username field because it's slug and readonly field
    def test_name_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['name'], str(self.food_attributes['name']))

    def test_calories_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['calories'], Decimal(self.food_attributes['calories']))

    def test_fat_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['fat'], Decimal(self.food_attributes['fat']))

    def test_protein_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['protein'], Decimal(self.food_attributes['protein']))

    def test_carbs_field_type(self):
        data = self.serializer_data

        self.assertEqual(data['carbs'], Decimal(self.food_attributes['carbs']))
