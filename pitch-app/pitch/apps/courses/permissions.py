from rest_framework.permissions import BasePermission, SAFE_METHODS
from apps.users.models import Profile


class IsTeacherOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if Profile.objects.filter(user=request.user).exists():
            profile = Profile.objects.get(user=request.user)
            if profile.role == 'teacher':
                return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.data
        return obj
