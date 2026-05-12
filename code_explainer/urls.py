from django.urls import path
from .views import code_explainer

urlpatterns=[
    path('',code_explainer,name='code_explainer'),
]