from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
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