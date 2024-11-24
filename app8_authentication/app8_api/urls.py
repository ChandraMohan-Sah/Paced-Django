from django.urls import path 
from .import views
from app8_authentication.forms import CustomRegistrationForm
from django.contrib.auth import views as auth_views
from app8_authentication.forms import CustomPasswordResetForm

#Google Auth
from .import google_auth

urlpatterns = [
    path("", views.LandingPage, name="landing-page-app8"),
    path("register/", views.register, name="register-app8"),
    path("delete-user/", views.deleteUsers, name="delete-all-users"),
    path("verify-email/", views.VerifyEmailTemplate, name="verify-email-app8"),

    #email varification
    path('verify-email/<uidb64>/<token>/', views.verify_email_view, name='verify-email'), 
    path('invalid-link/', views.Invalid_Link,  name="invalid-link"),
    path('resend-verification-email/', views.resend_verification_email,  name="resend_verification_email"),

    #Google Login
    path('login/google/', google_auth.google_login, name='google_login'),
    # path('complete/google/', google_auth.google_callback, name='google_callback'),


    path(
        'login-app8/',
        auth_views.LoginView.as_view(
            template_name='app8_authentication/login.html',
            extra_context={'sidebar_content': 'Authentication Demo'}
        ),
        name='login-app8'
    ),

    path(
        'logout-app8/pass/', 
        auth_views.LogoutView.as_view(
            template_name='app8_authentication/logout.html',
            extra_context={
                'sidebar_content': 'Authentication Demo',
                'message':"Logged Out"
            }
        ), 
        name='logout-app8'
    ),

    path('login-app8/after-login-app8/', views.afterLogin, name='after-login-app8'),



    #Reset Urls
    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name='app8_authentication/password_reset.html',
        form_class=CustomPasswordResetForm,
        extra_context={'sidebar_content': 'Authentication Demo'}
        ), 
        name="password_reset"
    ),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name='app8_authentication/password_reset_done.html',
        extra_context={'sidebar_content': 'Authentication Demo'}
        ), name="password_reset_done"),

    path("password_reset/<uidb64>/<token>/", 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='app8_authentication/password_reset_confirm.html',
             extra_context={'sidebar_content': 'Authentication Demo'}
         ), 
         name="password_reset_confirm"),

    path("password_reset/complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name='app8_authentication/password_reset_complete.html',
        extra_context={'sidebar_content': 'Authentication Demo'}
    ), name="password_reset_complete"),


]





