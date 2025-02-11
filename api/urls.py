from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .views import product_list, category_list, product_by_id, category_by_id

@api_view(['GET'])
def api_home(request):
    return Response({"message": "Django api server is running successfully!"}, status=200)

urlpatterns = [
    path('', api_home, name='api_home'),
        path('products/', product_list, name='product_list'),
        path('products/<uuid:product_id>/', product_by_id, name='product_by_id'),
        path('categories/', category_list, name='category_list'),
        path('categories/<uuid:category_id>/', category_by_id, name='category_by_id'),
]
