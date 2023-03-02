from django.urls import path
from . import views


urlpatterns = [
    path("training/", views.TrainingView.as_view()),
    path("training/<int:pk>", views.DetailTrainingView.as_view()),
]
