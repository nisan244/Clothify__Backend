from django.db import models
from django.contrib.auth.models import User
from products.models import Product_Model

# Create your models here.


class Wishlist_Model(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'wishlists')
    product = models.ForeignKey(Product_Model, on_delete= models.CASCADE, related_name= 'wishlist_products')
    time = models.DateTimeField(auto_now_add= True)
    
    
    def __str__(self):
        return f"{self.user.username} Wishlist --- {self.product.name}"
    
    