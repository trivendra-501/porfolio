from django.db import models
# models.py

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    dob = models.DateField(null=True, blank=True)
    phonenumber = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=100, blank=True)
    degree = models.CharField(max_length=100, blank=True)

    # Specify unique related_names to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',  # Specify a unique related_name
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set',  # Specify a unique related_name
        related_query_name='user'
    )
    

    def __str__(self):
        return self.username
