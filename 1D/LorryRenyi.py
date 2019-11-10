from random import uniform, randint, random

def numberOfCarsOnCurb(length, lorryProportion):
    if length < 1:
        return 0
    isLorry = random() < lorryProportion
    u = uniform(0, length - 1)
    return 1 + numberOfCarsOnCurb(u) + numberOfCarsOnCurb(length - 1 - u)

print(numberOfCarsOnCurb(100))
