from decimal import Decimal
from django.db.models import Sum
from applications.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    total_calories = serializers.SerializerMethodField()
    total_fat = serializers.SerializerMethodField()
    total_proteins = serializers.SerializerMethodField()
    total_carbs = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "profile_picture",
            "city",
            "state",
            "country",
            "job",
            "phone_number",
            "facebook",
            "instagram",
            "twitter",
            "total_calories",
            "total_fat",
            "total_proteins",
            "total_carbs"
        )

    def get_total_calories(self, obj):
        totalcalories = Food.objects.filter(user=self.context['request'].user).aggregate(total_calories=Sum('calories'))
        return totalcalories["total_calories"] or Decimal('0.00')

    def get_total_fat(self, obj):
        totalfat = Food.objects.filter(user=self.context['request'].user).aggregate(total_fat=Sum('fat'))
        return totalfat["total_fat"] or Decimal('0.00')

    def get_total_proteins(self, obj):
        totalprotein = Food.objects.filter(user=self.context['request'].user).aggregate(total_protein=Sum('protein'))
        return totalprotein["total_protein"] or Decimal('0.00')

    def get_total_carbs(self, obj):
        totalcarbs = Food.objects.filter(user=self.context['request'].user).aggregate(total_carbs=Sum('carbs'))
        return totalcarbs["total_carbs"] or Decimal('0.00')


class ProfileLikeSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = ProfileLike
        fields = ("id", "user", "profile", "created_at", "updated_at")

    
class ProfileFollowerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = ProfileFollower
        fields = ("id", "user", "profile", "created_at", "updated_at")


class WorkoutSerializer(serializers.ModelSerializer):
    workout_image = serializers.ImageField(default="default_workout_image.png")
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Workout
        fields = ("id", "user", "title", "workout_image", "video_url", "description", "exercises", "public", "created_at", "updated_at")


class ToDoListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Task
        fields = ("id", "user", "title", "description", "completed", "created_at", "updated_at")


class BMICalculatorSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    
    class Meta:
        model = BMICalculator
        fields = ("id", "user", "height", "weight", "result", "created_at", "updated_at")


class FoodSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    
    class Meta:
        model = Food
        fields = ("id", "user", "name", "calories", "fat", "protein", "carbs", "created_at", "updated_at")
