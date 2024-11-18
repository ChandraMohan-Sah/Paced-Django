from django.shortcuts import render

# Create your views here.

cards = [
    {
        "topic": "Multipage Navigation",
        "icon": "🌐",
        "link": "multipage-navigation"
    },
    {
        "topic": "Simple Form [3-types]",
        "icon": "📝",
        "link": "home"
    },
    {
        "topic": "Contact Form [with SMTP]",
        "icon": "✉️",
        "link": "home"
    },
    {
        "topic": "File Uploads",
        "icon": "📤",
        "link": "home"
    },
    {
        "topic": "CRUD Operation",
        "icon": "💾",
        "link": "home"
    },
    {
        "topic": "Pagination",
        "icon": "➡️",
        "link": "home"
    },
    {
        "topic": "Filter, Search, Order",
        "icon": "🔍",
        "link": "home"
    },
    {
        "topic": "Session Management",
        "icon": "⏳",
        "link": "home"
    },
    {
        "topic": "Authentication [5-types]",
        "icon": "🔐",
        "link": "home"
    },
    {
        "topic": "Web Sockets",
        "icon": "📡",
        "link": "home"
    }
]



def home(request):
    context ={
        "cards":cards
    }
    return render(request, "base.html", context )

