from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Car (models.Model):
  totalGas = models.FloatField(default = 45, blank = False, null = False)
  currentGas = models.FloatField(default = 20, blank = False, null = False)

  def __str__(self):
    return '{} - {} - {}'.format(self.id, self.totalGas, self.currentGas)

@receiver(pre_save, sender=Car)
def checkRequirements(sender, instance, update_fields, *args, **kwargs):
  if not instance._state.adding:
    currentGasPercentage = Car.objects.get(pk=instance.id).currentGas/Car.objects.get(pk=instance.id).totalGas
    if (currentGasPercentage>0.05):
      raise Exception('Current Gas above 5%.')
  return

class Tyre (models.Model):
  car = models.ForeignKey(Car, related_name='tyres', on_delete=models.CASCADE, blank=False, null=False)
  degradation = models.FloatField(default = 0, blank = False, null = False)

  def __str__(self):
    return '{} - {}'.format(self.id, self.degradation)

  def save(self, *args, **kwargs):
    tyreCount = Tyre.objects.filter(car_id = self.car_id).count()
    if tyreCount >= 4:
      raise Exception('Maximum tires reached.')
    super().save(*args, **kwargs)