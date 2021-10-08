from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import CarSerializer

from .models import Car

class CarView(APIView):
  permission_classes = [AllowAny]

  def post(self, request):
    try:
      newCar = Car.objects.create()
      newCar = CarSerializer(newCar)
      return Response({'created': newCar.data}, status=status.HTTP_200_OK)
    except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

Car_View = CarView.as_view()