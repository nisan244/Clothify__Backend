from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('list', views.ProductListView)
router.register('categories', views.CategoriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('details/<int:product_id>/', views.Product_And_ReviewsAPIView.as_view(), name='product_and_reviews'),

]
# http://127.0.0.1:8000/products/details/2/

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
