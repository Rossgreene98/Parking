import numpy as np
from math import sqrt
from scipy.stats import norm, normaltest
import matplotlib.pyplot as plt
import statsmodels.api as sm

plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)})  # set font and plot size to be larger

floryFilePath = 'allFlory2DSims'
kRange = [50, 100, 300, 500]
n = 1000

allData = np.loadtxt(floryFilePath)
flory500Data = allData[2]

def processAllData():
    print("k: " + str(kRange))

    means = np.mean(allData, axis=1)
    print("Observed Means: " + str(means))

    stds = np.std(allData, axis=1)
    print("Standard Deviations: " + str(stds))

    errorBarSizes = 2.58 * stds / sqrt(n)
    print("Error Bar Sizes: " + str(errorBarSizes))

    CI = [means + errorBarSizes, means-errorBarSizes]
    print("CI: " + str(CI))

    plt.figure()
    plt.xlabel('k')
    plt.ylabel('Proportion of space occupied')

    plt.errorbar(kRange, means, yerr=errorBarSizes, color='red', label='Simulated')
    plt.show()

def testNormality(allSims):
    (mu, sigma) = norm.fit(allSims)

    # the histogram of the data
    n, bins, patches = plt.hist(
        allSims,
        27,
        weights=np.ones_like(allSims)/len(allSims),
        density=1,
        facecolor='green',
        alpha=0.75
    )

    # add a 'best fit' line
    plt.plot(bins, norm.pdf(bins, mu, sigma), 'r--', linewidth=2)

    # plot
    plt.xlabel('Proportion of kerb occupied')
    plt.ylabel('Quantity')
    plt.grid(True)

    plt.savefig('FloryHistogram.png')
    plt.show()

    sm.qqplot(allSims, line='s')
    plt.show()

def dAgostinaTest(data):
    print(len(data))
    stat, p = normaltest(data)
    print(p)

processAllData()
testNormality(flory500Data)
dAgostinaTest(flory500Data)
