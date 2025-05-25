from django.core.paginator import Paginator
from django.shortcuts import render
from app6_pfso.models import TableData

# For Pagination Content
dataset = [
        {
        "name": "Tiger",
        "description": "The tiger is a majestic and powerful carnivorous feline, recognized for its distinctive orange coat with black stripes. It is native to Asia and is known for its strength, solitary nature, and as one of the apex predators in its habitat.",
        "image": "app6_pfso/images/tiger.png"
    },
    {
        "name": "Turtle",
        "description": "A turtle is a reptile with a hard shell that protects its body and lives in water or on land.",
        "image": "app6_pfso/images/turtle.png"
    },
    {
        "name": "Monkey",
        "description": "Monkeys are intelligent primates known for their social behavior, dexterity, and ability to use tools. They are often characterized by their playful nature, and they can be found in various habitats, from jungles to savannas.",
        "image": "app6_pfso/images/monkey.png"
    },
]


def LandingPageApp6(request):
    paginator = Paginator(dataset, 1)  # Show 1 animal per page
    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the current page object

    context = {
        "page_obj": page_obj,
        "sidebar_content": "Pagination, Searching, Filtering, Ordering"
    }
    return render(request, "app6_pfso/index.html", context)



'''--------------------Fetch all data when page loads------------------------'''
def AllData(request):
    tableDatas = TableData.objects.all()

    context = {
        "sidebar_content": "Pagination, Searching, Filtering, Ordering",
        "tableDatas" : tableDatas
    }
    return render(request, "app6_pfso/fso.html", context)     



'''--------------------Filtering the Data based on name="zoomId" form frontent ------------------------'''
# When zoomId exceeds max value then starts fetching all data
# Remedy : Use Max Function

from django.db.models import Max

def FilteredData(request):
    zoom_id = int(request.GET.get('zoomId', None))  # Default to None if zoomId is not present
    max_zoom_id = int(TableData.objects.aggregate(Max('zoom_id'))['zoom_id__max'])
    reached_max_value = False

    if zoom_id:
        zoom_id = int(zoom_id)  
        if zoom_id > max_zoom_id:
            zoom_id = max_zoom_id  
            reached_max_value = True

    tableDatas = TableData.objects.all()
    
    if zoom_id:
        tableDatas = TableData.objects.filter(zoom_id__gte=zoom_id)  # use gte not gt;

    context = {
        "sidebar_content": "Pagination, Searching, Filtering, Ordering",
        "tableDatas": tableDatas,
        "zoom_id": zoom_id,
        "reached_max_value": reached_max_value,
    }
    print(f"Filtering with zoom_id: {zoom_id}")
    return render(request, "app6_pfso/fso.html", context)



'''--------------------Searching the Data by animal name------------------------'''
from django.db.models import Q

def SearchByAnimalName(request):
    search_query = request.GET.get('search', '')  # Get the search query from the request
    tableDatas = TableData.objects.all()
    
    if search_query:
        tableDatas = tableDatas.filter(Q(animal__icontains=search_query))  # Case-insensitive search

    context = {
        "sidebar_content": "Searching by Animal Name",
        "tableDatas": tableDatas,
        "search_query": search_query,
    }
    return render(request, "app6_pfso/fso.html", context)




'''---------------------Ordering the Data  by zoom_id (from database)----------------------------'''

def OrderingByZommId(request):
    order_direction = request.GET.get('order_direction', 'asc')  # Default to ascending order
    tableDatas = TableData.objects.all()

    if order_direction == 'desc':
        tableDatas = tableDatas.order_by('-zoom_id')  # descending
    else:
        tableDatas = tableDatas.order_by('zoom_id')  # ascending

    context = {
        "sidebar_content": "Searching and Ordering by Animal Name",
        "tableDatas": tableDatas,
        "order_direction": order_direction,
    }
    return render(request, "app6_pfso/fso.html", context)
