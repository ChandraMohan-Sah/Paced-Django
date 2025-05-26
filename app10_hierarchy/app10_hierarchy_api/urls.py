from django.urls import path 
from .import views

urlpatterns = [
    path("", views.hierarchy, name="hierarchy")
]
 