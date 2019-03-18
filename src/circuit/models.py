from django.db import models

class Circuit(models.Model):
    name = models.CharField(max_length=100, default='Circuit')
    description = models.TextField(default=None)

    def __str__(self):
        return self.name

class Workout(models.Model):
    exercise = models.CharField(max_length=100, default='Exercise')
    minutes = models.IntegerField(default=00)
    seconds = models.IntegerField(default=00)
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE, related_name='circuit')

    def __str__(self):
        return self.exercise