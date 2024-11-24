from django.shortcuts import render

# Create your views here.

cards = [
    {
        "topic": "Multipage Navigation",
        "icon": "🌐",
        "link": "monthlist"
    },
    {
        "topic": "Simple Form [3-types]",
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
        "topic": "Capstone 1 [Simple Blog]",
        "icon": "👨‍🎓",
        "link": "home"
    },
    {
        "topic": "Authentication [2-types]",
        "icon": "🔐",
        "link": "landing-page-app8"
    },
    {
        "topic": "Session Management",
        "icon": "⏳",
        "link": "home"
    },
    {
        "topic": "Capstone 2 [ToDo App]",
        "icon": "👨‍🎓",
        "link": "home"
    },
    {
        "topic": "Web Sockets: Async Comm",
        "icon": "📡",
        "link": "home"
    },
    {
        "topic": "Payment Gateway",
        "icon": "➡️",
        "link": "home"
    },
    {
        "topic": "Capstone 3 [E-Commerce]",
        "icon": "👨‍🎓",
        "link": "home"
    },
    {
    "topic": "Model Deployment",
    "icon": "🚀",
    "link": "deploy-model"
    }
]



def home(request):
    context ={
        "cards":cards
    }
    return render(request, "base.html", context )

