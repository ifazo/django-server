from django.urls import path
from .views import order_list, order_by_id

urlpatterns = [
        path('', order_list, name='order_list'),
        path('<uuid:order_id>/', order_by_id, name='order_by_id'),
]