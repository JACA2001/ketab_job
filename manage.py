#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ketab.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    
    
    
    
# import json
# from job.models import Job
# from info.models import Info

# # Convertir les compétences des Jobs
# for job in Job.objects.all():
#     if isinstance(job.skills_required, str):  # Vérifier si c'est une chaîne
#         try:
#             job.skills_required = json.loads(job.skills_required)  # Convertir en JSON
#             job.save()
#         except json.JSONDecodeError:
#             print(f"Erreur de conversion pour le Job ID: {job.id}")

# # Convertir les compétences des Candidats
# for candidate in Info.objects.all():
#     if isinstance(candidate.skills, str):  # Vérifier si c'est une chaîne
#         try:
#             candidate.skills = json.loads(candidate.skills)  # Convertir en JSON
#             candidate.save()
#         except json.JSONDecodeError:
#             print(f"Erreur de conversion pour le candidat ID: {candidate.id}")



if __name__ == '__main__':
    main()
