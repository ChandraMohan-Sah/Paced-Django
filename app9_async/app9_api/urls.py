from django.urls import path 
from .import views
urlpatterns = [
    path("", views.OpenChat, name="async-app9")
]
