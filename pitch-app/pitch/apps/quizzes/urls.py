from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('pitch/tests', views.TestView, basename='tests')
router.register('pitch/tests/questions', views.QuestionView, basename='questions')
router.register('pitch/student_answers', views.StudentAnswersView, basename='student_answers')


urlpatterns = router.urls + [
    path('pitch/check/', views.CheckResultView.as_view(), name='check'),
    path('pitch/results/', views.TestResultView.as_view(), name='results'),
    path('pitch/student_answers/', views.StudentAnswersView, name='student_answers')
]
