from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .views import review_list, review_by_id

@api_view(['GET'])
def api_home(request):
    return Response({"message": "Django Server is running successfully!"}, status=200)

urlpatterns = [
        path('', api_home, name='api_home'),
        path('auth/', include('api.auth.urls')),
        path('users/', include('api.users.urls')),
        path('categories/', include('api.categories.urls')),
        path('products/', include('api.products.urls')),
        path('reviews/', review_list, name='review_list'),
        path('reviews/<uuid:review_id>/', review_by_id, name='review_by_id'),
]
