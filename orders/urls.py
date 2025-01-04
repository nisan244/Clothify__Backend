from django.urls import path
from .views import AddToCart, CartView, OrderPlace, OrderView

urlpatterns = [
    path('cart/add/', AddToCart.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart_view'),
    path('order/place/', OrderPlace.as_view(), name='order_place'),
    path('order/', OrderView.as_view(), name='order_view'),
]
