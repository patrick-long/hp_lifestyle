from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm

from .models import Workout, Exercise

print(generic)

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/workouts/')
        else:
            return redirect('/signup/')
    else:
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

def detail(request, pk):
    workout = Exercise.objects.filter(workout_id=pk)
    template_name = 'workouts/detail.html'
    return render(request, template_name, context={'specific_workout': workout})

class CreateWorkout(CreateView):
    model = Workout
    fields = ['workout_name']
    success_url = '/workouts/'

class CreateExercise(CreateView):
    model = Exercise
    fields = ['workout', 'exercise_name', 'num_sets', 'num_reps', 'rest_time_between_sets_in_seconds', 'weight_in_pounds']
    success_url = '/workouts/'

class UpdateWorkout(UpdateView):
    model = Workout
    fields = ['workout_name']
    success_url = '/workouts/'

class UpdateExercise(UpdateView):
    model = Exercise
    fields = ['workout', 'exercise_name', 'num_sets', 'num_reps', 'rest_time_between_sets_in_seconds', 'weight_in_pounds']
    success_url = '/workouts/'

class DeleteWorkout(DeleteView):
    model = Workout
    success_url = '/workouts/'


class DeleteExercise(DeleteView):
    model = Exercise
    success_url = '/workouts/'