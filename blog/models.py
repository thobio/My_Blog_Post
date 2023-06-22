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

    class Meta:
        ordering = ('-created_at',)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, related_name="commented_user", on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

