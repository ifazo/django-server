from django.urls import path
from .views import review_list, review_by_id

urlpatterns = [
        path('', review_list, name='review_list'),
        path('<uuid:review_id>/', review_by_id, name='review_by_id'),
]