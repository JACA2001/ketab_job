from django import forms
from .models import Info


class UpdateInfoForm(forms.ModelForm):
    class Meta:
      model=Info
      exclude=('user',)
    
