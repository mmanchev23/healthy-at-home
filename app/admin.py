from .models import *
from django.contrib import admin


admin.site.site_header = "Healthy at Home - Admin Panel"


class LikeAdmin(admin.ModelAdmin):
    list_display = ("customer", "profile")


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("title", "customer")


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "customer")


class BMICalculatorAdmin(admin.ModelAdmin):
    list_display = ("result", "customer")


class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "customer")


admin.site.register(Customer)
admin.site.register(Like, LikeAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(BMICalculator, BMICalculatorAdmin)
admin.site.register(Food, FoodAdmin)