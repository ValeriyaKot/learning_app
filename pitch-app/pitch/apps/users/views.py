from django.contrib.auth import logout
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from . import serializers
from .models import Profile
from .utils import get_and_authenticate_user, create_user_account


class AuthViewSet(viewsets.GenericViewSet):
    queryset = ''
    permission_classes = [AllowAny, ]
    serializer_classes = {
        'login': serializers.UserLoginSerializer,
        'register': serializers.UserRegisterSerializer,
        'password_change': serializers.PasswordChangeSerializer,
    }

    @action(methods=['POST', ], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        profile_data = serializer.validated_data.pop('profile')
        user = create_user_account(**serializer.validated_data)
        user.profile.birthday = profile_data['birthday']
        user.profile.role = profile_data['role']
        user.save()
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    @action(methods=['POST', ], detail=False)
    def logout(self, request):
        logout(request)
        data = {'success': 'Successfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated, ])
    def password_change(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
