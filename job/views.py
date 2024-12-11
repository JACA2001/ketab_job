from django.shortcuts import render,redirect
from django.contrib import messages
from .form import  CreateJobForm,UpdateJobForm
from .models import Job,Apply
from info.models import Info



def create_job(request):
    if request.user.is_recruiter and request.user.has_company:
        if request.method == 'POST':
            form = CreateJobForm(request.POST)
            if form.is_valid():
                var = form.save(commit=False)
                if hasattr(request.user, 'staf'):
                    var.user = request.user
                    var.staf = request.user.staf
                    var.save()
                    messages.info(request, 'New job has been created')
                    return redirect('dashboard')
                else:
                    messages.warning(request, 'No staf associated with the user.')
                    return render(request, 'job/create_job.html', {'form': form})
            else:
                print("Form errors:", form.errors)  # Affiche les erreurs du formulaire
                messages.warning(request, 'Something went wrong')
                return render(request, 'job/create_job.html', {'form': form})
        else:
            form = CreateJobForm()
            return render(request, 'job/create_job.html', {'form': form})
    else:
        messages.warning(request, 'Permission denied')
        return redirect('dashboard')


    
def update_job(request, pk):
    job=Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateJobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your job has been updated')
            return redirect('dashboard')
        else:
            print(form.errors)  # Affiche les erreurs dans la console
            messages.warning(request, 'Something went wrong. Please correct the errors below.')
            context = {'form': form}
            return render(request, 'job/update_job.html', context)
    else:
        form = UpdateJobForm(instance=job)
        context = {'form': form}
        return render(request, 'job/update_job.html', context)



def manage_jobs(request):
    jobs=Job.objects.filter(user=request.user, staf=request.user.staf)
    context={'jobs':jobs}
    return render(request, 'job/manage_jobs.html', context)

    
    
    
   

def apply_job(request, pk):
    if request.user.is_authenticated and request.user.is_applicant:
        if not request.user.has_resume:
            messages.warning(request, 'Please upload your resume before applying for jobs.')
            return redirect('dashboard')
        job=Job.objects.get(pk=pk)
        if Apply.objects.filter(user=request.user, job=job).exists():
            messages.warning(request, 'You have already applied for this job.')
            return redirect('dashboard')
        else:
            
            Apply.objects.create(
                job=job,
                user=request.user,
                status='Pending'
            )
            messages.success(request, 'You have successfully applied for this job.')
            return redirect('dashboard')
    else:
        
        messages.info(request, 'Please log in to apply for jobs.')
        return redirect('login')



# def all_applicants(request, pk):
#     job=Job.objects.get(pk=pk)
#     applicants=job.apply_set.all()
#     context={'job':job,'applicants':applicants}
#     return render(request,'job/all_applicants.html',context)



def  applied_details(request):
    jobs = Apply.objects.filter(user=request.user)
    context={'jobs':jobs}
    return render(request,'job/applied_details.html',context)
    

def all_applicants(request, pk):
    job = get_object_or_404(Job, pk=pk)
    applicants = Apply.objects.filter(job=job)
    print(applicants)  # Vérifiez ici que les données sont correctes
    context = {'job': job, 'applicants': applicants}
    return render(request, 'job/all_applicants.html', context)




def update_application_status(request, application_id, status):
    # Vérifiez si le statut est valide
    if status not in ['Accepted', 'Rejected']:
        messages.error(request, "Statut invalide.")
        return redirect('manage-jobs')

    # Récupérez la candidature
    application = get_object_or_404(Apply, pk=application_id)

    # Mettez à jour le statut
    application.status = status
    application.save()

    # Ajoutez un message de confirmation
    messages.success(request, f"Le statut de la candidature de {application.user.username} a été mis à jour : {status}.")
    return redirect('manage-jobs')


    





from .utils import calculate_candidate_score
from django.shortcuts import render, get_object_or_404




    

def ranked_candidates_view(request, pk):
    job = Job.objects.get(pk=pk)
    applicants = Apply.objects.filter(job=job)  # Filtrer les candidatures pour le job donné

    # Calculer le score pour chaque candidat en fonction des compétences
    ranked_applicants = []
    for apply in applicants:
        candidate = apply.user  # Utilisez le champ `user` comme candidat
        # Supposons que les compétences du candidat sont dans le modèle `Info`
        candidate_info = Info.objects.get(user=candidate)  # Récupérer les informations du candidat
        candidate_skills = set(candidate_info.skills.lower().split(', ')) if candidate_info.skills else set()
        job_skills = set(job.skills_required.lower().split(', ')) if job.skills_required else set()

        # Calcul du score : intersection entre les compétences requises du job et celles du candidat
        score = len(candidate_skills.intersection(job_skills))

        ranked_applicants.append({
            'candidate': candidate_info,
            'score': score,
        })

    # Trier les candidats par score décroissant
    ranked_applicants = sorted(ranked_applicants, key=lambda x: x['score'], reverse=True)

    context = {
        'job': job,
        'ranked_applicants': ranked_applicants,
    }
    return render(request, 'job/ranked_candidates.html', context)
