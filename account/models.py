from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique =  True)
    username = models.CharField(max_length=225)
    bio = models.CharField(max_length=100,null=True,blank=True)
    profile_pic = models.ImageField(upload_to='account/images/',null=True,blank=True)
    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username