from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_recruiter = models.BooleanField(default=False)
    is_applicant=models.BooleanField(default=False)
    username = models.CharField(max_length=100, unique=True)
    
    has_resume = models.BooleanField(default=False)
    has_company= models.BooleanField(default=False)
    
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    face_image = models.ImageField(upload_to='face_images/', blank=True, null=True)
    voice_sample = models.FileField(upload_to='voice_samples/', blank=True, null=True)

    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )