from .models import Serie
from .serializers import SerieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics


class SerieView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

    def perform_create(self, serializer):
        exercise_id = self.request.data["exercise_id"]
        serializer.save(exercise_id=exercise_id)


class DetailSerieView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Serie.objects.all()
    serializer_class = SerieSerializer


class FilterSerieView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SerieSerializer

    lookup_url_kwarg = "exercise_id"

    def get_queryset(self):
        exercise_id = self.kwargs["exercise_id"]
        return Serie.objects.filter(exercise_id=exercise_id)
