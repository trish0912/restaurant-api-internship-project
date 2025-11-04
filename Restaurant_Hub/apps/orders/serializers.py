from rest_framework import serializers
from .models import Customer, Order, OrderItem
from apps.menu.models import MenuItem
from apps.menu.serializers import MenuItemSerializer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)
    menu_item_id = serializers.PrimaryKeyRelatedField(
        queryset=MenuItem.objects.all(), source='menu_item', write_only=True
    )

    class Meta:
        model = OrderItem
        fields = ('id', 'menu_item', 'menu_item_id', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    items = OrderItemSerializer(source='orderitem_set', many=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'items', 'status', 'created_at')

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        items_data = validated_data.pop('orderitem_set')

        # Get or create customer
        customer, _ = Customer.objects.get_or_create(**customer_data)
        order = Order.objects.create(customer=customer, **validated_data)

        # Create OrderItems
        for item in items_data:
            menu_item = item['menu_item']
            qty = item.get('quantity', 1)
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=qty)

        return order