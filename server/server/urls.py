from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home_view(request):
    return JsonResponse({"message": "Welcome to the Django API server!"})

urlpatterns = [
    path('', home_view, name='home'),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
