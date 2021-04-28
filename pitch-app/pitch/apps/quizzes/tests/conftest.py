import factory
import pytest
from apps.quizzes import models


class TestFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Test

    course = factory.SubFactory('apps.courses.tests.conftest.CourseFactory')
    title = 'Test n1'


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Question

    text = 'What is correct?'
    test = factory.SubFactory(TestFactory)

class AnswerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Answer

    text = 'a'
    question = factory.SubFactory(QuestionFactory)
    is_correct = True


class TestResultFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.TestResult

    profile = factory.SubFactory('apps.users.tests.conftest.ProfileFactory')
    test = factory.SubFactory(TestFactory)


class StudentAnswerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Answer

    answer = 'b'
    profile = factory.SubFactory('apps.users.tests.conftest.ProfileFactory')
    question = factory.SubFactory(QuestionFactory)
    test = factory.SubFactory(TestFactory)
    correct_answer = factory.SubFactory(AnswerFactory)
