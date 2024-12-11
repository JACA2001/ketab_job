from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Info
from users.models import User
from .form import UpdateInfoForm


def update_info(request):
    if request.user.is_applicant:
        info = Info.objects.get(user=request.user)
        if request.method == 'POST':
            form = UpdateInfoForm(request.POST, request.FILES, instance=info)
            if form.is_valid():
                var = form.save(commit=False)
                user = User.objects.get(pk=request.user.id)
                user.has_resume = True
                user.save()
                var.save()
                messages.info(request, 'Your info has been updated')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Something went wrong')
        else:
            form = UpdateInfoForm(instance=info)
        
        context = {'form': form}
        return render(request, 'info/update_info.html', context)
    else:
        messages.warning(request, 'Permission denied')
        return redirect('dashboard')

        


def info_details(request,pk):
    info=Info.objects.get(pk=pk)
    context={'info':info}
    return render(request, 'info/info_details.html' , context)
