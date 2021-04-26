from django.db import models
from apps.users.models import Profile
from .behavior import Timestampable


class Course(Timestampable):
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE)
    students = models.ManyToManyField(Profile, related_name='course_students')
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Module(Timestampable):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)


class Material(Timestampable):
    module = models.ForeignKey(Module,  related_name='materials', on_delete=models.CASCADE)
    text = models.TextField()
