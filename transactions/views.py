from django.shortcuts import render
from rest_framework.views import APIView
from decimal import Decimal
from rest_framework.response import Response
from . models import Transaction_Model, UserBalance_Model

# Create your views here.

class DepositApiView(APIView):
    def post(self, req):
        amount = req.data.get("amount")
        if not amount or Decimal(amount) <= 0:
            return Response({"error": "Invalid deposit amount."})
        
        Transaction_Model.objects.create(
            user = req.user,
            amount = Decimal(amount),
            transaction_type = "Deposit",
            description = "Balance deposit"
        ) 
        
        user_balance, created = UserBalance_Model.objects.get_or_create(user = req.user)
        user_balance.current_balance += Decimal(amount)
        user_balance.save()
        
        return Response({"message": "Deposit successful!", "Balance": user_balance.current_balance})
    
    
    
class PaymentApiView(APIView):
    def post(self, req):
        amount = req.data.get("amount")
        if not amount or Decimal(amount) <= 0:
            return Response({"error": "Invalid payment amount."})
        
        try:
            user_balance = UserBalance_Model.objects.get(user = req.user)
        except UserBalance_Model.DoesNotExist:
            return Response({"error": "User balance not found."})
             
            
        if user_balance.current_balance < Decimal(amount):
            return Response({"error": "Insufficient balance."})
        
        
        Transaction_Model.objects.create(
            user = req.user,
            amount = Decimal(amount),
            transaction_type = "Payment",
            description = "Order payment"
        ) 
        
        user_balance.current_balance -= Decimal(amount)
        user_balance.save()
        
        return Response({"message": "Payment successful!", "Balance": user_balance.current_balance})
    
    