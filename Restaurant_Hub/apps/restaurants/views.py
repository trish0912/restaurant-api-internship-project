
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Restaurant



# Template views
def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {'restaurants': restaurants})

def restaurant_detail(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    return render(request, 'restaurants/restaurant_detail.html', {'restaurant': restaurant})