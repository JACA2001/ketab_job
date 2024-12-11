from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model
from .models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields=['email', 'username','password1','password2','phone_number', 'address', 'face_image', 'voice_sample']
        
        
def save(self, commit=True):
    user = super().save(commit=False)
    if commit:
         user.save()  
    return user


class UpdateProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'phone_number',
            'address'
            
        ]
        
       
