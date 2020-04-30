from random import choice, randint
import matplotlib.pyplot as plt

""" 
This code runs in conjunction with Flory2dCircles, there is more information about its purpose at the top of that file.
"""

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
        # to be implemented in e.g. Flory2dCircles. gets location cars can be placed in starting lot.
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

    def display(self, grid=False, border=True):
        print("Number of Cars: " + str(len(self.parkedCars)))
        plt.axes()

        plt.xlim([0, self.lengthOfSide])
        plt.xlim([0, self.lengthOfSide])

        # axes = plt.gca()
        #
        # axes.set_xlim([0, self.lengthOfSide])
        # axes.set_ylim([0, self.lengthOfSide])

        for car in self.parkedCars:
            car.displayOntoPlot()

        if grid:
            for i in range(self.pointsPerSide):
                plt.axhline(i / self.pointsPerCar, xmin=0.05, xmax=0.95, alpha=0.4)
                plt.axvline(i / self.pointsPerCar, ymin=0.05, ymax=0.95, alpha=0.4)

        if border:
            plt.plot([0, 0], [self.lengthOfSide, 0], color='blue')
            plt.plot([0, self.lengthOfSide], [self.lengthOfSide, self.lengthOfSide], color='blue')
            plt.plot([self.lengthOfSide, self.lengthOfSide], [0, self.lengthOfSide], color='blue')
            plt.plot([self.lengthOfSide, 0], [0, 0], color='blue')

        font = {'family': 'serif',
                'color': 'darkred',
                'weight': 'normal',
                'size': 24,
                }

        plt.axis('scaled')

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

# Change these parameters to change all simulations run through template
k = 100

standardParkingLotSize = 10
standardNumberOfIterations = 100

class TemplateSimulation:
    def __init__(
            self,
            ParkingLotClass,
            parkingLotSize=standardParkingLotSize,
            meshDensity=k,
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
