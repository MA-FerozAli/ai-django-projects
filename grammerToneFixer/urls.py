from django.urls import path
from .views import GrammerView

urlpatterns=[
    path("",GrammerView,name='Grammer'),
]