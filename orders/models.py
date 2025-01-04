from django.db import models
from django.contrib.auth.models import User
from products.models import Product_Model

# Create your models here.

STATUS_CHOICES = [
    ("Pending", "Pending"),
    ("Completed", "Completed"),
]

class CartItem_Model(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'cart_items')
    product = models.ForeignKey(Product_Model, on_delete= models.CASCADE, related_name= 'cart_products')
    quantity = models.PositiveIntegerField(default= 1)
    
    def total_price(self):
        return self.product.price * self.quantity
    

class Order_Model(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'orders')
    total_price = models.DecimalField(max_digits= 10, decimal_places= 2, editable= False)
    status = models.CharField(max_length= 15, choices= STATUS_CHOICES, default= 'Pending')
    order_time = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return f"Order by {self.user.username} for {self.total_price} BDT"
    
    

class OrderItem_Model(models.Model):
    order = models.ForeignKey(Order_Model, on_delete=models.CASCADE, related_name= 'order_items')
    product = models.ForeignKey(Product_Model, on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField()

    def total_price(self):
        return self.quantity * self.product.price

        
