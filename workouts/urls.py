from django.urls import path

from . import views

app_name = 'workouts'
urlpatterns = [
    # ex: /workouts/
    path('', views.index, name='index'),
    # ex: /workouts/1/
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.CreateWorkout.as_view(), name='create_workout'),
    path('exercises/create/', views.CreateExercise.as_view(), name='create_exercise'),
    path('<int:pk>/update/', views.UpdateWorkout.as_view(), name='update_workout'),
    path('exercises/<int:pk>/update/', views.UpdateExercise.as_view(), name='update_exercise'),
    path('<int:pk>/delete/', views.DeleteWorkout.as_view(), name='delete_workout'),
    path('exercises/<int:pk>/delete/', views.DeleteExercise.as_view(), name='delete_exercise'),
]