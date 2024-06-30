from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="flashcards-home"),
    path('add-flashcard/', views.add_flashcard, name="flashcards-add"),
]