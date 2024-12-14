from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager




# Create your models here.
'''class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extrafields):
        extrafields.setdefault('is_active', True)
        if not email:
            raise ValueError('Email is required')
        if not password:
            raise ValueError('Password is required')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_staff=True
        user.is_superuser=True
        user.is_admin=True
        user.save(using=self._db)
        return user'''

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=500,)
    profile_picture = models.ImageField(blank=True)
    followers = models.ManyToManyField("self", symmetrical=False, related_name='follow')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    following = models.ManyToManyField("self", symmetrical=False)
    
    #objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username
    
    

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    def __str__(self):
        return self.username