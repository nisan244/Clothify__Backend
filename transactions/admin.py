from django.contrib import admin
from . models import Transaction_Model, UserBalance_Model

# Register your models here.

admin.site.register(Transaction_Model)
admin.site.register(UserBalance_Model)

