from django.urls import path 
from .import views 

urlpatterns = [
    path("simplform/", views.SimpleFormHome, name="simple-form"),
    path("thank-you-simple-form/", views.ThankYou, name="thank-you-app2"),
    path("delete/", views.DeleteSimpleForm, name="delete-all")
]



