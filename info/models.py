from django.db import models
from users.models import User
from job.models import Job


class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=150, null=True, blank=True)
    surname=models.CharField(max_length=150, null=True, blank=True)
    location=models.CharField(max_length=150, null=True, blank=True)
    job_title=models.CharField(max_length=150, null=True, blank=True)
    skills = models.TextField(null=True, blank=True) 
    upload_cv=models.FileField(upload_to='info',null=True, blank=True)


# insert cv

    def __str__(self):
        return f'{self.first_name} {self.surname}'

