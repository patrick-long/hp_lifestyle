from django.shortcuts import render
from django.http import HttpResponse

from .models import Workout

# Create your views here.
def home(request):
    return HttpResponse("This is the home page of the app")

def index(request):
    return HttpResponse("This is the official index page of the workout app. Time to get started making something cool!")

def detail(request, workout_id):
    return HttpResponse( f"This is the detail page of workout {workout_id} in the database.")
