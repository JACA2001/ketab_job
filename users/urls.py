from django.urls import path
from . import views
from django.contrib.auth import views as auth_views





urlpatterns = [
    path('register-applicant/', views.register_applicant,name='register-applicant'),
    path('register-recruiter/', views.register_recruiter,name='register-recruiter'),
    path('login/', views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('update-profile/<int:pk>/',views.update_profile, name='update-profile'),
    path('change-password/',views.change_password,name='change-password'),
    path('profile/',views.profile,name='profile'),
    
    
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password-reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    
   
]



