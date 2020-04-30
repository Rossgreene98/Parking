import numpy as np
from math import sqrt
from scipy.stats import norm, normaltest
import matplotlib.pyplot as plt
import statsmodels.api as sm

lam = 0.747597920
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)})  # set font and plot size to be larger

renyiFilePath = 'allRenyiSimulations'
renyiRoadRange = [100, 1000, 10000, 100000, 1000000]
n = 10000

allRenyiData = np.loadtxt(renyiFilePath)
renyiTenThousandData = allRenyiData[2]

def processAllData(allSims, roadRange):
    print("x: " + str(roadRange))

    expectedMeans = list(map(lambda x: lam - (1 - lam) / x, roadRange))
    print("Expected Means: " + str(expectedMeans))

    means = np.mean(allSims, axis=1)
    print("Observed Means: " + str(means))

    stds = np.std(allSims, axis=1)
    print("Standard Deviations: " + str(stds))

    errorBarSizes = 2.58 * stds / sqrt(n)
    print("Error Bar Sizes: " + str(errorBarSizes))

def testNormality(allSims):
    (mu, sigma) = norm.fit(allSims)

    # the histogram of the data
    n, bins, patches = plt.hist(allSims, 30, weights=np.ones_like(allSims)/len(allSims), density=1, facecolor='green', alpha=0.75)

    # add a 'best fit' line
    plt.plot(bins, norm.pdf(bins, mu, sigma), 'r--', linewidth=2)

    # plot
    plt.xlabel('Proportion of kerb occupied')
    plt.ylabel('Quantity')
    plt.grid(True)

    plt.savefig('RenyiHistogram.png')
    plt.show()

    sm.qqplot(allSims, line='s')
    plt.show()

def dAgostinaTest(data):
    print(len(data))
    stat, p = normaltest(data)
    print(p)

processAllData(allRenyiData, renyiRoadRange)
# testNormality(renyiTenThousandData)
# dAgostinaTest(renyiTenThousandData)
