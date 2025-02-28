from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import SignupSerializer, SigninSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


@api_view(['POST'])
def signup_user(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'success': True,
            'message': 'User created successfully',
            'data': {
                'id': str(user.id),
                'username': user.username,
                'email': user.email,
                'role': user.role
            }
        }, status=status.HTTP_201_CREATED)
    return Response({
        'success': False,
        'message': 'User creation failed',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def signin_user(request):
    serializer = SigninSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        refresh_token = RefreshToken.for_user(user)
        access_token = refresh_token.access_token

        access_token['username'] = user.username
        access_token['email'] = user.email
        access_token['role'] = user.role

        return Response({
            'refresh_token': str(refresh_token),
            'access_token': str(access_token),
        }, status=status.HTTP_200_OK)
    
    return Response({
        'success': False,
        'message': 'Invalid credentials',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
