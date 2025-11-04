from django.db import models
from apps.restaurants.models import Restaurant
from django.contrib.auth.models import User

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
    related_name='menu_items')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='menuitem', null=True, blank=True)


def __str__(self):
    return f"{self.name} — {self.restaurant.name}"
