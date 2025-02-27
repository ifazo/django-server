from django.urls import path
from .views import user_list, user_by_id

urlpatterns = [
        path('', user_list, name='user_list'),
        path('<uuid:user_id>/', user_by_id, name='user_by_id'),
]