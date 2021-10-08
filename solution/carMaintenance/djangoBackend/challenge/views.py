from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import CarSerializer, TyreSerializer

from .models import Car, Tyre

class CarView(APIView):
  permission_classes = [AllowAny]

  def post(self, request):
    try:
      newCar = Car.objects.create()
      newCar = CarSerializer(newCar)
      return Response({'created': newCar.data}, status=status.HTTP_201_CREATED)
    except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def get(self, request):
    selectedCarId = self.request.GET.get('carId','')
    try:
      car = Car.objects.get(pk=selectedCarId)
      car = CarSerializer(car)
      return Response({'selected': car.data}, status=status.HTTP_200_OK)
    except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

Car_View = CarView.as_view()

class TyreView(APIView):
  permission_classes = [AllowAny]

  def post(self, request):
    selectedCarId = self.request.GET.get('carId','')
    try:
      newTyre = Tyre.objects.create(car_id=selectedCarId)
      newTyre = TyreSerializer(newTyre)
      return Response({'created': newTyre.data}, status=status.HTTP_201_CREATED)
    except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

Tyre_View = TyreView.as_view()