from django.shortcuts import render
from . serializers import Product_Serializer, Category_Serializer, Brand_Serializer
from . models import *
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.filters import SearchFilter, BaseFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class ProductListView(ModelViewSet):
    queryset = Product_Model.objects.all()
    serializer_class = Product_Serializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filter -------> brand name
        brand_name = self.request.query_params.get("brand")
        if brand_name:
            queryset = queryset.filter(brand__name__icontains= brand_name)
        
        
        # Filter -------> size
        size = self.request.query_params.get("size")
        if size:
            queryset = queryset.filter(size= size)
        
        
        # Filter --------> color
        color = self.request.query_params.get("color")
        if color:
            queryset = queryset.filter(color__icontains= color)
        
        
        # Filter ---------> category
        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category__name__icontains= category)
        
        return queryset


     
class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer
    

# class Product_And_ReviewsAPIView(APIView):
#     def get(self, request, product_id):
#         try:
#             product = Product_Model.objects.get(id= product_id)
#             print(product)
#             serializer = Product_Serializer(product)
#             return Response(serializer.data)
#         except Product_Model.DoesNotExist:
#             return Response({'error': 'Product not found'}, status=404)

