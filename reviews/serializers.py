from rest_framework import serializers
from . models import User_Review

class Review_Serializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name', read_only=True)
    class Meta:
        model = User_Review
        fields = ['id', 'reviewer', 'product', 'rating', 'body', 'create_time']
        read_only_fields = ['reviewer', 'create_time']
        
        
        