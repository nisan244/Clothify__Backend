from django.db import models
from django.utils import timezone
import pytz

# Create your models here.

SIZE_CHOICES = [
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
    ('XXL', 'Extra Extra Large'),
]

class Brand_Model(models.Model):
    name = models.CharField(max_length= 200, unique= True)
    slug = models.SlugField(unique= True, max_length= 250)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length= 200)
    slug = models.SlugField(max_length= 255)
    
    def __str__(self):
        return self.name



class Product_Model(models.Model):
    name = models.CharField(max_length= 200)
    price = models.DecimalField(max_digits= 10, decimal_places= 2)
    size = models.CharField(max_length= 3, choices = SIZE_CHOICES)
    color = models.CharField(max_length= 50)
    image = models.ImageField(upload_to='products/images/')
    quantity = models.PositiveIntegerField(blank= True, null= True)
    description = models.TextField()
    create_time = models.DateTimeField(auto_now_add = True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    brand = models.ForeignKey(Brand_Model, on_delete= models.CASCADE)
    slug = models.SlugField(unique= True, blank= True, null= True, max_length= 250)
    
    

    # bangladesh time dekhanor jonno
    def get_bangladesh_time(self):
        bangladesh_timezone = pytz.timezone('Asia/Dhaka')
        return self.create_time.astimezone(bangladesh_timezone)
    
    def __str__(self):
        return self.name



