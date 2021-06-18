from rest_framework import viewsets, filters, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.authentication import TokenAuthentication
from .serializers import UserProfileSerializer
from .models import UserProfile


class RegisterViewSet(viewsets.ModelViewSet):
    """Handle Creating and Updating Profile"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (permissions.UpdateOwnProfile,)
    #filter_backends = (filters.SearchFilter,)
    #search_fields = ('username', 'email')

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()
    #
    #     return Response({
    #         'user': UserProfileSerializer(user, context=self.get_serializer_context()).data,
    #         'token': AuthToken.objects.create(user)[1]
    #     })
