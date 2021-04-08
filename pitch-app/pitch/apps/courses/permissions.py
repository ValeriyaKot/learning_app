from rest_framework.permissions import BasePermission, SAFE_METHODS
from apps.users.models import Profile


class IsTeacherOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        try:
            profile = Profile.objects.get(user=request.user)
            if profile.role == 'teacher':
                return obj
        except Profile.DoesNotExist:
            raise ValueError('Profile does not exist')
