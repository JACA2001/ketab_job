from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('<int:user_id>/', views.chat_view, name='chat_view'),
    path('message/<int:message_id>/', views.view_message, name='view_message'),
    path('inbox/', views.inbox, name='inbox'),
]
