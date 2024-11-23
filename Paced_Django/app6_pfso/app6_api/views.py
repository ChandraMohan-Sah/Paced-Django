from django.core.paginator import Paginator
from django.shortcuts import render

# Define the dataset as a list of dictionaries
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
    # Paginate the dataset, showing 1 animal per page
    paginator = Paginator(dataset, 1)  # Show 1 animal per page
    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the current page object

    context = {
        "page_obj": page_obj,
        "sidebar_content": "Pagination, Searching, Filtering, Ordering"
    }

    return render(request, "app6_pfso/index.html", context)

def FSOApp6(request):
    context = {
        "sidebar_content": "Pagination, Searching, Filtering, Ordering"
    }
    return render(request, "app6_pfso/fso.html", context)  