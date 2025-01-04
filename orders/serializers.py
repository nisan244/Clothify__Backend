from rest_framework import serializers
from .models import CartItem_Model, Order_Model, OrderItem_Model
from products.serializers import Product_Serializer


class CartItem_Serializer(serializers.ModelSerializer):
    product = Product_Serializer()
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = CartItem_Model
        fields = ['id', 'product', 'quantity', 'total_price']
    
    def get_total_price(self, obj):
        return obj.total_price()


class OrderItem_Serializer(serializers.ModelSerializer):
    product = Product_Serializer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem_Model
        fields = ['id', 'product', 'quantity', 'total_price']

    def get_total_price(self, obj):
        return obj.total_price()



class Order_Serializer(serializers.ModelSerializer):
    order_items = OrderItem_Serializer(many= True)

    class Meta:
        model = Order_Model
        fields = ['id', 'user', 'total_price', 'status', 'order_time', 'order_items']
        
        
