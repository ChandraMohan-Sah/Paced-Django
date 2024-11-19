from django.shortcuts import render, redirect
from app2_simple_form.forms import ReviewForm
from app2_simple_form.models import Review

#POST Request
def SimpleFormHome(request):
    form = None
    if request.method == "POST":
        form = ReviewForm(request.POST)

        #Count Objects in database first
        if Review.objects.count() >= 5:
            message = "Database Full -First Delete Previous Reviews"
            #GET Preious Reviews
            reviews = Review.objects.all() 
            context = {
                "sidebar_content": "Simple Form Demo",
                "message": message,
                "form_data":ReviewForm(),
                "reviews":reviews
            }
            return render(request, "app2_simple_form/page0.html", context)


        if form.is_valid():
            form.save()
            print("Form Submitted Successfully")
            return redirect("thank-you-app2")
        else:
            form = ReviewForm()

    #GET Request
    reviews = Review.objects.all() 
    context = {
        "sidebar_content": "Simple Form Demo",
        "form_data":ReviewForm(),
        "reviews":reviews
    }
    return render(request, "app2_simple_form/page0.html", context)



def DeleteSimpleForm(request):
    reviews = Review.objects.all().delete()
    return redirect("simple-form")


def ThankYou(request):
    context = {
        "sidebar_content": "Simple Form Demo",
    }
    return render(request, "app2_simple_form/thank-you.html", context)









