from random import randint


def numberOfCarsOnCurbFloyd(lengthOfCurb, lengthOfCar=1):
    if lengthOfCar > lengthOfCurb:
        return 0
    u = randint(0, lengthOfCurb - lengthOfCar)
    return 1 + numberOfCarsOnCurbFloyd(u - 1, lengthOfCar) \
           + numberOfCarsOnCurbFloyd(lengthOfCurb - lengthOfCar - u - 1, lengthOfCar)


def pseudoRenyi(lengthOfCurb, meshDensity):
    equivCarLength = 1 * meshDensity
    equivLengthOfCurb = lengthOfCurb * meshDensity
    return numberOfCarsOnCurbFloyd(equivLengthOfCurb, equivCarLength)


print([pseudoRenyi(100, 100) for i in range(100)])
