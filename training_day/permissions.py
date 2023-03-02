from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Training_day


class IsAdminOrTrainingOwner(permissions.BasePermission):
    def has_object_permission(self, req: Request, view: View, obj: Training_day):
        return req.user.is_superuser or req.user == obj.user
