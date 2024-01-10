from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.apps import UsersConfig
from users.views import *

app_name = UsersConfig

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('email-confirmation-sent/', EmailConfirmationSentView.as_view(), name='email_confirmation_sent'),
    path('activate-user/<str:token>/', VerifyEmailView.as_view(), name='activate_user'),
    path('email-confirmed/', EmailConfirmedView.as_view(), name='email_confirmed'),
    path('confirm-email-failed/', EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),
    path('password-reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('password-reset-sent/', PasswordResetSentView.as_view(), name='password-reset-sent'),
    path('<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password')
]