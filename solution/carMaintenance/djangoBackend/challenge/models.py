from django.db import models

class Car (models.Model):
  totalGas = models.FloatField(default = 0, blank = False, null = False)
  currentGas = models.FloatField(default = 0, blank = False, null = False)

  def __str__(self):
    return '{} - {} - {}'.format(self.id, self.totalGas, self.currentGas)