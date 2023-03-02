from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        have_password = validated_data.get("password")

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if have_password:
            instance.set_password(validated_data["password"])

        instance.save()

        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "name",
            "is_superuser",
        ]
        extra_kwargs = {"password": {"write_only": True}}