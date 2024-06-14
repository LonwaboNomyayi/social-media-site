from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserImageExtension(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to='user-images')

    def __str__(self):
        return f"{self.user.username} User's image"
