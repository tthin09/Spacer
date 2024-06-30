from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "flashcards/home.html")

def add_flashcard(request):
    return render(request, "flashcards/add_flashcard.html")