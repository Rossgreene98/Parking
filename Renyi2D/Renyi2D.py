from random import choice, uniform
from math import sqrt
from time import time
import numpy as np
from math import pi

"""
Following the methodology of Wang (reference in dissertation), this code produces the results discussed in Chapter 5; 
Simulating the Renyi Model Directly. 'Cell' and 'Disk' are helper classes, whilst the bulk of the work is done by
'simulate'.
"""

lotSize = 5
standardQuitRate = 2

class Cell:
    def __init__(self, leftmost, lowest, w):
        self.w = w
        self.x = leftmost
        self.y = lowest

class Disk:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.diameter = 1

    def noOverlapsWith(self, diskList):
        possibles = getDisksInSurroundingSquares(self.x, self.y, diskList)
        for disk in possibles:
            if self.overlaps(disk):
                return False
        return True

    def overlaps(self, disk):
        # the absolute values are because of the periodic boundary condition
        xDistance = min(abs(self.x - disk.x), lotSize - abs(self.x - disk.x))
        yDistance = min(abs(self.y - disk.y), lotSize - abs(self.y - disk.y))
        return sqrt(xDistance**2 + yDistance**2) < 1

    def covers(self, cell):
        fourCorners = [
            [cell.x, cell.y],
            [cell.x + cell.w, cell.y],
            [cell.x, cell.y + cell.w],
            [cell.x + cell.w, cell.y + cell.w]
        ]

        for corner in fourCorners:
            if not self.excludes(corner):
                return False
            return True

    def excludes(self, point):
        xDistance = min(abs(self.x - point[0]), lotSize - abs(self.x - point[0]))
        yDistance = min(abs(self.y - point[1]), lotSize - abs(self.y - point[1]))
        return sqrt(xDistance ** 2 + yDistance ** 2) < 1


def simulate(quitRate=standardQuitRate):
    w = 1  # Initial size of cells
    allPossibleCells = getInitialCells(lotSize, w)

    #  Parked Disks grouped by grid cell of centre to make filtering quicker
    allParkedDisks = [[[] for i in range(lotSize)] for j in range(lotSize)]

    noConsecutiveUnsuccessfulParks = 0
    while allPossibleCells:
        newDisk = getNewDisk(allPossibleCells, w)

        if newDisk.noOverlapsWith(allParkedDisks):
            allParkedDisks[int(newDisk.x)][int(newDisk.y)].append(newDisk)
            noConsecutiveUnsuccessfulParks = 0
        else:
            noConsecutiveUnsuccessfulParks += 1

        if noConsecutiveUnsuccessfulParks == quitRate:
            noConsecutiveUnsuccessfulParks = 0
            if w == 1:
                allPossibleCells = removeImpossibleCells(allPossibleCells, allParkedDisks)

            w /= 2

            allPossibleCells = divideInto4(allPossibleCells)
            allPossibleCells = removeImpossibleCells(allPossibleCells, allParkedDisks)

    noDisks = sum(sum(len(disksInGridSquare) for disksInGridSquare in row) for row in allParkedDisks)
    return noDisks

def getInitialCells(x, w):
    return [Cell(i, j, w) for i in range(x) for j in range(x)]

def getNewDisk(allPossibleCells, w):
    attemptedCell = choice(allPossibleCells)
    return Disk(
        attemptedCell.x + uniform(0, w),
        attemptedCell.y + uniform(0, w)
    )

def divideInto4(allPossibleCells):
    newSmallerCells = []
    for cell in allPossibleCells:
        newSmallerCells += subCells(cell)
    return newSmallerCells

def getDisksInSurroundingSquares(leftmost, lowest, diskList):
    myx = int(leftmost)
    myy = int(lowest)
    surroundingDisks = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            x1 = myx + i
            x = x1 + lotSize if x1 < 0 \
                else x1 - lotSize if x1 >= lotSize \
                else x1

            y1 = myy + j
            y = y1 + lotSize if y1 < 0 \
                else y1 - lotSize if y1 >= lotSize \
                else y1

            surroundingDisks += (diskList[x][y])

    return surroundingDisks

def subCells(cell):
    x = cell.x
    y = cell.y
    w = cell.w / 2
    return [Cell(x, y, w), Cell(x, y+w, w), Cell(x+w, y, w), Cell(x+w, y+w, w)]

def removeImpossibleCells(allPossibleCells, allParkedDisks):
    return list(filter(
        lambda cell: notCoveredBySingleDisk(cell, allParkedDisks), allPossibleCells
    ))

def notCoveredBySingleDisk(cell, allParkedDisks):
    relevantDisks = getDisksInSurroundingSquares(cell.x, cell.y, allParkedDisks)
    for disk in relevantDisks:
        if disk.covers(cell):
            return False
    return True

def timeSimulate(quitRate):
    start_time = time()
    simulate(quitRate)
    return time() - start_time
    # Runs quickest when quitRate is ~200

def writeFlory2DData(n, filePath):
    sims = []
    for i in range(n):
        if i % 100 == 0:
            print(i)
        sims.append(simulate())

    allSims = np.array(sims) * pi / 4 / lotSize**2
    np.savetxt(filePath, allSims)
