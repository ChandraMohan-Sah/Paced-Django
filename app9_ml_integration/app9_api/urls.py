from django.urls import path 
from .import views

urlpatterns = [
    path("", views.ML_integration, name="ml-integration")
]
