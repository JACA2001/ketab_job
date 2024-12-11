from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import ResumeForm
from .utils import extraire_donnees, generer_lettre_motivation
from job.models import Job 

def upload_resume(request, job_id):
    job = get_object_or_404(Job, pk=job_id)  # Récupérer l'emploi spécifique

    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()
            contenu_cv = extraire_donnees(resume.file.path)

            # Combine les informations du CV et les exigences du poste
            job_info = (
                f"Exigences du poste : {job.requirements}\n"
                f"Description du poste : {job.ideal_candidate}"
            )
            donnees_combinees = f"{contenu_cv}\n\n{job_info}"

            # Générer la lettre de motivation
            lettre_motivation = generer_lettre_motivation(donnees_combinees)

            # Retourner la réponse avec la lettre générée
            return HttpResponse(
                f"CV téléchargé avec succès et lettre de motivation générée :<br><br>{lettre_motivation.replace(chr(10), '<br>')}"
            )
    else:
        form = ResumeForm()

    return render(request, 'letter/upload_resume.html', {'form': form, 'job': job})
