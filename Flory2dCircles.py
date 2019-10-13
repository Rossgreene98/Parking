import matplotlib.pyplot as plt
import ParkingTemplate

class SquareParkingLot(ParkingTemplate.TemplateParkingLot):
    def __init__(self, lengthOfSide, pointsPerUnitLength):
        self.carRadius = pointsPerUnitLength / 2  # Since cars have diameter 1
        super(SquareParkingLot, self).__init__(lengthOfSide, pointsPerUnitLength, CircleCar)

    def getEverywhereCanParkInitially(self):
        allPlacesForNewCar = []
        for i in range(self.pointsPerSide - self.pointsPerCar):
            allPlacesForNewCar += [Point(i, j) for j in range(self.pointsPerSide - self.pointsPerCar)]
        return allPlacesForNewCar

    def findNewlyUnavailableSpace(self, newCar):
        newCarLocation = newCar.bottomLeftPoint
        newUnavailableSpace = []
        for i in range(newCarLocation.x - self.pointsPerCar, newCarLocation.x + self.pointsPerCar + 1):
            for j in range(newCarLocation.y - self.pointsPerCar, newCarLocation.y + self.pointsPerCar + 1):
                newUnavailableSpace.append(Point(i, j))
        return newUnavailableSpace

class SquareCar(ParkingTemplate.TemplateCar):
    def __init__(self, bottomLeftPoint, pointsPerCar):
        super().__init__()
        self.bottomLeftPoint = bottomLeftPoint
        self.pointsPerCar = pointsPerCar

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


# ParkingTemplate.run1SimulationWithLotSize(SquareParkingLot, 10, display=True)
ParkingTemplate.runManySimulations(SquareParkingLot, 10, 10)