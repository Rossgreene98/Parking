from random import randint

def numberOfCarsOnCurbFloyd(lengthOfCurb, lengthOfCar=1):
    if lengthOfCar > lengthOfCurb:
        return 0
    u = randint(0, lengthOfCurb - lengthOfCar + 1)
    return 1 + numberOfCarsOnCurbFloyd(u-1) + numberOfCarsOnCurbFloyd(lengthOfCurb - lengthOfCar - u - 1)


for i in range(5, 20):
    print(numberOfCarsOnCurbFloyd(2))
