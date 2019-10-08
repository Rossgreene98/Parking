from random import uniform

class Car:
    def __init__(self, leftmostPoint, length=1):
        self.leftmostPoint = leftmostPoint
        self.length = length

class ParkingLot:
    def __init__(self, length, carLength=1):
        self.parkedCars = []
        self.remainingParkingSpaces = [SpaceToPark(0, length - carLength)]
        self.length = length
        self.carLength = carLength

    def createRandomCarThatCanBeAdded(self):
        totalAvailableSpace = sum(
            parkingSpace.length for parkingSpace in self.remainingParkingSpaces
        )
        u = uniform(0, totalAvailableSpace)
        i = 0
        # i is the index of interval that new car goes into
        while self.remainingParkingSpaces[i].length < u:
            u -= self.remainingParkingSpaces[i].length
            i += 1
        i -= 1  # since final loop increments i when it shouldn't
        newCar = Car(self.remainingParkingSpaces[i].leftmost + u)
        return newCar

    def addNewCar(self, newCar):
        self.parkedCars.append(newCar)
        self.remainingParkingSpaces = self.updateRemainingSpace(newCar)

    def updateRemainingSpace(self, newCar):
        updatedRemainingSpace = []
        for parkingSpace in self.remainingParkingSpaces:
            updatedRemainingSpace += \
                parkingSpace.remainingSpaceAfterCarParked(newCar) if parkingSpace.contains(newCar.leftmostPoint) \
                else [parkingSpace]
        return updatedRemainingSpace

    def isJammed(self):
        # empty lists evaluate to false, so we return true when there are no remaining parking spaces
        return not self.remainingParkingSpaces

    def display(self):
        print(str(len(self.parkedCars)))


class SpaceToPark:
    # A Space to Park is an interval where the leftmost point of a car
    # could be added anywhere in the interval and not overlap with other cars in a lot
    def __init__(self, leftmost, rightmost, carLength=1):
        self.leftmost = leftmost
        self.rightmost = rightmost
        self.length = rightmost - leftmost
        self.carLength = carLength

    def contains(self, point):
        return self.leftmost <= point <= self.rightmost

    def carCouldFitInSpace(self):
        return self.length > 0

    def remainingSpaceAfterCarParked(self, newCar):
        spaceLeftOfNewCar = SpaceToPark(self.leftmost, newCar.leftmostPoint - self.carLength)
        spaceRightOfNewCar = SpaceToPark(newCar.leftmostPoint + newCar.length, self.rightmost)
        remainingParkingSpace = []
        if spaceLeftOfNewCar.carCouldFitInSpace():
            remainingParkingSpace.append(spaceLeftOfNewCar)
        if spaceRightOfNewCar.carCouldFitInSpace():
            remainingParkingSpace.append(spaceRightOfNewCar)
        return remainingParkingSpace

def run1Simulation(lengthOfCurb, lengthOfCar=1):
    parkingLot = ParkingLot(lengthOfCurb, lengthOfCar)
    while not parkingLot.isJammed():
        newCar = parkingLot.createRandomCarThatCanBeAdded()
        parkingLot.addNewCar(newCar)
    parkingLot.display()


run1Simulation(100)
