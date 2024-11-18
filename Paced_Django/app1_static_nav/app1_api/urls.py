from django.urls import path 
from .import views

urlpatterns = [
    path("", views.MultiPageNav, name="multipage-navigation")
]
