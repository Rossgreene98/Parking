from math import sqrt
from random import random

standardParkingLotSideLength = 100
standardSphereRadius = 0.5
consecutiveFailuresToDeclareJammed = 1000

class SphereParkingLot:
    @staticmethod
    def createStandardLotWithDimension(dimension):
        return SphereParkingLot(dimension, standardParkingLotSideLength, standardSphereRadius)

    def __init__(self, dimension, edgeLength, sphereRadius):
        self.dimension = dimension
        self.parkedSpheres = []
        self.successfullyAddedHistory = []
        self.edgeLength = edgeLength
        self.sphereRadius = sphereRadius

    def generateRandomSphereInsideLot(self):
        center = [self.generateRandomValidCoordinate() in range(self.dimension)]
        return Sphere(self.dimension, center, self.sphereRadius)

    def generateRandomValidCoordinate(self):
        return random(0 + self.sphereRadius, self.edgeLength - self.sphereRadius)

    def attemptToAddNewSphere(self, newSphere):
        if self.sphereCanBeAdded(newSphere):
            self.successfullyAddedHistory.append(True)
            self.parkedSpheres.append(newSphere)
        else:
            self.successfullyAddedHistory.append(False)

    def sphereCanBeAdded(self, newSphere):
        return not any(
            map(lambda parkedSphere: parkedSphere.overlapsWithSphere(newSphere), self.parkedSpheres)
        )

    def isJammed(self):
        return len(self.successfullyAddedHistory) > consecutiveFailuresToDeclareJammed \
               and not any(self.successfullyAddedHistory[-consecutiveFailuresToDeclareJammed:])

    def displayInformation(self):
        print('Number of Spheres: ' + str(len(self.parkedSpheres)))
        print('Number of Attempts: ' + str(len(self.successfullyAddedHistory) - consecutiveFailuresToDeclareJammed))

class Point:
    def __init__(self, coordinates, dimension):
        self.dimension = dimension
        self.coordinates = coordinates

    def distanceFrom(self, point):
        return sqrt(
            sum((self.coordinates[i] - point[i]) ** 2 for i in range(self.dimension))
        )

class Sphere:
    def __init__(self, dimension, center, radius=1):
        self.dimension = dimension
        self.center = Point(center, dimension)
        self.radius = radius

    def isPointInsideSphere(self, point):
        return self.center.distanceFrom(point) < self.radius

    def overlapsWithSphere(self, sphere):
        return self.center.distanceFrom(sphere.center) < self.radius + sphere.radius


def run1Simulation(dimension):
    parkingLot = SphereParkingLot.createStandardLotWithDimension(dimension)
    while not parkingLot.isJammed():
        newSphere = parkingLot.generateRandomSphereInsideLot()
        parkingLot.attemptToAddNewSphere(newSphere)

    parkingLot.displayInformation()
