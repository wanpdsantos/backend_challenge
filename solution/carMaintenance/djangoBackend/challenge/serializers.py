from rest_framework import serializers
from .models import Car, Tyre

class CarSerializer(serializers.ModelSerializer):
  class Meta:
    model = Car
    fields = [
      'id',
      'totalGas',
      'currentGas',
    ]

class TyreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tyre
    fields = '__all__'
