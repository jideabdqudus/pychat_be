from django.urls import path, include
# from .views import RegisterView
from knox import views as knox_views

urlpatterns = [
    path('api/auth', include('knox.urls')),
  #  path('api/auth/register', RegisterView.as_view())
]