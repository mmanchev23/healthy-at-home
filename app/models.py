import uuid
from decimal import Decimal
from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class Customer(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_picture = models.ImageField(null=True, blank=True, default='default_profile_picture.png')
    public = models.BooleanField(default=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    total_calories = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), validators=[MinValueValidator(Decimal('0.00'))])
    total_fat = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), validators=[MinValueValidator(Decimal('0.00'))])
    total_protein = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), validators=[MinValueValidator(Decimal('0.00'))])
    total_carbs = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00), validators=[MinValueValidator(Decimal('0.00'))])
    pass

    def __str__(self):
        return self.username


class Workout(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    workout_image = models.ImageField(null=True, blank=True, default='default_workout_image.png')
    video_url = models.CharField(max_length=200, default='https://www.youtube.com/embed/oAPCPjnU1wA')
    description = models.TextField()
    exercises = models.TextField()
    public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.title} - {self.customer}"

    @property
    def imageURL(self):

        try:
            url = self.image.url
        except:
            url = ''

        return url

    def save(self, *args, **kwargs):
        url = self.video_url
        url = url.replace("watch?v=", "embed/")
        self.video_url = url
        super().save(*args,**kwargs)

    @staticmethod
    def convert_video_url(self):
        url = self.video_url
        url = url.replace("watch?v=", "embed/")
        return url


class Task(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.title} - {self.customer}"


class BMICalculator(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    height = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    weight = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    result = models.DecimalField(max_digits=10, decimal_places=2, editable=False, validators=[MinValueValidator(Decimal('0.00'))])
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.customer} - {self.result}"

    def save(self,*args,**kwargs):
        self.result = self.weight / (self.height / 100) ** 2
        super().save(*args,**kwargs)

    @staticmethod
    def calculate_bmi(weight, height):
        return (weight / (height / 100) ** 2)


class Food(models.Model):
    CATEGORIES = (
        ('BR', 'Breakfast'),
        ('LU', 'Lunch'),
        ('DI',' Dinner'),
        ('SN', 'Snack'),
        ('DR', 'Drink'),
        ('CM', 'Cheat Meal'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    calories = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    fat = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    protein = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    carbs = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    category = models.CharField(choices=CATEGORIES,max_length=2)
    date_eaten = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f"{self.name} - {self.customer}"
