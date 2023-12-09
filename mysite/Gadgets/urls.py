from django.urls import path
from Gadgets import views

app_name = 'Gadgets'

urlpatterns = [
    path('home/',views.index , name='index'),
    path('detail/<int:item_id>/',views.detail , name='detail'),
    path('allproduct/', views.allproduct , name = 'allproduct'),
    path('add/',views.create_item , name='create_item'),
    path('update/<int:id>/', views.update_item , name = 'update_item'),
    path('delete/<int:id>/', views.delete_item , name='delete_item'),
    path('category/<str:val>/',views.category, name='category'),
]
