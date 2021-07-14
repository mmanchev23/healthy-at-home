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

def custom_exception_handler(exc, context):
    if isinstance(exc, NotAuthenticated):
        request = context['request']
        return Response({"You are not logged in!": {
            "register": f"{request.build_absolute_uri()}api/register/",
            "login": f"{request.build_absolute_uri()}api/login/",
            "facebook": f"{request.build_absolute_uri()}api/facebook/",
            "google": f"{request.build_absolute_uri()}api/google/",
        }}, status=401)

    return exception_handler(exc, context)


class APIRoot(routers.APIRootView):
    def get_view_name(self) -> str:
        return "Healthy at Home"

    def get(self, request):
        if request.user.is_authenticated == True:
            return Response({
                f"Logged in as {request.user.username}": {
                    f"{request.user.username}": f"{request.build_absolute_uri()}credentials/",
                    "food": f"{request.build_absolute_uri()}food/",
                    "workouts": f"{request.build_absolute_uri()}workouts/",
                    "tasks": f"{request.build_absolute_uri()}tasks/",
                    "bmi": f"{request.build_absolute_uri()}bmi/",
                    "documentation": f"{request.build_absolute_uri()}docs/",
                    "schema": f"{request.build_absolute_uri()}schema/",
                    "logout": f"{request.build_absolute_uri()}api/logout/",
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
    url(r'^accounts/', include('allauth.urls'), name='socialaccount_signup'),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    path('api/', include('rest_auth.urls')),
    path('api/register/', include('rest_auth.registration.urls')),
    path('api/facebook/', views.FacebookLogin.as_view(), name='fb_login'),
    path('api/google/', views.GoogleLogin.as_view(), name='google_login'),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)), 
    path('schema/', schema_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)