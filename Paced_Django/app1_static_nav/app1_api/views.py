from django.shortcuts import render

# Create your views here.

def MultiPageNav(request):
    return render(request, "app1_static_nav/page1.html")