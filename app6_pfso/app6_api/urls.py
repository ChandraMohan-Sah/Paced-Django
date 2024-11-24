from django.urls import path 
from .import views

urlpatterns = [
    path("", views.LandingPageApp6, name="landing-page-app6"),
    path("all-data/", views.AllData, name="fso-all-app6"),
    path("filter-data/", views.FilteredData, name="fso-filter-app6"),
    path("search_by_animal/", views.SearchByAnimalName, name="search-app6"),
    path("ordering/", views.OrderingByZommId, name="ordering-app6")
]



