from django.urls import path
from .views import menu_list

urlpatterns = [
    path('', menu_list, name='menu_list'),
    path('<slug:restaurant_slug>/', menu_list, name='restaurant_menu'),
]
