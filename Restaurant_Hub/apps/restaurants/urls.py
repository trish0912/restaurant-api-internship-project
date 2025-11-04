from django.urls import path
from .views import home, restaurant_detail

urlpatterns = [
    path('', home, name='home'),
    path('<slug:slug>/', restaurant_detail, name='restaurant_detail'),
]
