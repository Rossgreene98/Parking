from math import sqrt
import time

"""
This code works in conjunction with ParkingTemplate to produce the same effect as Flory2D.py. 
Although this is not the code used to run simulations, it was used to create images used in the dissertation,
since the function Flory2D did not have this functionality.
"""

import matplotlib.pyplot as plt
import ParkingTemplate

class CircleParkingLot(ParkingTemplate.TemplateParkingLot):
    def __init__(self, lengthOfSide, pointsPerUnitLength):
        self.pointsAlongCarRadius = int(pointsPerUnitLength / 2)  # Since all cars have diameter 1
        super().__init__(lengthOfSide, pointsPerUnitLength, CircularCar)

    def getEverywhereCanParkInitially(self):
        r = range(self.pointsAlongCarRadius, self.pointsPerSide - self.pointsAlongCarRadius)
        return [
            Point(i, j) for i in r for j in r
        ]

class CircularCar(ParkingTemplate.TemplateCar):
    def __init__(self, centrePoint, pointsAlongDiameter):
        self.centrePoint = centrePoint
        self.pointsAlongRadius = int(pointsAlongDiameter / 2)
        self.pointsPerUnitLength = pointsAlongDiameter
        super().__init__()

    def stopsPointBeingParkedIn(self, point):
        # Since circles only overlap if their centres are separated by less than 2 radii
        return self.centrePoint.distanceTo(point) <= self.pointsAlongRadius * 2

    def displayOntoPlot(self):
        circle = plt.Circle(
            (self.centrePoint.x / self.pointsPerUnitLength, self.centrePoint.y / self.pointsPerUnitLength),
            self.pointsAlongRadius / self.pointsPerUnitLength,
            fc=self.colour
        )
        plt.gca().add_patch(circle)

class Point(ParkingTemplate.TemplatePoint):
    def __init__(self, x, y):
        super().__init__(x, y)

    def distanceTo(self, point):
        return sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

def simulateManyCircles():
    return ParkingTemplate.TemplateSimulation(CircleParkingLot).nSimulations()

def timeSimulation():
    start_time = time.time()
    ParkingTemplate.TemplateSimulation(CircleParkingLot).simulate()
    print("--- %s seconds ---" % (time.time() - start_time))
    # Printed 18.69 for x=10, k=100

timeSimulation()

ParkingTemplate.TemplateSimulation(CircleParkingLot).simulate(display=True)
plt.title('Flory2D Flory, k=100')
plt.show()
# print(simulateManyCircles())
