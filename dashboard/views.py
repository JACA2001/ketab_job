from django.shortcuts import render, redirect
from info.models import Info
from job.models import Job
from job.utils import match_jobs_to_candidate
import openai


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


def recruiter_cvs(request):
    if request.user.is_recruiter:
        # Récupérer tous les CVs ayant un fichier associé
        cvs = Info.objects.exclude(upload_cv="")  # Exclut les CVs sans fichier

        # Filtrer par recherche si nécessaire
        search_query = request.GET.get('search', '')
        if search_query:
            cvs = cvs.filter(skills__icontains=search_query)

        # Classer les CVs par pertinence
        ranked_cvs = sorted(cvs, key=lambda cv: cv.skills or "", reverse=True)

        return render(request, 'dashboard/recruiter_cvs.html', {'cvs': ranked_cvs})
    else:
        return redirect('login')


def recommended_jobs(request):
    if request.user.is_applicant:
        info = Info.objects.get(user=request.user)
        recommended_jobs = []

        for job in Job.objects.filter(is_available=True):
            match_score = match_jobs_to_candidate(info.skills, job.skills_required)
            if match_score > 0.5:  # Seuil de pertinence
                recommended_jobs.append((job, match_score))

        # Classer les offres par pertinence
        recommended_jobs = sorted(recommended_jobs, key=lambda x: x[1], reverse=True)

        return render(request, 'dashboard/recommended_jobs.html', {'recommended_jobs': recommended_jobs})
    else:
        return redirect('login')
    
    


