import pytest
import json
from rest_framework import status
from apps.users.tests.conftest import UserFactory
from apps.courses.tests.conftest import CourseFactory
from apps.quizzes.tests.conftest import TestFactory, QuestionFactory, AnswerFactory
from apps.quizzes.models import Test, Answer, Question
from apps.users.tests.conftest import api_client, get_token


@pytest.mark.django_db(transaction=True)
class TestQuiz:
    url = '/pitch/tests/'

    def test_list(self, api_client):
        user = UserFactory()
        course = CourseFactory(teacher=user.profile)
        TestFactory(course=course)
        get_token(api_client, user)
        response = api_client.get(self.url)
        assert response.status_code == status.HTTP_200_OK

    def test_create(self, api_client):
        user = UserFactory()
        CourseFactory(teacher=user.profile)
        test = TestFactory.build()
        get_token(api_client, user)
        test_data = {'title': test.title, 'course': 1}
        response = api_client.post(self.url, data=test_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_retrieve(self, api_client):
        user = UserFactory()
        course = CourseFactory(teacher=user.profile)
        test = TestFactory(course=course)
        get_token(api_client, user)
        response = api_client.get(f'{self.url}{test.pk}/')
        assert response.status_code == status.HTTP_200_OK

    def test_update(self, api_client):
        user = UserFactory()
        course = CourseFactory(teacher=user.profile)
        test = TestFactory(course=course)
        test_data = {'title': 'Test n2', 'course': 1}
        get_token(api_client, user)
        response = api_client.put(f'{self.url}{test.pk}/', data=test_data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert json.loads(response.content)['title'] == test_data['title']

    def test_delete(self, api_client):
        user = UserFactory()
        course = CourseFactory(teacher=user.profile)
        test = TestFactory(course=course)
        get_token(api_client, user)
        response = api_client.delete(f'{self.url}{test.pk}/')
        assert response.status_code == 204
        assert Test.objects.all().count() == 0


@pytest.mark.django_db(transaction=True)
class TestQuestion:
    url = '/pitch/questions/'

    def test_list(self, api_client):
        user = UserFactory()
        course = CourseFactory(teacher=user.profile)
        test = TestFactory(course=course)
        QuestionFactory(test=test)
        get_token(api_client, user)
        response = api_client.get(self.url)
        assert response.status_code == status.HTTP_200_OK

    def test_create(self, api_client):
        user = UserFactory()
        course = CourseFactory(teacher=user.profile)
        test = TestFactory(course=course)
        question = QuestionFactory.build(test=test)
        get_token(api_client, user)
        question_data = {'text': question.text, 'test': test.pk, 'answers': [{'text': 'a', 'is_correct': True},
                                                                             {'text': 'b', 'is_correct': False}]}
        response = api_client.post(self.url, data=question_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert len(Answer.objects.all()) == 2

    def test_retrieve(self, api_client):
        user = UserFactory()
        course = CourseFactory(teacher=user.profile)
        test = TestFactory(course=course)
        question = QuestionFactory(test=test)
        get_token(api_client, user)
        response = api_client.get(f'{self.url}{question.pk}/')
        assert response.status_code == status.HTTP_200_OK

    def test_update(self, api_client):
        user = UserFactory()
        course = CourseFactory(teacher=user.profile)
        test = TestFactory(course=course)
        question = QuestionFactory(test=test)
        AnswerFactory(question=question)
        question_data = {'text': 'What is correct?', 'test': test.pk, 'answers': [{"text": "a", "is_correct": False}]}
        response = api_client.put(f'{self.url}{question.pk}/', data=question_data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert json.loads(response.content)['text'] == question_data['text']
        assert json.loads(response.content)['answers'] == question_data['answers']

    def test_delete(self, api_client):
        user = UserFactory()
        course = CourseFactory(teacher=user.profile)
        test = TestFactory(course=course)
        question = QuestionFactory(test=test)
        get_token(api_client, user)
        response = api_client.delete(f'{self.url}{question.pk}/')
        assert response.status_code == 204
        assert Question.objects.all().count() == 0
