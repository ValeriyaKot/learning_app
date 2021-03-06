from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('pitch/tests', views.TestView, basename='tests')
router.register('pitch/questions', views.QuestionView, basename='questions')


urlpatterns = router.urls + [
    path('pitch/check/', views.CheckResultView.as_view(), name='check'),
    path('pitch/results/', views.TestResultView.as_view(), name='results'),
    path('pitch/course-tests/<int:pk>/tests', views.TestCourseView.as_view(), name='course-tests'),
]
