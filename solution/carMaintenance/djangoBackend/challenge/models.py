from django.db import models

class Car (models.Model):
  totalGas = models.FloatField(default = 0, blank = False, null = False)
  currentGas = models.FloatField(default = 0, blank = False, null = False)

  def __str__(self):
    return '{} - {} - {}'.format(self.id, self.totalGas, self.currentGas)

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