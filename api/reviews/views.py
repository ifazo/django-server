from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer


# Create your views here.
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def review_list(request):
    product_id = request.GET.get('productId')
    if not product_id:
        return Response({
            'success': False,
            'message': 'productId query parameter is required',
            'errors': {'productId': 'This field is required'}
        }, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        reviews = Review.objects.filter(product_id=product_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response({
            'success': True,
            'message': 'Review list retrieved successfully',
            'data': serializer.data
        })

    elif request.method == 'POST':
        user = request.user
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({
                'success': True,
                'message': 'Review created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'message': 'Review creation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
# @permission_classes([IsAuthenticated])
def review_by_id(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response({
            'success': False,
            'message': 'Review not found',
            'errors': {'review_id': 'Review not found'}
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response({
            'success': True,
            'message': 'Review retrieved successfully',
            'data': ReviewSerializer(review).data
        })

    if review.user != request.user:
        return Response({
            'success': False,
            'message': 'You can only update or delete your own review',
            'errors': {'user': 'Permission denied'}
        }, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PATCH':
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Review updated successfully',
                'data': serializer.data
            })
        return Response({
            'success': False,
            'message': 'Review update failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review.delete()
        return Response({
            'success': True,
            'message': 'Review deleted successfully',
            'data': {'review_id': str(review.id)}
        }, status=status.HTTP_204_NO_CONTENT)
    