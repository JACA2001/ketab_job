from django.urls import path
from .import views

urlpatterns = [
    path('update-info/', views.update_info, name='update-info'),
    path('info-details/', views.info_details, name='info-details')
]
