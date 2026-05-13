from django.urls import path
from .views import fact_create,fact_list,fact_delete,fact_update,ask_question
urlpatterns=[
    path('',fact_list,name='list'),
    path('create/',fact_create,name='create'),
    path('update/<int:pk>',fact_update,name='update'),
    path('delete/<int:pk>',fact_delete,name='delete'),
    path('ask/',ask_question,name='ask_question')
]