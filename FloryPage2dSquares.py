from random import choice, randint
import matplotlib.pyplot as plt

class SquareParkingLot:
    def __init__(self, lengthOfSide, pointsPerUnitLength, lengthOfCar=1):
        self.lengthOfSide = lengthOfSide
        self.pointsPerSide = (lengthOfSide * pointsPerUnitLength) + 1  # because both ends are included as points
        self.pointsPerCar = lengthOfCar * pointsPerUnitLength
        self.pointsPerUnitLength = pointsPerUnitLength
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

    def display(self):
        print("Number of Squares: " + str(len(self.parkedCars)))
        plt.axes()

        axes = plt.gca()
        axes.set_xlim([0, self.lengthOfSide])
        axes.set_ylim([0, self.lengthOfSide])

        for car in self.parkedCars:
            car.displayOntoPlot()

        plt.axis('scaled')
        plt.show()

class Car:
    def __init__(self, bottomLeftPoint, pointsPerCar, lengthOfCar=1):
        self.lengthOfCar = lengthOfCar
        self.bottomLeftPoint = bottomLeftPoint
        self.pointsPerCar = pointsPerCar

    def displayOntoPlot(self):
        rectangle = plt.Rectangle(
            (self.bottomLeftPoint.x / self.pointsPerCar, self.bottomLeftPoint.y / self.pointsPerCar),
            self.lengthOfCar,
            self.lengthOfCar,
            fc=self.randomCarColour()
        )
        plt.gca().add_patch(rectangle)

    @staticmethod
    def randomCarColour():
        u = randint(0, 64)
        if u < 19:
            return 'k'
        elif u < 35:
            return '0.6'
        elif u < 41:
            return '#C0C0C0'
        elif u < 49:
            return 'b'
        elif u < 59:
            return 'r'
        elif u < 62:
            return 'g'
        elif u < 63:
            return 'y'
        else:
            return 'm'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = [x, y]

    def isInSetOfPoints(self, setOfPoints):
        return any([self.equals(point) for point in setOfPoints])

    def equals(self, point):
        return self.x == point.x and self.y == point.y


standardPointsPerUnitLength = 10

def run1SimulationWithLotSize(parkingLotSize, display=False):
    parkingLot = SquareParkingLot(parkingLotSize, standardPointsPerUnitLength, 1)
    while parkingLot.pointsCarCanPark:  # False when list is empty i.e. nowhere left to park
        newCar = parkingLot.generateNewCarThatCanPark()
        parkingLot.parkNewCar(newCar)

    if display:
        parkingLot.display()

    return len(parkingLot.parkedCars)

def runManySimulations(parkingLotSize, iterations):
    numberOfParkedCars = [
        run1SimulationWithLotSize(parkingLotSize, display=False) in range(iterations)
    ]
    print(numberOfParkedCars)


run1SimulationWithLotSize(10, display=True)
# runManySimulations(10, 10)
