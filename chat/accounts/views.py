from rest_framework import viewsets, filters, status
from rest_framework.authentication import TokenAuthentication
from .serializers import UserProfileSerializer
from .models import UserProfile
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .permissions import UpdateOwnProfile


class RegisterViewSet(viewsets.ModelViewSet):
    """Handle Creating and Updating Profile"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email')

class UserLoginApiView(ObtainAuthToken):
    """Creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# class UserLogout(APIView):
#     def get(self, request):
#         # simply delete the token to force a login
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)