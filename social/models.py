from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser


class Post(models.Model):
    body = models.TextField()
    media = models.ImageField(upload_to='media', null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    # likes = models.IntegerField(default=0)
    # comments = models.TextField(max_length=200, blank=True)

class Comment(models.Model):
    text = models.TextField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to='user_image', null=True, blank=True)
    liked_posts = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    # posts = models.ForeignKey(Post, default=None, blank=True,on_delete=models.CASCADE)

class Like(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        # Define a unique constraint to prevent duplicate likes by a user on a post
        unique_together = ('user', 'post')

