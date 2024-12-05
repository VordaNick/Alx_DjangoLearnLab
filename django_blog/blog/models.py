from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    def __str__(self):
        return self.user.username

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    tag = models.ManyToManyField(Post, related_name='tags')