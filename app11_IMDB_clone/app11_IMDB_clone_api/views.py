from django.shortcuts import render

# Create your views here.

def imdb_clone_home(request):
    context = {
        "sidebar_content": "IMDB Clone Demo",
    }
    return render(request, "app11_IMDB_clone/imdb_clone_home.html", context)

