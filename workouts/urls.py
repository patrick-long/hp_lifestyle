from django.urls import path

from . import views

app_name = 'workouts'
urlpatterns = [
    # ex: /workouts/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /workouts/1/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]