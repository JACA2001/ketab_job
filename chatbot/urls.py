from django.urls import path
from . import views# Assurez-vous d'importer la vue home

urlpatterns = [
     path('chatbot/', views.chatbot, name='Chatbot'),  # Route pour la vue home
]
