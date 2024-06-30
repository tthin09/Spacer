from django.shortcuts import render
from .models import Post

posts = [
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "date_posted": "August 1, 1988",
    },
    {
        "title": "Garden of Words",
        "author": "Shinkai Makoto",
        "date_posted": "September 4, 2013",
    },
]

# Create your views here.
def home(request):
    context = {
        "posts": Post.objects.all(),
        "title": "Home Page",
    }
    return render(request, "blog/home.html", context)

def about(request):
    context = {
        "posts": posts[::-1],
        "title": "My About Page",
    }
    return render(request, "blog/about.html", context)