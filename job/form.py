from django import forms
from .models import Job

class CreateJobForm(forms.ModelForm):
    class Meta:
        model=Job
        exclude=('user','staf','timestamp')
        

class UpdateJobForm(forms.ModelForm):
    class Meta:
        model=Job
        exclude=('user','staf','timestamp')