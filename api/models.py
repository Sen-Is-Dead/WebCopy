from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images', blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
