from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from .serializers import CarSerializer, TyreSerializer
from .models import Car, Tyre
from .validadors import *

class CarEventsViewset(viewsets.ViewSet):

  def list(self, request, *args, **kwargs):
    return Response({}, status = status.HTTP_501_NOT_IMPLEMENTED)

  def retrieve(self, request, pk = None, *args, **kwargs):
    queryset = Car.objects.all()
    car = get_object_or_404(queryset, pk = pk)
    serializer = CarSerializer(car)
    return Response(serializer.data, status = status.HTTP_200_OK)

  def create(self, request, *args, **kwargs):
    newCar = Car.objects.create()
    serializer = CarSerializer(newCar)
    return Response(serializer.data, status = status.HTTP_201_CREATED)

  @action(detail=True, methods=['post'])
  def tyres(self, request, pk = None, *args, **kwargs):
    try:
      newTyre = Tyre.objects.create(car_id = pk)
      serializer = TyreSerializer(newTyre)
      return Response(serializer.data, status = status.HTTP_201_CREATED)
    except Exception as e:
      return Response({'error': str(e)}, status = status.HTTP_400_BAD_REQUEST)

  @action(detail = True, methods = ['patch'])
  def fuel(self, request, pk = None, *args, **kwargs):
    try:
      queryset = Car.objects.all()
      car = get_object_or_404(queryset, pk = pk)
      checkMinimumGasBeforeFuel(car)
      car.currentGas = car.currentGas + float(request.data['quantity'])
      car.save(update_fields = ['currentGas'])
      gasQuantityAfterFuel = '{}%'.format(round((car.currentGas/car.totalGas)*100,2))
      return Response({'currentGas': gasQuantityAfterFuel}, status = status.HTTP_202_ACCEPTED)
    except Exception as e:
      return Response({'error': str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
  
  @action(detail = True, methods = ['patch'])
  def trip(self, request, pk = None, *args, **kwargs):
    try:
      gasConsumption = 8
      queryset = Car.objects.all()
      car = get_object_or_404(queryset, pk=pk)

      car.currentGas = car.currentGas - float(request.data['distance'])/gasConsumption
      checkEnoughtFuelToTravel(car)

      tyres = Tyre.objects.filter(car_id=pk)
      checkAllTyresPlaced(tyres)

      for tyre in tyres:
        tyre.degradation = round(tyre.degradation + float(request.data['distance'])/3, 2)
        if(tyre.degradation>=100):
          raise Exception('Tyre too degradated to travel.')

      Tyre.objects.bulk_update(tyres, ['degradation'])
      car.save(update_fields = ['currentGas'])
      serializer = CarSerializer(car)
      return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
    except Exception as e:
      return Response({'error': str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)





