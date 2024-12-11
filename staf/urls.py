from django.urls import path
from . import views



urlpatterns = [
    path('update-staf/', views.update_staf, name='update-staf'),
    path('staf-details/<int:pk>/',views.staf_details, name= 'staf-details'),
    
]
