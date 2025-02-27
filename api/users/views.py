from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from uuid import UUID

@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response({
        'success': True,
        'message': 'User list retrieved successfully',
        'data': serializer.data
    })

@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_by_id(request, user_id):
    try:
        user_id = UUID(user_id)
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({
            'success': False,
            'message': 'User not found',
            'errors': {'user_id': 'User not found'}
        }, status=status.HTTP_404_NOT_FOUND)
    except ValueError:
        return Response({
            'success': False,
            'message': 'Invalid user ID format',
            'errors': {'user_id': 'Invalid user ID format'}
        }, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response({
            'success': True,
            'message': 'User retrieved successfully',
            'data': serializer.data
        })

    if user != request.user:
        return Response({
            'success': False,
            'message': 'You can only update or delete your own account',
            'errors': {'user': 'Permission denied'}
        }, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PATCH':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'User updated successfully',
                'data': serializer.data
            })
        return Response({
            'success': False,
            'message': 'User update failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response({
            'success': True,
            'message': 'User deleted successfully',
            'data': {'user_id': str(user.id)}
        }, status=status.HTTP_204_NO_CONTENT)
