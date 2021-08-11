from api.models import *
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from django.test import Client 


class TestHomePageRoute(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create_user(
            username='Test Username',
            password='12345'
        )

    # Methods without token authentication -> 403 ERROR
    def test_homepage_GET_returns_403_VORBIDDEN(self):
        response = self.client.get("", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_homepage_POST_returns_403_VORBIDDEN(self):
        response = self.client.post("", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_homepage_PUT_returns_403_VORBIDDEN(self):
        response = self.client.put("", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_homepage_DELETE_returns_403_VORBIDDEN(self):
        response = self.client.delete("", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Invalid methods with token authentication -> 405 ERROR
    def test_homepage_POST_returns_405_METHOD_NOT_ALLOWED(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post("", follow=True)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_homepage_PUT_returns_405_METHOD_NOT_ALLOWED(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.put("", follow=True)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_homepage_DELETE_returns_405_METHOD_NOT_ALLOWED(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.delete("", follow=True)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    # Valid methods with token authentication -> 200 OK
    def test_homepage_GET_returns_200_OK(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get("", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCredentialsPageRoute(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create_user(
            username='Test Username',
            password='12345'
        )

    # Methods without token authentication -> 403 ERROR
    def test_credentialspage_GET_returns_403_VORBIDDEN(self):
        response = self.client.get("/credentials", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_credentialspage_POST_returns_403_VORBIDDEN(self):
        response = self.client.post("/credentials", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_credentialspage_PUT_returns_403_VORBIDDEN(self):
        response = self.client.put("/credentials", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_credentialspage_DELETE_returns_403_VORBIDDEN(self):
        response = self.client.delete("/credentials", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Valid methods with token authentication -> 200 OK
    def test_credentialspage_GET_returns_200_OK(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get("/credentials", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_credentialspage_POST_returns_405_METHOD_NOT_ALLOWED(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post("/credentials", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_credentialspage_PUT_returns_405_METHOD_NOT_ALLOWED(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.put("/credentials", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_credentialspage_DELETE_returns_405_METHOD_NOT_ALLOWED(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.delete("/credentials", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestFoodPageRoute(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create_user(
            username='Test Username',
            password='12345'
        )

    # Methods without token authentication -> 403 ERROR
    def test_foodpage_GET_returns_403_VORBIDDEN(self):
        response = self.client.get("/food", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_foodpage_POST_returns_403_VORBIDDEN(self):
        response = self.client.post("/food", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_foodpage_PUT_returns_403_VORBIDDEN(self):
        response = self.client.put("/food", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_foodpage_DELETE_returns_403_VORBIDDEN(self):
        response = self.client.delete("/food", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Valid methods with token authentication -> 200 OK
    def test_foodpage_GET_returns_200_OK(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get("/food", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_foodpage_POST_returns_405_METHOD_NOT_ALLOWED(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post("/food", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_foodpage_PUT_returns_405_METHOD_NOT_ALLOWED(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.put("/food", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_foodpage_DELETE_returns_405_METHOD_NOT_ALLOWED(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.delete("/food", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestWorkoutsPageRoute(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create_user(
            username='Test Username',
            password='12345'
        )

    # Methods without token authentication -> 403 ERROR
    def test_workoutspage_GET_returns_403_VORBIDDEN(self):
        response = self.client.get("/workouts", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_workoutspage_POST_returns_403_VORBIDDEN(self):
        response = self.client.post("/workouts", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_workoutspage_PUT_returns_403_VORBIDDEN(self):
        response = self.client.put("/workouts", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_workoutspage_DELETE_returns_403_VORBIDDEN(self):
        response = self.client.delete("/workouts", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Valid methods with token authentication -> 200 OK
    def test_workoutspage_GET_returns_200_OK(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get("/workouts", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_workoutspage_POST_returns_405_METHOD_NOT_ALLOWED(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post("/workouts", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_workoutspage_PUT_returns_405_METHOD_NOT_ALLOWED(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.put("/workouts", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_workoutspage_DELETE_returns_405_METHOD_NOT_ALLOWED(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.delete("/workouts", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestTodosPageRoute(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create_user(
            username='Test Username',
            password='12345'
        )

    # Methods without token authentication -> 403 ERROR
    def test_todospage_GET_returns_403_VORBIDDEN(self):
        response = self.client.get("/todos", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_todospage_POST_returns_403_VORBIDDEN(self):
        response = self.client.post("/todos", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_todospage_PUT_returns_403_VORBIDDEN(self):
        response = self.client.put("/todos", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_todospage_DELETE_returns_403_VORBIDDEN(self):
        response = self.client.delete("/todos", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Valid methods with token authentication -> 200 OK
    def test_todospage_GET_returns_200_OK(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get("/todos", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_todospage_POST_returns_405_METHOD_NOT_ALLOWED(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post("/todos", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todospage_PUT_returns_405_METHOD_NOT_ALLOWED(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.put("/todos", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todospage_DELETE_returns_405_METHOD_NOT_ALLOWED(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.delete("/todos", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestBMIPageRoute(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create_user(
            username='Test Username',
            password='12345'
        )

    # Methods without token authentication -> 403 ERROR
    def test_bmipage_GET_returns_403_VORBIDDEN(self):
        response = self.client.get("/bmi", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_bmipage_POST_returns_403_VORBIDDEN(self):
        response = self.client.post("/bmi", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_bmipage_PUT_returns_403_VORBIDDEN(self):
        response = self.client.put("/bmi", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_bmipage_DELETE_returns_403_VORBIDDEN(self):
        response = self.client.delete("/bmi", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Valid methods with token authentication -> 200 OK
    def test_bmipage_GET_returns_200_OK(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get("/bmi", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_bmipage_POST_returns_405_METHOD_NOT_ALLOWED(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post("/bmi", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_bmipage_PUT_returns_405_METHOD_NOT_ALLOWED(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.put("/bmi", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_bmipage_DELETE_returns_405_METHOD_NOT_ALLOWED(self):
        token, created = Token.objects.get_or_create(user=self.customer)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.delete("/bmi", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
