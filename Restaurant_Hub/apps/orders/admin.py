from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer, Order, OrderItem


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # show one empty row for adding new items
    autocomplete_fields = ['menu_item']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer__name',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    inlines = [OrderItemInline]  # display order items inline


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'menu_item', 'quantity')
    search_fields = ('order__customer__name', 'menu_item__name')
