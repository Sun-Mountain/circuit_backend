
from rest_framework import serializers
from django.db.models import Lookup
from circuit.models import Circuit, Workout

class CircuitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Circuit
        fields = ('id', 'name', 'description')

    def __str__(self):
        return self.name

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ('id', 'exercise', 'minutes', 'seconds', 'circuit')

    def __str__(self):
        return self.exercise