from django.urls import path, include
from .views import api_view

urlpatterns = [
        path('', api_view, name='api_home'),
        path('auth/', include('api.auth.urls')),
        path('users/', include('api.users.urls')),
        path('categories/', include('api.categories.urls')),
        path('products/', include('api.products.urls')),
        path('reviews/', include('api.reviews.urls')),
        path('orders/', include('api.orders.urls')),
]
