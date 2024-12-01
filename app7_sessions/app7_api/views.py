from django.shortcuts import render, redirect
from django.contrib.auth import logout
from app7_sessions.models import SessionModel
from django.contrib.auth.decorators import login_required


data = [
    {
        "image_loc" : "app7_sessions/images/tray.png",
        "product" : "Tray"
    },{
        "image_loc" : "app7_sessions/images/trolly.png",
         "product" : "Trolly"
    },{
        "image_loc" : "app7_sessions/images/wash.png",
         "product" : "Wash"
    },{
        "image_loc" : "app7_sessions/images/gloves.png",
         "product" : "GLoves"
    },

]


# Function-based view
def custom_logout_view(request):
    logout(request)  # Logs out the user
    return redirect('session-mgmt-app7')  # Redirect to a home page or any URL of your choice


@login_required
def PostData(request):
    if request.method == "POST":

        product_name = request.POST.get('product_name')  # This should match the name of the product field
        product_value = request.POST.get('product_value')  # This matches the name of the value field

        if product_name and product_value:
            # Get or create a SessionModel entry for the product
            session_item, created = SessionModel.objects.create(product=product_name)
            
            # Update the quantity field with the submitted value
            session_item.quantity = int(product_value)  # Convert the value to an integer

            # Save the updated session item to the database
            session_item.save()

            print(f"Saved {session_item.product} with quantity {session_item.quantity}")
        else:
            print("Product name or value not found")

    # Render the template after processing the POST request
    return render(request, 'app7_sessions/session.html')



def SessionMgmt(request):
    context = {
        "sidebar_content" : "Session Management",
        "data":data
    }
    return render(request, 'app7_sessions/session.html', context) 