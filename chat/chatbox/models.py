from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    post = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    # owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, null=False, default=1)