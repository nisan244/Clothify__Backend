from rest_framework import serializers
from . models import *
from reviews . serializers import Review_Serializer

class Product_Serializer(serializers.ModelSerializer):
    reviews = Review_Serializer(many=True, read_only=True)
    brand = serializers.CharField(source='brand.name', read_only=True)  
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product_Model
        fields = ['id', 'name', 'price', 'size', 'color', 'image', 'category', 'brand', 'quantity', 'description', 'create_time', 'reviews']
        


class Brand_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Brand_Model
        fields = '__all__'
    

class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        
    