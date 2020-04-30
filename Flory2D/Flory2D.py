from math import sqrt, pi
import numpy as np
from numpy.random import choice
import time
from math import ceil, floor

x = 10

"""
This code is used to generate the simulations discussed in Chapter 5; Simulating the Flory model.
The first function, 'simulate', does the bulk of the work, and is discussed in this chapter.
"""

def simulate(k):
    lotSize = k * x
    allPossibleParkingSpots = getEveryPoint(lotSize)
    parkedDisks = 0

    while stillSpaceToPark(allPossibleParkingSpots):
        newDisk = getRandomDisk(allPossibleParkingSpots, lotSize)
        parkedDisks += 1
        allPossibleParkingSpots = removeNewlyUnavailableSpace(
            allPossibleParkingSpots,
            newDisk,
            lotSize,
            k
        )

    return parkedDisks


def getEveryPoint(lotSize):
    return np.ones((lotSize, lotSize))


def stillSpaceToPark(allPossibleSpaces):
    return np.sum(np.sum(allPossibleSpaces)) != 0


def getRandomDisk(allPossibleSpots, lotSize):
    pointsPerRow = np.sum(allPossibleSpots, axis=1)
    chosenRowIndex = choice(lotSize, p=pointsPerRow / sum(pointsPerRow))
    columnCount = choice(int(pointsPerRow[chosenRowIndex]))
    chosenColumnIndex = [i for i, n in enumerate(allPossibleSpots[chosenRowIndex]) if n == 1][columnCount]
    return [chosenRowIndex, chosenColumnIndex]


def removeNewlyUnavailableSpace(allPossibleParkingSpots, newDisk, lotSize, k):
    for i in range(-k, 1 + k):

        x1 = newDisk[0] + i
        x = x1 + lotSize if x1 < 0 \
            else x1 - lotSize if x1 >= lotSize \
            else x1

        jBound = sqrt(k ** 2 - i ** 2)
        for j in range(-ceil(jBound), floor(jBound)+1):
            y1 = newDisk[1] + j
            y = y1 + lotSize if y1 < 0 \
                else y1 - lotSize if y1 >= lotSize \
                else y1

            allPossibleParkingSpots[x][y] = 0

    return allPossibleParkingSpots


def timeSimulate(k):
    start_time = time.time()
    print(simulate(k))
    print("--- %s seconds ---" % (time.time() - start_time))
    # Printed 0.9756 for x=10, k=100
    # Printed 1698 for x=100, k=100

def manyFlory2D(k, n):
    return np.array([simulate(k) for i in range(n)]) * pi / 4 / x**2

def writeFlory2DData(kRange, n, filePath):
    allSims = np.array([manyFlory2D(k, n) for k in kRange])
    np.savetxt(filePath, allSims)
    print("Done!")

writeFlory2DData([50, 100, 300, 500], 1000, 'allFlory2DSims')

# timeSimulate(500)
