from django.urls import path 
from .import views


#Google Auth
from .import google_auth_app7
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.SessionMgmt, name="session-mgmt-app7"),
    path('login/google/', google_auth_app7.google_login, name='google_login-app7'),
    path('logout-app7/pass/', views.custom_logout_view, name='logout-app7' ),
    
]
 

