from django.urls import path
from . import views
from rest_framework import routers
from .views import CourseView, CourseDetailView, ModuleView, MaterialView

router = routers.SimpleRouter()
router.register('pitch/courses', CourseView, basename='courses')
router.register('pitch/courses', CourseDetailView, basename='course-detail')
router.register('pitch/modules', ModuleView, basename='modules')
router.register('pitch/materials', MaterialView, basename='materials')


urlpatterns = router.urls + [
    # path('pitch/course/<int:pk>/', views.CourseDetailView.as_view(), name='course')
]


# urlpatterns = [
#     # path('pitch/courses/', views.CourseView.as_view()),
#     # path('pitch/add_course/', views.CourseAddView.as_view()),
# ]