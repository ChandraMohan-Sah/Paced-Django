from django.shortcuts import render

# Create your views here.

def hierarchy(request):
    context ={
        "sidebar_content": "Django Setup + Hierarchy in Depth "
    }
    return render(request, "app10_hierarchy/hierarchy.html", context)


