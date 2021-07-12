from django.db.models import Q
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import *
from .models import *
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.serializers import SocialLoginSerializer


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

        
class CustomerView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        customer = self.request.user
        return Customer.objects.filter(pk=customer.pk)

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        if self.object_list:
            return Response({'credentials': serializer.data})
        else:
            return Response({'message': "No user found!"})


class WorkoutView(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    def perform_update(self, serializer):
        serializer.save(customer=self.request.user)

    def get_queryset(self):
        customer = self.request.user
        public = Workout.public
        return Workout.objects.filter(Q(customer=customer) | Q(public=True))


    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        if self.object_list:
            return Response({'workouts': serializer.data})
        else:
            return Response({'message': "No workouts found!"})


class TaskView(viewsets.ModelViewSet):
    serializer_class = ToDoListSerializer
    queryset = Task.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    def perform_update(self, serializer):
        serializer.save(customer=self.request.user)

    def get_queryset(self):
        customer = self.request.user
        return Task.objects.filter(customer=customer)

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        if self.object_list:
            return Response({'tasks': serializer.data})
        else:
            return Response({'message': "No tasks found!"})


class BMICalculatorView(viewsets.ModelViewSet):
    serializer_class = BMICalculatorSerializer
    queryset = BMICalculator.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    def perform_update(self, serializer):
        serializer.save(customer=self.request.user)

    def get_queryset(self):
        customer = self.request.user
        return BMICalculator.objects.filter(customer=customer)

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        if self.object_list:
            return Response({'results': serializer.data})
        else:
            return Response({'message': "No results found!"})


class FoodView(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    def perform_update(self, serializer):
        serializer.save(customer=self.request.user)

    def get_queryset(self):
        customer = self.request.user
        return Food.objects.filter(customer=customer)

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        if self.object_list:
            return Response({'meals': serializer.data})
        else:
            return Response({'message': "No meals found!"})
