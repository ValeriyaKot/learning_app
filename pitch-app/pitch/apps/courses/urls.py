from django.urls import path
from . import views
from rest_framework import routers
from .views import CourseView, CourseDetailView

router = routers.SimpleRouter()
router.register('pitch/courses', CourseView, basename='courses')
router.register('pitch/courses', CourseDetailView, basename='course-detail')


urlpatterns = router.urls


# urlpatterns = [
#     # path('pitch/courses/', views.CourseView.as_view()),
#     # path('pitch/add_course/', views.CourseAddView.as_view()),
# ]