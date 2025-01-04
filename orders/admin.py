from django.contrib import admin
from . models import CartItem_Model, Order_Model, OrderItem_Model

# Register your models here.


admin.site.register(CartItem_Model)
admin.site.register(Order_Model)
admin.site.register(OrderItem_Model)
