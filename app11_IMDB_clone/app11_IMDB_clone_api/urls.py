from django.urls import path 
from .import views

urlpatterns = [
    path("", views.imdb_clone_home, name="imdb-clone-home")
]
