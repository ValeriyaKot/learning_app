import pytest
import json
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token

from .conftest import UserFactory, get_token


@pytest.mark.django_db(transaction=True)
class TestAuth:

    def test_register(self, api_client):
        user = UserFactory.build()
        user_data = {'username': user.username, 'password': user.password,
                     'email': user.email, 'first_name': user.first_name,
                     'last_name': user.last_name, 'profile': {'birthday': user.profile.birthday,
                                                              'role': user.profile.role}}
        response = api_client.post('/pitch/auth/register', data=user_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_login(self, api_client):
        user = UserFactory()
        user_data = {'username': user.username, 'password': 'tommy1234'}
        response = api_client.post('/pitch/auth/login', data=user_data, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_password_change(self, api_client):
        user = UserFactory()
        url = '/pitch/auth/password_change'
        get_token(api_client, user)
        user_data = {'current_password': 'tommy1234', 'new_password': 'password1234!'}
        response = api_client.post(url, data=user_data, format='json')
        assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db(transaction=True)
class TestProfile:
    url = '/pitch/profile'

    def test_list(self, api_client):
        user = UserFactory()
        get_token(api_client, user)
        response = api_client.get(self.url)
        assert response.status_code == 200
