from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('pitch/courses', views.CourseView, basename='courses')
router.register('pitch/courses', views.CourseDetailView, basename='course-detail')
router.register('pitch/modules', views.ModuleView, basename='modules')
router.register('pitch/materials', views.MaterialView, basename='materials')


urlpatterns = router.urls + [
    path('pitch/teacher/courses/', views.TeacherCourseView.as_view(), name='teacher-courses'),
    path('pitch/student/courses/', views.StudentEnrolledCourseView.as_view(), name='student-courses'),
    path('pitch/courses/<int:pk>/enroll/', views.EnrollCourse.as_view(), name='enroll-course'),
]
