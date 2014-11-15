from rest_framework.viewsets import ModelViewSet

from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer


class OrderViewSet(ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(ModelViewSet):

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
