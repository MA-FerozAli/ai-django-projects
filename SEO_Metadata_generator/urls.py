from django.urls import path
from . import views
urlpatterns = [
    path('',views.seo_generator,name='seo_generator'),
]