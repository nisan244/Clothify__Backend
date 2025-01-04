from django.urls import path
# from .views import RatingListAPIView, ReviewAPIView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('products/review/', ReviewAPIView.as_view(), name='user_review'),
    # path('products/reviews/<int:product_id>/', RatingListAPIView.as_view(), name='product_reviews'),
]

# http://127.0.0.1:8000/reviews/products/reviews/2/

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

