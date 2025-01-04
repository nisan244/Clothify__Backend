from django.db import models
from django.contrib.auth.models import User
from products.models import Product_Model
from django.utils import timezone
import pytz
# Create your models here.

RATING_CHOICES = [
    ("⭐", 1),
    ("⭐⭐", 2),
    ("⭐⭐⭐", 3),
    ("⭐⭐⭐⭐", 4),
    ("⭐⭐⭐⭐⭐", 5),
]


class User_Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Product_Model, on_delete= models.CASCADE, related_name='reviews') 
    rating = models.CharField(choices= RATING_CHOICES, max_length= 6)
    body = models.TextField() 
    create_time = models.DateTimeField(auto_now_add= True) 

    class Meta:
        unique_together = ('reviewer', 'product') 
        ordering = ['-create_time'] 
        
    # Bangladesh time দেখানোর জন্য
    def get_bangladesh_time(self):
        bangladesh_timezone = pytz.timezone('Asia/Dhaka')
        return self.create_time.astimezone(bangladesh_timezone)
       
    def __str__(self):
        return f"{self.reviewer.username} rated {self.product.name} - {self.rating}"
