from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=100, blank=True)
    degree = models.CharField(max_length=100, blank=True)
    profile_photo = models.ImageField(upload_to="media", default='0.jpeg')
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    about_desc = models.TextField(blank=True)
    role = models.CharField(max_length=50, blank=True)
