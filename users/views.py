from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout,update_session_auth_hash
from .models import User
from .form import RegisterUserForm,UpdateProfileForm
from info.models import Info
from staf.models import Staf
import os
from django.conf import settings

import face_recognition
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm


import speech_recognition as sr
from django.core.files.storage import default_storage




# register applicant only.

import base64
from django.core.files.base import ContentFile

def register_applicant(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_applicant = True
            user.username = user.email

            # Traiter l'image faciale (base64)
            facial_image_data = request.POST.get('facial_recognition_image')
            if facial_image_data:
                format, imgstr = facial_image_data.split(';base64,')
                ext = format.split('/')[-1]
                user.face_image.save(f"{user.username}_face.{ext}", ContentFile(base64.b64decode(imgstr)))

            # Traiter l'audio (base64)
            voice_audio_data = request.POST.get('voice_recognition_audio')
            if voice_audio_data:
                format, audiostr = voice_audio_data.split(';base64,')
                ext = format.split('/')[-1]
                user.voice_sample.save(f"{user.username}_voice.{ext}", ContentFile(base64.b64decode(audiostr)))

            user.save()
            Info.objects.create(user=user)
            messages.info(request, 'Your account has been created successfully')
            return redirect('login')
        else:
            error_messages = [f"{field}: {error}" for field, errors in form.errors.items() for error in errors]
            messages.warning(request, "Errors: " + ", ".join(error_messages))
    else:
        form = RegisterUserForm()
    return render(request, 'users/register_applicant.html', {'form': form})




    
    
    
    

# register recruiter only


def register_recruiter(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_recruiter = True
            user.username = user.email

            # Traiter l'image faciale (base64)
            facial_image_data = request.POST.get('facial_recognition_image')
            if facial_image_data:
                try:
                    format, imgstr = facial_image_data.split(';base64,')
                    ext = format.split('/')[-1]
                    user.face_image.save(f"{user.username}_face.{ext}", ContentFile(base64.b64decode(imgstr)))
                except Exception as e:
                    messages.warning(request, f"Failed to save facial image: {str(e)}")

            # Traiter l'audio (base64)
            voice_audio_data = request.POST.get('voice_recognition_audio')
            if voice_audio_data:
                try:
                    format, audiostr = voice_audio_data.split(';base64,')
                    ext = format.split('/')[-1]
                    user.voice_sample.save(f"{user.username}_voice.{ext}", ContentFile(base64.b64decode(audiostr)))
                except Exception as e:
                    messages.warning(request, f"Failed to save voice sample: {str(e)}")

            user.save()

            # Créer une entrée pour `Staf`
            Staf.objects.create(user=user)
            messages.info(request, 'Your account has been created successfully')
            return redirect('login')
        else:
            error_messages = [f"{field}: {error}" for field, errors in form.errors.items() for error in errors]
            messages.warning(request, "Errors: " + ", ".join(error_messages))
            return redirect('register-recruiter')
    else:
        form = RegisterUserForm()
    return render(request, 'users/register_recruiter.html', {'form': form})
    
    
    
#login a user

def login_user(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username= email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'error')
            return redirect('login')
    else:
        return render(request, 'users/login.html')
    
# logout a user
 
def logout_user(request):
    logout(request)
    messages.info(request,'logout successfully')
    return redirect('home')





#update profile
def update_profile(request, pk):
    user=User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your profile has been updated')
            return redirect('profile')
        else:
            print(form.errors)  # Affiche les erreurs dans la console
            messages.warning(request, 'Something went wrong. Please correct the errors below.')
            context = {'form': form}
            return render(request, 'users/update_profile.html', context)
    else:
        form = UpdateProfileForm(instance=user)
        context = {'form': form}
        return render(request, 'users/update_profile.html', context)




#change password

def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Your password has been changed')
            return redirect('profile')
        else:
            messages.warning(request,'Something went wrong.Please verify password')
            return redirect('change-password')
    else:
        form=PasswordChangeForm(request.user)
        context={'form':form}
        return render(request,'users/change_password.html',context)


#Profile

def profile(request):
    return render(request,'users/profile.html')