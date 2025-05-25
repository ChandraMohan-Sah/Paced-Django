from django.urls import path 
from .import views

#Google Auth
from .import google_auth_app9
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.ChatHome, name="async-app9"),
    path("chat_with_user/<int:user_id>/", views.ChatWithPeople, name="chat-with-people-app9"),
    path('login-app9/google/', google_auth_app9.APP9_google_login, name='google_login-app9'),
    path('logout-app9/pass/', views.custom_logout_view, name='logout-app9' ),
]

