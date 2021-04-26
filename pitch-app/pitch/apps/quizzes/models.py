from django.db import models
from apps.courses.models import Course
from apps.users.models import Profile


class Test(models.Model):
    title = models.CharField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class TestResult(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    result = models.IntegerField()


class StudentAnswer(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='student_answer')
    answer = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    correct_answer = models.TextField()
