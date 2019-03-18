from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

from circuit.models import Circuit, Workout
from .serializers import CircuitSerializer, WorkoutSerializer

class circuit_list(ListAPIView):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer

class circuit_detail(RetrieveAPIView):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer


class workout_list(ListAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class workout_detail(RetrieveAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer