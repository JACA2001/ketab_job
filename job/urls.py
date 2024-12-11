from django.urls import path
from .import views

urlpatterns = [
    path('create-job/', views.create_job, name='create-job'),
    path('update-job/<int:pk>/', views.update_job, name='update-job'),
    path('manage-jobs/', views.manage_jobs, name='manage-jobs'),
    path('apply-job/<int:pk>/',views.apply_job,name='apply-job'),
    path('all-applicants/<int:pk>/',views.all_applicants,name='all-applicants'),
    path('applied-details/',views.applied_details,name='applied-details'),
    path('jobs/<int:pk>/candidates/', views.ranked_candidates_view, name='ranked_candidates'),
    path('application/<int:application_id>/<str:status>/', views.update_application_status, name='update_application_status'),
]
