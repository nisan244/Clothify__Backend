from django.contrib import admin
from . models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}
    list_display = ['name', 'price', 'brand', 'slug']
    
    
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}
    list_display = ['name', 'slug']
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}
    list_display = ['name', 'slug']
    
    
admin.site.register(Product_Model, ProductAdmin)
admin.site.register(Brand_Model, BrandAdmin)
admin.site.register(Category, CategoryAdmin)

