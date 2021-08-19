from . import views
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Authentication routing
    path("api/", include("api.urls")),
    path("", views.index_view, name="index"),
    path("admin/", admin.site.urls, name="admin"),
    path("register/", views.register_view, name="register"),
    path("register-submit/", views.register_submit, name="register-submit"),
    path("login/", views.login_view, name="login"),
    path("login-submit/", views.login_submit, name="login-submit"),
    path("logout/", views.logout_view, name="logout"),
    path("logout-submit/", views.logout_submit, name="logout-submit"),

    path('oauth/', include('social_django.urls', namespace='social')),

    # Profile routing
    path("<username>/", views.profile_view, name="profile"),
    path("<username>/settings/", views.profile_settings_view, name="settings"),
    path("<username>/edit-profile-submit/", views.profile_edit_submit, name="edit-profile-submit"),
    path("<username>/delete/", views.profile_delete_view, name="delete-profile"),
    path("<username>/delete-profile-submit/", views.profile_delete_submit, name="delete-profile-submit"),

    # Workouts routing
    path("workouts/", views.workouts, name="workouts"),
    path("workout/<id>/", views.workout, name="workout"),
    path("workout/create/", views.workout_create, name="create_workout"),
    path("workout/create-submit/", views.workout_create_submit, name="create-workout-submit"),
    path("workout/<id>/edit/", views.workout_edit, name="edit_workout"),
    path("workout/<id>/edit-submit/", views.workout_edit_submit, name="edit-workout-submit"),
    path("workout/<id>/delete/", views.workout_delete, name="delete_workout"),
    path("workout/<id>/delete-submit/", views.workout_delete_submit, name="delete-workout-submit"),

    # Tasks routing
    path("tasks/", views.tasks, name="tasks"),
    path("task/<id>/", views.task, name="task"),
    path("task/create/", views.task_create, name="create_task"),
    path("task/create-submit/", views.task_create_submit, name="create-task-submit"),
    path("task/<id>/edit/", views.task_edit, name="edit_task"),
    path("task/<id>/edit-submit/", views.task_edit_submit, name="edit-task-submit"),
    path("task/<id>/delete/", views.task_delete, name="delete_task"),
    path("task/<id>/delete-submit/", views.task_delete_submit, name="delete-task-submit"),

    # BMIs Routing
    path("bmis/", views.bmis, name="bmis"),
    path("bmi/<id>/", views.bmi, name="bmi"),
    path("bmi/create/", views.bmi_create, name="create_bmi"),
    path("bmi/create-submit/", views.bmi_create_submit, name="create-bmi-submit"),
    path("bmi/<id>/edit/", views.bmi_edit, name="edit_bmi"),
    path("bmi/<id>/edit-submit/", views.bmi_edit_submit, name="edit-bmi-submit"),
    path("bmi/<id>/delete/", views.bmi_delete, name="delete_bmi"),
    path("bmi/<id>/delete-submit/", views.bmi_delete_submit, name="delete-bmi-submit"),

    # Calorie Counters Routing
    path("calorie-counters/", views.calorie_counters, name="calorie_counters"),
    path("calorie-counter/<id>/", views.calorie_counter, name="calorie_counter"),
    path("calorie-counter/create/", views.calorie_counter_create, name="create-calorie-counter"),
    path("calorie-counter/create-submit/", views.calorie_counter_create_submit, name="create-calorie-counter-submit"),
    path("calorie-counter/<id>/edit/", views.calorie_counter_edit, name="edit-calorie-counter"),
    path("calorie-counter/<id>/edit-submit/", views.calorie_counter_edit_submit, name="edit-calorie-counter-submit"),
    path("calorie-counter/<id>/delete/", views.calorie_counter_delete, name="delete-calorie-counter"),
    path("calorie-counter/<id>/delete-submit/", views.calorie_counter_delete_submit, name="delete-calorie-counter-submit"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
