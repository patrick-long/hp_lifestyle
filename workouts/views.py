from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

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

def index(request):
    template_name = 'workouts/index.html'
    if request.user.is_authenticated:
        workouts = Workout.objects.filter(user=request.user)
    else: 
        workouts = None
    return render(request, template_name, {'workouts': workouts})

def detail(request, pk):
    workout = Exercise.objects.filter(workout_id=pk)
    template_name = 'workouts/detail.html'
    return render(request, template_name, context={'specific_workout': workout})

class CreateWorkout(CreateView, LoginRequiredMixin):
    model = Workout
    fields = ['workout_name']
    success_url = '/workouts/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CreateExercise(CreateView, LoginRequiredMixin):
    model = Exercise
    fields = ['workout', 'exercise_name', 'num_sets', 'num_reps', 'rest_time_between_sets_in_seconds', 'weight_in_pounds']
    success_url = '/workouts/'

class UpdateWorkout(UpdateView, LoginRequiredMixin):
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