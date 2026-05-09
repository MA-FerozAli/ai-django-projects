from django.urls import path
from .views import Resume_Matcher_View

urlpatterns =[
    path('',Resume_Matcher_View,name='resume-matcher'),
]