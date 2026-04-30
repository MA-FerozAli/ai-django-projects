from django.urls import path
from .views import joke_view

urlpatterns = [
    path('',joke_view,name="Joke"),
]