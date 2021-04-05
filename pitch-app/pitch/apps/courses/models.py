from django.db import models
from apps.users.models import Profile
from .behavior import Timestampable


class Course(Timestampable):
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE)
    students = models.ManyToManyField(Profile, related_name='students_of_course')
    title = models.CharField(max_length=250)


class Module(Timestampable):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)


class Material(Timestampable):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = models.TextField()


class Test(models.Model):
    title = models.CharField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Question(models.Model):
    text = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE)


class Answer(models.Model):
    answer = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)


class StudentAnswer(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    answer = models.ForeignKey(Answer, on_delete=models.DO_NOTHING)
