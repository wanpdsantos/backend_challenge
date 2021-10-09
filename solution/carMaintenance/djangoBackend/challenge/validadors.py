def checkMinimumGasBeforeFuel(car):
  currentGasPercentage = car.currentGas/car.totalGas
  if (currentGasPercentage > 0.05):
    raise Exception('Current Gas above 5%.')

def checkEnoughtFuelToTravel(car):
  if car.currentGas <= 0:
    raise Exception('Not enought fuel to travel.')

def checkAllTyresPlaced(tyres):
  if tyres.count() < 4:
    raise Exception('Missing tyres to travel.')

