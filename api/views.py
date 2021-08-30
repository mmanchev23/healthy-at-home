from .serializers import *
from django.db.models import Q
from applications.models import *
from rest_framework.response import Response
from rest_framework import viewsets, permissions

        
class UserView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.pk)

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        if self.object_list:
            return Response({'credentials': serializer.data})
        else:
            return Response({'message': "No user found!"})


class ProfileLikeView(viewsets.ModelViewSet):
    serializer_class = ProfileLikeSerializer
    queryset = ProfileLike.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return ProfileLike.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        if self.object_list:
            return Response({'likes': serializer.data})
        else:
            return Response({'message': "No likes found!"})


class ProfileFollowerView(viewsets.ModelViewSet):
    serializer_class = ProfileFollowerSerializer
    queryset = ProfileFollower.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return ProfileFollower.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        if self.object_list:
            return Response({'followers': serializer.data})
        else:
            return Response({'message': "No followers found!"})


class WorkoutView(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        public = Workout.public
        return Workout.objects.filter(Q(user=user) | Q(public=True))


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
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)

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
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return BMICalculator.objects.filter(user=user)

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
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Food.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        if self.object_list:
            return Response({'meals': serializer.data})
        else:
            return Response({'message': "No meals found!"})
