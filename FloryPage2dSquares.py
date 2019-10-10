from random import choice
import matplotlib.pyplot as plt

class SquareParkingLot:
    def __init__(self, lengthOfSide, pointsPerCar):
        self.pointsPerSide = lengthOfSide + 1  # because both ends are included as points
        self.pointsPerCar = pointsPerCar
        self.parkedCars = []
        self.pointsCarCanPark = self.getEverywhereCanParkInitially()

    def getEverywhereCanParkInitially(self):
        allPlacesForNewCar = []
        for i in range(self.pointsPerSide - self.pointsPerCar):
            allPlacesForNewCar += [Point(i, j) for j in range(self.pointsPerSide - self.pointsPerCar)]
        return allPlacesForNewCar

    def generateNewCarThatCanPark(self):
        newCarLocation = choice(self.pointsCarCanPark)
        return Car(newCarLocation, self.pointsPerCar)

    def parkNewCar(self, newCar):
        self.parkedCars.append(newCar)
        newUnavailableSpace = self.findNewUnavailableSpace(newCar)
        self.removeFromAvailableSpace(newUnavailableSpace)

    def findNewUnavailableSpace(self, newCar):
        newCarLocation = newCar.bottomLeftPoint
        newUnavailableSpace = []
        for i in range(newCarLocation.x - self.pointsPerCar, newCarLocation.x + self.pointsPerCar + 1):
            for j in range(newCarLocation.y - self.pointsPerCar, newCarLocation.y + self.pointsPerCar + 1):
                newUnavailableSpace.append(Point(i, j))
        return newUnavailableSpace

    def removeFromAvailableSpace(self, newUnavailableSpace):
        self.pointsCarCanPark = list(
            filter(lambda point: not point.isInSetOfPoints(newUnavailableSpace), self.pointsCarCanPark)
        )

    def display(self, withImage=True):
        print("Number of Squares: " + str(len(self.parkedCars)))
        if withImage:
            plt.axes()

            axes = plt.gca()
            axes.set_xlim([0, self.pointsPerSide])
            axes.set_ylim([0, self.pointsPerSide])

            for car in self.parkedCars:
                car.displayOntoPlot()

            plt.axis('scaled')
            plt.show()

class Car:
    def __init__(self, bottomLeftPoint, pointsPerCar):
        self.bottomLeftPoint = bottomLeftPoint
        self.pointsPerCar = pointsPerCar

    def displayOntoPlot(self):
        rectangle = plt.Rectangle(
            (self.bottomLeftPoint.x, self.bottomLeftPoint.y),
            self.pointsPerCar,
            self.pointsPerCar,
            fc='r'
        )
        plt.gca().add_patch(rectangle)


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
standardMeshSize = 0.1

def run1SimulationWithLotSize(parkingLotSize):
    parkingLot = createParkingLotWithSize1Cars(parkingLotSize, standardMeshSize)
    while parkingLot.pointsCarCanPark:  # False when list is empty i.e. nowhere left to park
        newCar = parkingLot.generateNewCarThatCanPark()
        parkingLot.parkNewCar(newCar)
    parkingLot.display()


run1SimulationWithLotSize(10)
