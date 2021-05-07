from django.urls import path

from . import views

app_name = 'workouts'
urlpatterns = [
    # ex: /workouts/
    path('', views.index, name='index'),
    # ex: /workouts/1/
    path('<int:workout_id>/', views.detail, name='detail'),
]