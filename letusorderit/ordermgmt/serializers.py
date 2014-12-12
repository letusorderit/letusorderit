from rest_framework.serializers import ModelSerializer

from .models import Order, OrderItem


class OrderSerializer(ModelSerializer):

    class Meta():
        model = Order


class OrderItemSerializer(ModelSerializer):

    class Meta():
        model = OrderItem
