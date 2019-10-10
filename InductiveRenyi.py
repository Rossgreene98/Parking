from random import uniform

def numberOfCarsOnCurb(length):
    if length < 1:
        return 0
    u = uniform(0, length - 1)
    return 1 + numberOfCarsOnCurb(u) + numberOfCarsOnCurb(length - 1 - u)


print(numberOfCarsOnCurb(100))
