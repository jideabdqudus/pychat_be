from rest_framework import serializers
from .models import Post

class PostSerializer (serializers.ModelSerializer):
    email = serializers.CharField(source='owner.email', read_only=True)
    username = serializers.CharField(source='owner.username', read_only=True)
    class Meta:
        model = Post
        fields ='__all__'
        extra_kwargs = {'owner': {'read_only': True}}