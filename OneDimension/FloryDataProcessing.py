import numpy as np
from math import sqrt
from scipy.stats import norm, normaltest
import matplotlib.pyplot as plt
import statsmodels.api as sm

lam = 0.747597920
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)})  # set font and plot size to be larger

floryFilePath = 'allFlorySims_x=10000'
kRange = [10**i for i in range(4, 12, 2)]
n = 10000

allFloryData = np.loadtxt(floryFilePath)
flory1MData = allFloryData[2]

def processAllData(allSims, kRange):
    print("k: " + str(kRange))

    means = np.mean(allSims, axis=1)
    print("Observed Means: " + str(means))

    stds = np.std(allSims, axis=1)
    print("Standard Deviations: " + str(stds))

    errorBarSizes = 2.58 * stds / sqrt(n)
    print("Error Bar Sizes: " + str(errorBarSizes))

    CI = [means + errorBarSizes, means-errorBarSizes]
    print("CI: " + str(CI))

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

    plt.savefig('FloryHistogram.png')
    plt.show()

    sm.qqplot(allSims, line='s')
    plt.show()

def dAgostinaTest(data):
    print(len(data))
    stat, p = normaltest(data)
    print(p)

processAllData(allFloryData, kRange)
testNormality(flory1MData)
dAgostinaTest(flory1MData)
