from django.urls import path
from .views import dictionary_view
urlpatterns=[
    path('',dictionary_view,name='Dicitonary'),
]