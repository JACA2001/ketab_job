from django.shortcuts import render,redirect
from django.contrib import messages
from .form import UpdateStafForm
from users.models import User
from staf.models import Staf



# Update Staf

def update_staf(request):
    if request.user.is_recruiter:
        staf = Staf.objects.get(user=request.user)
        if request.method == 'POST':
            form = UpdateStafForm(request.POST, instance=staf)
            if form.is_valid():
                var = form.save(commit=False)
                user = User.objects.get(id=request.user.id)
                user.has_company = True
                var.save()
                user.save()
                messages.info(request, 'Your company is created, now you can start creating job')
                return redirect('dashboard')
            else:
                print("Form errors:", form.errors) 
                messages.warning(request, 'Something went wrong')
        else:
            form = UpdateStafForm(instance=staf)
        context = {'form': form}
        return render(request, 'staf/update_staf.html', context)
    else:
        messages.warning(request, 'Permission denied')
        return redirect('dashboard')

    
        
        
        
#staf details
        
def staf_details(request,pk):
    staf= Staf.objects.get(pk=pk)
    context= {'staf':staf}
    return render(request, 'staf/staf_details.html', context)