from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . models import User_Review
from . serializers import Review_Serializer
from rest_framework.viewsets import ModelViewSet

# -=------------------=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-==
# -=------------------=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-==
# -=------------------=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-==
# -=------------------=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-==

class ReviewAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = Review_Serializer(data= request.data)
        if serializer.is_valid():
            serializer.save(reviewer= request.user)
            product = serializer.instance.product
            reviews = product.reviews.all()
            return Response({'message': 'Review added successfully!', 'reviews': Review_Serializer(reviews, many=True).data})
        return Response(serializer.errors, status=400)


# class RatingListAPIView(APIView):
#     def get(self, request, product_id):
#         reviews = User_Review.objects.filter(product__id=product_id)
#         if not reviews.exists():
#             return Response({'message': 'No reviews found for this product.'}, status=404)

#         response_data = []
#         for review in reviews:
#             response_data.append({
#                 'reviewer': review.reviewer.username,
#                 'rating': review.rating,
#                 'body': review.body,
#                 'create_time': review.get_bangladesh_time().strftime('%Y-%m-%d %H:%M:%S'),
#             })

#         return Response(response_data)

        
        

    
    
