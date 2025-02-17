from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .views import signup_view, login_view, product_list, category_list, product_by_id, category_by_id, review_list, review_by_id

@api_view(['GET'])
def api_home(request):
    return Response({"message": "Django api server is running successfully!"}, status=200)

urlpatterns = [
        path('', api_home, name='api_home'),
        path('signup/', signup_view, name='signup'),
        path('login/', login_view, name='login'),
        path('products/', product_list, name='product_list'),
        path('products/<uuid:product_id>/', product_by_id, name='product_by_id'),
        path('categories/', category_list, name='category_list'),
        path('categories/<uuid:category_id>/', category_by_id, name='category_by_id'),
        path('reviews/', review_list, name='review_list'),
        path('reviews/<uuid:review_id>/', review_by_id, name='review_by_id'),
]
