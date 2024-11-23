from django.urls import path 
from .import views

urlpatterns = [
    path("", views.LandingPageApp6, name="landing-page-app6"),
    path("fso-app6/", views.FSOApp6, name="fso-app6")
]
