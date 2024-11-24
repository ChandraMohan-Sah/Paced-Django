from django.shortcuts import render

# Create your views here.
def SessionMgmt(request):
    context = {
        "sidebar_content" : "Session Management",
    }
    return render(request, 'app7_sessions/session.html', context)