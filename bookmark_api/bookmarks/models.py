from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField(max_length=130)
    url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                       on_delete=models.CASCADE, related_name='bookmark')
