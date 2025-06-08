from django.shortcuts import render

# Create your views here.
def payment_gateway(request):
    context = {
        "sidebar_content": "Payment Gateway",
    }
    return render(request, "app12_payment_gateway/payment_gateway.html", context )

    