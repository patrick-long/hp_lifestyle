from django.db import models
from django.utils import timezone

# Create your models here.
class Workout(models.Model):
    workout_name = models.CharField(max_length=300, default='my workout')
    date_created = models.DateTimeField('date created')
    def was_created_recently(self):
        return self.date_created >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.workout_name

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, default=1, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=200, default='my exercise')
    num_sets = models.IntegerField(default=0)
    num_reps = models.IntegerField(default=0)
    rest_time_between_sets_in_seconds = models.IntegerField(default=0)
    weight_in_pounds = models.IntegerField(default=0)

    def __str__(self):
        return self.exercise_name
