from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .permissions import UpdateOwnPost


# Create your views here.

# Post ViewSet
class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = Post.objects.all()
    permission_classes = (
        UpdateOwnPost,
        IsAuthenticatedOrReadOnly
    )
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

