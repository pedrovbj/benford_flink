import csv
import sys, getopt
from os import system
from math import log, log10, pow
from scipy.stats import chisquare, chi2


def benfordDist(d, n=1):
    assert n > 0, "Error: n must be > 0"
    assert d >= 0, "Error: d must be >= 0"
    assert d <= 9, "Error: d must be <= 9"
    if n <= 1:
        assert d > 0, "Error: d > 0 is a must when n == 1"
        return log10(1.0 + 1.0/d)

    inf = int(pow(10.0, n-2.0))
    sup = 10*inf

    p = 0.0
    for i in xrange(inf, sup):
        p += log10(1.0 + 1.0/(10.0*i+d))

    return p

def benfordProb(digits):
    return log10(1.0+1.0/(digits))

def freqFromResults(filename):
    freq = {}
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for line in reader:
            freq[int(line[0])] = int(line[1])
    return freq

def goodnessOfFit(freqObs, freqExp, confLevel=0.05):
    chisq, p = chisquare(freqObs, f_exp=freqExp)
    return p > confLevel, p

def mergeResults(outputFolder):
    system("cat " + outputFolder + "/* | sort > " + outputFolder + "/merge")

def main(argv):
    outputFolder=sys.argv[1]
    mergeResults(outputFolder)
    freqObsDict = freqFromResults(outputFolder+"/merge")
    keys = freqObsDict.keys()
    keys.sort()
    freqObs = [freqObsDict[key] for key in keys]
    print freqObs, sum(freqObs)
    probExp=map(benfordProb, keys)
    freqExp=map(lambda x: int(round(x*sum(freqObs))), probExp)
    print freqExp, sum(freqExp)
    print goodnessOfFit(freqObs, freqExp)


if __name__ == '__main__':
    main(sys.argv[1:])
