from django.shortcuts import render

# Create your views here.

'''Actually these data should come from DATABASE'''
month_detail = {
    "january": "This month is January !",
    "february": "This month is February !",
    "march": "This month is March !",
    "april": "This month is april !",
    "may": "This month is may!",
    "june": "This month is june !",
    "july": "This month is July",
    "august": "This month is august",
    "september":"This month is september",
    "october":"This month is october",
    "november":"Thsi month is november",
    "december":"This mointh is december"
}

month_activity = {
    "january": "football",
    "february": "Baseball",
    "march": "Cricket",
    "april": "Badminton",
    "may": "Calisthenics",
    "june": "Swimming",
    "july": "Tennis Ball",
    "august": "Gymming",
    "september":"Volleyball",
    "october":"Tug of War",
    "november":"Hide and Seek",
    "december":"Karate"
}

 
def home1(request):
    month_list = list(month_detail.keys())
    context = {
        "months":month_list
    }
    '''A lot of work is done on 1homepage.html'''
    return render(request, "app1_static_nav/1homepage.html", context)


def month_detail_By_String(request, month):
    detail = month_detail[month]
    context ={
        "month":month,
        "detail": detail
    }
    '''A lot of work is done in 2detail_monthpage.html'''
    return render(request, "app1_static_nav/2detail_monthpage.html", context)


def favourite_month_activity_By_Str(request, month):
    activity_name = month_activity[month]
    context = {
        "activity" : activity_name,
        "month":month
    }
    return render(request, "app1_static_nav/3all_activity.html", context)
