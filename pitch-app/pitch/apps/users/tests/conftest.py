import factory
import pytest
from django.db.models.signals import post_save
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from apps.users.models import Profile
from pytest_factoryboy import register
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password


@pytest.fixture
def api_client():
    return APIClient()


def get_token(api_client, user):
    token, _ = Token.objects.get_or_create(user=user)
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return api_client


@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Profile

    user = factory.SubFactory('apps.users.tests.conftest.UserFactory', profile=None)
    birthday = '2000-02-02'
    role = 'teacher'


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'Tommy'
    password = make_password('tommy1234')
    email = 'tommy99@example.com'
    first_name = 'Tommy'
    last_name = 'West'
    profile = factory.RelatedFactory(ProfileFactory, factory_related_name='user')

