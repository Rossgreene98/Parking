from random import uniform
import numpy as np

def renyi(x):
    if x < 1:
        return 0
    locationOfNewCar = uniform(0, x - 1)
    carsToTheLeft = renyi(locationOfNewCar)
    carsToTheRight = renyi(x - (1 + locationOfNewCar))
    return 1 + carsToTheLeft + carsToTheRight

def manyRenyi(x, n):
    return [renyi(x) for i in range(n)]

def writeRenyiData(roadRange, n, filePath):
    allSims = np.array([manyRenyi(x, n) for x in roadRange])
    np.savetxt(filePath, allSims)
    print("Done!")

writeRenyiData([100, 1000, 10000, 100000, 1000000], 10000, 'allRenyiSimulationsNumberParked')

def renyi2(x):
    # Briefer version of Renyi function for poster, accomplishes same thing
    if x < 1:
        return 0
    u = uniform(0, x - 1)
    return 1 + renyi2(u) + renyi2(x - (1 + u))
