from rest_framework import routers

from .views import AuthViewSet, ProfileViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('pitch/auth', AuthViewSet, basename='auth')
router.register('pitch/profile', ProfileViewSet, basename='profile')


urlpatterns = router.urls