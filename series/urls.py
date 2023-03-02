from django.urls import path
from . import views


urlpatterns = [
    path("series/", views.SerieView.as_view()),
    path("series/<int:pk>", views.DetailSerieView.as_view()),
    path("series/exercise/<int:exercise_id>", views.FilterSerieView.as_view()),
]
