from django.db import models
from account.models import Profile
import uuid
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    post_content = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_user')
    post_image = models.ImageField(upload_to='post_image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
