from random import randint
import numpy as np

def floryBig(totalSites, k):
    if k > totalSites:
        return 0
    u = randint(0, totalSites - k)
    return 1 + floryBig(u, k) + floryBig(totalSites - k - u, k)

def flory(x, k):
    return floryBig(x * (k - 1), k)

def manyFloryProportion(x, k, n):
    return [flory(x, k) / x for i in range(n)]

def writeFloryDatWithFixedX(x, kRange, n, filePath):
    allSims = np.array([manyFloryProportion(x, k, n) for k in kRange])
    np.savetxt(filePath, allSims)
    print("Done!")

writeFloryDatWithFixedX(x=10000, kRange=[10**i for i in range(4, 12, 2)], n=10000, filePath='allFlorySims_x=10000')

