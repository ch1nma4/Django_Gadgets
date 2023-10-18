from django.urls import path
from Gadgets import views

app_name = 'Gadgets'

urlpatterns = [
    path('home/',views.index , name='index'),
    path('detail/<int:item_id>/',views.detail , name='detail'),
]
