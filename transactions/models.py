from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TRANSACTION_TYPE = [
    ("Deposit", "Deposit"),
    ("Payment", "Payment"),
]

class Transaction_Model(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'transactions')
    amount = models.DecimalField(max_digits= 10, decimal_places= 2)
    transaction_type = models.CharField(max_length= 15, choices= TRANSACTION_TYPE)
    time = models.DateTimeField(auto_now_add= True)
    description = models.TextField(blank= True, null= True)
    
    
    def __str__(self):
        return f"{self.user.username} -- {self.transaction_type} -- {self.amount} BDT"
    
    
    
class UserBalance_Model(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name= 'balance')
    current_balance = models.DecimalField(max_digits= 10, decimal_places= 2, default= 0.00)
    
    def __str__(self):
        return f"{self.user.username} -- Balance: {self.current_balance} BDT"
    
    