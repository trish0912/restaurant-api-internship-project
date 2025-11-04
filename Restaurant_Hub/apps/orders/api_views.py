from rest_framework import viewsets, permissions
from .models import Order, Customer, OrderItem
from .serializers import OrderSerializer, CustomerSerializer, OrderItemSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Customer.objects.filter(user=self.request.user)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Show only the logged-in user's orders
        return Order.objects.filter(customer__user=self.request.user)

    def perform_create(self, serializer):
        customer = self.request.user.customer
        serializer.save(customer=customer)
