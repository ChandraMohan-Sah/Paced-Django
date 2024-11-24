from django.urls import path 
from .import views

urlpatterns = [
    path("", views.SessionMgmt, name="session-mgmt-app7")
]
