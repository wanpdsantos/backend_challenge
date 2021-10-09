from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from .serializers import CarSerializer, TyreSerializer
from .models import Car, Tyre

class CarEventsViewset(viewsets.ViewSet):
  
  def list(self, request):
    return Response({}, status=status.HTTP_501_NOT_IMPLEMENTED)

  def retrieve(self, request, pk=None):
    queryset = Car.objects.all()
    car = get_object_or_404(queryset, pk=pk)
    serializer = CarSerializer(car)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def create(self, request):
    newCar = Car.objects.create()
    serializer = CarSerializer(newCar)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

  @action(detail=True, methods=['post'])
  def tyres(self, request, pk=None):
    try:
      newTyre = Tyre.objects.create(car_id=pk)
      serializer = TyreSerializer(newTyre)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


