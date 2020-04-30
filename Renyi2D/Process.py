import numpy as np
from math import sqrt
from scipy.stats import norm, normaltest
import matplotlib.pyplot as plt
import statsmodels.api as sm
from math import pi

plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)})  # set font and plot size to be larger

floryFilePath = 'Renyix=500'
n = 5000

data500 = np.loadtxt("Renyix=500")
data1000 = np.loadtxt("Renyix=1000")

def processAllData():

    means = np.array([np.mean(data500), np.mean(data1000)])
    print("Observed Mean: " + str(means))

    std = np.array([np.std(data500), np.std(data1000)])
    print("Standard Deviations: " + str(std))

    errorBarSizes = std * 2.58 / np.array([sqrt(5000), sqrt(1000)])
    print("Error Bar Sizes: " + str(errorBarSizes))

    CI = [means + errorBarSizes, means - errorBarSizes]
    print("CI: " + str(CI))

    plt.figure()
    plt.xlabel('x')
    plt.ylabel('Proportion of space occupied')

    plt.xlim(300, 1300)
    plt.ylim(0.5468,0.5476)

    plt.errorbar([500, 1000], means, yerr=errorBarSizes, color='red', label='Simulated', fmt='.')
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
testNormality(data500)
dAgostinaTest(data500)


