import pytest
import json
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from apps.users.tests.conftest import UserFactory
from .conftest import CourseFactory, ModuleFactory, MaterialFactory
from apps.courses.models import Course
from apps.users.tests.conftest import api_client, get_token


@pytest.mark.django_db(transaction=True)
class TestCourse:
    url = '/pitch/courses/'

    def test_list(self, api_client):
        user = UserFactory()
        CourseFactory(teacher=user.profile)
        get_token(api_client, user)
        response = api_client.get(self.url)
        assert response.status_code == status.HTTP_200_OK

    def test_add_course(self, api_client):
        user = UserFactory()
        course = CourseFactory.build(teacher=user.profile)
        get_token(api_client, user)
        course_data = {'title': course.title}
        response = api_client.post(f'{self.url}add_course/', data=course_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_retrieve(self, api_client):
        user = UserFactory()
        course = CourseFactory(teacher=user.profile)
        ModuleFactory(course=course)
        get_token(api_client, user)
        response = api_client.get(f'{self.url}1/')
        assert response.status_code == status.HTTP_200_OK

    def test_update(self, api_client):
        user = UserFactory()
        CourseFactory(teacher=user.profile)
        course_data = {'title': 'Course number 2'}
        get_token(api_client, user)
        response = api_client.put(f'{self.url}1/', data=course_data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert json.loads(response.content)['title'] == course_data['title']

    def test_delete(self, api_client):
        user = UserFactory()
        CourseFactory(teacher=user.profile)
        get_token(api_client, user)
        response = api_client.delete(f'{self.url}1/')
        assert response.status_code == 204
        assert Course.objects.all().count() == 0
