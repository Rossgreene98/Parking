from random import choice

class SquareParkingLot:
    def __init__(self, pointsPerSide, pointsPerCar):
        self.pointsPerSide = pointsPerSide
        self.pointsPerCar = pointsPerCar
        self.parkedCars = []
        self.pointsCarCanPark = self.getEverywhereCanCanParkInitially()

    def getEverywhereCanCanParkInitially(self):
        allPlacesForNewCar = []
        for i in range(self.pointsPerSide - self.pointsPerCar):
            allPlacesForNewCar += [Point(i, j) for j in range(self.pointsPerSide - self.pointsPerCar)]
        return allPlacesForNewCar

    def generateNewCarThatCanPark(self):
        newCarLocation = choice(self.pointsCarCanPark)
        return Car(newCarLocation)

    def parkNewCar(self, newCar):
        self.parkedCars.append(newCar)
        newUnavailableSpace = self.findNewUnavailableSpace(newCar)
        self.removeFromAvailableSpace(newUnavailableSpace)

    def findNewUnavailableSpace(self, newCar):
        newCarLocation = newCar.bottomLeftPoint
        newUnavailableSpace = []
        for i in range(newCarLocation.x - self.pointsPerCar, newCarLocation.x + self.pointsPerCar):
            for j in range(newCarLocation.y - self.pointsPerCar, newCarLocation.x + self.pointsPerCar):
                newUnavailableSpace.append(Point(i, j))
        return newUnavailableSpace

    def removeFromAvailableSpace(self, newUnavailableSpace):
        filter(lambda point: not point.inSetOfPoint(newUnavailableSpace), self.pointsCarCanPark)

    def display(self):
        print(len(self.parkedCars))

class Car:
    def __init__(self, bottomLeftPoint):
        self.bottomLeftPoint = bottomLeftPoint

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = [x, y]

    def isInSetOfPoints(self, setOfPoints):
        return any([self.equals(point) for point in setOfPoints])

    def equals(self, point):
        return self.x == point.x and self.y == point.y

def createParkingLotWithSize1Cars(sizeOfLot, meshSize=0.01):
    return SquareParkingLot(int(sizeOfLot / meshSize), int(1 / meshSize))


# Mesh Size is smallest possible distance separating parked cars. All cars placed on intersection of Mesh
standardMeshSize = 0.01

def run1SimulationWithLotSize(parkingLotSize):
    parkingLot = createParkingLotWithSize1Cars(parkingLotSize, standardMeshSize)
    while parkingLot.pointsCarCanPark:  # False when list is empty i.e. nowhere left to park
        newCar = parkingLot.generateNewCarThatCanPark()
        parkingLot.parkNewCar(newCar)
    parkingLot.display()


run1SimulationWithLotSize(10)
