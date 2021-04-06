from django.urls import path
from . import views
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('pitch/courses', views.CourseView, basename='courses')
router.register('pitch/courses', views.CourseDetailView, basename='course-detail')
router.register('pitch/modules', views.ModuleView, basename='modules')
router.register('pitch/materials', views.MaterialView, basename='materials')


urlpatterns = router.urls


# urlpatterns = [
#     # path('pitch/courses/', views.CourseView.as_view()),
#     # path('pitch/add_course/', views.CourseAddView.as_view()),
# ]