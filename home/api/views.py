from django.shortcuts import render, redirect

# Create your views here.

cards = [
    {
        "topic": "Multipage Navigation",
        "icon": "🌐",
        "link": "monthlist"
    },
    {
        "topic": "Simple Form Submission",
        "icon": "📝",
        "link": "simple-form"
    },
    {
        "topic": "Contact Form [with SMTP]",
        "icon": "✉️",
        "link": "contact-post"
    },
    {
        "topic": "File Uploads",
        "icon": "📤",
        "link": "upload-app4"
    },
    {
        "topic": "Pagination, Filter, Search, Order",
        "icon": "🔍",
        "link": "landing-page-app6"
    },
    {
        "topic": "Capstone 1 : Portfolio ",
        "icon": "👨‍🎓",
        "link": "portfolio"
    },
    {
        "topic": "Authentication [2-types]",
        "icon": "🔐",
        "link": "landing-page-app8"
    },
    {
        "topic": "Session Management",
        "icon": "⏳",
        "link": "index-app7-capstone"
    },
    # {
    #     "topic": "Capstone 2 : PSC MCQ Helper",
    #     "icon": "👨‍🎓",
    #     "link": "mcq-helper"
    # },
    {
        "topic": "Payment Gateway",
        "icon": "➡️",
        "link": "payment-gateway"
    },
    {
        "topic": "DRF : IMDB Clone ",
        "icon": "🔗",
        "link": "imdb-clone-home"
    },
    {
        "topic": "ML Model Integration",
        "icon": "🚀",
        "link": "ml-integration"
    }
]



def home(request):
    context ={
        "cards":cards
    }
    return render(request, "base.html", context )

 

def capstone1(request):
    # portfolio site 
    return redirect("https://chandramohan.pythonanywhere.com/")


def capstone2(request):
    # portfolio site 
    return redirect("https://gkhelper.pythonanywhere.com/")
