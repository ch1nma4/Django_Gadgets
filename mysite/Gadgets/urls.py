from django.urls import path
from Gadgets import views

urlpatterns = [
    path('home/',views.index , name='index'),
]
