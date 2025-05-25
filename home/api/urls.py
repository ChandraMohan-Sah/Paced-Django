from django.urls import path 
from .import views


urlpatterns = [
    path("", views.home, name="home"),
    path("/portfolio", views.capstone1, name="portfolio")
    
]
