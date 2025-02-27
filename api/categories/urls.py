from django.urls import path
from .views import category_list, category_by_id

urlpatterns = [
        path('', category_list, name='category_list'),
        path('<uuid:category_id>/', category_by_id, name='category_by_id'),
]