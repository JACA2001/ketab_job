from django.shortcuts import render
from job.models import Job,Apply
from .filter import JobFilter

def home(request):
    filter = JobFilter(request.GET, queryset=Job.objects.filter(is_available=True).order_by('-timestamp'))
    is_searching = any(param for param in request.GET.values())
    
    # Limiter à 3 emplois par défaut
    jobs = Job.objects.filter(is_available=True).order_by('-timestamp')[:3]

    context = {
        'filter': filter,
        'jobs': jobs,
        'is_searching': is_searching,  # Indique si une recherche est en cours
    }
    return render(request, 'website/home.html', context)

def Job_list(request):
    jobs=Job.objects.filter(is_available=True).order_by('-timestamp')
    context={'jobs':jobs}
    return render(request,'website/job_list.html',context)


def job_details(request,pk):
    job= Job.objects.get(pk=pk)
    
    if request.user.is_authenticated:
        has_applied = Apply.objects.filter(user=request.user, job=job).exists()
    else:
        has_applied = False
  
    context={'job':job, 'has_applied':has_applied}
    return render(request,'website/job_details.html', context)