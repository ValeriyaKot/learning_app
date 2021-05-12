from django.db import models
from django.core.validators import MinValueValidator
from apps.courses.models import Course
from apps.users.models import Profile


class Test(models.Model):
    title = models.CharField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tests')
    attempts_number = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1)])

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
    created = models.DateField(auto_now_add=True)


class StudentAnswer(models.Model):
    answer = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    test_result = models.ForeignKey(TestResult, on_delete=models.CASCADE, related_name='student_answers', blank=True, null=True)
    correct_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
