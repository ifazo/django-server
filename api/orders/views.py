from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer
from .models import Order


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response({
        'success': True,
        'message': 'Orders retrieved successfully',
        'data': serializer.data
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_by_id(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({
            'success': False,
            'message': 'Order not found',
            'errors': {'order_id': 'Order not found'}
        }, status=status.HTTP_404_NOT_FOUND)
    except ValueError:
        return Response({
            'success': False,
            'message': 'Invalid order ID format',
            'errors': {'order_id': 'Invalid order ID format'}
        }, status=status.HTTP_400_BAD_REQUEST)

    serializer = OrderSerializer(order)
    return Response({
        'success': True,
        'message': 'Order retrieved successfully',
        'data': serializer.data
    })