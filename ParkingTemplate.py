from math import sqrt
from random import uniform

standardParkingLotSideLength = 100
standardSphereRadius = 0.5
consecutiveFailuresToDeclareJammed = 20

class ParkingLot:
    @staticmethod
    def createStandardLot():
        pass

    def __init__(self, sizeOfLot):
        self.parkedCars = []
        self.sizeOfLot = sizeOfLot

    def generateRandomCarInsideLot(self):
        pass

    def addNewCar(self, newCar):
        self.parkedSpheres.append(newCar)

    def carCanBeAdded(self, newCar):
        pass

    def isJammed(self):
        return False

    def displayInformation(self):
        print('Number of Cars: ' + str(len(self.parkedCars)))

class Point:
    def __init__(self, coordinates, dimension):
        self.dimension = dimension
        self.coordinates = coordinates

    def distanceFrom(self, point):
        return sqrt(
            sum((self.coordinates[i] - point.coordinates[i]) ** 2 for i in range(self.dimension))
        )

class Car:
    def __init__(self, location, size=1):
        self.location = location
        self.size = size

    def isPointInsideSphere(self, point):
        return self.center.distanceFrom(point) < self.radius

    def overlapsWithSphere(self, sphere):
        return self.center.distanceFrom(sphere.center) < self.radius + sphere.radius

def run1Simulation(dimension):
    parkingLot = SphereParkingLot.createStandardLotWithDimension(dimension)
    while not parkingLot.isJammed():
        print(parkingLot.successfullyAddedHistory)
        newSphere = parkingLot.generateRandomSphereInsideLot()
        parkingLot.attemptToAddNewSphere(newSphere)

    parkingLot.displayInformation()

run1Simulation(2)