from .views import *
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # API Route
    path("api/", include("api.urls")),

    # Index Route
    path("", index, name="index"),

    # Admin Route
    path("admin/", admin.site.urls, name="admin"),

    # Register Routes
    path("sign-up/", sign_up, name="sign_up"),
    path("sign-up/submit/", sign_up_submit, name="sign_up_submit"),

    # Log In Routes
    path("sign-in/", sign_in, name="sign_in"),
    path("sign-in/submit/", sign_in_submit, name="sign_in_submit"),

    # Log Out Routes
    path("sign-out/", sign_out, name="sign_out"),

    # Social Log In Route
    path("oauth/", include("social_django.urls", namespace="social")),

    # Profile Route
    path("profile/", profile, name="profile"),

    # Profile Settings Routes
    path("profile/settings/", profile_edit, name="profile_edit"),
    path("profile/settings/submit/", profile_edit_submit, name="profile_edit_submit"),
    
    # Profile Delete Routes
    path("profile/delete/", profile_delete, name="profile_delete"),
    path("profile/delete/submit/", profile_delete_submit, name="profile_delete_submit"),

    # Tasks routing
    path("tasks/", tasks, name="tasks"),
    path("task/create/", task_create, name="task_create"),
    path("task/<id>/edit/", task_edit, name="task_edit"),
    path("task/<id>/delete/", task_delete, name="task_delete"),

    # Workouts routing
    path("workouts/", workouts, name="workouts"),
    path("workout/create/", workout_create, name="workout_create"),
    path("workout/<id>/", workout, name="workout"),
    path("workout/<id>/edit/", workout_edit, name="workout_edit"),
    path("workout/<id>/delete/", workout_delete, name="workout_delete"),

    path("meals-and-bmis/", meals_and_bmis, name="meals_and_bmis"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
