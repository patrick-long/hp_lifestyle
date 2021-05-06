from django.db import models

# Create your models here.
class Workout(models.Model):
    workout_name = models.CharField(max_length=300), 

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE),
    exercise_name = models.CharField(max_length=200),
    num_sets = models.IntegerField(default=0),
    num_reps = models.IntegerField(default=0),
    rest_time = models.IntegerField(default=0),
    weight = models.IntegerField(default=0),

