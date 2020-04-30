import numpy as np
import scipy.stats
from math import sqrt
import matplotlib.pyplot as plt

lam = 0.747597920

x = 10000
lamTilde = lam - (1-lam)/x
print(lamTilde)
c = 0.038156
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)})  # set font and plot size to be larger

floryPlotName = 'FloryPlot.png'
floryFilePath = 'allFlorySims_x=10000'
floryFilePathNumberParked = 'allRenyiSimulationsNumberParked'
kRange = [10**i for i in range(4, 12, 2)]

n = 10000

def graphAllData(filePath, kRange, plotName):
    allSims = np.loadtxt(filePath)

    means = np.mean(allSims, axis=1)
    stds = np.std(allSims, axis=1)
    errorBarSizes = 2.58 * stds / sqrt(n)

    plt.figure()
    plt.xlabel('k')
    plt.ylabel('Proportion of space occupied')
    plt.xlim(1000, 1000000000000) # Make x-axis range desirable
    plt.xscale("log")

    plt.errorbar(kRange, means, yerr=errorBarSizes, color='red', label='Simulated')

    # Add a point 'at infinity' for Renyi simulations
    plt.errorbar(
        [10**11.5, 10**11.7, 10**11.9], # So the mean can be seen on the plot
        [lamTilde, lamTilde, lamTilde],
        [0, 5.09249333e-05, 0],
        color='purple',
        label='Renyi'
    )
    plt.axhline(lam, label='λ = 0.74759...')
    plt.axhline(lamTilde, color='purple')

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


graphAllData(floryFilePath, kRange, floryPlotName)
# graphVariances(renyiFilePathNumberParked, renyiRoadRange, "RenyiVariancePlot")
