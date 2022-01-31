from django.urls import path
from .views import main_page, laptop_detail, create_laptop

urlpatterns = [
    path('', main_page, name='main_page'),
    path('laptop-detail/<int:pk>/', laptop_detail, name='laptop_detail'),
    path('create-laptop/', create_laptop, name='create_laptop'),
]