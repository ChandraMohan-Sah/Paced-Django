from django.urls import path 
from .import views

urlpatterns = [
    path("monthlist/", views.home1, name="monthlist"),
    path("monthDetail/<str:month>/", views.month_detail_By_String, name="month-detail"),
    path("activity_of_month/<str:month>/", views.favourite_month_activity_By_Str, name="month-activity")
]


