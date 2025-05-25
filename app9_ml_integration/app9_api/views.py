from django.shortcuts import render, redirect


def ML_integration(request):
    context = {
        "sidebar_content": "Video Demo on ML Model Integration"
    }
    return render(request, "app9_api/iframe.html", context)
