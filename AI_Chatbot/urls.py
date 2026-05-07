from django.urls import path
from .views import ChatView,clear_chat
urlpatterns=[
    path('',ChatView,name='chat-view'),
    path('clear_chat/',clear_chat,name='clear-chat')
]