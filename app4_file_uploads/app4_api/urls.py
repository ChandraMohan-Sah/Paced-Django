from django.urls import path 
from .views import  CreateUploadView
from .import views

urlpatterns = [
    path("upload/", CreateUploadView.as_view(), name="upload-app4"),
    path("delete/", views.DeleteImages_and_Files , name="delete-all-uploads"),
    path("thank-you-page-app4/", views.ThankYou, name="thank-you-app4")

]
