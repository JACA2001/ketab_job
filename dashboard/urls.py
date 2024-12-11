from django.urls import path
from . import views

urlpatterns = [
   path('', views.dashboard, name='dashboard'),
    # Pour les recruteurs
    path('recruiter/cvs/', views.recruiter_cvs, name='recruiter-cvs'),

    # Pour les candidats
    path('recommended-jobs/', views.recommended_jobs, name='recommended-jobs'),
   #  path('letters-table/', views.letters_table, name='letters-table'),
   
]
