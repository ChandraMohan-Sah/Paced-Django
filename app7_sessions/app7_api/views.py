from django.shortcuts import render, redirect
from django.contrib.auth import logout
from app7_sessions.models import SessionModel
from django.contrib.auth.decorators import login_required


data = [
    {   "id":1,
        "image_loc" : "app7_sessions/images/tray.png",
        "product" : "Tray"
    },{
        "id":2,
        "image_loc" : "app7_sessions/images/trolly.png",
         "product" : "Trolly"
    },{
        "id":3,
        "image_loc" : "app7_sessions/images/wash.png",
         "product" : "Wash"
    },{
        "id":4,
        "image_loc" : "app7_sessions/images/gloves.png",
         "product" : "Gloves"
    },

]
 

# Function-based view
def custom_logout_view(request):
    logout(request)  # Logs out the user
    return redirect('session-mgmt-app7')  # Redirect to a home page or any URL of your choice

def SessionMgmt(request):
    context = {
        "sidebar_content" : "Session Management",
        "data":data
    }
    return render(request, 'app7_sessions/session.html', context) 


def SingleProductDetail(request, pk):
    pass

def FavoriteProduct(request):
    pass 

