from django.urls import path
from . import views


urlpatterns = [
    path("exercises/", views.ExerciseView.as_view()),
    path("exercises/<int:pk>", views.DetailExerciseView.as_view()),
    path("exercises/training/<int:training_id>", views.FilterExerciseView.as_view()),
]
