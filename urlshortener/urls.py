from django.urls import path
from urlshortener import views

urlpatterns = [
    path('',views.createShorturl,name='createShorturl'),
    path('list/',views.list,name='list'),
]