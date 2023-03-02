from rest_framework import serializers
from .models import Training_day


class Training_daySerializer(serializers.ModelSerializer):
    class Meta:
        model = Training_day
        fields = [
            "id",
            "date",
            "name",
            "user_id",
        ]
