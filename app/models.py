from django.db import models
from authapp.models import CustomUser
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    PROJECT_TYPES = [
        ('professional', 'Professional'),
        ('personal', 'Personal'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=PROJECT_TYPES, default='professional')
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
