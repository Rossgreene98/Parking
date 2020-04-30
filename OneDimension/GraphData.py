import numpy as np
import scipy.stats
from math import sqrt
import matplotlib.pyplot as plt

lam = 0.747597920
c = 0.038156
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)})  # set font and plot size to be larger

renyiPosterPlotName = 'RenyiExpectationsGraph_Poster.png'
renyiFilePath = 'allRenyiSimulations'
renyiFilePathNumberParked = 'allRenyiSimulationsNumberParked'
renyiRoadRange = [100, 1000, 10000, 100000, 1000000]

n = 10000

def graphAllData(filePath, roadRange, plotName):
    allSims = np.loadtxt(filePath)

    means = np.mean(allSims, axis=1)
    stds = np.std(allSims, axis=1)
    errorBarSizes = 2.58 * stds / sqrt(n)

    r1 = np.arange(1.8, 6., 0.05)
    r2 = 10 ** r1
    r3 = lam - (1 - lam) / r2

    plt.figure()
    plt.xlabel('Road Length')
    plt.ylabel('Proportion of space occupied')

    plt.errorbar(roadRange, means, yerr=errorBarSizes, color='red', label='Simulated')
    plt.axhline(lam, label='0.74759...')
    # plt.plot(r2, r3, marker='', color='olive', linewidth=2, label='λ - (1-λ)/x')

    plt.xscale("log")
    plt.legend(loc='lower right')

    plt.savefig(plotName)
    plt.show()

def graphVariances(filePath, roadRange, plotName):
    allSims = np.loadtxt(filePath)
    varis = np.var(allSims, axis=1)

    upperBounds = computeVarianceBound(n, varis, True)
    lowerBounds = computeVarianceBound(n, varis, False)

    upError = upperBounds - varis
    downError = varis - lowerBounds

    r1 = np.arange(1.8, 6., 0.05)
    r2 = 10 ** r1
    r3 = c + c/r2

    plt.figure()
    plt.xlabel('x')
    plt.ylabel('Variance / x')

    plt.errorbar(roadRange,  varis / roadRange, yerr=[downError/roadRange, upError/roadRange], color='red', label='Simulated')
    plt.axhline(c, label='v=0.038156')
    plt.plot(r2, r3, marker='', color='olive', linewidth=2, label='v + v/x')

    plt.xscale("log")
    plt.legend(loc='lower left')

    plt.savefig(plotName)
    plt.show()

def computeVarianceBound(n, v, isUpperBound):
    chiStat = scipy.stats.chi2.ppf(0.005, n) if isUpperBound else scipy.stats.chi2.ppf(0.995, n)
    return (n-1)*v / chiStat


# graphAllData(renyiFilePath, renyiRoadRange, renyiPosterPlotName)
graphVariances(renyiFilePathNumberParked, renyiRoadRange, "RenyiVariancePlot")
