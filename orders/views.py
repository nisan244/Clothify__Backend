from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CartItem_Model, Order_Model, OrderItem_Model
from decimal import Decimal
from .serializers import CartItem_Serializer, Order_Serializer
from products.models import Product_Model



class AddToCart(APIView):
    def post(self, req):
        user = req.user
        product_id = req.data.get('product_id')
        quantity = req.data.get('quantity', 1)

        
        if not product_id:
            return Response({"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        
        try:
            product = Product_Model.objects.get(id= product_id)
        except Product_Model.DoesNotExist:
            return Response({"error": "Product not found"}, status= status.HTTP_404_NOT_FOUND)
    
        try:
            quantity = int(quantity)
            if quantity <= 0:
                return Response({"error": "Quantity must be greater than 0"}, status= status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({"error": "Invalid quantity"}, status= status.HTTP_400_BAD_REQUEST)

        
        cart_item, created = CartItem_Model.objects.get_or_create(user= user, product= product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

        return Response({"message": "Product added to cart", "cart_item": cart_item.id}, status=status.HTTP_201_CREATED)



class OrderPlace(APIView):
    def post(self, req):
        user = req.user
        cart_item_id = req.data.get("cart_item_id")
        if not cart_item_id:
            return Response({"error" : "Cart item ID required"})
        
        try:
            cart_item = CartItem_Model.objects.filter(user= user, id = cart_item_id)

        except CartItem_Model.DoesNotExist:
            return Response({"error": "Cart item not found"}, status= status.HTTP_400_BAD_REQUEST)

        product = cart_item.product
        if product.quantity < cart_item.quantity:
            return Response({"error" : "Stock out"})

        total_price = cart_item.quantity * product.price

        if user.balance < total_price:
            return Response({"error" : "Insufficient balance"})
        
        
        order = Order_Model.objects.create(user=user, total_price= Decimal(total_price))

        OrderItem_Model.objects.create(
            order= order,
            product= cart_item.product,
            quantity= cart_item.quantity
        )
        
        product.quantity -= cart_item.quantity
        product.save()
        
        user.balance -= Decimal(total_price)
        user.save()

        cart_item.delete()

        return Response({
            "message": "Order placed successfully",
            "order_id": order.id,
            "user_balance" : user.balance
        }, status= status.HTTP_201_CREATED)



class CartView(APIView):
    def get(self, req):
        user = req.user
        cart_items = CartItem_Model.objects.filter(user= user)
        serializer = CartItem_Serializer(cart_items, many= True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    
    
class OrderView(APIView):
    def get(self, req):
        user = req.user
        orders = Order_Model.objects.filter(user= user)
        serializer = Order_Serializer(orders, many= True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    
    
class DirectOrder(APIView):
    def post(self, req):
        user = req.user
        product_id = req.data.get("product_id")
        quantity = int(req.data.get("quantity", 1))

        if not product_id:
            return Response({"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product_Model.objects.get(id=product_id)
        except Product_Model.DoesNotExist:
            return Response({"error": "Product not found"}, status= status.HTTP_404_NOT_FOUND)

        if product.quantity < quantity:
            return Response(
                {"error": "Insufficient stock available"},
                status= status.HTTP_400_BAD_REQUEST,
            )

        total_price = Decimal(product.price) * Decimal(quantity)

        order = Order_Model.objects.create(user= user, total_price= total_price)

        OrderItem_Model.objects.create(
            order= order,
            product= product,
            quantity= quantity
        )

        product.quantity -= quantity
        product.save()

        return Response(
            {
                "message": "Order placed successfully",
                "order_id": order.id,
                "remaining_stock": product.quantity
            },
            status= status.HTTP_201_CREATED,
        )
