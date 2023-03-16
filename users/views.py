from rest_framework.views import APIView, Request, Response, status
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsAccountOwner
from rest_framework import generics
from training_day.models import Training_day
from training_day.serializers import Training_daySerializer
from exercises.models import Exercise
from exercises.serializers import ExerciseSerializer
from series.models import Serie
from series.serializers import SerieSerializer
import json
from rest_framework.permissions import IsAuthenticated


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserWorksheets(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]
    
    def get(self, req: Request, training_day_id: int) -> Response:
        training_day_id = self.kwargs["training_day_id"]
        training = Training_day.objects.get(id=training_day_id)
        training_serializer = Training_daySerializer(training)
        training_data = training_serializer.data

        return_data = training_data

        exercises = Exercise.objects.filter(training_day_id=training_data["id"])
        exercises_serializer = ExerciseSerializer(exercises, many=True)
        exercises_data = json.loads(json.dumps(exercises_serializer.data))

        return_data["exercises"] = exercises_data
        for exercise in return_data["exercises"]:
            series = Serie.objects.filter(exercise_id=exercise["id"])
            series_serializer = SerieSerializer(series, many=True)
            series_data = json.loads(json.dumps(series_serializer.data))
            exercise["series"] = series_data

        return Response(return_data, status.HTTP_200_OK)
