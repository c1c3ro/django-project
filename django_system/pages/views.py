from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    my_context = {
        "title": "This is my h1 title, did you like it?",
        "paragraph": "This is my paragraph, it came from the context, how awesome is that?",
        "my_items": ['apple', "banana", 'mango', 'pie', "eggs", 'delicious', 'fruit']
    }

    

    return render(request, "home.html", my_context)