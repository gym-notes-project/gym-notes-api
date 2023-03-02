from .models import Exercise
from .serializers import ExerciseSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics


class ExerciseView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def perform_create(self, serializer):
        training_day_id = self.request.data["training_day_id"]
        serializer.save(training_day_id=training_day_id)

class DetailExerciseView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class FilterExerciseView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    serializer_class = ExerciseSerializer
    
    lookup_url_kwarg = "training_id"
    
    def get_queryset(self):
        training_day_id = self.kwargs["training_id"]
        return Exercise.objects.filter(training_day_id=training_day_id)
