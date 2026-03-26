from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import HealthCheckSerializer

class HealthCheckView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = {'status': 'ok', 'version': '1.0.0'}
        serializer = HealthCheckSerializer(data)
        return Response(serializer.data)