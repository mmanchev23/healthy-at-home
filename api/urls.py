from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import exception_handler
from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response
from django.conf.urls import url
from django.contrib.sites.shortcuts import get_current_site

def custom_exception_handler(exc, context):
    if isinstance(exc, NotAuthenticated):
        request = context['request']
        return Response({"You are not logged in!": {
            "home page": f"{request.scheme}://{request.get_host()}/",
            "register": f"{request.build_absolute_uri()}auth/register/",
            "login": f"{request.build_absolute_uri()}auth/login/",
        }}, status=401)

    return exception_handler(exc, context)


class APIRoot(routers.APIRootView):
    def get_view_name(self) -> str:
        return "Healthy at Home"

    def get(self, request):
        if request.user.is_authenticated == True:
            return Response({
                f"Logged in as {request.user.username}": {
                    "home page": f"{request.scheme}://{request.get_host()}/",
                    f"{request.user.username}": f"{request.build_absolute_uri()}credentials/",
                    "food": f"{request.build_absolute_uri()}food/",
                    "workouts": f"{request.build_absolute_uri()}workouts/",
                    "tasks": f"{request.build_absolute_uri()}tasks/",
                    "bmi": f"{request.build_absolute_uri()}bmi/",
                    "documentation": f"{request.build_absolute_uri()}docs/",
                    "schema": f"{request.build_absolute_uri()}schema/",
                    "logout": f"{request.build_absolute_uri()}auth/logout/",
                }
            })


class Healthy_at_Home_Router(routers.DefaultRouter):
    APIRootView = APIRoot


API_TITLE = 'Healthy at Home API'
API_DESCRIPTION = 'API for Healthy at Home!'
schema_view = get_schema_view(title=API_TITLE)

router = Healthy_at_Home_Router()
router.register(r'credentials', views.CustomerView, 'customer')
router.register(r'food', views.FoodView, 'food')
router.register(r'workouts', views.WorkoutView, 'workout')
router.register(r'tasks', views.TaskView, 'task')
router.register(r'bmi', views.BMICalculatorView, 'bmi')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('auth/register/', include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)), 
    path('schema/', schema_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)