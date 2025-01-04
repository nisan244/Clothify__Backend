from rest_framework import serializers
from . models import Transaction_Model, UserBalance_Model

class Transaction_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction_Model
        fields = '__all__'
        
        
        
class UserBalance_Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserBalance_Model
        fields = ['balance']
        
        
        