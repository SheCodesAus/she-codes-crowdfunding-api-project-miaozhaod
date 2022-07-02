from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUser(AbstractUser):
    pass
    bio=models.CharField(max_length=500)
    avatar=models.URLField()
            
    def __str__(self):
        return self.username
    