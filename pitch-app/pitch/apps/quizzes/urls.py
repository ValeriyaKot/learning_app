from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('pitch/tests', views.TestView, basename='tests')
router.register('pitch/tests/questions', views.QuestionView, basename='questions')


urlpatterns = router.urls + [
    path('pitch/tests/check/', views.CheckResultView.as_view(), name='check'),
    path('pitch/tests/results/', views.TestResultView.as_view(), name='results')
]
