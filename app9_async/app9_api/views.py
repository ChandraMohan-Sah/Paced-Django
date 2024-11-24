from django.shortcuts import render

# Create your views here.

def OpenChat(request):
    context ={
        "sidebar_content":"Async Communication"
    }
    return render(request, "app9_async/openchat.html", context)