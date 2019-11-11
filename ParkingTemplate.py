from random import choice, randint
import matplotlib.pyplot as plt

class TemplateParkingLot(object):
    def __init__(self, lengthOfSide, pointsPerUnitLength, CarClass):
        self.CarClass = CarClass
        self.lengthOfSide = lengthOfSide
        self.pointsPerCar = pointsPerUnitLength
        self.pointsPerUnitLength = pointsPerUnitLength
        self.pointsPerSide = (lengthOfSide * pointsPerUnitLength) + 1  # because both ends are included as points
        self.parkedCars = []
        self.pointsCarCanPark = self.getEverywhereCanParkInitially()

    def getEverywhereCanParkInitially(self):
        # to be implemented. gets location cars can be placed in starting lot.
        return []

    def generateNewCarThatCanPark(self):
        newCarLocation = choice(self.pointsCarCanPark)
        return self.CarClass(newCarLocation, self.pointsPerCar)

    def parkNewCar(self, newCar):
        self.parkedCars.append(newCar)
        self.removeNewlyUnavailableSpace(newCar)

    def removeNewlyUnavailableSpace(self, newCar):
        self.pointsCarCanPark = list(
            filter(lambda point: not newCar.stopsPointBeingParkedIn(point), self.pointsCarCanPark)
        )

    def display(self):
        print("Number of Cars: " + str(len(self.parkedCars)))
        plt.axes()

        axes = plt.gca()
        axes.set_xlim([0, self.lengthOfSide])
        axes.set_ylim([0, self.lengthOfSide])

        for car in self.parkedCars:
            car.displayOntoPlot()

        plt.axis('scaled')
        plt.show()

    def reset(self):
        self.parkedCars = []
        self.pointsCarCanPark = self.getEverywhereCanParkInitially()


class TemplateCar(object):
    def __init__(self):
        self.colour = self.randomCarColour()

    def stopsPointBeingParkedIn(self, point):
        # to be implemented. Returns true if a car parked in 'point' would overlap with self
        pass

    def displayOntoPlot(self):
        # to be implemented. Displays car onto matplotlib plot
        pass

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

class TemplatePoint(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

standardPointsPerUnitLength = 10
standardParkingLotSize = 10
standardNumberOfIterations = 100

class TemplateSimulation:
    def __init__(
            self,
            ParkingLotClass,
            parkingLotSize=standardParkingLotSize,
            meshDensity=standardPointsPerUnitLength,
    ):
        self.parkingLot = ParkingLotClass(parkingLotSize, meshDensity)

    def reset(self):
        self.parkingLot.reset()

    def simulate(self, display=False):
        while self.parkingLot.pointsCarCanPark:  # False when list is empty i.e. nowhere left to park
            newCar = self.parkingLot.generateNewCarThatCanPark()
            self.parkingLot.parkNewCar(newCar)

        if display:
            self.parkingLot.display()

        return len(self.parkingLot.parkedCars)

    def nSimulations(self, n=standardNumberOfIterations):
        numberOfParkedCars = []
        for i in range(n):
            self.reset()
            numberOfParkedCars.append(self.simulate())
        return numberOfParkedCars


