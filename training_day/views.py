from .models import Training_day
from .serializers import Training_daySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from .permissions import IsAdminOrTrainingOwner


class TrainingView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Training_day.objects.all()
    serializer_class = Training_daySerializer

    def get_queryset(self):
        return Training_day.objects.filter(user_id=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DetailTrainingView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrTrainingOwner]

    queryset = Training_day.objects.all()
    serializer_class = Training_daySerializer
