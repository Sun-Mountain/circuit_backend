from rest_framework import serializers

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
        field = ('id', 'exercise', 'minutes', 'seconds', 'circuit')