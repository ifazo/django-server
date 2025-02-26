from django.urls import path
from .views import signup_user, signin_user

urlpatterns = [
    path('signup/', signup_user, name='signup'),
    path('signin/', signin_user, name='signin'),
]