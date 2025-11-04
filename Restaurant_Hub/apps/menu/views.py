from django.shortcuts import render, get_object_or_404
from apps.restaurants.models import Restaurant
from .models import MenuItem

def menu_list(request, restaurant_slug=None):
    q = request.GET.get('q')
    if restaurant_slug:
        restaurant = get_object_or_404(Restaurant, slug=restaurant_slug)
        items = restaurant.menu_items.filter(available=True)
    else:
        restaurant = None
        items = MenuItem.objects.filter(available=True)
    if q:
        items = items.filter(name__icontains=q)
    return render(request, 'menu/menu_list.html', {'items': items, 'q': q, 'restaurant': restaurant})
