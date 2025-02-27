from django.urls import path
from .views import product_list, product_by_id

urlpatterns = [
        path('', product_list, name='product_list'),
        path('<uuid:product_id>/', product_by_id, name='product_by_id'),
]