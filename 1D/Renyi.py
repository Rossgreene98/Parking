from random import uniform

def renyi(x):
    if x < 1:
        return 0
    u = uniform(0, x - 1)
    return 1 + renyi(u) + renyi(x - 1 - u)

print([renyi(100) for i in range(100)])
