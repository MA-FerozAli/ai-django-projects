from django.urls import path
from .views import generate_outline,blog_result,write_full_post,outline_details

urlpatterns =[
    path('outline/',generate_outline,name='outline'),
    path('outline-details/<int:pk>/',outline_details,name='outline-details'),
    path('full-post/<int:pk>/',write_full_post,name='full_post'),
    path('blog_result/<int:pk>/',blog_result,name='blog_result'),
]
