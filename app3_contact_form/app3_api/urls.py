from django.urls import path 
from .import views

urlpatterns = [
    path("contact_post/", views.contactPOST, name = "contact-post"),
    path("thank-you/", views.ThankYou, name="thank-you-app3")
]
