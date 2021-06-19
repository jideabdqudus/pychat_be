from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    post = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        """Return the model as a string"""
        return self.post