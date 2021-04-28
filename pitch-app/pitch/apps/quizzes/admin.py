from django.contrib import admin
from .models import StudentAnswer, TestResult, Test

admin.site.register(StudentAnswer)
admin.site.register(TestResult)
admin.site.register(Test)
