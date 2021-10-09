from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Car, Tyre

class TyreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tyre
    fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
  tyres = TyreSerializer(many=True, read_only=True)
  class Meta:
    model = Car
    fields = [
      'id',
      'totalGas',
      'currentGas',
      'tyres'
    ]
