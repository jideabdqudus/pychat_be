from django.urls import path, include
from .views import RegisterViewSet
from rest_framework.routers import DefaultRouter
from knox import views as knox_views

router = DefaultRouter()
router.register('api/auth/register', RegisterViewSet)


urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('', include(router.urls))
  #  path('api/auth/register', RegisterView.as_view())
]