from django.urls import path, include
from .views import RegisterViewSet, UserLoginApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/auth/register', RegisterViewSet,)


urlpatterns = [
    path('', include(router.urls)),
    path('api/auth', UserLoginApiView.as_view())
]