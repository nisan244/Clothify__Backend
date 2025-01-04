from django.urls import path
from .views import DepositApiView, PaymentApiView

urlpatterns = [
    path('deposit/', DepositApiView.as_view(), name='deposit'),
    path('payment/', PaymentApiView.as_view(), name='payment'),  
]
