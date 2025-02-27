from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_view(request):
    return Response({"message": "Django Server is running successfully!"}, status=200)
