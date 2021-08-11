from django.db.models import Q
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import *
from app.models import *

        
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
