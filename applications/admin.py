from .models import *
from django.contrib import admin


admin.site.site_header = "Healthy at Home - Admin Panel"

class ProfileLikeAdmin(admin.ModelAdmin):
    list_display = ("user", "profile")

class ProfileFollowerAdmin(admin.ModelAdmin):
    list_display = ("user", "profile")

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("title", "user")

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "user")

class BMICalculatorAdmin(admin.ModelAdmin):
    list_display = ("result", "user")

class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "user")

admin.site.register(User)
admin.site.register(ProfileLike, ProfileLikeAdmin)
admin.site.register(ProfileFollower, ProfileFollowerAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(BMICalculator, BMICalculatorAdmin)
admin.site.register(Food, FoodAdmin)