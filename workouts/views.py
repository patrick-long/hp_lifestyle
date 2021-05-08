from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm

from .models import Workout, Exercise

print(generic)

# Create your views here.
def signup(request):
    form = UserCreationForm()
    return render(request, 'workouts/signup.html', {'form': form })

def home(request):
    template_name = 'workouts/home.html'
    return render(request, template_name, {'Workout': 'Workout'})

class IndexView(generic.ListView):
    template_name = 'workouts/index.html'
    context_object_name = 'workouts'

    def get_queryset(self):
        return Workout.objects.order_by('date_created')

class DetailView(generic.DetailView):
    model = Workout
    template_name = 'workouts/detail.html'

class CreateWorkout(CreateView):
    model = Workout
    fields = ['workout_name']
    success_url = 'workouts/'

class CreateExercise(CreateView):
    model = Exercise
    fields = ['exercise_name', 'num_sets', 'num_reps', 'rest_time_between_sets_in_seconds', 'weight_in_pounds']
    success_url = 'workouts/<int:pk>/'