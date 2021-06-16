from django.shortcuts import render
from models import Post
from rest_framework import viewsets, permissions
from serializers import PostSerializer

# Create your views here.

# Post ViewSet
class PostViewSet(viewsets.ModelViewSet):

