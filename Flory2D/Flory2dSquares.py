import matplotlib.pyplot as plt
import ParkingTemplate

class SquareParkingLot(ParkingTemplate.TemplateParkingLot):
    def __init__(self, lengthOfSide, pointsPerUnitLength):
        self.pointsPerCar = pointsPerUnitLength  # Since all cars have length 1
        super(SquareParkingLot, self).__init__(lengthOfSide, pointsPerUnitLength, SquareCar)

    def getEverywhereCanParkInitially(self):
        allPlacesForNewCar = []
        for i in range(self.pointsPerSide - self.pointsPerCar):
            allPlacesForNewCar += [Point(i, j) for j in range(self.pointsPerSide - self.pointsPerCar)]
        return allPlacesForNewCar

class SquareCar(ParkingTemplate.TemplateCar):
    def __init__(self, bottomLeftPoint, pointsPerCar):
        super().__init__()
        self.bottomLeftPoint = bottomLeftPoint
        self.pointsPerCar = pointsPerCar

    def stopsPointBeingParkedIn(self, point):
        return abs(self.bottomLeftPoint.x - point.x) <= self.pointsPerCar and\
               abs(self.bottomLeftPoint.y - point.y) <= self.pointsPerCar

    def displayOntoPlot(self):
        rectangle = plt.Rectangle(
            (self.bottomLeftPoint.x / self.pointsPerCar, self.bottomLeftPoint.y / self.pointsPerCar),
            1,
            1,
            fc=self.colour
        )
        plt.gca().add_patch(rectangle)

class Point(ParkingTemplate.TemplatePoint):
    pass

def simulateManySquares():
    return ParkingTemplate.TemplateSimulation(SquareParkingLot).nSimulations()

ParkingTemplate.TemplateSimulation(SquareParkingLot).simulate(display=True)

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 24,
        }

plt.title('k=100', fontdict=font)
plt.show()
#  simulateManySquares()
