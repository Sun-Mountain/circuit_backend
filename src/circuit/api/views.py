from django.shortcuts import render, redirect
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    RetrieveAPIView,
    UpdateAPIView
)

from rest_framework import viewsets
from circuit.models import Workout, Circuit
from .serializers import WorkoutSerializer, CircuitSerializer

class circuit_list(ListAPIView):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer

class circuit_detail(RetrieveAPIView):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer

class circuit_create(CreateAPIView):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer

class circuit_update(UpdateAPIView):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer

class circuit_delete(DestroyAPIView):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer


class workout_list(ListAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class workout_detail(RetrieveAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class workout_create(CreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class workout_update(UpdateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class workout_delete(DestroyAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer