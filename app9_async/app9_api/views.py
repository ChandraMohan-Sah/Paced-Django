from django.shortcuts import render, redirect
from channels.layers import get_channel_layer 
from asgiref.sync import async_to_sync
from django.contrib.auth import logout
from django.contrib.auth.models import User

def ChatHome(request):
    if request.user.is_authenticated:  
        users = User.objects.all()

    context ={
        "sidebar_content":"Async Communication",
        "users":users
    }

    return render(request, "app9_async/chathome.html", context)


def ChatWithPeople(request, user_id):
    if request.user.is_authenticated:  
        all_users = User.objects.all()
        particular_user = User.objects.get(id = user_id)
        me = request.user

    context ={
        "sidebar_content":"Async Communication",
        "all_users":all_users,
        "particular_user":particular_user,
        "me":me
    }  

    return render(request, "app9_async/chat.html", context)


def custom_logout_view(request):
    logout(request)  # Logs out the user
    return redirect('async-app9')  # Redirect to a home page or any URL of your choice
